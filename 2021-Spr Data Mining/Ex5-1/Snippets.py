$ pyspark

from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Loads data.
dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")

# Trains a k-means model.
kmeans = KMeans().setK(2).setSeed(1)
model = kmeans.fit(dataset)

# Make predictions
predictions = model.transform(dataset)

# Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# Shows the result.
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)


#######

wc -l /home/data/apache-spark/sample_kmeans_data.txt 
hadoop fs -ls /user/data/CSC533DM/

$ pyspark

from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
data = spark.read.format("libsvm").load("/user/data/CSC533DM/sample_kmeans_data.txt")
data.show(truncate=False)


kmeans = KMeans().setK(7).setSeed(1)
model = kmeans.fit(data)

predictions = model.transform(data)
predictions.show(truncate=False)


evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette)) 


centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers: print(center)
