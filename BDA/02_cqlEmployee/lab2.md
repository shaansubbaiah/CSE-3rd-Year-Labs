## LAB 2 - Employee DB using CQL

```sql
cqlsh> create keyspace employee_info with replication={'class':'SimpleStrategy','replication_factor':1};


cqlsh> use employee_info;
cqlsh:employee_info> create table employee_details(emp_id int, emp_name text, designation text, doj timestamp, salary double, dept_name text, primary key(emp_id,salary));


cqlsh:employee_info> describe table employee_details;

CREATE TABLE employee_info.employee_details (
    emp_id int,
    salary double,
    dept_name text,
    designation text,
    doj timestamp,
    emp_name text,
    PRIMARY KEY (emp_id, salary)
) WITH CLUSTERING ORDER BY (salary ASC)
    AND additional_write_policy = '99p'
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


cqlsh:employee_info> begin batch insert into employee_details(emp_id,emp_name,designation,doj,salary,dept_name) values (100,'tanya','manager','2020-09-11',30000,'testing') insert into employee_details(emp_id,emp_name,designation,doj,salary,dept_name) values (111,'sriram','associate','2020-06-11',25000,'development') insert into employee_details(emp_id,emp_name,designation,doj,salary,dept_name) values (121,'shiva','manager','2020-01-03',35000,'hr') apply batch;


cqlsh:employee_info> select * from employee_details;

 emp_id | salary | dept_name   | designation | doj                             | emp_name
--------+--------+-------------+-------------+---------------------------------+----------
    111 |  25000 | development |   associate | 2020-06-10 18:30:00.000000+0000 |   sriram
    121 |  35000 |          hr |     manager | 2020-01-02 18:30:00.000000+0000 |    shiva
    100 |  30000 |     testing |     manager | 2020-09-10 18:30:00.000000+0000 |    tanya

(3 rows)


cqlsh:employee_info> update employee_details set emp_name='shaan' where emp_id = 121 and salary=35000;


cqlsh:employee_info> select * from employee_details;

 emp_id | salary | dept_name   | designation | doj                             | emp_name
--------+--------+-------------+-------------+---------------------------------+----------
    111 |  25000 | development |   associate | 2020-06-10 18:30:00.000000+0000 |   sriram
    121 |  35000 |          hr |     manager | 2020-01-02 18:30:00.000000+0000 |    shaan
    100 |  30000 |     testing |     manager | 2020-09-10 18:30:00.000000+0000 |    tanya

(3 rows)


cqlsh:employee_info> alter table employee_details add project text;


cqlsh:employee_info> update employee_details set project='chat app' where emp_id=111 and salary=25000;
cqlsh:employee_info> update employee_details set project='campusx' where emp_id=121 and salary=35000;
cqlsh:employee_info> update employee_details set project='canteen app' where emp_id=100 and salary=30000;


cqlsh:employee_info> select * from employee_details;

 emp_id | salary | dept_name   | designation | doj                             | emp_name | project
--------+--------+-------------+-------------+---------------------------------+----------+-------------
    111 |  25000 | development |   associate | 2020-06-10 18:30:00.000000+0000 |   sriram |    chat app
    121 |  35000 |          hr |     manager | 2020-01-02 18:30:00.000000+0000 |    shaan |     campusx
    100 |  30000 |     testing |     manager | 2020-09-10 18:30:00.000000+0000 |    tanya | canteen app

(3 rows)


cqlsh:employee_info> insert into employee_details(emp_id,emp_name,designation,doj,salary,dept_name) values(113,'sam','manager','2020-09-09',30000,'testing') using ttl 30;


cqlsh:employee_info> select ttl(emp_name) from employee_details where emp_id=113 and salary=30000;

 ttl(emp_name)
---------------
            22

(1 rows)


cqlsh:employee_info> paging off;
Disabled Query paging.


cqlsh:employee_info>  select * from employee_details where emp_id in (111,121,100) order by salary;

 emp_id | salary | dept_name   | designation | doj                             | emp_name | project
--------+--------+-------------+-------------+---------------------------------+----------+-------------
    111 |  25000 | development |   associate | 2020-06-10 18:30:00.000000+0000 |   sriram |    chat app
    100 |  30000 |     testing |     manager | 2020-09-10 18:30:00.000000+0000 |    tanya | canteen app
    121 |  35000 |          hr |     manager | 2020-01-02 18:30:00.000000+0000 |    shaan |     campusx

(3 rows)
```
