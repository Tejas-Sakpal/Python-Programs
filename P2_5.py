Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def cube():
	n=eval(input("Enter the Number:"))
	sum=0
	for i in range (1,n+1):
		sum+=i**3
		print("sum of cube=",sum)

		
>>> 
>>> cube()
Enter the Number:5
sum of cube= 1
sum of cube= 9
sum of cube= 36
sum of cube= 100
sum of cube= 225
>>> 