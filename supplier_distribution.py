import pandas as pd


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



def supply_distribution(inputs_list, target_customer, mrp, invest_amt, invest_per):

    df = pd.DataFrame(inputs_list)
    df.columns = ['Level', 'Number', 'Target_Customer', 'margin_per', 'Direct_cost']

    for i, j in df.iterrows():
        if i == 0:
            df.loc[i, 'supply_Chain_Customers'] = round(target_customer / df.loc[0, 'Number'], 2)
            df.loc[i, 'cost'] = 0


        else:
            df.loc[i, 'supply_Chain_Customers'] = round(df.loc[i - 1, 'supply_Chain_Customers'] / df.loc[i, "Number"], 2)
            df.loc[i, 'cost'] = round((mrp * df.loc[i, "margin_per"] / 100) + 0.01, 0)



    df.loc[len(df) - 1, 'supply_Chain_Customers'] = 1
    df.loc[len(df) - 1, 'cost'] = mrp

    df.loc[len(df) - 1, 'sp'] = mrp

    for i, j in df.iterrows():
        if len(df) - i > 1:
            df.loc[len(df) - 2 - i, 'sp'] = df.loc[len(df) - 1 - i, 'sp'] - df.loc[len(df) - 2 - i, 'cost']

        df.loc[i, 'Total_margin'] = df.loc[i, 'supply_Chain_Customers'] * df.loc[i, 'cost']

        df.loc[i, 'Net income'] = df.loc[i, 'Total_margin'] - df.loc[i, 'Direct_cost']

        df.loc[i, 'investment'] = ((df.loc[i, 'supply_Chain_Customers'] * invest_per)/100) * invest_amt


    df.loc[len(df) - 1, 'Total_margin'] = 0
    df.loc[len(df) - 1, 'investment'] = 0
    df.loc[len(df) - 1, 'Net income'] = 0
    df.loc[0, 'investment'] = 0

    df = df.astype({"margin_per": 'int', "Direct_cost": 'int', "supply_Chain_Customers": 'int', "cost": 'int',
                    "sp": 'int', "Total_margin": 'int', "Net income": 'int',
                    "investment": 'int'})
    #
    # total = [df['margin_per'].sum(), df['margin_per'].sum() ]

    return df




