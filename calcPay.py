#sys.argv[1] = hours worked
#sys.argv[2] = hourly wage
#sys.argv[3] = state working in

import sys

def calculatePay():
	filterParameters()
	
	print(str(sys.argv[1])+" hours worked")

	grossPay = float(sys.argv[1]) * float(sys.argv[2])

	totalTax = calcTax(grossPay)

	projPay = grossPay - totalTax
	print("Projected pay --> $ %.2f" % projPay)


def calcTax(income):
	state = calcStateTax(income)
	#print(state)
	fed = calcFederalTax(income)
	#print("Fed  "+str(fed))
	FICA = calcFICATax(income)
	#print("FICA  "+str(FICA))

	totalTax = state + fed + FICA + .25

	## -.25 for flower fund

	return totalTax

def filterParameters():
	print()
	if (len(sys.argv) > 4):
		print("Too many arguments.  Try again. :)")
		exit()
	if (sys.argv[1] == "help" or sys.argv[1] == "-h" or sys.argv[1] == "-i"):
		myHelp()

def myHelp():
	print("******** Help Menu ********")
	print("1st argument is hours worked")
	print("2nd argument is hourly rate")
	print("3rd argument is state you work in")
	print("Ex: python calcPay.py hoursWorked hourlyRate state")
	print("\nTaxes are taken into account based off your location")
	print("***************************")

	exit()

def calcStateTax(income):
	string = str(sys.argv[3]).lower()
	if (string == 'il' or string == "illinois"):
		return (income * .04949787)
	elif (string == 'mo' or string == "missouri"):
		return (income * .06)

def calcFederalTax(income):
	## based off the 2017 tax brackets (taxfoundation.com)
	## for single workers
	if (income > 0 and income < 9325):
		return (income * .09245)
	
	elif (income >= 9325 and income <= 37950):
		income = income - 932.5
		if (income > 9325):
			return ((income - 9325) * .15) + 932.5
		else:
			return 932.5
	
	elif (income >= 37950 and income <= 91900):
		income = income - 5226.25
		if (income > 37950):
			return ((income - 5226.25) * .25) + 5226.25
		else:
			return 5226.25
	
	elif (income >= 91900 and income <= 191650):
		income = income - 18713.75
		if (income > 91900):
			return ((income - 91900) * .28) + 18713.75
		else:
			return 18713.75

def calcFICATax(income):
	return (income * .0765)

def main():
	calculatePay()

main()
