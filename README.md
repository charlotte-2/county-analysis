# county-analysis

The propose of this project:
1. I want to check if there is a correlation between happiness and the rate of higher education in counties.(A county’s happiness rate = (income * homeownership) / commute. )

      a. Find the average happiness rating among all the counties in the US and then group the counties into two Groups.
      
         G1- Those counties whose happiness rating is above the average
         
         G2- Those counties whose happiness rating is below the average
         
      b. Then find the average higher education rate among counties in G1 (avgHappy). Do the same for counties in G2 (avgUnhappy). If the difference between G1 and G2 is more than 20, then the correlation is significant. If it is more than 5, there is a slight correlation, otherwise, we could not find any significant correlation.

2. I want to find and report all counties that are similar. Two counties are similar if all the information on them is within 2% of each other. To find all counties, whose properties (except county name and state) are within only 2%  different.
