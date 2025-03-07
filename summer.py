actual_cost = float(input("The ice-cream they bought in summer camps.. :"))
sale_amount = float(input("they got in sale_amount.. :"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("no they did't..")