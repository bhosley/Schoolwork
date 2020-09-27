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
medCrim = median(b$crim)
b$highCrim = if(b$crim < medCrim) 0 else 1
summary(b$highCrim)

set.seed(123)
train_ind <- sample(seq_len(nrow(b)), size = floor(0.8 * nrow(b)))
train <- b[train_ind, ]
test <- b[-train_ind, ]

# Logistic Regression
glm.fits=glm(crim~rad+tax+lstat, data=train, family=binomial)
summary(glm.fits)

glm.pred=predict(glm.fits, test, type="response")
mse(test$crim,glm.pred)

# Linear Discriminant Analysis
lda.fit = lda(crim~rad+tax+lstat, data=train)
lda.pred=predict(lda.fit, test, type="response")
mse(test$crim,lda.pred)
