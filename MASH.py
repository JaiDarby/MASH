#M.A.S.H
#Spouse
#NumberOfKids
#Pet
#Location
#Carrer
#Salary
#City
import random
SpouseList = [input("Enter a spouse 1: "), input("Enter a spouse 2: "), input("Enter a spouse 3: "), input("Enter a spouse 4: ")]
NumKidsList = [input("\nEnter number of kids: "), input("Enter number of kids: "), input("Enter number of kids: "), input("Enter number of kids: ")]
PetsList = [input("\nEnter pet: "),input("Enter pet: "),input("Enter pet: "),input("Enter pet: ")]
LocationList = [input("\nEnter Location: "),input("Enter Location: "),input("Enter Location: "),input("Enter Location: ")]
CarrerList = [input("\nEnter a carrer: "),input("Enter a carrer: "),input("Enter a carrer: "),input("Enter a carrer: ")]
SalaryList = [input("\nEnter a salary: "),input("Enter a salary: "),input("Enter a salary: "),input("Enter a salary: ")]
CityList = [input("\nEnter a city: "),input("Enter a city: "),input("Enter a city: "),input("Enter a city: ")]

Spouse = random.choice(SpouseList)
NumKids = random.choice(NumKidsList)
Pet = random.choice(PetsList)
Location = random.choice(LocationList)
Carrer = random.choice(CarrerList)
Salary = random.choice(SalaryList)
City = random.choice(CarrerList)

input("Click enter to recieve the story of your life")

print ("\nYou will marry", Spouse, "and you guys will have", NumKids, "kids.\n You will also have a pet", Pet, ".\n You'll live in a", Location, " and work as a", Carrer, ". \nYou'll make", Salary, "per year and you are pretty satified about it. Lastly you'll live in", City)

print()
