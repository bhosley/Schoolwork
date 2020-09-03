# Load Boston data set from the MASS library
library(MASS)

# How many rows are in this data set?
nrow(Boston)

# How many columns?
ncol(Boston)

# Make some pairwise scatterplots of the predictors (columns) in this data set. Describe your findings.
pairs(Boston)

# Do any of the suburbs of Boston appear to have particularly high crime rates? Tax rates? Pupil-teacher ratios? Comment on the range of each predictor.
ggplot(stack(Boston), aes(x = ind, y = values)) +
     geom_boxplot(aes(fill= ind)) +
     theme(legend.position = "none") 

# How many of the suburbs in this data set bound the Charles river?
library(plyr)
count(Boston$chas, vars = 1)