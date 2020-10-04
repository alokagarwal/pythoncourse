from_currency = input("from currency - GBP or EUR - ")
amount =  float(input("amount to be converted - "))
to_currency = input("to currency - GBP or EUR - ")

if from_currency.upper() == "GBP" and to_currency.upper() == "EUR":
	print(amount * 1.08)
elif from_currency.upper() == "EUR" and to_currency.upper() == "GBP":
	print(amount * 0.89)
else:
	print(amount)
