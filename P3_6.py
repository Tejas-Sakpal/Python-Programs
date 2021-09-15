Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def credit(x):
	if x<=23:
		print("Student is Freshman.")
	elif x<=53:
		print("Student is Sophomore.")
	elif x<=83:
		print("Student is Junior.")
	else:
		print("Student is Senior.")

		
>>> credit(100)
Student is Senior.
>>> credit(30)
Student is Sophomore.
>>> 