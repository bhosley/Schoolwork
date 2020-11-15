library(MASS)
attach(Boston)
library( randomForest)
set.seed(1234)

train = sample(1:nrow(Boston), nrow(Boston)/2)
test=Boston[-train ,"crim"]
rf.boston= randomForest(crim~.,data=Boston , subset=train, mtry=6, importance =TRUE)
yhat.rf = predict(rf.boston ,newdata=Boston[-train ,])
mean((yhat.rf-test)^2)
