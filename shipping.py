# Ground shipping 
weight=41.5
cost=20
ground_premium = 125.00
if weight <=2:
  cost += weight*1.50
elif weight <=6:
  cost += weight*3
elif weight <=10:
  cost += weight*4
else:
  cost += weight*4.75 
  print(cost)
  #premium
cost_ground_premium = 125.00
#drome
drome_cost=0
if weight <=2:
    drome_cost = weight*4.50
elif weight <=6:
    drome_cost = weight*9
elif weight <=10:
    drome_cost = weight*12
else:
 drome_cost = weight*14
if cost<=drome_cost and cost<=ground_premium:
  print("your cheapest method is  ground    shipping ") 
  print(cost)
elif drome_cost<=ground_premium:         
  print("your cheapest method is drome: cost ") 
  print(drome_cost)
else:
 print("your cheapest method is ground_premium: cost " ) 
 print (ground_premium)
