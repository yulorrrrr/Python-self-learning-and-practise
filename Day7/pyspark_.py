from pyspark import SparkConf, SparkContext
#create SparkConf class object
conf = SparkConf().setMaster("local[*]") .setAppName("test_spark_app")
#create soarkContent base om SparkCon class object
sc = SparkContext(conf = conf)
'''

#print spark verison
print(sc.version)


#turn python's object into spark, to rdd
rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize((1,2,3,4,5))
rdd3 = sc.parallelize("abcdefg")
rdd4 = sc.parallelize({1,2,3,4,5})
rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})

#use collect() to check rdd
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())


#read rdd
rdd = sc.textFile()
print(rdd.collect())

#stop pyspark
sc.stop()

#------------------------------------------------------------
#map func: (T) -> U
rdd2_1 = sc.parallelize([1,2,3,4,5])

#multiply each data by 10 through map method
def func(data):
    return data*10

rdd2_2 = rdd2_1.map(func)
#rdd2 = rdd.map(lambda X: X*10)

print(rdd2_2.collect())
sc.stop()

#-----------------------------------------------------------
#flatmap
rdd3_1 = sc.parallelize(["Christine Aven 666","Christine Christine Aven", "Python Christine"])

rdd3_1.flatMap(lambda x: x.split(" "))
print(rdd.collect())"""
'''
#-----------------------------------------------------------
rdd4_1 = sc.parallelize([('male',99), ('male', 66), ('female', 99), ('female', 88)])
rdd4_2 = rdd4_1.reduceByKey(lambda a,b: a+b)
print(rdd4_2.collect())