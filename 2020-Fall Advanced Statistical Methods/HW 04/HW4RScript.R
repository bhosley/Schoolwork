# Load Boston data set
library(Metrics)
library(MASS)
attach(Boston)

# Determine best Classifiers
dim(Boston)
cor(Boston[,-14])

# Scale Crime to 0<y<1
summary(crim)
b <- Boston
b$crim = b$crim/max(b$crim)
summary(b$crim)

set.seed(123)
train_ind <- sample(seq_len(nrow(b)), size = floor(0.8 * nrow(b)))
train <- b[train_ind, ]
test <- b[-train_ind, ]

# Logistic Regression
glm.fits=glm(crim~rad+tax+lstat, data=train, family=binomial)
summary(glm.fits)

glm.probs=predict(glm.fits, test, type="response")
mse(test$crim,glm.probs)

