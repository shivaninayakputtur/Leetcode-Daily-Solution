def convertTemperature(celsius):
    kelvin=celsius+273.15
    Fahernheit=celsius*1.80+32.00
    return[kelvin,Fahernheit]
celsius=float(input("enter thevalue"))
print(convertTemperature(celsius))