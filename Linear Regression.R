library(ggplot2)
library(dplyr)

# data wranglings
data <- read.csv("data/Ratios.csv")
hpindex <- read.csv("data/Dublin Location Indexes.csv")
working_data <- merge(data, hpindex)[,c(-2, -3)]

# creates linear regression plot
ggplot(working_data, aes(Index, Ratio))+
  labs(title="Linear Regression", x="HP Index", y="Article Ratios")+
  geom_point()+
  geom_smooth(method="lm", se=FALSE)+
  theme_classic()

remove_extremes <- working_data %>%
  filter(Ratio != 1) %>%
  filter(Ratio != 0)

ggplot(remove_extremes, aes(Index, Ratio))+
  labs(title="Linear Regression", x="HP Index", y="Article Ratios")+
  geom_point()+
  geom_smooth(method="lm", se=FALSE)+
  theme_classic()

# linear regression so we can get coefficients and slope
LinearRegression1 <- lm(formula = Index ~ Ratio, data = working_data)
LinearRegression2 <- lm(formula = Index ~ Ratio, data = remove_extremes)
summary(LinearRegression1)
summary(LinearRegression2)
LinearRegression1
LinearRegression2
