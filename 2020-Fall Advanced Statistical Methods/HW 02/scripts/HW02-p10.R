# Load Boston data set from the MASS library
library(MASS)

# How many rows are in this data set?
nrow(Boston)

# How many columns?
ncol(Boston)

# Make some pairwise scatterplots of the predictors (columns) in this data set. Describe your findings.
pairs(Boston)

# Do any of the suburbs of Boston appear to have particularly high crime rates? Tax rates? Pupil-teacher ratios? Comment on the range of each predictor.
b <- Boston
# Scale data to be relative
b[,-1] = apply(b[,-1],2,function(x){x/max(x)})
b$crim <- b$crim/max(b$crim)

b$id <- rownames(b) ## Part of Attempt to offer labels to outlier data

ggplot(melt(b, id.vars = "id"), aes(x = variable, y = value)) +
     geom_boxplot(aes(fill= variable)) +
     theme(legend.position = "none") 

# How many of the suburbs in this data set bound the Charles river?
library(plyr)
count(Boston$chas, vars = 1)