param(
    [string] = "/Repos/Pierre/databricks-spark-ml-project"
)

Write-Output "Déploiement vers Databricks…"

databricks workspace mkdirs 

databricks workspace import_dir 
    -o 
    -f SOURCE 
    notebooks 
    /notebooks

Write-Output "Import terminé."
