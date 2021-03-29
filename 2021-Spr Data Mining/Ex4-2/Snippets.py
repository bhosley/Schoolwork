$ pyspark

raw_df = spark.read.csv("/user/data/CSC533DM/titanic.csv", header=True, inferSchema=True)
raw_df.describe().show()

# Imputation

from pyspark.ml.feature import Imputer
imputer = Imputer(strategy='mean', inputCols=['Age'], outputCols=['ImputedAge'])
imputed_df = imputer.fit(filtered_df).transform(filtered_df)
imputed_df.show()

# String Indexer (1-3)

from pyspark.ml.feature import StringIndexer
indexed_df = StringIndexer(inputCol="Gender", outputCol="IndexedGender").fit(imputed_df).transform(imputed_df)
indexed_df.show(5)

# Create Features VectorIndexer

from pyspark.ml.feature import VectorAssembler
assembler = VectorAssembler(inputCols=['Pclass', 'SibSp', 'Parch', 'Fare', 'ImputedAge', 'IndexedGender'], outputCol='features')
features_df = assembler.transform(indexed_df)

# Splitting Dataset

(trainingData, testData) = features_df.randomSplit([0.8, 0.2])
features_df.count()
trainingData.count()
testData.count()

# trainingData

from org.apache.spark.ml.classification import RandomForestClassifier
rf = RandomForestClassifier(labelCol="Survived", featuresCol="features")
modelRF = rf.fit(trainingData)

# Evaluate

from org.apache.spark.ml.evaluation import BinaryClassificationEvaluator

predictions = modelRF.transform(testData)
evaluator = BinaryClassificationEvaluator(labelCol="Survived", predictionCol="predictions", metricName="Accuracy")
