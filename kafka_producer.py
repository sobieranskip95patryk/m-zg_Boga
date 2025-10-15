from kafka import KafkaProducer
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def send_task_to_migi(task: str, bootstrap_servers: str = 'localhost:9092'):
    """
    Wysyła zadanie do sieci MIGI 7G przez Kafkę.
    """
    try:
        producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        producer.send('migi_tasks', {'task': task})
        producer.flush()
        logging.info(f"Wysłano zadanie do MIGI 7G: {task}")
    except Exception as e:
        logging.error(f"Błąd wysyłania zadania: {e}")

if __name__ == '__main__':
    send_task_to_migi("Zaprojektuj robota.")