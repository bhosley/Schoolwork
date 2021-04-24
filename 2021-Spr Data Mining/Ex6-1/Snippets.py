$ pyspark

# raw_df = spark.read.option("header", "true").option("inferSchema", "true").csv("/user/data/CSC533DM/titanic.csv")
raw_df = spark.read.csv("/user/data/CSC533DM/titanic.csv", header=True, inferSchema=True)
raw_df.describe().show()

filtered_df = raw_df.select(['Survived', 'Pclass', 'Gender', 'Age', 'SibSp', 'Parch', 'Fare'])


filtered_df.select('Fare').describe().show()

## Fare
quantiles = filtered_df.approxQuantile("Fare", [0.25, 0.75], 0.0)
Q1, Q3 = quantiles[0], quantiles[1]
IQR = Q3-Q1
fareLowerRange, fareUpperRange = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
fareLowerRange, fareUpperRange

trimmed_df = filtered_df \
    .filter(filtered_df.Fare > fareLowerRange) \
    .filter(filtered_df.Fare < fareUpperRange)
trimmed_df.count()


## Age

# Check for Nulls
filtered_df.filter(filtered_df.Age.isNull()).count()
# Impute missing values with arithmetic mean
from pyspark.ml.feature import Imputer
imputer = Imputer(strategy='mean', inputCols=['Age'], outputCols=['ImputedAge'])
filtered_df = imputer.fit(filtered_df).transform(filtered_df)

# Find IQR 
quantiles = filtered_df.approxQuantile('ImputedAge', [0.25, 0.75], 0.0)
Q1, Q3 = quantiles[0], quantiles[1]
IQR = Q3-Q1
ageLowerRange, ageUpperRange = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
# Count outliers
filtered_df.filter(filtered_df.ImputedAge < ageLowerRange).count() + \
filtered_df.filter(filtered_df.ImputedAge > ageUpperRange).count()

# Re-trim
trimmed_df = filtered_df \
    .filter(filtered_df.Fare > fareLowerRange) \
    .filter(filtered_df.Fare < fareUpperRange) \
    .filter(filtered_df.ImputedAge > ageLowerRange) \
    .filter(filtered_df.ImputedAge < ageUpperRange)
trimmed_df.count()


## SibSp

# Check for Nulls
filtered_df.filter(filtered_df.SibSp.isNull()).count()
# Find IQR 
quantiles = filtered_df.approxQuantile('SibSp', [0.25, 0.75], 0.0)
Q1, Q3 = quantiles[0], quantiles[1]
IQR = Q3-Q1
sibSpLowerRange, sibSpUpperRange = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
# Count outliers
filtered_df.filter(filtered_df.SibSp < sibSpLowerRange).count() + \
filtered_df.filter(filtered_df.SibSp > sibSpUpperRange).count()

# Trim
trimmed_df = trimmed_df \
    .filter(trimmed_df.SibSp > sibSpLowerRange) \
    .filter(trimmed_df.SibSp < sibSpUpperRange)
trimmed_df.count()


## Parch

# Check for Nulls
filtered_df.filter(filtered_df.Parch.isNull()).count()

# Find IQR 
quantiles = filtered_df.approxQuantile('Parch', [0.25, 0.75], 0.0)
Q1, Q3 = quantiles[0], quantiles[1]
IQR = Q3-Q1
parchLowerRange, parchUpperRange = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
# Count outliers
filtered_df.filter(filtered_df.Parch < parchLowerRange).count() + \
filtered_df.filter(filtered_df.Parch > parchUpperRange).count()

# Check IQR
parchLowerRange, parchUpperRange
# Check result if Applied to trim
trimmed_df.filter(trimmed_df.Parch == parchUpperRange).count()

# Trim
trimmed_df = trimmed_df.filter(trimmed_df.Parch == parchUpperRange)
trimmed_df.count()

######### Redoing 4-2
