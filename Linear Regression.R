library(ggplot2)

# data wranglings
data <- read.csv("data/Ratios.csv")
hpindex <- read.csv("data/Dublin Location Indexes.csv")
working_data <- merge(data, hpindex)[,c(-2, -3)]

# linear regression so we can get coefficients and slope
LinearRegression <- lm(formula = Index ~ Ratio, data = working_data)

# creates linear regression plot
ggplot(working_data, aes(Index, Ratio))+
  labs(title="Linear Regression", x="HP Index", y="Article Ratios")+
  geom_point()+
  geom_smooth(method="lm", se=FALSE)+
  theme_classic()
