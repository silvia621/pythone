class Cliente:
    SOGLIA_SCONTO = 100
    SCONTO = 10
    def __init__(self, nome):
        self._nome = nome
        self._totaleAcquisti = 0
        self._sconto = False #sconto maturato nell'acquisto corrente
        self._scontoDaApplicare = False #sconto maturato con gli acquisti precedenti

    def effettuaAcquisto(self, ammontare):
        self._ammontare = ammontare
        self._totaleAcquisti += self._ammontare #aggiorno il totale di cliente
        if self._totaleAcquisti >= Cliente.SOGLIA_SCONTO: #se il totale raggiunge la soglia il cliente ottiene lo sconto per il prossimo acquisto
            self._sconto = True #il cliente ottiene lo sconto
        
    def applica_sconto_acquisti_precedenti(self):
        if self._scontoDaApplicare == True : #è True solo se nell'acquisto precedente ho ottenuto lo sconto
            if self._ammontare > Cliente.SCONTO : #acquisto corrente almeno superiore a 10€
                print(f"Ciao {self._nome}, dopo aver applicato lo sconto maturato con gli acquisti precedenti, ") #OK!!!
                print(f"oggi paghi {self._ammontare - Cliente.SCONTO} € ({self._ammontare}€ - {Cliente.SCONTO}€).", end = '\n') #OK!!!!
                self._scontoDaApplicare = False #azzero lo sconto      
            else : 
                print(f"Ciao {self._nome}, non posso applicare lo sconto perchè l'importo dell'acquisto è troppo basso. ", end = "")
                print(f"Oggi paghi {self._ammontare} €")
        else :
            print(f"Ciao {self._nome}, oggi paghi {self._ammontare} €. ", end ="") ##non ho sconti da applicare
    
    def sconto_raggiunto(self):
        if self._sconto == True : #se nell'acquisto corrente ho maturato lo sconto
            self._totaleAcquisti -= Cliente.SOGLIA_SCONTO #aggiorno il saldo punti
            self._scontoDaApplicare = True #ho uno sconto da applicare all'acquisto corrente
            self._sconto = False #azzero lo sconto che utilizzo con l'acquisto corrente
            print(f"Complimenti, hai diritto a {Cliente.SCONTO} € di sconto sul tuo prossimo acquisto! ") #OK!!!
            print(f"Il saldo aggiornato è di {self._totaleAcquisti} punti.") #OK!!!!
            print("-" * 100)
        else :
            print(f"Mi dispiace ma non hai ancora raggiunto la soglia per ottenere lo sconto. ") ##ok!
            print(f"Il tuo saldo aggiornato è di {self._totaleAcquisti} punti.", end = '\n') ##ok!
            print("-" * 100)
   
            
cliente1 = Cliente("Mario")

cliente1.effettuaAcquisto(50)
cliente1.applica_sconto_acquisti_precedenti()
cliente1.sconto_raggiunto()

cliente1.effettuaAcquisto(60)
cliente1.applica_sconto_acquisti_precedenti()
cliente1.sconto_raggiunto()

cliente1.effettuaAcquisto(105)
cliente1.applica_sconto_acquisti_precedenti()
cliente1.sconto_raggiunto()

# # cliente1.applica_sconto()
cliente1.effettuaAcquisto(90)
cliente1.applica_sconto_acquisti_precedenti()
cliente1.sconto_raggiunto()

cliente1.effettuaAcquisto(8)
cliente1.applica_sconto_acquisti_precedenti()
cliente1.sconto_raggiunto()