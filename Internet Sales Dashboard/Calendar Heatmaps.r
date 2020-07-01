# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset <- data.frame(SalesAmount_USD, Weekday, Year, Monthweek, MonthName)
# dataset <- unique(dataset)
library(ggplot2)

ggplot(dataset, aes(Monthweek, Weekday, fill = SalesAmount_USD)) + 
  geom_tile(colour = "white") + 
  facet_grid(Year~MonthName) + 
  scale_fill_gradient(low="red", high="green") +
  labs(x="Week of Month",
       y="",
       title = "Time-Series Calendar Heatmap", 
       subtitle="Sales of Selected Product Category", 
       fill="Sales Amount")
