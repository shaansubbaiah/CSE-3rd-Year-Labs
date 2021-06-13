## LAB 3 - Library DB using CQL

```sql
cqlsh> create keyspace library_info with replication = {'class':'SimpleStrategy','replication_factor':1};


cqlsh> use library_info;


cqlsh:library_info> create table library_details(stud_id int,counter_value
                ... counter,stud_name text,book_name text,date_of_issue timestamp,book_id
                ... int,primary key(stud_id,stud_name,book_name,date_of_issue,book_id));


cqlsh:library_info> update library_details set counter_value=counter_value+1
                ... where stud_id=111 and stud_name='sam' and book_name='ML' and
                ... date_of_issue='2020-11-09' and book_id=200;
cqlsh:library_info> update library_details set counter_value=counter_value+1
                ... where stud_id=112 and stud_name='shaan' and book_name='BDA' and
                ... date_of_issue='2020-01-01' and book_id=300;
cqlsh:library_info> update library_details set counter_value=counter_value+1
                ... where stud_id=113 and stud_name='ayman' and book_name='OOMD' and
                ... date_of_issue='2020-06-01' and book_id=400;


cqlsh:library_info>  select * from library_details;

 stud_id | stud_name | book_name | date_of_issue                   | book_id | counter_value
---------+-----------+-----------+---------------------------------+---------+---------------
     111 |       sam |        ML | 2020-11-08 18:30:00.000000+0000 |     200 |             1
     113 |     ayman |      OOMD | 2020-05-31 18:30:00.000000+0000 |     400 |             1
     112 |     shaan |       BDA | 2019-12-31 18:30:00.000000+0000 |     300 |             1

(3 rows)


cqlsh:library_info> update library_details set counter_value=counter_value+1
                ... where stud_id=112 and stud_name='shaan' and book_name='BDA' and
                ... date_of_issue='2020-01-01' and book_id=300;

cqlsh:library_info>  select * from library_details where stud_id=112;

 stud_id | stud_name | book_name | date_of_issue                   | book_id | counter_value
---------+-----------+-----------+---------------------------------+---------+---------------
     112 |     shaan |       BDA | 2019-12-31 18:30:00.000000+0000 |     300 |             2

(1 rows)


cqlsh:library_info>  copy library_details(stud_id,stud_name,book_name,book_id,date_of_issue,counter_value) to 'library.csv' ;
Using 1 child processes

Starting copy of library_info.library_details with columns [stud_id, stud_name, book_name, book_id, date_of_issue, counter_value].
cqlshlib.copyutil.ExportProcess.write_rows_to_csv(): writing row
cqlshlib.copyutil.ExportProcess.write_rows_to_csv(): writing row
cqlshlib.copyutil.ExportProcess.write_rows_to_csv(): writing row
Processed: 3 rows; Rate:      32 rows/s; Avg. rate:      32 rows/s
3 rows exported to 1 files in 0.123 seconds.


cqlsh:library_info> truncate library_details;


cqlsh:library_info>  copy library_details(stud_id,stud_name,book_name,book_id,date_of_issue,counter_value) from 'library.csv' ;
Using 1 child processes

Starting copy of library_info.library_details with columns [stud_id, stud_name, book_name, book_id, date_of_issue, counter_value].
Processed: 3 rows; Rate:       5 rows/s; Avg. rate:       8 rows/s
3 rows imported from 1 files in 0.394 seconds (0 skipped).


cqlsh:library_info> select * from library_details;

 stud_id | stud_name | book_name | date_of_issue                   | book_id | counter_value
---------+-----------+-----------+---------------------------------+---------+---------------
     111 |       sam |        ML | 2020-11-08 18:30:00.000000+0000 |     200 |             1
     113 |     ayman |      OOMD | 2020-05-31 18:30:00.000000+0000 |     400 |             1
     112 |     shaan |       BDA | 2019-12-31 18:30:00.000000+0000 |     300 |             2

```
