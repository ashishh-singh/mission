
def container_report(total_cartons, freight, dinner_set_per_carton, gst_per, DO, BL_fees, THC, others, port_handling,
                     documentation, transport, ex_factory_price,  custom_duty, vat, add_whole_seller_margin,
                     add_retailer_margin, do_label, bl_label, thc_label, others_label, port_label, documentation_label,
                     transport_label ):


    freight_list_1 = freight / total_cartons
    freight_list = [round(freight, 2), round(freight_list_1, 2), round(freight_list_1 / 4, 2), "Freight"]


    gst_list_0 = (freight * gst_per) / 100
    gst_list_1 = gst_list_0 / total_cartons
    gst_list = [round(gst_list_0, 2), round(gst_list_1, 2), round(gst_list_1 / dinner_set_per_carton, 2), "GST"]


    sub_total_A_0 = freight + gst_list_0
    sub_total_A_1 = freight_list_1 + gst_list_1
    sub_total_A_list = [round(sub_total_A_0, 2), round(sub_total_A_1, 2),
                        round(sub_total_A_1 / dinner_set_per_carton, 2),
                        "Sub total   A"]


    DO_1 = DO / total_cartons
    DO_list = [DO, round(DO_1, 2), round(DO_1 / dinner_set_per_carton, 2), do_label]



    BL_fees_1 = BL_fees / total_cartons
    BL_fees_list = [BL_fees, round(BL_fees_1, 2), round(BL_fees_1 / dinner_set_per_carton, 2), bl_label]



    THC_1 = THC / total_cartons
    THC_list = [THC, round(THC_1, 2), round(THC_1 / dinner_set_per_carton, 2), thc_label]


    others_1 = others / total_cartons
    others_list = [others, round(others_1, 2), round(others_1 / dinner_set_per_carton, 2), others_label]



    port_handling_1 = port_handling / total_cartons
    port_handling_list = [port_handling, round(port_handling_1, 2), round(port_handling_1 / dinner_set_per_carton, 2),
                          port_label]


    documentation_1 = documentation / total_cartons
    documentation_list = [documentation, round(documentation_1, 2), round(documentation_1 / dinner_set_per_carton, 2),
                          documentation_label]



    transport_1 = transport / total_cartons
    transport_list = [transport, round(transport_1, 2), round(transport_1 / dinner_set_per_carton, 2), transport_label]



    sub_total_B_0 = DO + BL_fees + THC + others + port_handling + documentation + transport

    sub_total_B_1 = DO_1 + BL_fees_1 + THC_1 + others_1 + port_handling_1 + documentation_1 + transport_1

    sub_total_B_list = [round(sub_total_B_0, 2), round(sub_total_B_1, 2),
                        round(sub_total_B_1 / dinner_set_per_carton, 2), "Sub Total B"]


    total_shipping_cost_ind_UAE_0 = sub_total_B_0 + sub_total_A_0
    total_shipping_cost_ind_UAE_1 = sub_total_B_1 + sub_total_A_1
    total_shipping_cost_ind_UAE_list = [round(total_shipping_cost_ind_UAE_0, 2),
                                        round(total_shipping_cost_ind_UAE_1, 2),
                                        round(total_shipping_cost_ind_UAE_1 / dinner_set_per_carton, 2),
                                        "Total Shipping cost"]




    ex_factory_price_0 = ex_factory_price * total_cartons
    ex_factory_price_1 = ex_factory_price_0 / total_cartons

    ex_factory_price_list = [round(ex_factory_price_0, 2), round(ex_factory_price_1, 2),
                             round(ex_factory_price_1 / dinner_set_per_carton, 2),
                             "Ex Factory Price"]

    total_custom_value_0 = sub_total_A_0 + sub_total_B_0 + ex_factory_price_0
    total_custom_value_1 = sub_total_A_1 + sub_total_B_1 + ex_factory_price_1

    total_custom_value_list = [round(total_custom_value_0, 2), round(total_custom_value_1, 2),
                               round(total_custom_value_1 / dinner_set_per_carton, 2),
                               "Total Custom Value"]


    custom_duty_0 = (total_custom_value_0 * custom_duty) / 100
    custom_duty_1 = custom_duty_0 / total_cartons
    custom_duty_list = [round(custom_duty_0, 2), round(custom_duty_1, 2), round(custom_duty_1 / dinner_set_per_carton, 2),
                        "Custom duty"]

    whole_seller_price_0 = total_custom_value_0 + custom_duty_0
    whole_seller_price_1 = total_custom_value_1 + custom_duty_1
    whole_seller_price_list = [round(whole_seller_price_0, 2), round(whole_seller_price_1, 2),
                               round(whole_seller_price_1 / dinner_set_per_carton, 2),
                               "Whole Seller Price"]


    vat_0 = (whole_seller_price_0 * vat) / 100
    vat_1 = vat_0 / total_cartons
    vat_list = [round(vat_0, 2), round(vat_1, 2), round(vat_1 / dinner_set_per_carton, 2),
                "VAT"]

    whole_seller_include_vat_0 = whole_seller_price_0 + vat_0
    whole_seller_include_vat_1 = vat_1 + whole_seller_price_1
    whole_seller_include_vat_list = [round(whole_seller_include_vat_0, 2), round(whole_seller_include_vat_1, 2),
                                     round(whole_seller_include_vat_1 / dinner_set_per_carton, 2),
                                     "Whole Seller Price  Including VAT"]


    add_whole_seller_margin_0 = (whole_seller_include_vat_0 * add_whole_seller_margin) / 100
    add_whole_seller_margin_1 = add_whole_seller_margin_0 / total_cartons
    add_whole_seller_margin_list = [round(add_whole_seller_margin_0, 2), round(add_whole_seller_margin_1, 2),
                                    round(add_whole_seller_margin_1 / dinner_set_per_carton, 2),
                                    "Add Whole Seller Margin "]


    retailer_price_0 = whole_seller_include_vat_0 + add_whole_seller_margin_0
    retailer_price_1 = whole_seller_include_vat_1 + add_whole_seller_margin_1

    retailer_price_list = [round(retailer_price_0, 2), round(retailer_price_1, 2),
                           round(retailer_price_1 / dinner_set_per_carton, 2), "Retailer Price"]



    add_retailer_margin_0 = (retailer_price_0 * add_retailer_margin) / 100
    add_retailer_margin_1 = add_retailer_margin_0 / total_cartons
    add_retailer_margin_list = [round(add_retailer_margin_0, 2), round(add_retailer_margin_1, 2),
                                round(add_retailer_margin_1 / dinner_set_per_carton, 2),
                                "Add Retailer Margin"]

    consumer_price_0 = add_retailer_margin_0 + retailer_price_0
    consumer_price_1 = round(add_retailer_margin_1 + retailer_price_1, 2)
    consumer_price_list = [round(consumer_price_0, 2), round(consumer_price_1, 2),
                           round(consumer_price_1 / dinner_set_per_carton, 2),
                           "Consumer Price"]



    vat_new_0 = (consumer_price_0 * vat) / 100
    vat_new_1 = vat_new_0 / total_cartons
    vat_new_list = [round(vat_new_0, 2), round(vat_new_1, 2), round(vat_new_1 / dinner_set_per_carton, 2), "VAT"]

    consumer_price_including_vat_carton_0 = vat_new_0 + consumer_price_0
    consumer_price_including_vat_carton_1 = vat_new_1 + consumer_price_1
    consumer_price_including_vat_carton_list = [round(consumer_price_including_vat_carton_0, 2),
                                                round(consumer_price_including_vat_carton_1, 2),
                                                round(consumer_price_including_vat_carton_1 / dinner_set_per_carton, 2),
                                                "Consumer Price Including VAT Carton"
                                                ]

    final_list = [freight_list, gst_list, sub_total_A_list, DO_list, BL_fees_list, THC_list, others_list,
                  port_handling_list,
                  documentation_list, transport_list, sub_total_B_list, total_shipping_cost_ind_UAE_list,
                  ex_factory_price_list, total_custom_value_list, custom_duty_list, whole_seller_price_list,
                  vat_list, whole_seller_include_vat_list, add_whole_seller_margin_list, retailer_price_list,
                  add_retailer_margin_list, consumer_price_list, vat_new_list, consumer_price_including_vat_carton_list
                  ]




    return final_list



