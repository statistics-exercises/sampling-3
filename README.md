# Pandas and statistics

As discussed in the previous exercises each of the following columns:

1. the films runtime in minutes
2. the films rating on IMDB
3. the number of votes that were cast to determine the rating
4. the amount of money the film made 
5. the metascore for the film.

from the panda data frame that we have been learning about in the last couple of tasks contains a series of samples from a distribution.  We now know that if we are given a series of samples from a distribution we can calculate various statistics from the data.  For instance, we can calculate the mean, the median, the range and percentiles.  A nice feature of the panda data frame is that we can calculate these quantities directly from the data frame.  For example, if we want to calculate the mean running time we can use the command:

````
mean_time = movies_df['runtime'].mean()
```` 
 
Furthermore, there are similar commands that we can use for the other statistics we know about:

1. `median()` returns the median
2. `min()` returns the lowest value
3. `max()` returns the highest value
4. `quantile(p)` returns the `100p`th percentile.  The variable `p` here must be between 0 and 1.

With that in mind to complete the exercise you need to set the variables below as follows:

1. `runtime_mean` = the mean runtime for the films
2. `rating_min` = the lowest rating for any of the films in the data base
3. `rating_max` = the highest rating for any of the films in the data base
4. `votes_median` = the median number of votes that films get on IMDB
5. `metascore_p25` = the 25th percentile of the metascores
6. `metascore_p75` = the 75th percentile of the metascores 
