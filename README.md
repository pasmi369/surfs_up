## Surfs_up
  ### Overview of the analysis:
  - Weather analysis for surfing and Ice-cream shop business.

  ### Purpose of the analysis:
  - The purpose of this project is to analyze Weather Data using SQLite and Flask to see if it is worth openning a surf shop on Oahu island.
  - Project involves gathering and analysing data based on the seasons, temperatures, percipitations.
  - Based on the anlaysis which season could effect surf and ice-cream shop business.

## Results:
### Results of the analysis based on the temperature data for months of June and December 
- ### June Temperature
![June Temperatures](./Resources/june_temps.png)

Data count for June Tempratures are 1700 entries.
  1. The average temperature is 74.94 degrees fahrenheit
  2. The minimum temperature is 64 degrees fahrenheit
  3. The maximum temperature is 85 degrees fahrenheit


- ### December Temperature
![December Tempratures](./Resources/dec_temps.png)

Data count for December temperatures are 1517 entries.
  1. The average temperature is 71.04 degrees fahrenheit
  2. The minimum temperature is 56 degrees fahrenheit
  3. The maximum temperature is 83 degrees fahrenheit


## Summary:

![June Precipitation](./Resources/june_prcp.png)   - ![December Precipitation](./Resources/dec_prcp.png)

As per the above table, the observations are that opening a surf shop would be a smart investment. This is because there is an enjoyable average temperature in two months that are 6 months apart from one another. That shows that for most months of the year, there will be enjoyable temperature for people to come and use the surf shop.
To dive a little deeper, we looked at the percipitation levels through the two months as well. The major takeaways from this analysis are:

- The minimum,mean and maximum temperatures in June is more than that of December, which is suitable for the surfing and ice-cream shop. The standard deviation in temperature for June is less than that of December.
- Also, the mean maximum precipitation in June is less than that of December, which is suitable for the surfing and ice-cream shop. The standard deviation in precipitation for June is less than that of December.
- The counts of precipitation and temperature for the month of June is also less than that of December. Because of the more standard deviation in the month of December, the weather across all the stations varies more as compared to the month of June.
- As per the above observations, the surfing and ice-cream shop will make more profit in the month of June as compared to the month of December.

Recommendations
- For further analysis, we should increase our range of summer and winter months for a better and indepth analysis.
- Also, looking at this further analysis it shows that there is little amount of percipitation on a normal day, but there is still days with excessive rainfall. This shows that the surf shop will be able to stay open on most days while a few rainy days will help keep the island ecosystem lush and inviting to people wanting to visit the surf shop.
- We can also do a seperate analysis for the best stations using some kind of filter like based on the total number of observations.
- We can also drop the stations which are outliers in terms of data for our analysis.














