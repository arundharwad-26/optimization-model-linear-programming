# Task 4 - Optimization Model using PuLP

import pulp

# Create optimization problem
model = pulp.LpProblem("Factory_Profit_Maximization", pulp.LpMaximize)

# Decision Variables
product_A = pulp.LpVariable('Product_A', lowBound=0)
product_B = pulp.LpVariable('Product_B', lowBound=0)

# Objective Function (Maximize Profit)
model += 20 * product_A + 30 * product_B

# Constraints

# Labor constraint
model += 2 * product_A + 4 * product_B <= 100

# Material constraint
model += 3 * product_A + 2 * product_B <= 90

# Solve problem
model.solve()

# Results
print("Status:", pulp.LpStatus[model.status])

print("Optimal Production Plan")
print("Product A:", product_A.value())
print("Product B:", product_B.value())

print("Maximum Profit:", pulp.value(model.objective))