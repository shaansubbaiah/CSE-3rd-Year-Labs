## SCALA FUNCTIONS IN PYTHON

```python
# MAP
>>> baby_names = sc.textFile("baby_names.csv")
>>> rows = baby_names.map(lambda line: line.split(","))

# FLATMAP
>>> sc.parallelize([2, 3, 4]).flatMap(lambda x: [x,x,x]).collect()
	[2, 2, 2, 3, 3, 3, 4, 4, 4]

# FILTER
>>> rows.filter(lambda line: "MICHAEL" in line).collect()
	Out[36]:
	[[u'2013', u'MICHAEL', u'QUEENS', u'M', u'155'],
	 [u'2013', u'MICHAEL', u'KINGS', u'M', u'146'],
	 [u'2013', u'MICHAEL', u'SUFFOLK', u'M', u'142']]
 
 # UNION
>>> one = sc.parallelize(range(1,10))
>>> two = sc.parallelize(range(10,21))
>>> one.union(two).collect()
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# INTERSECTION
>>> one = sc.parallelize(range(1,10))
>>> two = sc.parallelize(range(5,15))
>>> one.intersection(two).collect()
	[5, 6, 7, 8, 9]

# DISTINCT
>>> parallel = sc.parallelize(range(1,9))
>>> par2 = sc.parallelize(range(5,15))
>>> parallel.union(par2).distinct().collect()
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# SUBTRACT
>>> val s1 = sc.parallelize(List("c","c","p","m","t"))
>>> val s2 = sc.parallelize(List("c","m","k"))
>>> val result = s1.subtract(s2)
>>> result.foreach{println}
	t
	p

# CARTESIAN
>>> val data1 = sc.parallelize(List(1,2,3))
>>> val data2 = sc.parallelize(List(3,4,5))
>>> val cartesianfunc = data1.cartesian(data2)
```
