lm.bayes <- function(y, x, tau.a, tau.b, alpha = 0.001, beta = 0.001, niter = 5000) {
n <- length(y)
a <- mean(y)
b <- 0
tau <- 1
result <- matrix(nrow = niter, ncol = 3)
for (i in 1:niter) {
a <- rnorm(1, mean = (tau/(n * tau + tau.a)) * sum(y - b * x), sd = 1/sqrt(n * tau +
tau.a))
b <- rnorm(1, mean = (tau * sum((y - a) * x))/(tau * sum(x^2) + tau.b), sd = 1/sqrt(tau *
sum(x^2) + tau.b))
tau <- rgamma(1, shape = alpha + n/2, rate = beta + 0.5 * sum((y - a - b * x)^2))
result[i, ] <- c(a, b, tau)
}
result
}

data2=data.frame(growth=c(12,10,8,11, 6,7), tannin=0:5)
growth.lm=lm.bayes(y=data2[,1], x=data2[,2], tau.a=0.001, tau.b=0.001, niter=10000)
# Drop the burn-in samples
growth.lm=growth.lm[-(1:2000),]
# posterior means
colSums(growth.lm)/8000


plot(cumsum(growth.lm[,1])/(1:8000), type="l", main="a", ylab="", xlab="")
plot(cumsum(growth.lm[,2])/(1:8000), type="l", main="b", ylab="", xlab="")
plot(cumsum(growth.lm[,3])/(1:8000), type="l", main="tau", ylab="", xlab="")
