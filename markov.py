

Bull = [0,0,0]
Bear = [0,0,0]
Stagnant = [0,0,0]

matrix = [Bull, Bear, Stagnant]

def step(m, days):
  return matrix^days

print(step(matrix, 50))