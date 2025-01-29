lista_prezzi_animale = [] #creo la lista dove andrò ad inserire i prezzi
print("Per ciascun prodotto scrivi il prezzo, seguito da Y se si tratta di un animale altrimenti scrivi N, se non hai più prodotti scrivi -1: ")
inputCassiere = str(input(""))

while inputCassiere != "-1": #finchè non digito -1 continuo ad aggiungere valori nella lista
    lista_prezzi_animale.append(str(inputCassiere)) #accodo i valori nella lista
    inputCassiere = str(input(""))

nuova_lista_prezzi = [float(prezzi[:-1]) for prezzi in lista_prezzi_animale] #creo una nuova lista con solo i prezzi
print(nuova_lista_prezzi)  

if any ("y" in oggetti.lower() for oggetti in lista_prezzi_animale) and len(lista_prezzi_animale) > 5 : #controllo se c'è almeno un animale e se ci sono almeno 6 prodotti
    print ("Hai diritto allo sconto, il totale è " , sum(nuova_lista_prezzi)*0.8 , " euro.")
else:
    print ("Non hai diritto allo sconto, il totale è " , sum(nuova_lista_prezzi) , " euro.")
