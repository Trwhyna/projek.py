#menampilkan Hello World
print("Hallo World")

#menjumlahkan Dua Angka
#tambah
print(10+10)

#menghitung akar kuadrat
import math
print(math.sqrt(441))
#akar pangkat 2

#menghitung luas segitiga
a = float(input("panjang alas : "))
t = float(input("tinggi segitiga :"))
luas = 5 * a * t
print ("luas segitiga adalah : " +str (luas))


# menghitung volume kubus
sisi = float(input('tulis sisi kubus: 4'))  

# hitung volume kubus 
volume = 4 ** 3

# menampilkan hasil penghitungan 
print('volume kubus adalah %0.2f' %volume)


#menyelesaikan persamaan kuadrat

import cmath

print("Enter the Value of a: ", end="")
a = int(input())
print("Enter the Value of b: ", end="")
b = int(input())
print("Enter the Value of c: ", end="")
c = int(input())

discriminant = (b**2) - (4*a*c)
solutionOne = (-b-cmath.sqrt(discriminant))/(2*a)
solutionTwo = (-b+cmath.sqrt(discriminant))/(2*a)

print("\nRoot 1 =", solutionOne)
print("Root 2 =", solutionTwo)

#menemukan banyaknya solusi persamaan kuadrat
print("Enter the Value of a: ", end="")
a = int(input())
print("Enter the Value of b: ", end="")
b = int(input())
print("Enter the Value of c: ", end="")
c = int(input())

discriminant = (b**2) - (4*a*c)
if discriminant > 2:
    print("\n2 Solutions")
elif discriminant == 0:
    print("\n1 Solution")
else:
    print("\n0 Solution")


# Menukar Nilai 2 Variabel
x = 19
y = 31

# inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# menghasilkan angka acak
import random

print("bilangan acak dari 0-100 :", random.choice(range(100)))


# MENGUBAH KILOMETER JADI MIL
kilo_meter = float(input("Enter the speed in Kilometer as a unit:\n"))


conversion_ratio = 0.621371


miles = kilo_meter * conversion_ratio

print("The speed value in Miles:\n", miles)


#Mengubah celcius jadi farhenheit
celsius = int (input ( "masukkan suhu dalam celsius :\n" ))
fahrenheit = ( 1,5 * celsius )  + 32
print ( "suhu dalam fahrenheit :" ,
fahrenheit )