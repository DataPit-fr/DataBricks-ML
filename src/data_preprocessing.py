from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def load_data(spark, path):
    return spark.read.format("csv").option("header", "true").load(path)

def clean_data(df):
    return df.na.drop()

def engineer_features(df):
    return df.withColumn("feature", col("value") * 2)
