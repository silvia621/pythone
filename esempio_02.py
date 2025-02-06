#il programma deve chiedere un numero intero e una lettera 3 A
#in output  3 spazi A
#2 spazi  AAA
#5 AAAAA
#print("A" *5)

numero = int(input("scrivi un numero intero "))
lettera = input("scrivi una lettera ")
i = 0
k = 1
while i < numero :
    print(" " * (numero - i) + lettera * k)
    i += 1
    k += 2