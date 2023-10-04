import time
# Defining Function to regulate temp
def heating_cooling(actual_temp, desired_temp = 72):
# Setting Perameters to determine actual temp then print one of these three things: Run A/C, Run heat, or Standby.
  actual_temp = int(input("What is the current temperature? "))
  desired_temp = int(input("What is your desired temperature? "))
  while True:
  # Running A/C
    if actual_temp > desired_temp:
      print('\r' + "Running AC: " + f"{actual_temp}", end = '\t'"")
      actual_temp -= 1
      time.sleep(1)
  # Running Heat
    elif actual_temp < desired_temp:
      print('\r' + "Running Heat: " + f"{actual_temp}", end = '\t'"")
      actual_temp += 1
      time.sleep(1)
  # Standby
    else:
      print("\nDesired temp reached: " + f"{desired_temp}", " Standby")
      break

heating_cooling(70)


#  Converting temperature to Celcius and Kelvin
def convert_temp(temp_celsius, target_unit):
  temp_celsius = float(input("What is the temperature you would like to convert? "))
  target_unit = input("Would you like to convert to C, F, or K? ")
#  converting to Kelvin
  if target_unit.upper() == "K":
    Kelvin = float(temp_celsius + 273.15)
    print(f"{Kelvin}" + " K")
# converting to fahrenheit
  elif target_unit.upper() == "F":
    Faren = float(temp_celsius * 2 + 30)
    print(f"{Faren}" + "°F")
# Printing Celcius
  elif target_unit.upper() == "C":
     print(f"{temp_celsius}" + "°C")
# Improper Entry
  else:
    print("Invalid Unit")

convert_temp(77, "F")