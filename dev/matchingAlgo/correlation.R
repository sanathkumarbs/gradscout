library(data.table) #loading data.table library in my R workspace
library(ggplot2) #loading ggplot2 library in my R workspace
library(corrplot) #loading corrplot library in my R workspace

GS <- data.table(University.Quantitative.Data) #loading dataset University.Quantitative.Data
summary(GS) #summarizing the dataframe
gs <- cor(GS) #generating the correlation values
corrplot(gs, method="number") #creating the correlation matrix