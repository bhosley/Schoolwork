# Load Libraries
library(MASS)
attach(Boston)
library(leaps)

# 1.1 Best Subset Selection
regfit.full=regsubsets (crim~.,Boston)
summary(regfit.full)
## Output >
regfit.full=regsubsets (crim~.,data=Boston ,nvmax=13)
reg.summary =summary (regfit.full)
par(mfrow=c(2,2))
plot(reg.summary$rss ,xlab="Number of Variables ",ylab="RSS", type="l")
plot(reg.summary$adjr2 ,xlab="Number of Variables ", ylab="Adjusted RSq",type="l")
which.max(reg.summary$adjr2)
points (8,reg.summary$adjr2[8], col="red",cex=2,pch =20)
plot(reg.summary$cp ,xlab="Number of Variables ",ylab="Cp", type='l')
which.min(reg.summary$cp)
points (8,reg.summary$cp [8], col ="red",cex=2,pch =20)
plot(reg.summary$bic ,xlab="Number of Variables ",ylab="BIC", type='l')
which.min(reg.summary$bic )
points (3,reg.summary$bic [3],col="red",cex=2,pch =20)
## Test
set.seed(1)
train=sample(c(TRUE ,FALSE), nrow(Boston),rep=TRUE)
test=(!train)
regfit.best=regsubsets(crim~.,data=Boston[train ,], nvmax=13)
test.mat=model.matrix(crim~.,data=Boston[test ,])
val.errors =rep(NA ,13)
for(i in 1:13){coefi=coef(regfit.best ,id=i)
  pred=test.mat[,names(coefi)]%*%coefi
  val.errors[i]=mean((Boston$crim[test]-pred)^2)
}
## Cross-Validation
predict.regsubsets = function(object , newdata ,id ,...){
  form=as.formula (object$call [[2]])
  mat=model.matrix(form ,newdata )
  coefi=coef(object ,id=id)
  xvars=names(coefi)
  mat[,xvars]%*%coefi
}
k <- 10
folds=sample (1:k,nrow(Boston),replace=TRUE)
cv.errors=matrix (NA,k,13, dimnames=list(NULL, paste (1:13)))
for(j in 1:k){
  best.fit <- regsubsets(crim~., data=Boston[folds!=j,],nvmax=13)
  for(i in 1:13){
    pred <- predict(best.fit ,Boston[folds ==j,], id=i)
    cv.errors[j,i] <- mean(( Boston$crim[folds==j]-pred)^2)
  }
}
mean.cv.errors=apply(cv.errors ,2, mean)
mean.cv.errors
par(mfrow=c(1,1))
plot(mean.cv.errors ,type='b')
reg.best=regsubsets (crim~.,data=Boston , nvmax=13)
coef(reg.best ,12)

# 1.2 Ridge Regression
library(glmnet)

x=model.matrix(crim~.,Boston )[,-1]
y=Boston$crim

grid=10^seq(10,-2, length =100)
ridge.mod=glmnet (x,y,alpha=0, lambda=grid)
dim(coef(ridge.mod))

train=sample (1: nrow(x), nrow(x)/2)
test=(-train)
y.test=y[test]
## Cross-validation
cv.out=cv.glmnet(x[train ,],y[ train],alpha=0)
plot(cv.out)
bestlam =cv.out$lambda.min
bestlam
ridge.pred=predict (ridge.mod ,s=bestlam ,newx=x[test ,])
mean((ridge.pred -y.test)^2)

# 1.3 The Lasso
lasso.mod=glmnet(x[train ,],y[ train],alpha=1, lambda =grid)
plot(lasso.mod)
cv.out=cv.glmnet(x[train ,],y[ train],alpha=1)

plot(cv.out)
bestlam =cv.out$lambda.min
lasso.pred=predict (lasso.mod ,s=bestlam ,newx=x[test ,])
mean((lasso.pred -y.test)^2)

out=glmnet (x,y,alpha=1, lambda=grid)
lasso.coef=predict (out ,type="coefficients",s= bestlam) [1:14,]
lasso.coef

# 1.4 PCR
library(pls)
set.seed(1)
pcr.fit=pcr(crim~., data=Boston, scale=TRUE, validation ="CV")
validationplot(pcr.fit ,val.type="MSEP")

pcr.pred=predict (pcr.fit ,x[test ,],ncomp =7)
mean((pcr.pred -y.test)^2)


# 2.1 Validation Set Error

# 2.2 Cross-Validation

# 3 Which features are used in the chosen model?
