import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#parte 1

nomeM="Mario Rossi"
etaM=34
saldo_contoM=2500.75
vipM=True
citta=["Roma","Milano","Napoli","Torino","Venezia"]
costi={citta[0]:40,citta[1]:65,citta[2]:25,citta[3]:30,citta[4]:50}

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
            self.viaggio.prezzo=self.viaggio.prezzo*9/10
            self.cliente.vip=False
        return self.viaggio.prezzo*self.viaggio.durata
    def dettagli(self):
        print(f"\nIl/La sig/sig.ra {self.cliente.nome} ha prenotato un viaggio verso {self.viaggio.destinazione} per {self.viaggio.durata} giorni.\nCosto totale: {self.importo_finale()}\n")

Mario=cliente(nomeM,etaM,vipM)
weekend_Roma=viaggio(citta[0],costi[citta[0]],2)
Mario_Roma=prenotazione(Mario,weekend_Roma)
#Mario_Roma.dettagli()

# parte 3

simulazione=np.random.randint(200,2001,100)
#print("\nSimulazione di prenoptazioni:\n",simulazione)
#print("\nMedia:\n",np.mean(simulazione))
#print("\nMassimo e minimo:\n",np.max(simulazione),np.min(simulazione))
#print("\nDeviazione standard:\n",np.std(simulazione))
n=0
for x in np.where(simulazione>np.mean(simulazione))[0]:
    n+=1
Prenotazioni_sopra_la_media=n/2
#print(f"\nPrenotazioni sopra la media:\n{Prenotazioni_sopra_la_media}%")

# parte 4

Paolo=cliente("Paolo Verdi",40,False)
Marina=cliente("Marina Verdi",18,False)
Marta=cliente("Marta Bianchi",27,True)
Andrea=cliente("Andrea Amari",28,True)

settimana_Milano=viaggio(citta[1],costi[citta[1]],7)
settimana_Napoli=viaggio(citta[2],costi[citta[2]],7)
visita_Torino=viaggio(citta[3],costi[citta[3]],4)
vacanza_Venezia=viaggio(citta[4],costi[citta[4]],14)

Paolo_Milano=prenotazione(Paolo,settimana_Milano)
Marina_Napoli=prenotazione(Marina,settimana_Napoli)
Marta_Torino=prenotazione(Marta,visita_Torino)
Andrea_Venezia=prenotazione(Andrea,vacanza_Venezia)

df=pd.DataFrame({
    "Cliente":[nomeM,Paolo.nome,Marina.nome,Marta.nome,Andrea.nome],
    "Destinazione":citta,
    "Prezzo":costi.values(),
    "Giorno Partenza":pd.date_range("2018-03-20",periods=5,freq="m"),
    "Durata":[weekend_Roma.durata,settimana_Milano.durata,settimana_Napoli.durata,visita_Torino.durata,vacanza_Venezia.durata],
    "Incasso":[Mario_Roma.importo_finale(),Paolo_Milano.importo_finale(),Marina_Napoli.importo_finale(),Marta_Torino.importo_finale(),Andrea_Venezia.importo_finale()]
})

totale=0
n=0
for x in df["Incasso"][:]:
    totale+=x
    n+=1
#print(f"\nTotale ricavato:\n{totale}\nIn media:\n{totale/n}\nLe 3 destinazioni più vendute:\n{df.sort_values("Incasso",ascending=False).head(3)}")

# parte 5

print(df)
base=plt.figure(figsize=(10,6))

base.add_subplot(223)
plt.bar(citta,df["Incasso"],0.5,color=["r","brown","g","yellow","b"])
plt.ylabel("INCASSO",color="b")
plt.title("INCASSO PER OGNI DESTINAZIONE",fontsize=9,color="r")

base.add_subplot(211)
plt.plot(df["Giorno Partenza"],df["Incasso"],marker=("s"))
plt.ylabel("INCASSO",color="b")
plt.title("INCASSI NEL TEMPO",color="r")

base.add_subplot(224)
plt.pie(df["Incasso"],labels=df["Destinazione"],autopct="%1.2f%%")
plt.title("PERCENTUALE DI OGNI DESTINAZIONE",fontsize=9,color="r")
plt.show()