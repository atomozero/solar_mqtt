# Simulazione della Produzione di Energia Fotovoltaica e Invio via MQTT

Un semplice script Python che simula la produzione di energia fotovoltaica utilizzando una curva a campana basata sull'ora del giorno e la posizione geografica. I dati simulati vengono inviati a un broker MQTT per l'integrazione con sistemi IoT o altre applicazioni.

## Funzionalità

- **Simulazione dell'energia fotovoltaica**: Calcola la produzione di energia durante il giorno, con un picco a mezzogiorno, utilizzando la posizione geografica (latitudine e longitudine) e l'ora corrente.
- **Invio dati via MQTT**: I dati simulati vengono inviati a un broker MQTT per consentire l'integrazione con altri sistemi di monitoraggio o automazione.
- **Facile configurazione**: Personalizza i parametri principali come l'indirizzo del broker MQTT, la posizione geografica e la frequenza di invio dei dati.

## Requisiti

- Python 3.x
- Librerie Python:
  - `paho-mqtt`
  - `astral`
  
## Installazione

1. **Clona il repository**:
    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. **Crea e attiva un ambiente virtuale**:
    ```bash
    python3 -m venv my_env
    source my_env/bin/activate
    ```

3. **Installa le dipendenze**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Modifica la configurazione**: Apri lo script e personalizza i parametri del broker MQTT e della posizione geografica.

5. **Esegui lo script**:
    ```bash
    python main.py
    ```

## Configurazione

Modifica le seguenti variabili nello script `main.py` per personalizzare la tua configurazione:

- `mqtt_broker`: Indirizzo del broker MQTT
- `mqtt_port`: Porta del broker MQTT (default: 1883)
- `mqtt_topic`: Topic MQTT su cui pubblicare i dati
- `city_name`: Nome della città per la posizione geografica
- `location`: Latitudine e longitudine della posizione

## Esempio di Utilizzo

Lo script simula la produzione di energia durante il giorno. Esegue un ciclo infinito che calcola e invia i dati di produzione ogni 15 minuti. Può essere utilizzato per testare sistemi IoT che richiedono dati in tempo reale, come piattaforme di monitoraggio dell'energia.

## Contributi

Se vuoi contribuire al progetto, sentiti libero di fare una pull request o di aprire un issue per discutere delle modifiche che vorresti vedere implementate.

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Consulta il file `LICENSE
