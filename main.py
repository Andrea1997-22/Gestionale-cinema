"""
Sistema di Ticketing Cinema - Programma Principale
"""
import sys
import os

# Aggiungi il percorso src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from app.cinema import Cinema, Sala, Spettacolo
from app.cliente import Cliente
from app.biglietto import Biglietto
from app.ordine import Ordine


class SistemaTicketing:
    """Classe principale per gestire il sistema di ticketing"""
    
    def __init__(self):
        self.cinema = self._inizializza_cinema()
        self.ordini = []
        self.cliente_corrente = None
    
    def _inizializza_cinema(self) -> Cinema:
        """Inizializza il cinema con sale e spettacoli"""
        cinema = Cinema("Cinema Torino")
        
        # Crea le sale
        sala1 = Sala(1, 30)
        sala2 = Sala(2, 30)
        sala3 = Sala(3, 30)
        
        cinema.aggiungi_sala(sala1)
        cinema.aggiungi_sala(sala2)
        cinema.aggiungi_sala(sala3)
        
        # Simula alcuni posti occupati
        sala1.prenota_posto("B3")
        sala1.prenota_posto("C2")
        sala2.prenota_posto("A1")
        
        # Crea gli spettacoli
        spettacolo1 = Spettacolo("S001", "Il Padrino", "20:30", sala1, 9.00)
        spettacolo2 = Spettacolo("S002", "Inception", "21:00", sala2, 8.50)
        spettacolo3 = Spettacolo("S003", "Interstellar", "22:00", sala3, 10.00)
        
        cinema.aggiungi_spettacolo(spettacolo1)
        cinema.aggiungi_spettacolo(spettacolo2)
        cinema.aggiungi_spettacolo(spettacolo3)
        
        return cinema
    
    def mostra_menu_principale(self):
        """Mostra il menu principale"""
        print("\n" + "="*50)
        print("  SISTEMA DI TICKETING CINEMA TORINO")
        print("="*50)
        print("\n1. Visualizza Film Disponibili")
        print("2. Acquista Biglietto")
        print("3. Visualizza Ordini")
        print("4. Esci")
        print()
    
    def visualizza_film(self):
        """Visualizza i film disponibili"""
        print("\n" + "="*50)
        print("  FILM DISPONIBILI")
        print("="*50)
        
        spettacoli = self.cinema.ottieni_spettacoli_disponibili()
        
        if not spettacoli:
            print("\nNessun film disponibile al momento.")
            return
        
        for i, spettacolo in enumerate(spettacoli, 1):
            posti_disp = spettacolo.verifica_capienza()
            print(f"\n{i}. {spettacolo}")
            print(f"   Posti disponibili: {posti_disp}/{spettacolo.sala.capacita}")
    
    def acquista_biglietto(self):
        """Processo di acquisto biglietto"""
        print("\n" + "="*50)
        print("  ACQUISTO BIGLIETTO")
        print("="*50)
        
        # Mostra spettacoli
        spettacoli = self.cinema.ottieni_spettacoli_disponibili()
        
        if not spettacoli:
            print("\n❌ Nessun film disponibile.")
            input("\nPremere Enter per continuare...")
            return
        
        print("\nFilm disponibili:")
        for i, spettacolo in enumerate(spettacoli, 1):
            print(f"{i}. {spettacolo}")
        
        try:
            scelta = int(input("\nSeleziona film (numero): "))
            if scelta < 1 or scelta > len(spettacoli):
                print("❌ Selezione non valida.")
                return
            
            spettacolo_selezionato = spettacoli[scelta - 1]
            
            # Verifica disponibilità
            if spettacolo_selezionato.verifica_capienza() == 0:
                print("\n❌ Spiacenti, non ci sono posti disponibili per questo spettacolo.")
                print("🔔 Registrazione per notifica disponibilità (funzionalità futura)")
                input("\nPremere Enter per continuare...")
                return
            
            # Mostra mappa posti
            print(spettacolo_selezionato.sala.mostra_mappa_posti())
            print("\nPosti disponibili:", ", ".join(spettacolo_selezionato.ottieni_posti_disponibili()[:10]) + "...")
            
            # Selezione posto
            posto_id = input("\nSeleziona posto (es. A1): ").upper()
            
            if not spettacolo_selezionato.sala.verifica_disponibilita(posto_id):
                print("\n❌ Posto non disponibile o non valido.")
                input("\nPremere Enter per continuare...")
                return
            
            # Dati cliente
            print("\n--- Dati Cliente ---")
            nome = input("Nome e Cognome: ")
            email = input("Email: ")
            telefono = input("Telefono (opzionale): ")
            
            cliente = Cliente(f"CLI{len(self.ordini)+1:03d}", nome, email, telefono if telefono else None)
            
            if not cliente.validazione_email():
                print("\n❌ Email non valida.")
                input("\nPremere Enter per continuare...")
                return
            
            # Prenota posto
            if spettacolo_selezionato.sala.prenota_posto(posto_id):
                posto = spettacolo_selezionato.sala.posti[posto_id]
                
                # Crea biglietto
                biglietto = Biglietto(spettacolo_selezionato, posto, cliente)
                
                # Crea ordine
                ordine = Ordine(cliente)
                ordine.aggiungi_biglietto(biglietto)
                
                # Mostra riepilogo
                print(ordine.stampa_riepilogo())
                
                conferma = input("Confermare l'acquisto? (s/n): ").lower()
                
                if conferma == 's':
                    print("\n⏳ Elaborazione pagamento in corso...")
                    
                    if ordine.conferma_ordine():
                        self.ordini.append(ordine)
                        print("\n✅ Pagamento confermato!")
                        print(biglietto.stampa_biglietto())
                        print(f"📧 Conferma inviata a: {cliente.email}")
                    else:
                        # Libera il posto in caso di errore
                        posto.libera()
                        print("\n❌ Pagamento fallito. Riprovare.")
                else:
                    # Libera il posto
                    posto.libera()
                    print("\n❌ Acquisto annullato.")
            else:
                print("\n❌ Errore nella prenotazione del posto.")
            
            input("\nPremere Enter per continuare...")
            
        except ValueError:
            print("\n❌ Input non valido.")
            input("\nPremere Enter per continuare...")
        except Exception as e:
            print(f"\n❌ Errore: {e}")
            input("\nPremere Enter per continuare...")
    
    def visualizza_ordini(self):
        """Visualizza gli ordini effettuati"""
        print("\n" + "="*50)
        print("  ORDINI EFFETTUATI")
        print("="*50)
        
        if not self.ordini:
            print("\nNessun ordine effettuato.")
        else:
            for ordine in self.ordini:
                print(ordine.stampa_riepilogo())
        
        input("\nPremere Enter per continuare...")
    
    def esegui(self):
        """Loop principale dell'applicazione"""
        while True:
            self.mostra_menu_principale()
            
            try:
                scelta = input("Scelta: ")
                
                if scelta == '1':
                    self.visualizza_film()
                    input("\nPremere Enter per continuare...")
                elif scelta == '2':
                    self.acquista_biglietto()
                elif scelta == '3':
                    self.visualizza_ordini()
                elif scelta == '4':
                    print("\n👋 Grazie per aver usato il sistema di ticketing!")
                    print("Arrivederci!\n")
                    break
                else:
                    print("\n❌ Scelta non valida. Riprovare.")
                    input("\nPremere Enter per continuare...")
            
            except KeyboardInterrupt:
                print("\n\n👋 Interruzione utente. Arrivederci!\n")
                break
            except Exception as e:
                print(f"\n❌ Errore imprevisto: {e}")
                input("\nPremere Enter per continuare...")


def main():
    """Funzione principale"""
    sistema = SistemaTicketing()
    sistema.esegui()


if __name__ == "__main__":
    main()