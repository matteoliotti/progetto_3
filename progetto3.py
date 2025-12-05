#parte 1

nomeM="Mario Rossi"
etaM=34
saldo_contoM=2500.75
vipM=True
citta=["Roma","Milano","Napoli","Torino","Venezia"]
costi={citta[0]:400,citta[1]:650,citta[2]:250,citta[3]:300,citta[4]:500}

#parte 2

class cliente:
    def __init__(self,nome,eta,vip):
        self.nome=nome
        self.eta=eta
        self.vip=vip
    def informazioni(self):
        print(f"Nome: {self.nome}\nEta: {self.eta}\nvip: {self.vip}")

class viaggio:
    def __init__(self,destinazione,prezzo,durata):
        self.destinazione=destinazione
        self.prezzo=prezzo
        self.durata=durata

class prenotazione(cliente,viaggio):
    def __init__(self,cliente,viaggio):
        self.cliente=cliente
        self.viaggio=viaggio
    def importo_finale(self):
        if self.cliente.vip:
            self.viaggio.prezzo=self.viaggio.prezzo-self.viaggio.prezzo/10
        return self.viaggio.prezzo*self.viaggio.durata
    def dettagli(self):
        print(f"\nIl/La sig/sig.ra {self.cliente.nome} ha prenotato un viaggio verso {self.viaggio.destinazione} per {self.viaggio.durata} giorni.\nCosto totale: {self.importo_finale()}\n")

Mario=cliente(nomeM,etaM,vipM)
weekend_al_colosseo=viaggio(citta[0],costi[citta[0]],2)
Mario_Roma=prenotazione(Mario,weekend_al_colosseo)
#Mario_Roma.dettagli()