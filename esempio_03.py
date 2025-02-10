punti1 = 0 #punti vinti dal giocatore 1
punti2 = 0 #punti vinti dal giocatore 2

while (punti1 < 5 and punti2 < 5) or abs((punti1 - punti2) < 2) : #continuo finchè un giocatore non fa almeno 4 punti con 2 di vantaggio
    vincitore = int(input("Scrivi il vincitore: "))
    if vincitore == 1 :
        punti1 += 1
    else:
        punti2 +=1
    print("risultato punti:" , punti1, punti2)

if punti1 > punti2 :
    print("Il vincitore è il giocatore 1 con" , punti1, "punti e", abs(punti1 - punti2) , "di vantaggio sul giocatore 2")
else: 
    print("Il vincitore è il giocatore 2 con" , punti2, "punti e", abs(punti1 - punti2) , "di vantaggio sul giocatore 1")
