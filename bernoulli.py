'''
Creation Date: 11-09-2019
Author: Amit
Purpose: TO find different hydraulic properties using Bernoulli equation 

Note: Define variable first as string then in if statement convert
it into float.(If you dont put anything before input then it
will taken as string)

'''

print("Bernoulli equation. Use 'find' for calculating particular quantity")


def ber():
	pi = input("Enter Pressure(N/m2) at inlet: ").lower()
	d = float(input("Enter density(kg/m3) of fluid: "))
	vi = input("Enter Velocity(m/s) at inlet: ").lower()
	g = 9.81
	hi = input("Enter Height(m) at the inlet from the reference point: ").lower()
	po = input("Enter Pressure(N/m2) at outlet: ").lower()
	vo = input("Enter Velocity(m/s) at outlet: ").lower()
	ho = input("Enter Height(m) at the outlet from the reference point: ").lower()
    
	if pi == "find":
		po = float(po)
		vo = float(vo)
		ho = float(ho)
		vi = float(vi)
		hi = float(hi)

		pi = po+(0.5*d*pow(vo,2))+(d*g*ho)-(0.5*d*pow(vi,2))-(d*g*hi)
		print(f'\nPressure at inlet = {pi} N/m2')

	elif vi == "find":
		po = float(po)
		vo = float(vo)
		ho = float(ho)
		pi = float(pi)
		hi = float(hi)
		vi = pow((po+(0.5*d*pow(vo,2))+(d*g*ho)-pi-(d*g*hi))/(0.5*d),0.5)
		print(f'\nVelocity at inlet = {vi} m/s')

	elif hi == "find":
		po = float(po)
		vo = float(vo)
		ho = float(ho)
		vi = float(vi)
		pi = float(pi)
		hi = (po+(0.5*d*pow(vo,2))+(d*g*ho)-pi-(0.5*d*pow(vi,2)))/(d*g)
		print(f"\nHeight at the inlet from the reference point = {hi} m")

	elif po == "find":
		pi = float(pi)
		vo = float(vo)
		ho = float(ho)
		vi = float(vi)
		hi = float(hi)
		po = pi+(0.5*d*pow(vi,2))+(d*g*hi)-(0.5*d*pow(vo,2))-(d*g*ho)
		print(f'\nPressure at outlet = {po} N/m2')

	elif vo == "find":
		po = float(po)
		pi = float(pi)
		ho = float(ho)
		vi = float(vi)
		hi = float(hi)
		vo = pow((pi+(0.5*d*pow(vi,2))+(d*g*hi)-po-(d*g*ho))/(0.5*d),0.5)
		print(f'\nVelocity at outlet = {vo} m/s')

	elif ho == "find":
		po = float(po)
		vo = float(vo)
		pi = float(pi)
		vi = float(vi)
		hi = float(hi)
		ho = (pi+(0.5*d*pow(vi,2))+(d*g*hi)-po-(0.5*d*pow(vo,2)))/(d*g)
		print(f"\nHeight at the outlet from the reference point = {ho} m")
    
	else:
		print("Wrong variable given\nUse 'find' for calculating particular quantity")
    

ber()
while True:
	choice = input("\nPress 'Enter' for calculating again or 'T' to Terminate...").lower()
	if choice == "t":
		break
	else:
		ber()
       
print("Program is Terminated")
