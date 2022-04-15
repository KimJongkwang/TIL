# PostgreSQL Error

## `current transaction is aborted, commands ignored until end of transaction block` 에러 해결법

해당 에러는 트랜잭션 수행중에 쿼리가 에러를 일으키는 상황에서 롤백하지 않고, 다른 쿼리를 실행하려 할 때 발생한다.

보통의 PostgreSQL 서버에서 log_statement와 log_min_error_statement 옵션을 사용하면 도움이 된다고 한다. [참고](https://brownbears.tistory.com/229)

나의 경우에는 Python에서 CRUD 클래스을 작성하여 pgsql과 통신하였는데, 문제는 예외처리였다.

```python
class CRUD:
    def __init__(self) -> None:
        self._conn = psycopg2.connect(**DB_INFO)
        self._cur = self._conn.cursor()

    def __del__(self):
        self._conn.close()
        self._cur.close()

    def insertDB(self, data_list: list, table: str, columns_n: int):
        cols = "%s," * columns_n
        sql = f"""
                INSERT INTO public.{table} VALUES
                    ({cols [:-1]})
        """
        try:
            self._cur.executemany(sql, data_list)
            self._conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        ...

db = CRUD()

db.insertDB(data1, table1, 10)
db.insertDB(data2, table2, 15)
db.insertDB(data3, table3, 30)
```

위와 같이 모든 데이터를 테이블에 insert 할때, try 에서 쿼리를 실행하는 executemany() 이후에 commit()을 하였다.

하나의 DB 세션에서 모두 처리하는데, 이때 첫번째 insert에서 pk 중복으로 에러가 발생하자,

열려있던 트랜잭션 블록이 유효하지 않아 다음 트랜잭션부터 계속 오류가 발생한 것이다.

이때, 해결법으로 위의 참고 사이트에서는 롤백을 제시하였으나, 나의 경우에는 각각의 insert가 테이블간 영향이 있지 않아 롤백은 하지 않았다.

다만, 위의 코드에서 except에 commit()을 추가하여 에러가 발생한 것 또한, commit() 으로 트랜잭션을 종료시켜주었다.

```python
    ...
    try:
        self._cur.executemany(sql, data_list)
        self._conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        self._conn.commit()
    ...

```

> 삽질한 시간에 비해 너무나도 간단하게 처리되었다. 아마 더 좋은 방법이 있을 것이라 생각된다.
>
> 트랜잭션을 분리할 수 있는 방법이 있는지 생각해보고, 또는 여러 데이터를 넣는 경우에는 DB세션을 여러개로 나누어 넣는 방법도 있겠다.
