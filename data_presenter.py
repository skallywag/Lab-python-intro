cupcake_invoices = open('CupcakeInvoices.csv')
for line in cupcake_invoices:
    print(line)

for order in cupcake_invoices:
  splitorder = order.rstrip('\n').split(',')
  print(splitorder[2])


total = 0
running_total = 0

for order in cupcake_invoices:
  splitorder = order.rstrip('\n').split(',')
  total = round((float(splitorder[3]) * float(splitorder[4])), 2)
  running_total += total
print(running_total)


cupcake_invoices.close()



   
    

