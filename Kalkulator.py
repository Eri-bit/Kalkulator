#!/bin/py

#module
import os,sys,time,requests
from time import sleep

#tampilan
os.system("clear")
os.system("figlet Kalkulator")
tampilan ="""
===================================
=  Author : Eri                   =
=  Github : Github/Eri-bit        =
==================================="""
sleep(1)
print(tampilan)
print("")
print("1)Pertambahan")
print("2)Pengurangan")
print("3)Perkalian")
print("4)Pembagian")
print("___________________________________")
pilih =input("Pilih Salah Satu: ")

#Data Perkalian
if pilih =="1":
   angka1 =int(input("Angka Pertama: "))
   angka2 =int(input("Angka Kedua : "))
   print(angka1 + angka2)

#Data Pengurangan
if pilih =="2":
   angka1 =int(input("Angka Pertama: "))
   angka2 =int(input("Angka Kedua : "))
   print(angka1 - angka2)

#Data Perkalian
if pilih =="3":
   angka1 =int(input("Angka Pertama: "))
   angka2 =int(input("Angka Kedua : "))
   print(angka1 * angka2)

#Data Pembagian
if pilih =="4":
   angka1 =int(input("Angka Pertama: "))
   angka2 =int(input("Angka Kedua : "))
   print(angka1 / angka2)

