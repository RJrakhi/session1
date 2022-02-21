one_plus_day1_sales=150
one_plus_day2_sales=250
one_plus_day3_sales=100

home_appl_day1_sales=200
home_appl_day2_sales=180
home_appl_day3_sales=300


Profit_to_amazon_from_oneplus=200.27

discount_from_sbi_to_oneplus=3000.12

profit_to_amazon_from_home_appl=50

discount_from_sbi_to_home_app=3000.12

total_oneplus_sales=one_plus_day1_sales+one_plus_day2_sales+one_plus_day3_sales
total_home_appl_sales=home_appl_day1_sales+home_appl_day2_sales+home_appl_day3_sales

net_oneplus_profit=total_oneplus_sales*Profit_to_amazon_from_oneplus
net_home_appl_profit=total_home_appl_sales*profit_to_amazon_from_home_appl
print("Total Profit by One Plus:",net_oneplus_profit)
print("Total Profit by Home Appliances:",net_home_appl_profit)

if net_oneplus_profit>net_home_appl_profit:
    print("Amazon made more Profit by oneplus by",(net_oneplus_profit-net_home_appl_profit))
else:
    print("Invalid data")


"""Assignment 1..
Evaluate SBI should invest in selling credit card to Home Appliances Shops or Mobile Shops to have more Customers"""

day1_sale_of_mobile=450
day2_sale_of_mobile=550
day3_sale_of_mobile=560

profit_earned_by_mobile=546

day1_sale_of_home_appl =236
day2_sale_of_home_appl =330
day3_sale_of_home_appl =450

profit_earned_by_home_appl=654

total_sale_mobile=day1_sale_of_mobile+day2_sale_of_mobile+day3_sale_of_mobile
total_sale_homeappl=day1_sale_of_home_appl+day2_sale_of_home_appl+day3_sale_of_home_appl
print("Total Mobile sale:",total_sale_mobile)
print("total home Applsale:",total_sale_homeappl)
net_mobile_profit=total_sale_mobile*profit_earned_by_mobile
net_home_appl_profit=total_sale_homeappl*profit_earned_by_home_appl
print("sbi invest in  mobile :",net_mobile_profit)
print("sbi invest in home appl",net_home_appl_profit)
if net_mobile_profit>net_home_appl_profit:
    print("sbi should invest in mobile phones",net_mobile_profit-net_home_appl_profit)
else:
    print("sbi should invest in home appliances")
"""Assignment2..
Evaluate Sbi spends more on home appliances on Amazon Portal can it get more customer and can amazon have the similar profit"""
if net_home_appl_profit>net_mobile_profit:
    print("sbi spend on home appliances on Amazon Portal",net_home_appl_profit-net_mobile_profit)
else:
    print("it can't get the more customer on amazon portal")


