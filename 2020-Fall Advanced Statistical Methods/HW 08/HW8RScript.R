library(MASS)
attach(Boston)
library(e1071)
set.seed(1234)

b = Boston
# Remove Chas variable
b <- subset(b,select=-c(chas))
# Normalize the Data (mean=0, SD = 1)
b <- as.data.frame(scale(b))
# Crim as a Factor(High = 1, Low = 0)
b$crim <- ifelse(b$crim > 0, 1, 0)
b$crim <- as.factor(b$crim)

# Separate a Training and Testing Set
ind = sort(sample(nrow(b), nrow(b)*0.8))
b_train <- b[ind,]
b_test <- b[-ind,]

# Training both a Linear and Polynomial Model
svm_lin=svm(crim~., data=b_train, kernel ="linear", cost=1, scale=FALSE)
svm_poly=svm(crim~., data=b_train, kernel ="polynomial", cost=1, scale=FALSE)

# View Summaries of Both Models
summary(svm_lin)
summary(svm_poly)

# Calculate Predictions
pred_lin = predict(svm_lin, b_test)
pred_poly = predict(svm_poly, b_test)
  
# Tabulate Predictions with Truth
table(predict=pred_lin, truth=b_test$crim)
table(predict=pred_poly, truth=b_test$crim)
