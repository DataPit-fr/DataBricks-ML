# Databricks Spark ML Project

Ce projet contient un pipeline complet :
- Ingestion de données Spark
- Préparation & Feature Engineering
- Entraînement d'un modèle MLlib
- Déploiement d’un job Databricks

Technologies :
- PySpark
- Databricks ML
- Delta Lake
- MLflow

# PROJET : Prévision de la demande et optimisation du stock pour une chaîne de magasins
## Problématique métier

Une chaîne de magasins souhaite :

- mieux prédire la demande quotidienne pour chaque produit et chaque magasin,

- réduire les ruptures de stock,

- optimiser les niveaux de stock pour éviter les surplus.

## Objectif du projet : Construire un pipeline complet qui :

- ingère les historiques de ventes et données produits dans un Delta Lake,

- prépare et nettoie les données avec PySpark,

- entraîne un modèle de prévision de la demande (forecast) avec Databricks ML,

- trace et compare les modèles avec MLflow,

- expose une table de recommandation des stocks à maintenir.
