"""
Modulo per la gestione dei biglietti
"""
from datetime import datetime
import random
import string


class Biglietto:
    """Rappresenta un biglietto per uno spettacolo"""
    
    def __init__(self, spettacolo, posto, cliente):
        self.codice = self.genera_codice()
        self.spettacolo = spettacolo
        self.posto = posto
        self.cliente = cliente
        self.prezzo = spettacolo.prezzo
        self.data_emissione = datetime.now()
    
    def genera_codice(self) -> str:
        """Genera un codice univoco per il biglietto"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return f"TKT-{timestamp}-{random_str}"
    
    def stampa_biglietto(self) -> str:
        """Genera una rappresentazione stampabile del biglietto"""
        biglietto_str = f"""
{'='*50}
           BIGLIETTO CINEMA
{'='*50}
Codice: {self.codice}
Film: {self.spettacolo.titolo_film}
Orario: {self.spettacolo.orario}
Sala: {self.spettacolo.sala.numero_sala}
Posto: {self.posto.id}
Cliente: {self.cliente.nome}
Prezzo: €{self.prezzo:.2f}
Data emissione: {self.data_emissione.strftime("%d/%m/%Y %H:%M")}
{'='*50}
        """
        return biglietto_str
    
    def __str__(self):
        return f"Biglietto {self.codice} - {self.spettacolo.titolo_film} - Posto {self.posto.id}"