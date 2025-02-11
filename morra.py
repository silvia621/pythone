punti1 = 0
punti2 = 0
pareggio = 0

while abs(punti1 - punti2) < 3 :
    risultato = input("Inserisci i risultati separati da uno spazio: C carta, F forbici, S sasso ")
    if risultato.upper() == "C C" or risultato.upper() == "S S" or risultato.upper() == "F F" : #valuto i casi di pareggio
        pareggio += 1
    elif risultato.upper() == "C S" or risultato.upper() == "S F"  or risultato.upper() == "F C" : #casi in cui vince il giocatore 1)
        punti1 += 1
    elif risultato.upper() == "S C" or risultato.upper() == "F S" or risultato.upper() == "C F" : #casi in cui vince il giocatore 2
        punti2 += 1
    else : 
        print("Hai inserito dei dati sbagliati")
    print("Il risultato è:" , punti1 , "-" , punti2)

if punti1 > punti2 :
    print("Il vincitore è il giocatore 1")
    print("Il giocatore 1 ha vinto" , punti1 , "volte")
 
else:
    print("Il vincitore della partita è il giocatore 2")
    print("Il giocatore 2 ha vinto" , punti2 , "volte")

print("Numero di casi di pareggio:" , pareggio)
