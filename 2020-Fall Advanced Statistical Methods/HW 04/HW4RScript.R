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
b$highCrim <- ifelse(b$crim < medCrim, 0, 1)
summary(b$highCrim)

set.seed(123)
train_ind <- sample(seq_len(nrow(b)), size = floor(0.8 * nrow(b)))
train <- b[train_ind, ]
test <- b[-train_ind, ]

# Logistic Regression
glm.fits=glm(highCrim~rad+tax+lstat, data=train, family=binomial)
summary(glm.fits)

glm.pred=predict(glm.fits, test, type="response")
mse(test$highCrim,glm.pred)

# Linear Discriminant Analysis
lda.fit = lda(highCrim~rad+tax+lstat, data=train)
lda.fit
lda.pred=predict(lda.fit, test)
names(lda.pred)
lda.class=lda.pred$class
table(lda.class, test$highCrim)

# Take 2
lda.fit = lda(highCrim~rad+tax+lstat+nox+dis, data=train)
lda.fit
lda.pred=predict(lda.fit, test)
names(lda.pred)
lda.class=lda.pred$class
table(lda.class, test$highCrim)

# KNN

