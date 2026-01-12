# Gestionale-cinema

# Sistema di Ticketing Cinema

Sistema completo per l'acquisto di biglietti cinematografici con modellazione UML, BPMN e C4.

## Struttura del Progetto

```
cinema-ticketing/
├── README.md
├── main.py
├── src/
│   ├── __init__.py
│   ├── cinema.py
│   ├── biglietto.py
│   ├── cliente.py
│   └── ordine.py
├── diagrammi/
│   ├── use_case.puml
│   ├── bpmn_processo.bpmn
│   ├── component.puml
│   ├── deployment.puml
│   ├── class.puml
│   ├── c4_context.puml
│   ├── c4_container.puml
│   └── c4_component.puml
└── requirements.txt
```

## Requisiti

- Python 3.8+
- VS Code con estensioni:
  - PlantUML
  - BPMN.io editor

## Installazione

```bash
# Clona o scarica il progetto
cd cinema-ticketing

# Installa dipendenze (opzionale per versione base)
pip install -r requirements.txt
```

## Esecuzione

### Da terminale
```bash
python main.py
```

### Da VS Code
1. Apri il progetto in VS Code
2. Apri `main.py`
3. Premi F5 o Run > Start Debugging

## Esempio di Utilizzo

```
=== Sistema di Ticketing Cinema ===

1. Visualizza Film Disponibili
2. Acquista Biglietto
3. Visualizza Ordini
4. Esci

Scelta: 2

Film disponibili:
1. Il Padrino - 20:30 - Sala 1
2. Inception - 21:00 - Sala 2

Seleziona film: 1

Posti disponibili per Sala 1:
A1 A2 A3 A4 A5
B1 B2 [X] B4 B5

Seleziona posto (es. A1): A2

Inserisci nome: Mario Rossi
Inserisci email: mario@email.com

Biglietto acquistato con successo!
Codice ordine: ORD-20250112-001
```

## Diagrammi

### Visualizzare i Diagrammi UML/C4
1. Apri file `.puml` in VS Code
2. Premi `Alt + D` per preview
3. Esporta come PNG/SVG se necessario

### Visualizzare BPMN
1. Apri file `.bpmn` in VS Code
2. L'estensione BPMN.io aprirà automaticamente l'editor

## Architettura

Il sistema implementa:
- **Pattern OOP** con classi Cinema, Biglietto, Cliente, Ordine
- **Gestione disponibilità** posti in tempo reale
- **Validazione** dati cliente e selezioni
- **Persistenza** semplice in memoria (estendibile a database)

## Note Tecniche

- Database: SQLite (simulato in memoria per semplicità)
- Backend: Architettura pronta per FastAPI
- Client: CLI (estendibile a mobile/web)
- Sistema operativo: Linux (deployment)

## Autore

Progetto per esercitazione su modellazione del software