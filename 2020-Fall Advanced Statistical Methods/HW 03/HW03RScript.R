# Load Boston data set
library(MASS)


attach(Boston)

lm.fit=lm(crim~medv)
plot(crim~medv)