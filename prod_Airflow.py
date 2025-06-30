from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from kafka import KafkaProducer
import json

def send_kafka_message():
    producer = KafkaProducer(
        bootstrap_servers='kfakasda.eastus.cloudapp.azure.com:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    message = {
        "destination": "elastic",
        "directory": "/tmp",
        "nomclient": "DIOP",
        "prix": 100,
        "ville": "Paris"
    }

    producer.send('diattara', value=message)
    producer.flush()
    print("✅ Message envoyé avec succès.")

# Définition du DAG
with DAG(
    dag_id='kafka_producer_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  # exécute manuellement
    catchup=False,
    tags=["kafka", "test"]
) as dag:

    send_message_task = PythonOperator(
        task_id='send_kafka_message',
        python_callable=send_kafka_message
    )
