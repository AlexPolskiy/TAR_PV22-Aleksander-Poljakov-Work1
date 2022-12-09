from math import * 
print("Hello World!") # Shows information on the screen.
name=input("What is your name?") # Function gives information in the "STR" format.
print() # Empty STR 
print(f"{name}, my pleasure working with you today")

print()
print("Vordse pindalaga riskulik ja ring")
a=float(input("Anna laius: "))
b=float(input("Anna korgus: "))
S=a*b 
P=2*a*b
d=round(sqrt(a**2+b**2),2)
print(f"Pindala = {S}\nPerimetr = {P}\nDiagonaal = {d}")
r=round(sqrt(S/pi),2)
print(f"Ringi raadius = {r} ")
