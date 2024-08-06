import xlsxwriter
import random


def generate_excel(total, avg_to_min, df, currency, summary_overall, margin_per):



    filename = '6_tier_str_org+{}.xlsx'.format(random.randrange(1, 1000, 1))

    workbook = xlsxwriter.Workbook("storage/{}".format(filename))
    worksheet = workbook.add_worksheet("My sheet")

    head = ["HC", "Max. Salary/Month", "Total Estb. Cost", "Daily Rate", "Daily Cost", "Monthly Rate", "Monthly Cost",
            "Annual Rate", "Annual Cost" ]

    head1 = ["Level", "HC", "Avg. Daily Rate", "Daily Cost", "Monthly Rate", "Monthly Cost", "Annual Rate", "Annual Cost",
          ]


    head0 = ["Summary", "Unit", "Total Annual", "Daily Average"]

    head0_1 = ["Head Count", "Man Days", "Establishment Cost", "Head Count Cost", "Sub Total",
               "Markup @ {}%".format(margin_per), "Total Expected Revenue"]

    head0_2 = ["HC", "days", "₹", "₹", "₹", "₹", "₹"]

    for i in range(0, len(head0)):
        worksheet.write(0, 0 + i, head0[i])

    for i in range(0, len(head0_1)):
        worksheet.write(1 + i, 0, head0_1[i])
        worksheet.write(1 + i, 1, head0_2[i])

    worksheet.write(1, 2, summary_overall[0])
    x = 0
    y = 1
    for i in range(0, len(summary_overall)):

        if i % 2 == 0:
            if i == 0 or i == 2:
                worksheet.write(1 + x, 3, summary_overall[i])

            else:
                worksheet.write(1 + x, 3, "{}{:,}".format(currency, summary_overall[i]))
            x = x + 1

        else:
            if i == 1:
                worksheet.write(1 + y, 2, summary_overall[i])

            else:
                worksheet.write(1 + y, 2, "{}{:,}".format(currency, summary_overall[i]))
            y = y + 1




    for i in range(0, len(head1)):
        worksheet.write(11, 0 + i, head1[i])

    for i in range(0, len(df)):
        worksheet.write(12 + i, 0, df['Level'][i])
        worksheet.write(12 + i, 1, int(df['HC'][i]))
        worksheet.write(12 + i, 2, "{}{:,}".format(currency,df['Daily_Rates'][i]))
        worksheet.write(12 + i, 3, "{}{:,}".format(currency, df['Daily_Cost'][i]))
        worksheet.write(12 + i, 4, "{}{:,}".format(currency,df['Monthly_Rates'][i]))
        worksheet.write(12 + i, 5, "{}{:,}".format(currency,df['Monthly_Cost'][i]))
        worksheet.write(12 + i, 6,"{}{:,}".format(currency,df['Annual_Rate'][i]))
        worksheet.write(12 + i, 7, "{}{:,}".format(currency,df['Annual_Cost'][i]))




    for i in range(0, len(head)):
        worksheet.write(20, 1 + i, head[i])

    worksheet.write(21, 0, "Total")
    worksheet.write(21, 1, int(total[0]))


    for i in range(1, 7):
        worksheet.write(21, 3 + i, "{}{:,}".format(currency, int(total[i])))

    worksheet.write(24, 0, "Avg. to Min")
    worksheet.write(24,  1,  avg_to_min[0])

    worksheet.write(25, 0, "Max. Salary/Month")
    # if avg_to_min[1] != 'nan':
    worksheet.write(25, 1, "{}{:,}".format(currency, avg_to_min[1]))


    workbook.close()

    return filename









