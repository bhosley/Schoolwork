$ pyspark

from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import LogisticRegression
training = spark.createDataFrame([
    (1.0, Vectors.dense([0.0, 1.1, 0.1])),
    (0.0, Vectors.dense([2.0, 1.0, -1.0])),
    (0.0, Vectors.dense([2.0, 1.3, 1.0])),
    (1.0, Vectors.dense([0.0, 1.2, -0.5]))], ["label", "features"])

###### 1 #####

# Create a LogisticRegression instance. This instance is an Estimator.
lr = LogisticRegression(maxIter=10, regParam=0.01)
# Print out the parameters, documentation, and any default values.
print("LogisticRegression parameters:\n" + lr.explainParams() + "\n")

# Learn a LogisticRegression model. This uses the parameters stored in lr.
model1 = lr.fit(training)

print("Model 1 was fit using parameters: ")
print(model1.extractParamMap())

##### 2 #####

paramMap = {lr.maxIter: 20}
paramMap[lr.maxIter] = 30 # Specify 1 Param, overwriting the original maxIter.
paramMap.update({lr.regParam: 0.1, lr.threshold: 0.55}) # Specify multiple Params.

paramMap2 = {lr.probabilityCol: "myProbability"} # Change output column name
paramMapCombined = paramMap.copy()
paramMapCombined.update(paramMap2)

model2 = lr.fit(training, paramMapCombined)
print("Model 2 was fit using parameters: ")
print(model2.extractParamMap())

##### 3 #####

test = spark.createDataFrame([
    (1.0, Vectors.dense([-1.0, 1.5, 1.3])),
    (0.0, Vectors.dense([3.0, 2.0, -0.1])),
    (1.0, Vectors.dense([0.0, 2.2, -1.5]))], ["label", "features"])

prediction = model2.transform(test)
result = prediction.select("features", "label", "myProbability", "prediction").collect()

for row in result:
    print("features=%s, label=%s -> prob=%s, prediction=%s"
        % (row.features, row.label, row.myProbability, row.prediction))

##### 4 #####

from pyspark.ml import Pipeline
from pyspark.ml.feature import HashingTF, Tokenizer

training = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0)
], ["id", "text", "label"])

tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10, regParam=0.001)
pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])

model = pipeline.fit(training)

test = spark.createDataFrame([
    (4, "spark i j k"),
    (5, "l m n"),
    (6, "spark hadoop spark"),
    (7, "apache hadoop")
], ["id", "text"])

prediction = model.transform(test)
selected = prediction.select("id", "text", "probability", "prediction")
for row in selected.collect():
    rid, text, prob, prediction = row
    print("(%d, %s) --> prob=%s, prediction=%f" % (rid, text, str(prob), prediction))

##### 5 #####

from pyspark.ml.linalg import Vectors
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline
from pyspark.ml.feature import HashingTF, Tokenizer, VectorAssembler, VectorIndexer
from pyspark.sql.functions import split

schema = 'TweetId LONG, Username STRING, Timestamp TIMESTAMP, Followers INT, Friends INT, Retweets INT, Favorites INT, Entities STRING, Sentiment STRING, Mentions STRING, Hashtags STRING, URLs STRING'

# TweetId LONG, 
# Username STRING, 
# Timestamp TIMESTAMP, 
# Followers INT, 
# Friends INT, 
# Retweets INT, 
# Favorites INT, 
# Entities STRING, 
# Sentiment STRING, 
# Mentions STRING, 
# Hashtags STRING, 
# URLs STRING

df = spark.read.schema(schema) \
    .option("delimiter", "\t") \
    .option("timestampFormat", "EEE MMM dd HH:mm:ss Z yyyy") \
    .csv("/user/data/CSC534BDA/COVID19-Retweet/TweetsCOV19-train.tsv")
df.printSchema()

## Fix Sentiment

sent_col = split(df['Sentiment'], ' ')
df = df.withColumn('Positivity', sent_col.getItem(0).cast('INT'))
df = df.withColumn('Negativity', sent_col.getItem(1).cast('INT'))

## Split Data

assembler = VectorAssembler( \
    outputCol='features', \
    inputCols=['Followers', 'Friends', 'Positivity', 'Negativity'])
features_df = assembler.transform(df)

(trainingData, testData) = features_df.randomSplit([0.8, 0.2])

## Generalized Linear Regression

from pyspark.ml.regression import GeneralizedLinearRegression

glr = GeneralizedLinearRegression(labelCol='Retweets', featuresCol='features', \
    family="gaussian", link="identity", maxIter=10, regParam=0.3)
glr_model = glr.fit(trainingData)

glr_predictions = glr_model.transform(testData)
glr_evaluator = RegressionEvaluator(predictionCol="prediction", \
    labelCol="Retweets",metricName="r2")
print("R Squared (R2) on test data = %g" % \
    glr_evaluator.evaluate(glr_predictions))
glr_predictions.select("prediction","Retweets","features").show(5)


## Decision Tree Regression

from pyspark.ml.regression import DecisionTreeRegressor

dt = DecisionTreeRegressor(labelCol='Retweets', featuresCol='features')
dt_model = dt.fit(trainingData)

dt_predictions = dt_model.transform(testData)
dt_evaluator = RegressionEvaluator(predictionCol="prediction", \
    labelCol="Retweets",metricName="r2")
print("R Squared (R2) on test data = %g" % \
    dt_evaluator.evaluate(dt_predictions))
dt_predictions.select("prediction","Retweets","features").show(5)


##### Isotonic Regression

from pyspark.ml.regression import IsotonicRegression

ir = IsotonicRegression(labelCol='Retweets', featuresCol='features', regParam=0.3)
ir_model = ir.fit(trainingData)

ir_predictions = ir_model.transform(testData)
ir_evaluator = RegressionEvaluator(predictionCol="prediction", \
    labelCol="Retweets",metricName="r2")
print("R Squared (R2) on test data = %g" % \
    ir_evaluator.evaluate(ir_predictions))
ir_predictions.select("prediction","Retweets","features").show(5)


### log regression

from pyspark.ml.classification import LogisticRegression

lr = LogisticRegression(labelCol='Retweets', featuresCol='features', maxIter=10, regParam=0.001)
lr_pipeline = Pipeline(stages=[lr])
lr_model = lr_pipeline.fit(trainingData)

lr_predictions = lr_model.transform(testData)
lr_evaluator = RegressionEvaluator(predictionCol="prediction", \
    labelCol="Retweets",metricName="r2")
print("R Squared (R2) on test data = %g" % \
    lr_evaluator.evaluate(lr_predictions))
lr_predictions.select("prediction","Retweets","features").show(5)


## glr revisited

from pyspark.ml.linalg import Vectors
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.ml.feature import HashingTF, Tokenizer, VectorAssembler, VectorIndexer
from pyspark.sql.functions import split

schema = 'TweetId LONG, Username STRING, Timestamp TIMESTAMP, Followers INT, Friends INT, Retweets INT, Favorites INT, Entities STRING, Sentiment STRING, Mentions STRING, Hashtags STRING, URLs STRING'

df = spark.read.schema(schema) \
    .option("delimiter", "\t") \
    .option("timestampFormat", "EEE MMM dd HH:mm:ss Z yyyy") \
    .csv("/user/data/CSC534BDA/COVID19-Retweet/TweetsCOV19-train.tsv")
df.printSchema()

sent_col = split(df['Sentiment'], ' ')
df = df.withColumn('Positivity', sent_col.getItem(0).cast('INT'))
df = df.withColumn('Negativity', sent_col.getItem(1).cast('INT'))

(trainingData, testData) = df.randomSplit([0.8, 0.2])

tokenizer = Tokenizer(inputCol="Entities", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="Words")
assembler = VectorAssembler(outputCol='features', \
    inputCols=['Followers', 'Friends', 'Favorites', 'Positivity', 'Negativity'])

estimator = LogisticRegression(labelCol='Retweets', featuresCol='features', maxIter=10, regParam=0.001)

pipeline = Pipeline(stages=[tokenizer, hashingTF, assembler, lr])
model = pipeline.fit(trainingData)

# Test

predictions = model.transform(testData)
evaluator = RegressionEvaluator(predictionCol="prediction", \
    labelCol="Retweets",metricName="r2")
print("R Squared (R2) on test data = %g" % \
    evaluator.evaluate(predictions))
predictions.select("prediction","Retweets","features").show(5)



predictions = model.transform(testData)
evaluator = RegressionEvaluator(predictionCol="prediction", \
    labelCol="Retweets",metricName="mse")
print("Mean Squared (MSE) on test data = %g" % \
    evaluator.evaluate(predictions))
predictions.select("prediction","Retweets","features").show(5)
