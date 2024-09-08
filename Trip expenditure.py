print("\033c")
def hotel_cost(nights):
    return 2500*nights

def plane_ride_cost(city):
    if city =="Sylhet":
        return 1500
    elif city == "Bandarban":
        return 1250
    elif city == "Cox":
        return 2375
    elif city =="STmartin":
        return 2357
    
def rental_car_cost(days):
    if days>=7:
        return 800*days - 500
    elif days >=3:
        return 800*days - 250
    else:
        return 800*days
    
def totalAmount (city,day):
    return hotel_cost(day)+plane_ride_cost(city)+rental_car_cost(day)

c = input("Where do u wanna go[Sylhet, bandarban,cox,stmartin]:")
d = int(input("How many days you want to stay:"))
total = totalAmount(c,d)


print()
print(f"Hotel cost for {d} days:{hotel_cost(d)}")
print(f"Plane ride cost for {d} days:{plane_ride_cost(c)}")
print(f"Rental Card cost for {d}:{rental_car_cost(d)}")
print(f"Toatal cost for {d}days: {total}")

import calendar
year = int(input("Enter a year:"))
month = int(input("Enter a month:"))

print(calendar.month(year,month))
      

