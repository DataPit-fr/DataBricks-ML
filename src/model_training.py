from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
import mlflow

def train_model(df):
    assembler = VectorAssembler(
        inputCols=["feature"],
        outputCol="features"
    )
    data = assembler.transform(df)
    
    lr = LinearRegression(featuresCol="features", labelCol="label")
    
    with mlflow.start_run():
        model = lr.fit(data)
        mlflow.spark.log_model(model, "model")

    return model
