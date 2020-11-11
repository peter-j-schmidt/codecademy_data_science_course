# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  return (print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars."), estimated_cost)

def cost_difference(cost1, cost2):
  cost_difference = cost1 - cost2
  return print("The difference in insurance cost is " + str(cost_difference) + " dollars.")

# Initial variables for Maria 
'''age = 28
sex = 0  
bmi = 26.2
num_of_children = 3
smoker = 0  '''

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)


# Initial variables for Omar
'''age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1'''  

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)

# Estimate my own insurance costs
peter_insurance_cost = calculate_insurance_cost("Peter", 29, 1, 25, 0, 0)

maria_omar_cost_difference = cost_difference(maria_insurance_cost[1], omar_insurance_cost[1])

omar_peter_cost_difference = cost_difference(omar_insurance_cost[1], peter_insurance_cost[1])

maria_peter_cost_difference = cost_difference(maria_insurance_cost[1], peter_insurance_cost[1])