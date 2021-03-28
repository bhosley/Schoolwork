wc -l ../data/apache-spark/sample_libsvm_data.txt

hadoop fs -put ../data/apache-spark/sample_libsvm_data.txt /user/data/CSC533DM/.

hadoop fs -ls /user/data/CSC533DM/

$ pyspark

data = spark.read.format("libsvm").load("/user/data/CSC533DM/sample_libsvm_data.txt")
from pyspark.ml.feature import StringIndexer
labelIndexer = StringIndexer(inputCol="label",outputCol="indexedLabel").fit(data)
labelIndexer.transform(data).show(5)

from pyspark.ml.feature import VectorIndexer
featureIndexer = VectorIndexer(inputCol="features", outputCol="indexedFeatures",maxCategories=4).fit(data)
featureIndexer.transform(data).show(5)

(trainingData, testData) = data.randomSplit([0.7, 0.3])

trainingData.show(5)
testData.show(5)



from pyspark.ml.classification import DecisionTreeClassifier
dt = DecisionTreeClassifier(labelCol="indexedLabel",featuresCol="indexedFeatures")
from pyspark.ml import Pipeline
pipeline = Pipeline(stages=[labelIndexer, featureIndexer, dt])
model = pipeline.fit(trainingData)
predictions = model.transform(testData)
#predictions.show(5)
predictions.select("prediction", "indexedLabel", "features").show(5)

from pyspark.ml.evaluation import MulticlassClassificationEvaluator
evaluator = MulticlassClassificationEvaluator(labelCol="indexedLabel",predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
evaluator.setMetricName("weightedPrecision")
precision = evaluator.evaluate(predictions)
evaluator.setMetricName("weightedRecall")
recall = evaluator.evaluate(predictions)
evaluator.setMetricName("f1")
f1Measure = evaluator.evaluate(predictions)

print("Accuracy: %g " % accuracy)
print("Precision: %g " % precision)
print("Recall: %g " % recall)
print("F1: %g " % f1Measure)

from pyspark.mllib.evaluation import MulticlassMetrics
predictionAndLabels = predictions.select("prediction", "indexedLabel").rdd
metrics = MulticlassMetrics(predictionAndLabels)

# Statistics by class
#labels = predictionAndLabels.map(lambda lp: lp.label).distinct().collect()
labels = [0.0,1.0]
for label in sorted(labels):
    print("Class %s precision = %s" % (label, metrics.precision(label)))
    print("Class %s recall = %s" % (label, metrics.recall(label)))
    print("Class %s F1 Measure = %s" % (label, metrics.fMeasure(label, beta=1.0)))

# Weighted stats
print("Weighted recall = %s" % metrics.weightedRecall)
print("Weighted precision = %s" % metrics.weightedPrecision)
print("Weighted F(1) Score = %s" % metrics.weightedFMeasure())
print("Weighted F(0.5) Score = %s" % metrics.weightedFMeasure(beta=0.5))
print("Weighted false positive rate = %s" % metrics.weightedFalsePositiveRate)
