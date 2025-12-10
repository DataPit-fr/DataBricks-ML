param(
    [string] = "1234"
)

Write-Output "Exécution du job Databricks..."

databricks jobs run-now --job-id 

Write-Output "Job lancé."
