scala> val txt = sc.textFile("./input.txt")
```shell
txt: org.apache.spark.rdd.RDD[String] = ./input.txt MapPartitionsRDD[7] at textFile at <console>:24
```

scala> val counts = txt.flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)
```shell
counts: org.apache.spark.rdd.RDD[(String, Int)] = ShuffledRDD[10] at reduceByKey at <console>:25
```

scala> counts.collect()
```shell
res2: Array[(String, Int)] = Array((this,1), (wolf,1), (is,1), (spot.,1), (repeated,1), (cappucino.,1), (anything,1), (with,1), (some,2), (as,1), (come,1), (dog,2), (cat,3), (Here,1), (up,1), (not,1), (text,1), (on,1), (could,1), (I,1), (aare,1), (else,1), (random,1), (words,1), (the,1))
```
