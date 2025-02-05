
print("Welcome to the tip calculator")
totalBill = input("How much was the total bill?\n")
totalBill = float(totalBill)

tipValue = input("How much tip would you like to give? 10, 12 or 15%\n" )
tipValue = float(tipValue) / 100
totalBill = (tipValue) * (totalBill) + (totalBill)

numPeople = input("How many people to split the bill?\n")
numPeople = int(numPeople)
splitBill = totalBill / numPeople
splitBill = round(splitBill, 2)

print(f"Each person should pay £{splitBill}")


