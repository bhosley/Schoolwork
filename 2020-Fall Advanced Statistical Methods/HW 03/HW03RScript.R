# Load Boston data set
library(MASS)

mount(Boston)
par(mfrow=c(2,7))
plot(crim,  crim); abline(lm(crim~crim)) 
plot(zn,    crim); abline(lm(zn~crim)) 
plot(indus, crim); abline(lm(indus~crim)) 
plot(chas,  crim); abline(lm(chas~crim))
plot(nox,   crim); abline(lm(nox~crim)) 
plot(rm,    crim); abline(lm(rm~crim))  
plot(age,   crim); abline(lm(age~crim))  
plot(dis,   crim); abline(lm(dis~crim))  
plot(rad,   crim); abline(lm(rad~crim))  
plot(tax,   crim); abline(lm(tax~crim))    
plot(ptratio, crim); abline(lm(ptratio~crim))
plot(black, crim); abline(lm(black~crim))
plot(lstat, crim); abline(lm(lstat~crim))
plot(medv,  crim); abline(lm(medv~crim))




library(reshape2)

b <- melt(Boston, "crim")

ggplot(b,aes(crim,value)) + facet_grid(.~variable) 