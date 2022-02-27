train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:
#Temperature Conversion
def f_to_c(f_temp):
  c_temp = (f_temp -32) * 5/9
  return c_temp
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#Force Calculation
def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies "+ str(train_force) + " Newtons of force")

#Energy Calculation
def get_energy(mass, c = 3*10**8):
  return mass * c
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#Work Calculation
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance
train_work = get_work(train_mass, train_acceleration, train_distance) 

print(train_work)

