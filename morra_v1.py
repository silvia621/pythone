punti1 = 0
punti2 = 0
pareggio = 0

while (abs(punti1 - punti2)) < 3 :
    risultato = input("scrivi i risultati del gioco. Scegli tra C carta, S sasso, F forbici: ")
    if risultato == "C C" or risultato == "S S" or risultato == "F F" :
        pareggio += 1
        #print("pareggio")
    elif risultato == "C S" or risultato == "S F" or risultato == "F C" :
        punti1 += 1
        print("vince il giocatore 1, ha" , punti1, "punti")
    elif risultato == "S C" or risultato == "F S" or risultato == "C F" :
        punti2 += 1
        #print("vince il giocatore 2, ha" , punti2 , "punti")
    print("Il risultato è:" , punti1 , punti2)

if punti1 > punti2 :
    print("Il vincitore è il giocatore 1")
    print("Il giocatore 1 ha vinto" , punti1 , "volte")
 
else:
    print("Il vincitore della partita è il giocatore 2")
    print("Il giocatore 2 ha vinto" , punti2 , "volte")

print("Ci sono stati" , pareggio, "pareggi" )
