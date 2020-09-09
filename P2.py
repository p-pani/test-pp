hrs = input ("Enter Hours:")
hrs = float(hrs)
rate = input('Enter Rate:')
rate= float(rate)
if hrs > 40.00:
  grosspay = (rate/2+rate)*(hrs-40)+(40*rate)
  print (grosspay)
elif hrs <=40:
    grosspay = hrs*rate
    print(grosspay)
