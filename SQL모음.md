# PostgreSQL

> http://www.devkuma.com/books/pages/1431

### show tables;

```bash
psql -p {port} -U {database}
\dt
```

### DESC; -> column 조회

- query

```sql
SELECT * FROM information_schema.columns
WHERE table_schema = '{schema}'
    AND table_name = '{table}';
```

- psql

```bash
{database} $ \d+
```

### to_timestamp() -> string to datetime

- query

```sql
SELECT anls_dt FROM {table};

  anls_dt
------------
 2021091123

SELECT to_timestamp("anls_dt", 'YYYYMMDDHH24') AS anls_dt FROM {table};
        anls_dt
------------------------
 2021-09-11 23:00:00+09
```

단, 포매팅시 시간에 대한 주의사항으로 HH에 대해서 24시 기준인지, am, pm을 명시해주어야 한다.

포매팅 함수와 패턴에 대한 자세항 내용은 공식문서의 [Table 9-22. Template Patterns for Date/Time Formatting](https://www.postgresql.org/docs/9.2/functions-formatting.html)에서 볼 수 있다.
