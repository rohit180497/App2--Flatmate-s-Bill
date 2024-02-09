from flat import Bill, Flatmate
from report import PdfReport

bill_amt = float(input("Hey user please enter the bill amount: "))
bill_period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days {name1} stayed in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stayed in the house during the bill period? "))

bill = Bill(amount=bill_amt, period=bill_period)
Flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
Flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{Flatmate1.name}_pays: ", Flatmate1.pays(bill, Flatmate2))
print(f"{Flatmate2.name}_pays: ", Flatmate2.pays(bill, Flatmate1))

# print(john_pays)

pdfreport = PdfReport(filename=f"{bill.period}.pdf")
pdfreport.generate(Flatmate1, Flatmate2, bill)
