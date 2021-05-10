hadoop@ubuntuVM:~/Downloads/mapred3$ hadoop jar ~/Downloads/mapred3/mapredweather.jar AverageDriver /input/sample.txt /output_mapredweather2

```
2021-05-10 15:11:07,888 INFO client.RMProxy: Connecting to ResourceManager at /127.0.0.1:8032
2021-05-10 15:11:08,283 WARN mapreduce.JobResourceUploader: Hadoop command-line option parsing not performed. Implement the Tool interface and execute your application with ToolRunner to remedy this.
2021-05-10 15:11:08,321 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1620637047177_0002
2021-05-10 15:11:08,598 INFO input.FileInputFormat: Total input files to process : 1
2021-05-10 15:11:09,335 INFO mapreduce.JobSubmitter: number of splits:1
2021-05-10 15:11:09,635 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1620637047177_0002
2021-05-10 15:11:09,636 INFO mapreduce.JobSubmitter: Executing with tokens: []
2021-05-10 15:11:09,936 INFO conf.Configuration: resource-types.xml not found
2021-05-10 15:11:09,936 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2021-05-10 15:11:10,040 INFO impl.YarnClientImpl: Submitted application application_1620637047177_0002
2021-05-10 15:11:10,118 INFO mapreduce.Job: The url to track the job: http://ubuntuVM:8088/proxy/application_1620637047177_0002/
2021-05-10 15:11:10,120 INFO mapreduce.Job: Running job: job_1620637047177_0002
2021-05-10 15:11:16,293 INFO mapreduce.Job: Job job_1620637047177_0002 running in uber mode : false
2021-05-10 15:11:16,295 INFO mapreduce.Job:  map 0% reduce 0%
2021-05-10 15:11:24,387 INFO mapreduce.Job:  map 100% reduce 0%
2021-05-10 15:11:31,438 INFO mapreduce.Job:  map 100% reduce 100%
2021-05-10 15:11:31,449 INFO mapreduce.Job: Job job_1620637047177_0002 completed successfully
2021-05-10 15:11:31,558 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=61
		FILE: Number of bytes written=468211
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=633
		HDFS: Number of bytes written=15
		HDFS: Number of read operations=8
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=1
		Launched reduce tasks=1
		Data-local map tasks=1
		Total time spent by all maps in occupied slots (ms)=3815
		Total time spent by all reduces in occupied slots (ms)=3335
		Total time spent by all map tasks (ms)=3815
		Total time spent by all reduce tasks (ms)=3335
		Total vcore-milliseconds taken by all map tasks=3815
		Total vcore-milliseconds taken by all reduce tasks=3335
		Total megabyte-milliseconds taken by all map tasks=3906560
		Total megabyte-milliseconds taken by all reduce tasks=3415040
	Map-Reduce Framework
		Map input records=5
		Map output records=5
		Map output bytes=45
		Map output materialized bytes=61
		Input split bytes=103
		Combine input records=0
		Combine output records=0
		Reduce input groups=2
		Reduce shuffle bytes=61
		Reduce input records=5
		Reduce output records=2
		Spilled Records=10
		Shuffled Maps =1
		Failed Shuffles=0
		Merged Map outputs=1
		GC time elapsed (ms)=131
		CPU time spent (ms)=940
		Physical memory (bytes) snapshot=456499200
		Virtual memory (bytes) snapshot=5060923392
		Total committed heap usage (bytes)=409993216
		Peak Map Physical memory (bytes)=275853312
		Peak Map Virtual memory (bytes)=2526674944
		Peak Reduce Physical memory (bytes)=180645888
		Peak Reduce Virtual memory (bytes)=2534248448
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=530
	File Output Format Counters 
		Bytes Written=15
```

hadoop@ubuntuVM:~/Downloads/mapred3$ hadoop fs -ls /output_mapredweather2

```
Found 2 items
-rw-r--r--   1 hadoop supergroup          0 2021-05-10 15:11 /output_mapredweather2/_SUCCESS
-rw-r--r--   1 hadoop supergroup         15 2021-05-10 15:11 /output_mapredweather2/part-r-00000
```

hadoop@ubuntuVM:~/Downloads/mapred3$ hadoop fs -cat /output_mapredweather2/part-r-00000

```
1949	94
1950	3
```
