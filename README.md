# dataops_project
Description
Ce projet met en œuvre un pipeline DataOps complet et automatisé pour le traitement de données de ventes en ligne. Il utilise les outils modernes du stack data (Airflow, dbt, PostgreSQL, GitHub Actions) pour orchestrer, transformer, tester et valider les données de manière reproductible et maintenable.

Architecture du Pipeline

CSV (Online Retail) 
   -->  [Python]
sales.csv (nettoyé)
   -->  [Airflow]
PostgreSQL (raw_sales)
   --> [dbt]
stg_sales → fct_daily_revenue
   -->  [dbt test + GitHub Actions]
Validation automatisée


Qualité des données
La qualité est assurée à plusieurs niveaux :
Python : suppression des nulls (CustomerID, UnitPrice) et des doublons (InvoiceNo + StockCode)

dbt : nettoyage et transformation dans stg_sales, agrégation dans fct_daily_revenue

CI/CD : exécution automatique de dbt test à chaque push Git

Étapes de mise en route
1. Installation des dépendances
pip install -r requirements.txt

2. Préparer les données sources
Convertir le fichier Excel en CSV : dans le fichier load.py

3. Charger les données dans PostgreSQL
python scripts/load_sales.py

5. Exécuter les transformations dbt
dbt run
dbt test

6. Lancer le DAG Airflow
Accéder à Airflow sur http://localhost:8080, activer le DAG dbt_sales_pipeline.

 7. CI/CD avec GitHub Actions
Chaque push sur main ou develop déclenche :
dbt run
dbt test

Validation PostgreSQL (via script Python)
Fichier CI : .github/workflows/dbt.yml




