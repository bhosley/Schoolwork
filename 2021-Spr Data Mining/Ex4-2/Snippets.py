$ pyspark

raw_df = spark.read.csv("/user/data/CSC533DM/titanic.csv", header=True, inferSchema=True)
raw_df.describe().show()

# Imputation

from pyspark.ml.feature import Imputer
imputer = Imputer(strategy='mean', inputCols=['Age'], outputCols=['ImputedAge'])
filtered_df = raw_df.select(['Survived', 'Pclass', 'Gender', 'Age', 'SibSp', 'Parch', 'Fare'])
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
trainingData.count()
testData.count()
trainingData.count() + testData.count()
features_df.count()

# trainingData

from pyspark.ml.classification import RandomForestClassifier
rf = RandomForestClassifier(labelCol="Survived", featuresCol="features")
modelRF = rf.fit(trainingData)

# Evaluate

from pyspark.ml.evaluation import BinaryClassificationEvaluator
predictions = modelRF.transform(testData)
evaluator = BinaryClassificationEvaluator(labelCol="Survived", rawPredictionCol="prediction", metricName="areaUnderROC")
evaluator.evaluate(predictions)
evaluator = BinaryClassificationEvaluator(labelCol="Survived", rawPredictionCol="prediction", metricName="areaUnderPR")
evaluator.evaluate(predictions)