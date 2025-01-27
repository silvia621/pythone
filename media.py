risposta = "si"
totale = 0
contanumeri = 0
while risposta == "si" :
    numero = input("Inserisci un numero: ")
    contanumeri +=1
    totale += float(numero)
    risposta = input("Se vuoi continuare scrivi si ")
print("La media dei numeri inseriti è ", totale/contanumeri)