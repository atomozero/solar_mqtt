import paho.mqtt.client as mqtt
import time
import datetime
import math
from astral.sun import sun
from astral import LocationInfo

# Configurazione MQTT
mqtt_broker = "indirizzo_broker"  # Indirizzo del broker MQTT
mqtt_port = 1883  # Porta MQTT
mqtt_topic = "energia_fotovoltaico"  # Topic MQTT

# Ottieni la posizione geografica
city_name = "Venice"
location = LocationInfo(city_name, "Italy", "Europe/Rome", 45.44, 12.31)

# Funzione per simulare la produzione di energia con andamento a campana
def simula_produzione_energia_campana():
    now = datetime.datetime.now(datetime.timezone.utc)
    solar_info = sun(location.observer, date=now, tzinfo=location.timezone)

    # Controlla se siamo fuori dalle ore di luce
    if now < solar_info['sunrise'] or now > solar_info['sunset']:
        return 0  # Nessuna produzione fuori dalle ore di luce

    day_length = (solar_info['sunset'] - solar_info['sunrise']).seconds
    time_since_sunrise = (now - solar_info['sunrise']).seconds
    midday = solar_info['sunrise'] + datetime.timedelta(seconds=day_length / 2)
    time_from_midday = abs((now - midday).seconds)

    # Calcola la produzione con una curva a campana
    max_production = 500  # Produzione massima a mezzogiorno in Wh
    std_dev = day_length / 6  # Deviazione standard per regolare la larghezza della campana
    production = max_production * math.exp(-(time_from_midday ** 2) / (2 * std_dev ** 2))

    return production

# Callback per la connessione MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connesso al broker MQTT")
    else:
        print(f"Errore di connessione MQTT, codice di ritorno: {rc}")

# Creazione del client MQTT
client = mqtt.Client()
client.on_connect = on_connect

# Connessione al broker MQTT
client.connect(mqtt_broker, mqtt_port)

# Avvia il loop di elaborazione in un thread separato
client.loop_start()

# Loop principale
while True:
    energia_prodotta = simula_produzione_energia_campana()
    client.publish(mqtt_topic, energia_prodotta)
    print("Energia prodotta:", energia_prodotta, "Wh")
    time.sleep(900)  # Attendi 15 minuti (900 secondi)
