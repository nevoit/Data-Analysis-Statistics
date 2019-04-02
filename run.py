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
    assert isinstance(df, pd.DataFrame)
    column_data = [x for x in (df[column].tolist()) if x != ' ']
    temp_df = pd.DataFrame()
    temp_df[column] = np.array(column_data)
    print('Name ' + column)
    print(df[column].describe(include='all'))

    describ = describe(column_data)
    print('Variance ' + str(describ.variance))
    print('Kurtosis ' + str(describ.kurtosis))
    print('Skewness ' + str(describ.skewness))
    print('Median: ' + str(np.median(column_data)))

    plt_column_hist(column, temp_df)
    plt_column_box_plot(column, temp_df)
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
    plt.ylabel('Values')
    df.boxplot(column, ax=ax)
    fig.savefig('output\\{}_box_plot.png'.format(column))


def t_tests(df, column):
    # TODO: I'm not sure about that
    alg1 = df[df['Paid'] == 0][column]
    alg2 = df[df['Paid'] == 1][column]
    alg1 = np.array([x for x in alg1 if x != ' '])
    alg2 = np.array([x for x in alg2 if x != ' '])
    print('{} T tests for un-paid and paid posts'.format(column))
    print('Levene test')
    levene_res = levene(alg1, alg2)
    print(levene_res)
    print('T test independent')
    var_equal = True if levene_res.pvalue > 0.05 else False
    print("Variance is equal: " + str(var_equal))
    print(ttest_ind(alg1, alg2, equal_var=var_equal))
    # print('T test relative')
    # print(ttest_rel(alg1, alg2))
    print()


def print_title(title):
    sep = '+' * 10
    print('\n{0} {1} {0}'.format(sep, title))


def read_data_set(file_name):
    """
    This function reads a excel file, fills NaN, prints all the columns and returns a data frame
    :return:
    """
    df_facebook = pd.read_excel(file_name)
    # df_facebook = df_facebook.fillna(0).replace(' ', 0).apply(pd.to_numeric)
    print_title("Column headings")
    print(df_facebook.columns)
    return df_facebook


def t_test_one_sample_summary(df, column_name, num):
    column_data = [x for x in (df[column_name].tolist()) if x != ' ']
    temp_df = pd.DataFrame()
    temp_df[column_name] = np.array(column_data)

    print("Degrees of Freedom: {}".format(temp_df[column_name].count() - 1))
    print("The mean is: {}".format(temp_df[column_name].mean()))
    print(ttest_1samp(temp_df[column_name], num))
    print()


def analyze_data_set(filename):
    df = read_data_set(filename)

    print_title('Q2.1')
    print_title('Continuous variables')
    column_descriptive_statistics(df=df, column='comment')
    column_descriptive_statistics(df=df, column='like')
    column_descriptive_statistics(df=df, column='share')
    column_descriptive_statistics(df=df, column='LifetimePostTotalReach')

    print_title('Q2.2')
    print_title('Discrete variables')
    column_descriptive_statistics(df=df, column='Category')
    column_descriptive_statistics(df=df, column='Paid')
    column_descriptive_statistics(df=df, column='PostWeekday')

    print_title('Q2.3')
    print_title('T test, share h_0 = 25')
    t_test_one_sample_summary(df=df, column_name='share', num=25)

    print_title('Q2.4')
    print_title('T test ...')
    # t_tests(df, 'comment')
    # t_tests(df, 'like')
    t_tests(df, 'share')
    # t_tests(df, 'LifetimePostTotalReach')

    print_title('Comparing Results from Different Methods')


def comparing_different_methods():
    # TODO: I'm not sure about that
    methods_one = [0.9, 0.6, 0.6, 0.5, 0.9, 0.6, 0.7, 0.7, 0.6, 0.6]
    methods_second = [0.95, 0.65, 0.65, 0.5, 0.9, 0.65, 0.75, 0.75, 0.6, 0.6]
    # print(levene(methods_one, methods_second))
    # print('T test independent')
    # print(ttest_ind(methods_one, methods_second))
    print("Degrees of Freedom: {}".format(len(methods_one) - 1))
    print("The mean is: {}".format(np.mean(methods_one)))
    print('T test relative')
    print(ttest_rel(methods_one, methods_second))


if __name__ == '__main__':
    analyze_data_set('FacebookData.xlsx')
    comparing_different_methods()
