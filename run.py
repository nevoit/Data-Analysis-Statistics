import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import *
import numpy as np


def column_descriptive_statistics(df, column):
    """
    This function prints a statistics about each data column
    :param df:
    :param column:
    :return:
    """
    print('Column Name: {}'.format(column))
    df[column].fillna(value=0)
    print(describe(df[column]))
    print('Median: ' + str(np.median(df[column])))
    plt_column_hist(column, df)
    plt_column_box_plot(column, df)
    print('')


def plt_column_hist(column, df):
    """
    This function plots histogram for each df column
    :param column:
    :param df:
    :return:
    """
    fig, ax = plt.subplots()
    plt.xlabel('Column values')
    plt.ylabel('Num of repetitions')
    df.hist(column, ax=ax)
    fig.savefig('output\\{}_hist.png'.format(column))


def plt_column_box_plot(column, df):
    """
    This function plots box plot for each df column
    :param column:
    :param df:
    :return:
    """
    fig, ax = plt.subplots()
    plt.xlabel('Column')
    plt.ylabel('Num of repetitions')
    df.boxplot(column, ax=ax)
    fig.savefig('output\\{}_box_plot.png'.format(column))


def t_tests(df, field):
    alg1 = df[df['Paid'] == 0][field]
    alg2 = df[df['Paid'] == 1][field]
    print('{} T tests for unpaied and paid posts'.format(field))
    print('Levene test')
    print(levene(alg1, alg2))
    print('T test independent')
    print(ttest_ind(alg1, alg2))
    print('T test relative')
    print(ttest_rel(alg1, alg2))


def print_title(title):
    sep = '+' * 10
    print('\n {0} {1} {0}'.format(sep, title))


def read_data_set():
    """
    This function reads a excel file, fills NaN, prints all the columns and returns a data frame
    :return:
    """

    file_name = 'FacebookData.xlsx'
    df_facebook = pd.read_excel(file_name)
    df_facebook = df_facebook.fillna(0).replace(' ', 0).apply(pd.to_numeric)
    """
    Every record in the DB represents a post on the Facebook page of a company.    
    The research goal is to realize what are the factors (i.e., columns value) to popular posts.
    [1] Moro, S., Rita, P., & Vala, B. (2016). 
    Predicting social media performance metrics and evaluation of the impact on brand building: A data mining approach.
    Journal of Business Research, 69(9), 3341-3351.
    
    Columns Name                    |   Description
    ---------------------------------------------------------------------------------------------          
    Category	                    |   “1” – “Promotion” ; “2” – “Product”; 3 – “General”
    PostMonth	                    |   Month ID
    PostWeekday	                    |   Day ID
    PostHour	                    |   Hour ID
    Paid	                        |   Whether the company paid Facebook to prompt the post 
    LifetimePostTotalReach	        |   The number of people who saw a page post (unique users).
    LifetimePostTotalImpressions	|   The total number of times the post was viewed.
    LifetimeEngagedUsers	        |   The number of people who clicked the post (unique users).
    LifetimePostConsumers	        |   The total number of clicks on the post
    comment	                        |   The number of comments to the post
    like	                        |   The number of likes to the post
    share	                        |   The number of shares  to the post
    TotalInteractions	            |   The total interactions (comment + like + share)
    """
    print_title("Column headings")
    print(df_facebook.columns)
    return df_facebook


def start():
    df = read_data_set()

    print_title('Continuous variables')
    column_descriptive_statistics(df, 'comment')
    column_descriptive_statistics(df, 'like')
    column_descriptive_statistics(df, 'share')
    column_descriptive_statistics(df, 'LifetimePostTotalReach')

    print_title('Discrete variables')
    column_descriptive_statistics(df, 'Category')
    column_descriptive_statistics(df, 'Paid')
    column_descriptive_statistics(df, 'PostWeekday')

    print('Q3')
    print(ttest_1samp(df['share'], 25))

    t_tests(df, 'share')

    'Question 2.5'  # <---
    engine1 = [0.9, 0.6, 0.6, 0.5, 0.9, 0.6, 0.7, 0.7, 0.6, 0.6]
    engine2 = [0.95, 0.65, 0.65, 0.5, 0.9, 0.65, 0.75, 0.75, 0.6, 0.6]

    print(levene(engine1, engine2))
    print('T test independent')
    print(ttest_ind(engine1, engine2))
    print('T test relative')
    print(ttest_rel(engine1, engine2))


if __name__ == '__main__':
    start()
