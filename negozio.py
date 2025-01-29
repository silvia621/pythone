lista_prezzi_animale = [] #creo la lista dove andrò ad inserire i prezzi
print("Per ciascun prodotto scrivi il prezzo, seguito da Y se si tratta di un animale altrimenti scrivi N, se non hai più prodotti scrivi -1: ")
inputCassiere = str(input(""))

while inputCassiere != "-1": #finchè non digito -1 continuo ad aggiungere valori nella lista
    lista_prezzi_animale.append(str(inputCassiere)) #accodo i valori nella lista
    inputCassiere = str(input(""))


def discount (prices, nItems) :
    pricesNum = [float(prezzi[:-1]) for prezzi in prices]

    if any ("y" in prezzo_oggetti.lower() for prezzo_oggetti in prices) :
        isPet = True
    else :
        isPet = False
    
    if nItems > 5 and isPet == True :
        print ("Hai diritto allo sconto, il totale da pagare è " , round((sum(pricesNum)), 2)*0.8 , "euro")
    
    else : 
        print ("Non hai diritto allo sconto, il totale è " , round((sum(pricesNum)), 2) , " euro.")


discount(lista_prezzi_animale, len(lista_prezzi_animale))
