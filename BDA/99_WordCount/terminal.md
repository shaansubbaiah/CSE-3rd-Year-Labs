hadoop@ubuntuVM:~$ cd Downloads

hadoop@ubuntuVM:~/Downloads$ ls

`hadoop-core-0.20.2.jar  mywordcount.jar`

hadoop@ubuntuVM:~/Downloads$ touch input.txt

hadoop@ubuntuVM:~/Downloads$ ls

`hadoop-core-0.20.2.jar  input.txt  mywordcount.jar`

hadoop@ubuntuVM:~/Downloads$ nano input.txt

hadoop@ubuntuVM:~/Downloads$ cat input.txt 
```
okay lmao nice
cool okay lmao
nice cool cool
rip lmao rip
okay cool cool
```

hadoop@ubuntuVM:~/Downloads$ hadoop fs -mkdir /input

hadoop@ubuntuVM:~/Downloads$ hadoop fs -ls /
```
Found 1 items
drwxr-xr-x   - hadoop supergroup          0 2021-04-29 10:46 /input
```

hadoop@ubuntuVM:~/Downloads$ hadoop fs -put ~/Downloads/input.txt /input/input.txt

hadoop@ubuntuVM:~/Downloads$ hadoop fs -ls /input
```
Found 1 items
-rw-r--r--   1 hadoop supergroup         73 2021-04-29 10:47 /input/input.txt
```

hadoop@ubuntuVM:~/Downloads$ hadoop jar mywordcount.jar WordCount /input/input.txt output
```
2021-04-29 10:51:49,443 INFO client.RMProxy: Connecting to ResourceManager at /127.0.0.1:8032
2021-04-29 10:51:50,504 WARN mapreduce.JobResourceUploader: Hadoop command-line option parsing not performed. Implement the Tool interface and execute your application with ToolRunner to remedy this.
2021-04-29 10:51:50,540 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1619673100611_0001
2021-04-29 10:51:50,775 INFO input.FileInputFormat: Total input files to process : 1
2021-04-29 10:51:51,937 INFO mapreduce.JobSubmitter: number of splits:1
2021-04-29 10:51:52,211 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1619673100611_0001
2021-04-29 10:51:52,212 INFO mapreduce.JobSubmitter: Executing with tokens: []
2021-04-29 10:51:52,426 INFO conf.Configuration: resource-types.xml not found
2021-04-29 10:51:52,427 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2021-04-29 10:51:52,700 INFO impl.YarnClientImpl: Submitted application application_1619673100611_0001
2021-04-29 10:51:52,759 INFO mapreduce.Job: The url to track the job: http://ubuntuVM:8088/proxy/application_1619673100611_0001/
2021-04-29 10:51:52,769 INFO mapreduce.Job: Running job: job_1619673100611_0001
2021-04-29 10:52:04,405 INFO mapreduce.Job: Job job_1619673100611_0001 running in uber mode : false
2021-04-29 10:52:04,417 INFO mapreduce.Job:  map 0% reduce 0%
2021-04-29 10:52:11,960 INFO mapreduce.Job:  map 100% reduce 0%
2021-04-29 10:52:26,223 INFO mapreduce.Job:  map 100% reduce 100%
2021-04-29 10:52:28,279 INFO mapreduce.Job: Job job_1619673100611_0001 completed successfully
2021-04-29 10:52:28,492 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=60
		FILE: Number of bytes written=468595
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=175
		HDFS: Number of bytes written=34
		HDFS: Number of read operations=8
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=1
		Launched reduce tasks=1
		Data-local map tasks=1
		Total time spent by all maps in occupied slots (ms)=4072
		Total time spent by all reduces in occupied slots (ms)=11982
		Total time spent by all map tasks (ms)=4072
		Total time spent by all reduce tasks (ms)=11982
		Total vcore-milliseconds taken by all map tasks=4072
		Total vcore-milliseconds taken by all reduce tasks=11982
		Total megabyte-milliseconds taken by all map tasks=4169728
		Total megabyte-milliseconds taken by all reduce tasks=12269568
	Map-Reduce Framework
		Map input records=5
		Map output records=15
		Map output bytes=133
		Map output materialized bytes=60
		Input split bytes=102
		Combine input records=15
		Combine output records=5
		Reduce input groups=5
		Reduce shuffle bytes=60
		Reduce input records=5
		Reduce output records=5
		Spilled Records=10
		Shuffled Maps =1
		Failed Shuffles=0
		Merged Map outputs=1
		GC time elapsed (ms)=137
		CPU time spent (ms)=1080
		Physical memory (bytes) snapshot=421908480
		Virtual memory (bytes) snapshot=5060018176
		Total committed heap usage (bytes)=407371776
		Peak Map Physical memory (bytes)=261107712
		Peak Map Virtual memory (bytes)=2525753344
		Peak Reduce Physical memory (bytes)=160800768
		Peak Reduce Virtual memory (bytes)=2534264832
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=73
	File Output Format Counters 
		Bytes Written=34
```

hadoop@ubuntuVM:~/Downloads$ hadoop fs -ls /user/hadoop/output
```
Found 2 items
-rw-r--r--   1 hadoop supergroup          0 2021-04-29 10:52 /user/hadoop/output.txt/_SUCCESS
-rw-r--r--   1 hadoop supergroup         34 2021-04-29 10:52 /user/hadoop/output.txt/part-r-00000
```

hadoop@ubuntuVM:~/Downloads$ hadoop fs -cat /user/hadoop/output/part-r-00000 
```
cool	5
lmao	3
nice	2
okay	3
rip	2
```

