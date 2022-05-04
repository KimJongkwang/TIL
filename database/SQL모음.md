# PostgreSQL

> http://www.devkuma.com/books/pages/1431

### show tables;

```bash
psql -p {port} -U {database}
\dt
```

### 세션 현황 조회

- query

```sql
select * from pg_stat_activity where datname='{db_name}';
```

- 현재 연결된 세션정보 조회
- state 에서 세션상태 확인
  - idle: 세션은 있으나, 쿼리 실행전
  - active: 쿼리 실행 상태

### DESC; -> column 조회

- query

```sql
SELECT * FROM information_schema.columns
WHERE table_schema = '{schema}'
    AND table_name = '{table}';
```

- 테이블 코멘트와 컬럼정보

```sql
with tableinfo as (
	select    c.relname as table_name
            , obj_description(c.oid) table_comment
            , a.attname  as column_name
            , (select col_description(a.attrelid, a.attnum)) as column_comment
	from
	    pg_catalog.pg_class c
	    inner join pg_catalog.pg_attribute a on a.attrelid = c.oid
	where
	    a.attnum > 0
	    and a.attisdropped is false
	    and pg_catalog.pg_table_is_visible(c.oid)
	order by a.attrelid, a.attnum
	)
select    a.table_name
        , b.table_comment
        , a.column_name
        , udt_name dtype
        , character_maximum_length
        , is_nullable
        , column_default
from information_schema.columns as a
left outer join tableinfo as b on a.table_name = b.table_name
where table_schema = 'public';
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
