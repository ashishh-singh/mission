import pandas as pd
# import numpy as np
import math


def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac


def convert_currency(amount, currency_factor, country_factor):
    currency_factor = convert_to_float(currency_factor)
    country_factor = convert_to_float(country_factor)
    new = float(amount) * currency_factor * country_factor

    return new



def level_table(currency_factor,country_factor, inrs, multiplier, days, team, ec1, margin):

    column_level = ['TEAM', 'Tl', 'MGR', 'SMGR', 'CXO', 'ORG']

    team = int(team)

    inr = round(convert_currency(float(inrs), currency_factor, country_factor) + 0.1)
    inr_float = convert_currency(float(inrs), currency_factor, country_factor)

    multiplier = float(multiplier)

    days = int(days)

    ec = round(convert_currency(float(ec1), currency_factor, country_factor) + 0.1)
    ec_float = convert_currency(float(ec1), currency_factor, country_factor)

    # initial list to create data frame
    team_arr = []
    # range to 6 because there are 6 level in organization
    for i in range(0, 6):
        if i == 0:
            # inp is head count
            inp = team
        else:

            if float(team_arr[i - 1][0] / 4) < int(float(team_arr[i - 1][0] / 4)) + 0.5:
                inp = math.floor(float(team_arr[i - 1][0] / 4))
                if inp == 0:
                    break

            else:
                inp = math.ceil(float(team_arr[i - 1][0] / 4))
                if inp == 0:
                    break

        inp = int(inp)
        if i == 0:
            # daily is daily wage
            daily = int(inr)
        else:
            if inp >= 1:
                daily = int(team_arr[i - 1][1] * multiplier)
            else:
                daily = 0

        # input1 = [head count, daily wage]
        input1 = [inp, daily]

        team_arr.append(input1)

    if team_arr[-2][0] == 1:
        team_arr[-1][0] = 0
        team_arr[-1][1] = 0



    # created initial data frame using team_arr[]
    df = pd.DataFrame(team_arr)
    # named 1st column as HC & Daily_rates
    df.columns = ['HC', 'Daily_Rates']

    for i, j in df.iterrows():
        df.loc[i, 'Daily_Cost'] = (j['HC'] * j['Daily_Rates'])

    # for i, j in df.iterrows():
        if df.loc[0]['HC'] >= 1:
            df.loc[i, 'Monthly_Rates'] = int(j['Daily_Rates'] * days)
        else:
            df.loc[i, 'Monthly_Rates'] = int(0)

    for i, j in df.iterrows():
        df.loc[i, 'Monthly_Cost'] = int(j['HC'] * j['Monthly_Rates'])

    for i, j in df.iterrows():
        df.loc[i, 'Annual_Rate'] = int(j['Monthly_Rates'] * 12)

    for i, j in df.iterrows():
        df.loc[i, 'Annual_Cost'] = int(j['Monthly_Cost'] * 12)

    sum_annual = df['Annual_Cost'].sum()

    for i, j in df.iterrows():
        if round((j['Annual_Cost'] / sum_annual) * 100, 2) > 0 :
            df.loc[i, 'Income_Share'] = round((j['Annual_Cost'] / sum_annual) * 100, 2)
        else:
            df.loc[i, 'Income_Share'] = 0

    for i, j in df.iterrows():
        if i == 0:
            df.loc[i, 'Cumulative_Share'] = round(df.loc[0]['Income_Share'], 2)

        else:
            df.loc[i, 'Cumulative_Share'] = round(df.loc[:i]['Income_Share'].sum(), 2)

    sum_head = df['HC'].sum()

    for i, j in df.iterrows():
        df.loc[i, 'Head_Share'] = round((j['HC'] / sum_head) * 100, 2)

    for i, j in df.iterrows():
        if i == 0:
            df.loc[i, 'Cumulative_Share_head'] = round(df.loc[0]['Head_Share'], 2)

        else:
            df.loc[i, 'Cumulative_Share_head'] = round(df.loc[:i]['Head_Share'].sum(), 2)

    for i, j in df.iterrows():
        if i == 0:
            df.loc[i, 'Cum_HC'] = df.loc[0]['HC']

        else:
            df.loc[i, 'Cum_HC'] = df.loc[:i]['HC'].sum()

    for i, j in df.iterrows():
        if i == 0:
            df.loc[i, 'Cum_Daily_Cost'] = df.loc[0]['Daily_Cost']

        else:
            df.loc[i, 'Cum_Daily_Cost'] = df.loc[:i]['Daily_Cost'].sum()

    for i, j in df.iterrows():
        df.loc[i, 'Chargeable_Daily_Rate'] = round(df.loc[i]['Cum_Daily_Cost'] / df.loc[i]['Cum_HC'], 2)

    for i, j in df.iterrows():
        if round(df.loc[i]['Chargeable_Daily_Rate'] / df.loc[0]['Daily_Rates'], 2) > 0:
            df.loc[i, 'Avg_to_Min'] = round(df.loc[i]['Chargeable_Daily_Rate'] / df.loc[0]['Daily_Rates'], 2)
        else:
            df.loc[i, 'Avg_to_Min'] = 0


    for i, j in df.iterrows():
        df.loc[i, 'Max_to_Min'] = round(math.pow(multiplier, i), 2)

    z = 0
    for i, j in df.iterrows():
        df.loc[i, 'Level'] = column_level[z]
        if z < len(column_level):
            z += 1

    # converted float values to integer
    df = df.astype({"Daily_Cost": 'int', "Monthly_Rates": 'int', "Monthly_Cost": 'int', "Annual_Rate": 'int',
                    "Annual_Cost": 'int', "Cum_Daily_Cost": 'int', "Chargeable_Daily_Rate": 'int',
                    "Cum_HC": 'int'})

    sum_daily_cost = df['Daily_Cost'].sum()
    sum_monthly_cost = df['Monthly_Cost'].sum()
    hybrid_daily_rate = round(sum_daily_cost / sum_head)
    total_monthly_rate = round(sum_monthly_cost / sum_head)
    sum_annual_cost = df['Annual_Cost'].sum()
    total_annual_rate = round(sum_annual_cost / sum_head)

    if round(total_monthly_rate / df.Monthly_Rates[0], 2) > 0:
        avg_monthly_rate = round(total_monthly_rate / df.Monthly_Rates[0], 2)
    else:
        avg_monthly_rate = 0



    # max is maximum salary per month which we display above table
    max_monthly_rates = df['Monthly_Rates'].max()
    # ec_hc is the product of establishment cost * head count



    avg_to_min = [avg_monthly_rate, max_monthly_rates ]

    total = [sum_head, hybrid_daily_rate, sum_daily_cost, total_monthly_rate, sum_monthly_cost, total_annual_rate,
             sum_annual_cost, ]


    float_inputs = [inr_float, ec_float]



    Daily_average_man_days = 240
    total_annual_man_days = Daily_average_man_days * sum_head
    total_annual_estb_amount = round((ec*sum_head) + 0.01)
    daily_average_estb_cost = round((total_annual_estb_amount/total_annual_man_days) + 0.1)
    Daily_Average_head_count_cost = hybrid_daily_rate
    total_Annual_head_count_cost = Daily_Average_head_count_cost * total_annual_man_days
    total_annual_sub_total = total_Annual_head_count_cost + total_annual_estb_amount
    daily_average_sub_total = round((total_annual_sub_total/total_annual_man_days) + 0.01)
    total_annual_margin = round(((total_annual_sub_total * margin) / 100) + 0.01)
    daily_average_margin = round((total_annual_margin / total_annual_man_days) + 0.01)
    total_annual_expected_revenue = total_annual_margin + total_annual_sub_total
    daily_average_expected_revenue = round((total_annual_expected_revenue / total_annual_man_days) + 0.01)


    summary_overall = [sum_head, total_annual_man_days, Daily_average_man_days, total_annual_estb_amount,
                       daily_average_estb_cost,
                       total_Annual_head_count_cost, Daily_Average_head_count_cost, total_annual_sub_total,
                       daily_average_sub_total, total_annual_margin, daily_average_margin,
                       total_annual_expected_revenue, daily_average_expected_revenue]


    return total, avg_to_min, df , ec, float_inputs, summary_overall


# total, avg_to_min, df, ec, float_inputs, summary_overall = level_table(1, 1,
#                                                                        3000, 2,
#                                                                        20, 16, 60000, 20)
#
# print(df)