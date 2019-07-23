from pyspark import SparkContext

input_file = sc.textFile("hdfs://localhost:9000/Myhadoopfolder/filepyspark.txt")
map = input_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))
counts = map.reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://localhost:9000/SparkTestingpy")
