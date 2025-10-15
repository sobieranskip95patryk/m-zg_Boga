from kafka import KafkaConsumer
import json
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def process_migi_tasks(bootstrap_servers: str = 'localhost:9092'):
    """
    Odbiera i przetwarza zadania z sieci MIGI 7G.
    """
    try:
        consumer = KafkaConsumer(
            'migi_tasks',
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        for message in consumer:
            task = message.value['task']
            logging.info(f"Odebrano zadanie: {task}")
            # Symulacja odpowiedzi deweloperów
            contribution = random.uniform(0.7, 0.95)
            logging.info(f"Odpowiedź MIGI 7G: contribution={contribution}")
            return contribution
    except Exception as e:
        logging.error(f"Błąd przetwarzania zadania: {e}")
        return 0.5

if __name__ == '__main__':
    process_migi_tasks()