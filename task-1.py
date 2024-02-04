unit=input("the temperature is in celsisus,kelvin or fahrenheit (C/F/K): ")
x=float(input("Enter the temperature:"))
if unit=="C":
    print("Temperature in kelvin:",x+273)
    print(f"Temperature in fahrenheit:",(x*9/5)+32)
elif unit=="F":
    print (f"Temperature in kelvin:",(x-32) (5/9)+273)
    
    print(f"temperature in celsisus is:",(x-32)(5/9))
elif unit=="K":
    print(f"Temperature in fahrenheit:",(x-273)*1.8+32)
    print(f"Temperature in celsisus:",x-273)

else:
    print(unit,"is an invalid unit of measure")