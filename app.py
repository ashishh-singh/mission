import math
import os
import copy

import shutil

from flask import Flask, render_template, request, send_from_directory, flash, redirect

from table import level_table

# from excel import generate_excel

from container_table import container_report
from supplier_distribution import supply_distribution, convert_to_float
import os.path

import pandas as pd
pd.set_option('display.max_columns', None)




app = Flask(__name__)

app.secret_key = 'mission@1@mil'
app.config['SECRET_KEY'] = app.secret_key





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":


        current_currency = request.form.get('current_currency')
        target_Currency = request.form.get('target_Currency')
        currency_factor = request.form.get('currency_factor')
        country_factor = request.form.get('country_factor')
        daily_wage = request.form.get('daily_wage')
        estb_amount = request.form.get('estb_amount')
        team_size = request.form.get('team_size')
        days_month = request.form.get('days_month')
        factor_for_lead = request.form.get('factor_for_lead')
        margin_per = int(request.form.get('margin_per'))
        daily_wage_float = request.form.get('daily_wage_float')
        ec_float = request.form.get('ec_float')


        if daily_wage_float:
            if int(daily_wage) - int(float(daily_wage_float)) == 0 or int(daily_wage) - int(float(daily_wage_float)) == 1:
                daily_wage_value = float(daily_wage_float)
            else:
                daily_wage_value = daily_wage
        else:
            daily_wage_value = daily_wage



        if ec_float:
            if int(estb_amount) - int(float(ec_float)) == 0 or int(estb_amount) - int(float(ec_float)) == 1:
                ec_value = float(ec_float)

            else:
                ec_value = estb_amount
        else:
            ec_value = estb_amount



        total, avg_to_min, df, ec, float_inputs, summary_overall = level_table(
                                                                             currency_factor,country_factor,
                                                                             daily_wage_value, factor_for_lead,
                                                                             days_month, team_size, ec_value, margin_per)


        inputs = [target_Currency, df['Daily_Rates'][0], factor_for_lead, days_month, team_size, ec,
                  currency_factor, country_factor, margin_per]



        return render_template("table.html", df=df, total=total, inputs=inputs,
                               avg_to_min=avg_to_min, filename='filename', float_inputs=float_inputs,
                               summary_overall=summary_overall)
    return render_template("index.html",)



@app.route('/container', methods=['GET', 'POST'])
def container():

    if request.method == "POST":

        # like 1$ = ?₹, when user converts the result in other currency
        currency_exchange = float(request.form.get("currency_exchange"))
        container_size = int(request.form.get("container_size"))
        dimension_unit = request.form.get("dimension_unit")
        item_cartoon = int(request.form.get("item_cartoon"))
        length_cartoon = float(request.form.get("length_cartoon"))
        width_cartoon = float(request.form.get("width_cartoon"))
        height_cartoon = float(request.form.get("height_cartoon"))
        c_currency = request.form.get("c_currency")
        currency_exchange2 = float(request.form.get("currency_exchange2"))

        # destination country DO,BL etc., like 1$ = ?₹
        c_currency2 = request.form.get("c_currency2")
        freight = float(request.form.get("freight"))
        gst = float(request.form.get("gst"))
        do = float(request.form.get("do"))
        bl = float(request.form.get("bl"))
        thc = float(request.form.get("thc"))
        others = float(request.form.get("others"))
        port = float(request.form.get("port"))
        documentation = float(request.form.get("documentation"))
        transport = float(request.form.get("transport"))
        custom_duty = float(request.form.get("custom_duty"))
        vat = float(request.form.get("vat"))
        ex_factory_price = float(request.form.get("ex_factory_price"))
        whole_seller = float(request.form.get("whole_seller"))
        retailor_margin = float(request.form.get("retailor_margin"))


        do_label = request.form.get("do_label")
        bl_label = request.form.get("bl_label")
        thc_label = request.form.get("thc_label")
        others_label = request.form.get("others_label")
        port_label = request.form.get("port_label")
        documentation_label = request.form.get("documentation_label")
        transport_label = request.form.get("transport_label")


        inputs = [container_size, dimension_unit, item_cartoon, length_cartoon, width_cartoon, height_cartoon,
                  c_currency, currency_exchange, freight, gst, do, bl, thc, others, port, documentation,
                  transport, custom_duty, vat, ex_factory_price, whole_seller, retailor_margin, currency_exchange2,
                  do_label, bl_label, thc_label, others_label, port_label, documentation_label,
                  transport_label
                  ]


        freight1 = freight / currency_exchange

        currency_exchange2_final_value = 1

        if currency_exchange2 > 0:
            currency_exchange2_final_value = currency_exchange2

        do1 = round(((do * currency_exchange2_final_value) / currency_exchange) + 0.001, 2)
        bl1 = round(((bl * currency_exchange2_final_value) / currency_exchange) + 0.001, 2)
        thc1 = round(((thc * currency_exchange2_final_value) / currency_exchange) + 0.001, 2)
        others1 = round(((others * currency_exchange2_final_value) / currency_exchange) + 0.001, 2)
        port1 = round(((port * currency_exchange2_final_value) / currency_exchange) + 0.001, 2)
        documentation1 = round(((documentation * currency_exchange2_final_value) / currency_exchange) + 0.001, 2)
        transport1 = round(((transport * currency_exchange2_final_value) / currency_exchange) + 0.001, 2)


        ex_factory_price1 = ex_factory_price/currency_exchange

        dimension_input = [length_cartoon, width_cartoon, height_cartoon]


        container_dimension = [240, 96, 102]
        volume_container = 240 * 96 * 102


        if container_size == 40:
            container_dimension = [480, 96, 102]
            volume_container = 480 * 96 * 102



        unit_list_dic = {
            "inch": 1,
            "ft": 11.999,
            "mtr": 39.370
        }

        l = round((dimension_input[0] * unit_list_dic[dimension_unit]) + 0.001, 2)
        b = round((dimension_input[1] * unit_list_dic[dimension_unit]) + 0.001, 2)
        h = round((dimension_input[2] * unit_list_dic[dimension_unit]) + 0.001, 2)

        volume_carton = l * b * h



        possible_dimension = [[l, b, h], [l, h, b], [b, h, l], [b, l, h], [h, l, b], [h, b, l]]

        max_carton = 0
        final_dimension = []

        for j in possible_dimension:
            total_cartons = 1

            for i in range(0, 3):
                total_cartons = total_cartons * (math.floor(container_dimension[i]/j[i]))

            total_carton_volume = total_cartons * volume_carton
            if total_carton_volume < volume_container and total_cartons > max_carton:


                max_carton = total_cartons
                final_dimension.clear()
                final_dimension = j


        if max_carton <= 0:
            flash('Error: Total Carton is 0 / Division by 0')
            final_list = []
            consumer_price = [0, 0, 0]
            ex_factory_price_list = [0, 0, 0]
            final_dimension_should_be = [0, 0, 0]

        else:

            final_list = container_report(max_carton, freight1, item_cartoon, gst, do1, bl1, thc1, others1,
                                          port1,
                                          documentation1, transport1, ex_factory_price1, custom_duty, vat,
                                          whole_seller,
                                          retailor_margin, do_label, bl_label, thc_label,
                                          others_label, port_label, documentation_label,
                                          transport_label
                                          )

            consumer_price = final_list[-1]
            ex_factory_price_list = [int(final_list[-12][0]), int(final_list[-12][1]), int(final_list[-12][2])]
            final_dimension_should_be = final_dimension


        extra = [max_carton, c_currency2, consumer_price, ex_factory_price_list, final_dimension_should_be]

        return render_template("container.html", final_list=final_list, inputs=inputs, extra=extra)




@app.route('/supply_chain', methods=['GET', 'POST'])
def supply_chain():
    inputs_list = []
    inputs = []
    supply_curr_exchange_final_value = 1
    if request.method == "POST":
        supply_curr_exchange = request.form.get("supply_curr_exchange")
        target_customer = int(request.form.get("target_customer"))
        supply_currency = request.form.get("supply_currency")
        mrp = float(request.form.get("mrp"))
        invest_amt = float(request.form.get("invest_amt"))
        invest_per = float(request.form.get("invest_per"))
        supply_currency1 = request.form.get("supply_currency1")

        for i in range(1, 7):
            level_name = request.form.get("level_name{}".format(i))
            number = int(request.form.get("number{}".format(i)))
            margin_percentage = float(request.form.get("margin_percentage{}".format(i)))
            direct_cost = float(request.form.get("direct_cost{}".format(i)))


            inputs = [level_name, number, target_customer, margin_percentage, direct_cost]
            inputs_list.append(inputs)

        inputs_list1 = copy.deepcopy(inputs_list)



        supply_converted_value = float(convert_to_float(supply_curr_exchange))
        if supply_converted_value > 0:
            supply_curr_exchange_final_value = float(convert_to_float(supply_curr_exchange))



        mrp1 = float(request.form.get("mrp")) * supply_curr_exchange_final_value
        invest_amt1 = float(request.form.get("invest_amt")) * supply_curr_exchange_final_value
        invest_per1 = float(request.form.get("invest_per")) * supply_curr_exchange_final_value

        for i in range(0, 6):
            inputs_list1[i][4] = inputs_list1[i][4]*supply_curr_exchange_final_value


        inputs_other = [target_customer, supply_currency, mrp, invest_amt, invest_per, supply_curr_exchange,
                        supply_currency1]



        df = supply_distribution(inputs_list1, target_customer, mrp1, invest_amt1, invest_per1)




        return render_template("supply_chain.html", df=df, inputs_list=inputs_list, inputs_other=inputs_other)





@app.route('/excel_download/<string:filename>', methods=['GET', 'POST'])
def excel_download(filename):

    return send_from_directory(directory="storage", filename=filename, as_attachment=True)


@app.route('/favicon.ico')
def favicon():

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


if __name__ == "__main__":
    app.run(debug=True)
