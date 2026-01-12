"""
Modulo per la gestione degli ordini
"""
from datetime import datetime
from typing import List
import random


class GestorePagamenti:
    """Gestisce le operazioni di pagamento"""
    
    @staticmethod
    def elabora_pagamento(ordine) -> bool:
        """Simula l'elaborazione di un pagamento"""
        # Simulazione: 95% di successo
        return random.random() > 0.05
    
    @staticmethod
    def verifica_transazione() -> bool:
        """Verifica lo stato di una transazione"""
        return True


class Ordine:
    """Rappresenta un ordine di acquisto biglietti"""
    
    _contatore_ordini = 0
    
    def __init__(self, cliente):
        Ordine._contatore_ordini += 1
        self.id = self._genera_id_ordine()
        self.cliente = cliente
        self.biglietti: List = []
        self.totale = 0.0
        self.stato = "In attesa"
        self.data_ordine = datetime.now()
    
    def _genera_id_ordine(self) -> str:
        """Genera un ID univoco per l'ordine"""
        data = datetime.now().strftime("%Y%m%d")
        return f"ORD-{data}-{Ordine._contatore_ordini:03d}"
    
    def aggiungi_biglietto(self, biglietto):
        """Aggiunge un biglietto all'ordine"""
        self.biglietti.append(biglietto)
        self.calcola_totale()
    
    def calcola_totale(self) -> float:
        """Calcola il totale dell'ordine"""
        self.totale = sum(b.prezzo for b in self.biglietti)
        return self.totale
    
    def conferma_ordine(self) -> bool:
        """Conferma l'ordine dopo il pagamento"""
        gestore = GestorePagamenti()
        if gestore.elabora_pagamento(self):
            self.stato = "Confermato"
            return True
        else:
            self.stato = "Pagamento fallito"
            return False
    
    def stampa_riepilogo(self) -> str:
        """Stampa un riepilogo dell'ordine"""
        riepilogo = f"""
{'='*50}
           RIEPILOGO ORDINE
{'='*50}
ID Ordine: {self.id}
Cliente: {self.cliente.nome}
Email: {self.cliente.email}
Data: {self.data_ordine.strftime("%d/%m/%Y %H:%M")}
Stato: {self.stato}

Biglietti:
"""
        for i, biglietto in enumerate(self.biglietti, 1):
            riepilogo += f"{i}. {biglietto.spettacolo.titolo_film} - Posto {biglietto.posto.id} - €{biglietto.prezzo:.2f}\n"
        
        riepilogo += f"\nTOTALE: €{self.totale:.2f}\n"
        riepilogo += "="*50 + "\n"
        
        return riepilogo
    
    def __str__(self):
        return f"Ordine {self.id} - {self.cliente.nome} - €{self.totale:.2f} - {self.stato}"