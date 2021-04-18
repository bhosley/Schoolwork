hadoop fs -put /home/data/CSC533DM/uber.csv 
hadoop fs -ls /user/data/CSC533DM/
head /user/data/CSC533DM/uber.csv 

$ pyspark

## 1.2.1

schema = '`Date/Time` TIMESTAMP, Lat DOUBLE, Lon DOUBLE, Base STRING'
uber_df = spark.read.schema(schema) \
    .option("header","true") \
    .option("timestampFormat", "M/d/yyyy HH:mm:ss") \
    .csv("/user/data/CSC533DM/uber.csv")
uber_df.printSchema()
uber_df.show(5)

##

# Import the class
from pyspark.ml.feature import VectorAssembler 
# Creating a vector
assembler = VectorAssembler(inputCols=['Lat', 'Lon'], outputCol='features') 
# Transform
features_df = assembler.transform(uber_df)
features_df.show(5)

## 2.1.1
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

kmeans3 = KMeans().setK(3).setSeed(1)
kmeans5 = KMeans().setK(5).setSeed(1)
kmeans8 = KMeans().setK(8).setSeed(1)

model3 = kmeans3.fit(features_df)
model5 = kmeans5.fit(features_df)
model8 = kmeans8.fit(features_df)

predictions3 = model3.transform(features_df)
predictions5 = model5.transform(features_df)
predictions8 = model8.transform(features_df)

evaluator = ClusteringEvaluator()

silhouette3 = evaluator.evaluate(predictions3)
silhouette5 = evaluator.evaluate(predictions5)
silhouette8 = evaluator.evaluate(predictions8)
print("Silhouette with squared euclidean distance = " + str(silhouette3))
print("Silhouette with squared euclidean distance = " + str(silhouette5))
print("Silhouette with squared euclidean distance = " + str(silhouette8))

centers = model3.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)
centers = model5.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)
centers = model8.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)

## 3.1.1

## 4

from pyspark.sql.functions import hour, mean
(df
    .groupBy(hour("Date/Time").alias("hour"))
    .agg(count("value").alias("pickups"))
    .sort("pickups")
    .show())

## 5

predictions8.collect()