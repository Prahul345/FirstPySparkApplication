from pyspark import SparkContext, SparkConf


#sc= SparkContext(master="local",appName="sparkwordcount")
conf = SparkConf().setAppName("sparkwordcount").setMaster("local")
sc = SparkContext(conf=conf)
data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
print(distData.count())