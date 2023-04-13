library(ggplot2)
library(dplyr)

# data wranglings
newsarticles <- read.csv("News Article Data/Ratios.csv")
twitterdata <- read.csv("Twitter Data/Ratios.csv")

hpindex <- read.csv("data/Dublin Location Indexes.csv")

newsarticles <- merge(newsarticles, hpindex)
twitterdata <- merge(twitterdata, hpindex)


# creates linear regression plot
ggplot(newsarticles, aes(Index, Ratio))+
  labs(title="Linear Regression of data from news articles", x="HP Index", y="Article Ratios")+
  geom_point()+
  geom_smooth(method="lm", se=FALSE)+
  theme_classic()


ggplot(twitterdata, aes(Index, Ratio))+
  labs(title="Linear Regression of twitter data", x="HP Index", y="Article Ratios")+
  geom_point()+
  geom_smooth(method="lm", se=FALSE)+
  theme_classic()

# Removes any cases with less than 10 occurences
twitterdata <- twitterdata %>%
  filter(Total.number.of.articles >= 10) 

newsarticles <- newsarticles %>%
  filter(Total.number.of.articles >= 10) 


# linear regression so we can get coefficients and slope
LinearRegression1 <- lm(formula = Index ~ Ratio, data = newsarticles)
LinearRegression2 <- lm(formula = Index ~ Ratio, data = twitterdata)
summary(LinearRegression1)
summary(LinearRegression2)
LinearRegression1
LinearRegression2
