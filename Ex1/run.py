from scipy.stats import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_statistics(field):
    """
    This function prints a statistics about each data column
    :param field:
    :return:
    """
    print(field)
    data[field] = get_clean_data(field)
    print(describe(data[field]))
    print('Median: ' + str(np.median(data[field])))
    plt.hist(data[field], bins='auto')
    plt.title("{} Histogram".format(field.title()))


def get_clean_data(field):
    return data[field].apply(lambda x: 0 if x == ' ' else x)


def t_tests(field):
    data[field] = get_clean_data(field)
    alg1 = data[data['Paid'] == 0][field]
    alg2 = data[data['Paid'] == 1][field]
    print('{} T tests for unpaied and paid posts'.format(field))
    print('Levene test')
    print(levene(alg1, alg2))
    print('T test independent')
    print(ttest_ind(alg1, alg2))
    print('T test relative')
    print(ttest_rel(alg1, alg2))


if __name__ == '__main__':
    data = pd.read_excel('FacebookData.xlsx')
    # print('Q1')
    # get_statistics('comment')
    # get_statistics('like')
    # get_statistics('share')
    # get_statistics('LifetimePostTotalReach')
    # print('Q2')
    # get_statistics('Category')
    # get_statistics('Paid')
    # get_statistics('PostWeekday')
    # print('Q3')
    # print(ttest_1samp(data['share'], 25))
    #
    # t_tests('share')

    'Question 2.5'  # <---
    engine1 = [0.9, 0.6, 0.6, 0.5, 0.9, 0.6, 0.7, 0.7, 0.6, 0.6]
    engine2 = [0.95, 0.65, 0.65, 0.5, 0.9, 0.65, 0.75, 0.75, 0.6, 0.6]

    print(levene(engine1, engine2))
    print('T test independent')
    print(ttest_ind(engine1, engine2))
    print('T test relative')
    print(ttest_rel(engine1, engine2))