from datetime import datetime
from enum import Enum
from dataclasses import dataclass

type ID = int

class Stav(Enum):
    ZAREGISTROVANA = "Zaregistrovaná"
    ODESLANA = "Odeslaná"
    NA_CESTE = "Na cestě"
    ZTRACENA = "Ztracená" 
    DORUCENA = "Doručená"
    VRACENA = "Vrácená"
    
@dataclass
class Zasilka:
    id: ID
    datum: datetime
    odesilatel: str
    prijemce: str
    adresa_prijemce: str
    stav: Stav
    historie: list[tuple[datetime, Stav]]

class PostovniSluzba:
    def __init__(self):
        self.zasilky:dict[ID,Zasilka] = {}

    def registruj_zasilku(self, id: ID, odesilatel: str, prijemce: str, adresa_prijemce: str):
        self.zasilky[id] = (Zasilka(id, datetime.now(), odesilatel, prijemce, adresa_prijemce, Stav.ZAREGISTROVANA, [(datetime.now(), Stav.ZAREGISTROVANA)]))

    def zmena_stavu_zasilky(self, id: ID, novy_stav: Stav):
        if id in self.zasilky:
            self.zasilky[id].stav = novy_stav
            self.zasilky[id].historie.append((datetime.now(), novy_stav))
        else:
            print(f"Zásilka s ID {id} nebyla nalezena.")
            
    def zasilka_prevzata(self, id: ID):
        self.zmena_stavu_zasilky(id, Stav.ODESLANA)

    def zasilka_ztracena(self, id: ID):
        self.zmena_stavu_zasilky(id, Stav.ZTRACENA)

    def zasilka_na_ceste(self, id: ID):
        self.zmena_stavu_zasilky(id, Stav.NA_CESTE)

    def zasilka_dorucena(self, id: ID):
        self.zmena_stavu_zasilky(id, Stav.DORUCENA)

    def zasilka_vracena(self, id: ID):
        self.zmena_stavu_zasilky(id, Stav.VRACENA)

    def historie_zasilky(self, id: ID) -> list[tuple[datetime, Stav]]:
        if id in self.zasilky:
            return self.zasilky[id].historie
        else:
            print(f"Zásilka s ID {id} nebyla nalezena.")
            return []
        
    def zasilka_info(self, id: ID) -> str:
        if id in self.zasilky:
            zasilka = self.zasilky[id]
            return f"ID: {zasilka.id}, Datum: {zasilka.datum}, Odesílatel: {zasilka.odesilatel}, Příjemce: {zasilka.prijemce}, Adresa příjemce: {zasilka.adresa_prijemce}, Stav: {zasilka.stav.value}"
        else:
            print(f"Zásilka s ID {id} nebyla nalezena.")
            return ""
