from pyspark.ml.fpm import FPGrowth
from pyspark.sql.functions import col, split

df0 = spark.read.text("/user/data/CSC533DM/groceries.csv").toDF("csv")
df0.show()

df = df0.withColumn("items", split(col("csv"), ",").cast("array<string>"))
df.show()
df.show(truncate=False)

fpGrowth = FPGrowth(itemsCol="items", minSupport=0.175, minConfidence=0.6)
model = fpGrowth.fit(df)
model.freqItemsets.show()

fpGrowth = FPGrowth(itemsCol="items", minSupport=0.06, minConfidence=0.6)
model = fpGrowth.fit(df)
model.freqItemsets.show(truncate=False,n=100)

fpGrowth = FPGrowth(itemsCol="items", minSupport=0.05, minConfidence=0.6)
model = fpGrowth.fit(df)
model.freqItemsets.show(truncate=False,n=100)

fpGrowth = FPGrowth(itemsCol="items", minSupport=0.04, minConfidence=0.6)
model = fpGrowth.fit(df)
model.freqItemsets.show(truncate=False,n=100)

fpGrowth = FPGrowth(itemsCol="items", minSupport=0.04, minConfidence=0.3)
model = fpGrowth.fit(df)
model.associationRules.show()

fpGrowth = FPGrowth(itemsCol="items", minSupport=0.04, minConfidence=0.2)
model = fpGrowth.fit(df)
model.associationRules.show()

fpGrowth = FPGrowth(itemsCol="items", minSupport=0.04, minConfidence=0.1)
model = fpGrowth.fit(df)
model.associationRules.show()