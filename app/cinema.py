"""
Modulo per la gestione del cinema, sale e spettacoli
"""
from typing import Dict, List
from datetime import datetime


class Posto:
    """Rappresenta un singolo posto in una sala"""
    
    def __init__(self, id: str, fila: str, numero: int):
        self.id = id
        self.fila = fila
        self.numero = numero
        self.occupato = False
    
    def prenota(self) -> bool:
        """Prenota il posto se disponibile"""
        if not self.occupato:
            self.occupato = True
            return True
        return False
    
    def libera(self):
        """Libera il posto"""
        self.occupato = False
    
    def __str__(self):
        stato = "[X]" if self.occupato else self.id
        return stato


class Sala:
    """Rappresenta una sala cinematografica"""
    
    def __init__(self, numero_sala: int, capacita: int = 30):
        self.numero_sala = numero_sala
        self.capacita = capacita
        self.posti: Dict[str, Posto] = {}
        self.inizializza_posti()
    
    def inizializza_posti(self):
        """Crea i posti della sala"""
        file = ['A', 'B', 'C', 'D', 'E']
        posti_per_fila = self.capacita // len(file)
        
        for fila in file:
            for num in range(1, posti_per_fila + 1):
                posto_id = f"{fila}{num}"
                self.posti[posto_id] = Posto(posto_id, fila, num)
    
    def verifica_disponibilita(self, posto_id: str) -> bool:
        """Verifica se un posto è disponibile"""
        if posto_id in self.posti:
            return not self.posti[posto_id].occupato
        return False
    
    def prenota_posto(self, posto_id: str) -> bool:
        """Prenota un posto specifico"""
        if posto_id in self.posti:
            return self.posti[posto_id].prenota()
        return False
    
    def ottieni_posti_disponibili(self) -> List[str]:
        """Restituisce lista dei posti disponibili"""
        return [pid for pid, posto in self.posti.items() if not posto.occupato]
    
    def mostra_mappa_posti(self) -> str:
        """Mostra la mappa dei posti"""
        mappa = "\nMappa posti:\n"
        file = {}
        for posto_id, posto in self.posti.items():
            if posto.fila not in file:
                file[posto.fila] = []
            file[posto.fila].append(str(posto))
        
        for fila in sorted(file.keys()):
            mappa += f"{fila}: " + " ".join(file[fila]) + "\n"
        
        return mappa


class Spettacolo:
    """Rappresenta uno spettacolo cinematografico"""
    
    def __init__(self, id: str, titolo_film: str, orario: str, sala: Sala, prezzo: float = 8.50):
        self.id = id
        self.titolo_film = titolo_film
        self.orario = orario
        self.sala = sala
        self.prezzo = prezzo
    
    def ottieni_posti_disponibili(self) -> List[str]:
        """Ottiene i posti disponibili per questo spettacolo"""
        return self.sala.ottieni_posti_disponibili()
    
    def verifica_capienza(self) -> int:
        """Verifica quanti posti sono ancora disponibili"""
        return len(self.ottieni_posti_disponibili())
    
    def __str__(self):
        return f"{self.titolo_film} - {self.orario} - Sala {self.sala.numero_sala} - €{self.prezzo:.2f}"


class Cinema:
    """Rappresenta il cinema con le sue sale e spettacoli"""
    
    def __init__(self, nome: str):
        self.nome = nome
        self.sale: List[Sala] = []
        self.spettacoli: List[Spettacolo] = []
    
    def aggiungi_sala(self, sala: Sala):
        """Aggiunge una sala al cinema"""
        self.sale.append(sala)
    
    def aggiungi_spettacolo(self, spettacolo: Spettacolo):
        """Aggiunge uno spettacolo alla programmazione"""
        self.spettacoli.append(spettacolo)
    
    def ottieni_spettacoli_disponibili(self) -> List[Spettacolo]:
        """Restituisce tutti gli spettacoli disponibili"""
        return [s for s in self.spettacoli if s.verifica_capienza() > 0]
    
    def cerca_spettacolo(self, id: str) -> Spettacolo:
        """Cerca uno spettacolo per ID"""
        for spettacolo in self.spettacoli:
            if spettacolo.id == id:
                return spettacolo
        return None