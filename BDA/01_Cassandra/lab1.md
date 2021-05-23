## LAB 1 - Cassandra Commands

```sql
cqlsh> create keyspace students with replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 };


cqlsh> describe keyspaces;

students  system_auth         system_schema  system_views         
system    system_distributed  system_traces  system_virtual_schema


cqlsh> use students;
cqlsh:students> create table student_info( rollNo int primary key, name text, joinDate timestamp, lastExamPerc double );


cqlsh:students> describe tables

student_info


cqlsh:students> describe table student
student_info  students.


cqlsh:students> describe table student_info

CREATE TABLE students.student_info (
    rollno int PRIMARY KEY,
    joindate timestamp,
    lastexamperc double,
    name text
) WITH additional_write_policy = '99p'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND cdc = false
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '16', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND extensions = {}
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99p';


cqlsh:students> begin batch insert into student_info(rollno, joindate, lastexamperc, name) values (1, '2021-05-23', 90.0, 'Adam') insert into student_info(rollno, joindate, lastexamperc, name) values (2, '2021-05-22', 97.7, 'Eve') apply batch;


cqlsh:students> select * from student_info;

 rollno | joindate                        | lastexamperc | name
--------+---------------------------------+--------------+------
      1 | 2021-05-22 18:30:00.000000+0000 |           90 | Adam
      2 | 2021-05-21 18:30:00.000000+0000 |         97.7 |  Eve

(2 rows)


cqlsh:students> update student_info set name = 'Micheal' where rollno = 1;


cqlsh:students> select * from student_info where rollno in (1,2);

 rollno | joindate                        | lastexamperc | name
--------+---------------------------------+--------------+---------
      1 | 2021-05-22 18:30:00.000000+0000 |           90 | Micheal
      2 | 2021-05-21 18:30:00.000000+0000 |         97.7 |     Eve

(2 rows)


cqlsh:students> create index on student_info(lastexamperc);


cqlsh:students> select rollno, name from student_info limit 2;

 rollno | name
--------+---------
      1 | Micheal
      2 |     Eve

(2 rows)


cqlsh:students> create index on student_info(name);


cqlsh:students> update student_info set name='Eve2', lastexamperc=100.0 where rollno=2;


cqlsh:students> select * from student_info;

 rollno | joindate                        | lastexamperc | name
--------+---------------------------------+--------------+---------
      1 | 2021-05-22 18:30:00.000000+0000 |           90 | Micheal
      2 | 2021-05-21 18:30:00.000000+0000 |          100 |    Eve2

(2 rows)


cqlsh:students> delete lastexamperc from student_info where rollno=2;


cqlsh:students> select * from student_info;

 rollno | joindate                        | lastexamperc | name
--------+---------------------------------+--------------+---------
      1 | 2021-05-22 18:30:00.000000+0000 |           90 | Micheal
      2 | 2021-05-21 18:30:00.000000+0000 |         null |    Eve2

(2 rows)


cqlsh:students> delete from student_info where rollno=2;


cqlsh:students> select * from student_info;

 rollno | joindate                        | lastexamperc | name
--------+---------------------------------+--------------+---------
      1 | 2021-05-22 18:30:00.000000+0000 |           90 | Micheal

(1 rows)
```
