# 📘 Introduction à Apache Airflow

## 🎯 Objectifs du cours
Ce document vise à vous faire découvrir Apache Airflow, un outil d’orchestration de workflows écrit en Python. À la fin de cette lecture, vous serez capable de :

- Comprendre ce qu’est Apache Airflow et à quoi il sert
- Identifier les concepts clés (DAG, tâche, opérateur…)
- Créer un premier DAG simple
- Comprendre comment Airflow planifie et exécute des workflows

---

## 📌 1. Qu’est-ce qu’Apache Airflow ?

Apache Airflow est un outil **open-source** développé par Airbnb en 2014, devenu un projet officiel de la **Fondation Apache**.

Il permet de :
- Concevoir, planifier, et surveiller des **workflows** (pipelines de données)
- Orchestrer des tâches sous forme de **graphes dirigés acycliques (DAGs)**
- Exécuter des tâches de manière planifiée, conditionnelle ou parallèle

> ✨ Airflow est écrit en **Python**, ce qui permet de décrire ses workflows sous forme de code.

---

## 🧩 2. Concepts clés

### 2.1 DAG (Directed Acyclic Graph)
Un **DAG** est un ensemble de tâches liées entre elles, représentées comme un graphe sans cycle. Il définit **l’ordre d’exécution** des tâches.

### 2.2 Task (Tâche)
Une tâche est une unité de travail (exécuter un script, une commande, une API, etc.).

### 2.3 Operator (Opérateur)
Un opérateur représente **le type de tâche** :
- `PythonOperator` : fonction Python
- `BashOperator` : commande shell
- `EmailOperator`, `PostgresOperator`, etc.

### 2.4 Scheduler
C’est le **planificateur** qui exécute les DAGs selon un calendrier défini (`@daily`, `@hourly`, etc.).

### 2.5 Executor
C’est l’**exécuteur** des tâches (localement, en parallèle, via Celery, etc.).

---

## 🏗️ 3. Exemple de DAG simple

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="mon_premier_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    t1 = BashOperator(
        task_id="tache_1",
        bash_command="echo 'Bonjour depuis Airflow!'"
    )

    t2 = BashOperator(
        task_id="tache_2",
        bash_command="echo 'Deuxième tâche.'"
    )

    t1 >> t2  # t1 s’exécute avant t2
