
# créer le container airflowlocal depuis la commande run
docker run --name airflowlocal -p 9090:8080  apache/airflow:latest standalone

# créer les services décrits dans le fichier airflow-compose.yml grâce à la commande compose
docker compose -f airflow-compose.yml up -d