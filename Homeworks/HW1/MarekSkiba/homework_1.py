import pandas as pd

def calculate_metrics(df: pd.DataFrame):
    # Demographic parity

    pass

def task1():
    """
    Task 1
    We have two populations Blue (privileged) and Red (unprivileged), with the Blue population being 9 times larger than the Red population.

    Individuals from both populations are requesting to attend XAI training to improve competency in this important area. Number of places is limited. The administrators of the training have decided to give priority to enrolling individuals who may need this training in the future, although unfortunately it is difficult to predict who will benefit.

    The decision rule adopted:

    In the Red group, half of the people will find the skills useful in future and half will not. Administrators randomly allocate 50% of people to training.
    in the Blue group, 80% of people will find the training useful in future and 20% will not, although of course it is not known who will find it useful. The administrators have built a predictive model based on user behaviour in predicting for whom it will be useful and whom will not. The model has the following performance:
    Blue	Will use XAI	Will not use XAI	Total
    Enrolled in training	60	5	65
    not enrolled in training	20	15	35
    Total	80	20	100
    Task: Calculate the Demographic parity, equal opportunity and predictive rate parity coefficients for this decision rule.

    Starred task: How can this decision rule be changed to improve its fairness?
"""
    df_blue = pd.DataFrame({'use': [60, 20], 'not_use': [5, 15]}, index=['enrolled', 'not_enrolled'])
    df_red = pd.DataFrame({'use': [25, 25], 'not_use': [25, 25]}, index=['enrolled', 'not_enrolled'])

    # Demographic parity
    # P(Enrolled | Blue) = P(Enrolled | Red)
    enrolled_blue = df_blue.loc['enrolled'].sum()
    enrolled_red = df_red.loc['enrolled'].sum()
    dp_ratio = enrolled_blue / enrolled_red
    print(f'Demographic parity ratio: {enrolled_blue:.3f} / {enrolled_red:.3f} = {dp_ratio:.3f}')

    # Equal opportunity
    # P(Enrolled | Blue, Will use XAI) = P(Enrolled | Red, Will use XAI)
    enrolled_blue_use = df_blue.loc['enrolled', 'use'] / df_blue['use'].sum() * 100
    enrolled_red_use = df_red.loc['enrolled', 'use'] / df_red['use'].sum() * 100
    eo_ratio = enrolled_blue_use / enrolled_red_use
    print(f'Equal opportunity ratio: {enrolled_blue_use:.3f} / {enrolled_red_use:.3f} = {eo_ratio:.3f}')

    # Predictive rate parity
    # P(Will use XAI | Blue, Enrolled) = P(Will use XAI | Red, Enrolled)
    will_use_blue = df_blue.loc['enrolled', 'use'] / df_blue.loc['enrolled'].sum() * 100
    will_use_red = df_red.loc['enrolled', 'use'] / df_red.loc['enrolled'].sum() * 100
    prp_ratio = will_use_blue / will_use_red
    print(f'Predictive rate parity: {will_use_blue:.3f} / {will_use_red:.3f} = {prp_ratio:.3f}')


def task2():
    pass


task1()
