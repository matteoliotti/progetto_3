import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#parte 1

nomeM="Mario Rossi"
etaM=34
saldo_contoM=2500.75
vipM=True
citta=["Roma","Milano","Bangkok","Hong Kong","New York","Los Angeles","Cairo","Johannesburg"]
costi={citta[0]:40,citta[1]:65,citta[2]:25,citta[3]:30,citta[4]:50,citta[5]:55,citta[6]:35,citta[7]:20}

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
        print(f"\nIl/La sig/sig.ra {self.cliente.nome} ha prenotato un viaggio verso {self.viaggio.destinazione} per {self.viaggio.durata} giorni.\nCosto totale: {self.importo_finale()}")
    def __repr__(self):
        return f"{self.cliente.nome} per {self.viaggio.destinazione}"

Mario=cliente(nomeM,etaM,vipM)
weekend_Roma=viaggio(citta[0],costi[citta[0]],2)
Mario_Roma=prenotazione(Mario,weekend_Roma)
Mario_Roma.dettagli()

# parte 3

simulazione=np.random.randint(200,2001,100)
print("\nSimulazione di prenoptazioni:\n",simulazione)
print("\nMedia:\n",np.mean(simulazione))
print("\nMassimo e minimo:\n",np.max(simulazione),np.min(simulazione))
print("\nDeviazione standard:\n",np.std(simulazione))

Prenotazioni_sopra_la_media=0
for x in np.where(simulazione>np.mean(simulazione))[0]:
    Prenotazioni_sopra_la_media+=1
print(f"\nPrenotazioni sopra la media:\n{Prenotazioni_sopra_la_media}%")

# parte 4

Paolo=cliente("Paolo Verdi",40,False)
Marina=cliente("Marina Verdi",18,False)
Marta=cliente("Marta Bianchi",27,True)
Andrea=cliente("Andrea Amari",28,True)
Giovanna=cliente("Giovanna Vento",22,False)
Matteo=cliente("Matteo Ventura",31,True)
Laura=cliente("Laura Ventura",30,False)

settimana_Milano=viaggio(citta[1],costi[citta[1]],7)
settimana_Bangkok=viaggio(citta[2],costi[citta[2]],7)
visita_Hong_Kong=viaggio(citta[3],costi[citta[3]],4)
vacanza_New_York=viaggio(citta[4],costi[citta[4]],14)
vacanza_Los_Angeles=viaggio(citta[5],costi[citta[5]],15)
weekend_Cairo=viaggio(citta[6],costi[citta[6]],3)
spedizione_Johannesburg=viaggio(citta[7],costi[citta[7]],28)

Paolo_Milano=prenotazione(Paolo,settimana_Milano)
Marina_Bangkok=prenotazione(Marina,settimana_Bangkok)
Marta_Hong_Kong=prenotazione(Marta,visita_Hong_Kong)
Andrea_New_york=prenotazione(Andrea,vacanza_New_York)
Giovanna_Los_Angeles=prenotazione(Giovanna,vacanza_Los_Angeles)
Matteo_Cairo=prenotazione(Matteo,weekend_Cairo)
Laura_Johannesburg=prenotazione(Laura,spedizione_Johannesburg)

df=pd.DataFrame({
    "Cliente":[nomeM,Paolo.nome,Marina.nome,Marta.nome,Andrea.nome,Giovanna.nome,Matteo.nome,Laura.nome],
    "Destinazione":citta,
    "Prezzo":costi.values(),
    "Giorno Partenza":pd.date_range("2023-03-20",periods=8,freq="ME"),
    "Durata":[Mario_Roma.viaggio.durata,Paolo_Milano.viaggio.durata,Marina_Bangkok.viaggio.durata,Marta_Hong_Kong.viaggio.durata,
              Andrea_New_york.viaggio.durata,Giovanna_Los_Angeles.viaggio.durata,Matteo_Cairo.viaggio.durata,Laura_Johannesburg.viaggio.durata],
    "Incasso":[Mario_Roma.importo_finale(),Paolo_Milano.importo_finale(),Marina_Bangkok.importo_finale(),Marta_Hong_Kong.importo_finale(),
               Andrea_New_york.importo_finale(),Giovanna_Los_Angeles.importo_finale(),Matteo_Cairo.importo_finale(),Laura_Johannesburg.importo_finale()]
})

totale=0
n=0
for x in df["Incasso"][:]:
    totale+=x
    n+=1
print(f"\nTotale ricavato da tutte le prenotazioni:\n{totale}\n\nIn media:\n{totale/n}\n\nLe 3 destinazioni più vendute:\n{df.sort_values("Incasso",ascending=False).head(3)}")

# parte 5

base=plt.figure(figsize=(8,6))

base.add_subplot(414)
plt.bar(citta,df["Incasso"],0.5,color=["b","orange","g","r","purple","brown","pink","gray"])
plt.ylabel("INCASSO",color="b")
plt.title("INCASSO PER OGNI DESTINAZIONE",fontsize=9,color="r")

base.add_subplot(411)
plt.plot(df["Giorno Partenza"],df["Incasso"],marker=("s"))
plt.ylabel("INCASSO",color="b")
plt.title("INCASSI NEL TEMPO",color="r")

base.add_subplot(312)
plt.pie(df["Incasso"],labels=df["Destinazione"],autopct="%1.0f%%")
plt.title("PERCENTUALE DI OGNI DESTINAZIONE",fontsize=9,color="r")
plt.show()

# parte 6

continenti={"Europa":[Mario_Roma,Paolo_Milano],"Asia":[Marina_Bangkok,Marta_Hong_Kong],
            "America":[Andrea_New_york,Giovanna_Los_Angeles],"Africa":[Matteo_Cairo,Laura_Johannesburg]}

media_incassi=[(Mario_Roma.importo_finale()+Paolo_Milano.importo_finale())/2,(Marina_Bangkok.importo_finale()+Marta_Hong_Kong.importo_finale())/2,
               (Andrea_New_york.importo_finale()+Giovanna_Los_Angeles.importo_finale())/2,(Matteo_Cairo.importo_finale()+Laura_Johannesburg.importo_finale())/2]

media_viaggi=[(Mario_Roma.viaggio.durata+Paolo_Milano.viaggio.durata)/2,(Marina_Bangkok.viaggio.durata+Marta_Hong_Kong.viaggio.durata)/2,
              (Andrea_New_york.viaggio.durata+Giovanna_Los_Angeles.viaggio.durata)/2,(Matteo_Cairo.viaggio.durata+Laura_Johannesburg.viaggio.durata)/2]

df2=pd.DataFrame({
    "Continenti":continenti.keys(),
    "Incasso medio":media_incassi,
    "Durata media": media_viaggi
})

df2.to_csv("prenotazioni_analizzate.csv",index=False)

# parte 7

clienti=(Mario,Paolo,Marina,Marta,Andrea,Giovanna,Matteo,Laura)
viaggi=(weekend_Roma,settimana_Milano,settimana_Bangkok,visita_Hong_Kong,
        vacanza_New_York,vacanza_Los_Angeles,weekend_Cairo,spedizione_Johannesburg)

Mario_Cairo=prenotazione(Mario,weekend_Cairo)
Mario_Hong_Kong=prenotazione(Mario,visita_Hong_Kong)
Marina_Milano=prenotazione(Marina,settimana_Milano)
Marta_Cairo=prenotazione(Marta,weekend_Cairo)
Andrea_Bangkok=prenotazione(Andrea,settimana_Bangkok)
Andrea_Roma=prenotazione(Andrea,weekend_Roma)
Andrea_Johannesburg=prenotazione(Andrea,spedizione_Johannesburg)
Giovanna_New_York=prenotazione(Giovanna,vacanza_New_York)
Matteo_Roma=prenotazione(Matteo,weekend_Roma)
Matteo_Hong_Kong=prenotazione(Matteo,visita_Hong_Kong)

prenotazioni=(Mario_Roma,Paolo_Milano,Marina_Bangkok,Marta_Hong_Kong,Andrea_New_york,Giovanna_Los_Angeles,Matteo_Cairo,
              Laura_Johannesburg,Mario_Cairo,Mario_Hong_Kong,Marina_Milano,Marta_Cairo,Andrea_Bangkok,Andrea_Roma,Andrea_Johannesburg,
              Giovanna_New_York,Matteo_Roma,Matteo_Hong_Kong)

d={}

continenti.clear()

media_incassi.clear()

media_viaggi.clear()

for x in prenotazioni:
    d.setdefault(x.cliente.nome,0)
    d[x.cliente.nome]+=1

    if x.viaggio.destinazione==citta[0] or x.viaggio.destinazione==citta[1]:
        continenti.setdefault("Europa",[])
        continenti["Europa"].append(x)
        
    elif x.viaggio.destinazione==citta[2] or x.viaggio.destinazione==citta[3]:
        continenti.setdefault("Asia",[])
        continenti["Asia"].append(x)

    elif x.viaggio.destinazione==citta[4] or x.viaggio.destinazione==citta[5]:
        continenti.setdefault("America",[])
        continenti["America"].append(x)

    elif x.viaggio.destinazione==citta[6] or x.viaggio.destinazione==citta[7]:
        continenti.setdefault("Africa",[])
        continenti["Africa"].append(x)

for x in continenti:
    i=0
    n=0
    for y in continenti[x]:
        i+=y.importo_finale()
        n+=1
    media_incassi.append(i/n)

    i=0
    n=0
    for y in continenti[x]:
        i+=y.viaggio.durata
        n+=1
    media_viaggi.append(i/n)


df3=pd.DataFrame({
    "Cliente":d.keys(),
    "prenotazioni":d.values()
})

print(f"\nI 3 clienti che hanno fatto il maggior numero di prenotazini sono:\n{df3.sort_values("prenotazioni",ascending=False).head(3)}")
base2=plt.figure(figsize=(8,6))

base2.add_subplot(211)
plt.bar(continenti.keys(),media_incassi,width=0.3,color=["g","r","b","black"])
plt.title("INCASSO MEDIO DEI VIAGGI",fontsize=9,color="r")
plt.ylabel("INCASSI",color="b")

base2.add_subplot(212)
plt.plot(continenti.keys(),media_viaggi,marker="o")
plt.title("DURATA MEDIA DEI VIAGGI",fontsize=9,color="r")
plt.ylabel("PERIODI",color="b")
plt.show()