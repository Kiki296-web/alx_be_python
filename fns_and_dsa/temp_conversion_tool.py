FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return  (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32

temperature_input = float(input("Enter the temperature to convert:"))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temp_type == "C":
  result = convert_to_fahrenheit(temperature_input)
  print(f"{temperature_input}\N{DEGREE SIGN}C is {result}\N{DEGREE SIGN}F")

elif temp_type == "F":
  result = convert_to_celsius(temperature_input)
  print(f"{temperature_input}\N{DEGREE SIGN}F is {result}\N{DEGREE SIGN}C")

else:
  print("Invalid temperature. Please enter a numeric value")



