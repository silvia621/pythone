punti1 = 0
punti2 = 0
while (punti1 < 6 and punti2 < 6) or (abs(punti1 - punti2) < 2 and (punti1 < 7 and punti2 < 7)) :
    vincitore = int(input("Scrivi il vincitore della partita "))
    if vincitore == 1 :
        punti1 += 1
    else:
        punti2 +=1
    print("risultato:" , punti1, punti2)

if punti1 > punti2 and abs(punti1 - punti2) > 1:
    print("Il vincitore della partita è il giocatore 1 con" , punti1 , "punti" ,
              "e", abs(punti1 - punti2) , "di vantaggio sul giocatore 2 che ha totalizzato", punti2 , "punti")
elif punti1 < punti2 and abs(punti1 - punti2) > 1:
    print("Il vincitore della partita è il giocatore 2 con" , punti2 , "punti" ,
              "e", abs(punti1 - punti2) , "di vantaggio sul giocatore 1 che ha totalizzato" , punti1 , "punti")
elif punti1 > punti2 and abs(punti1 - punti2) < 2 : #risultato tie-break 
    print("Il vincitore del tie-break è il giocatore 1")
elif punti1 < punti2 and abs(punti1 - punti2) < 2 : #risultato tie-break 
    print("Il vincitore del tie-break è il giocatore 2")