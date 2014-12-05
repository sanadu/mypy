from pandas import DataFrame, Series

import pandas as pd
import numpy as np

def create_dataframe():
    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    d = {'country_name' : Series(countries),
         'gold': Series(gold),
         'silver': Series(silver),
         'bronze': Series(bronze)}
    olympic_medal_counts_df = pd.DataFrame(d, columns=['country_name', 'gold','silver','bronze'])
    return olympic_medal_counts_df

def avg_medal_count():
    olympic_medal_counts_df = create_dataframe()
    olympic_medal_counts_grouped_filtered_df = olympic_medal_counts_df[olympic_medal_counts_df['gold'] > 0]
    olympic_medal_counts_grouped_avg_df = olympic_medal_counts_grouped_filtered_df.mean()
    avg_bronze_at_least_one_gold = olympic_medal_counts_grouped_avg_df['bronze']
    return avg_bronze_at_least_one_gold

def avg_medal_count2():
    olympic_medal_counts_df = create_dataframe()
    olympic_medal_counts_df['sum'] = olympic_medal_counts_df['gold']+olympic_medal_counts_df['silver']+olympic_medal_counts_df['bronze']
    olympic_medal_counts_filtered_df = olympic_medal_counts_df[['gold','silver','bronze']][olympic_medal_counts_df['sum']>0]
    return olympic_medal_counts_filtered_df.apply(np.mean, axis=0)

def numpy_dot():
    '''
    Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each 
    bronze medal.  

    Using the numpy.dot function, create a new dataframe called 
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.
           
    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    points =[4,2,1]
    
    d = {'gold': Series(gold),
         'silver': Series(silver),
         'bronze': Series(bronze)}
    olympic_medal_counts_df = pd.DataFrame(d, columns=['gold','silver','bronze'])
    s = np.dot(olympic_medal_counts_df,points)
    dic = {'country_name': countries, 'points': s}
    olympic_points_df = pd.DataFrame(dic, columns=['country_name','points'])
    return olympic_points_df

print(numpy_dot())