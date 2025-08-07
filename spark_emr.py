from pyspark.sql import SparkSession

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Inizialization of spark Session with S3 Access 
spark = SparkSession.builder.appName("WriteDataFrameToS").getOrCreate()

# Definition of the DataFrame schema 

schema = StructType(
    [
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("profession", StringType(), True),
]
)


# Create a DataFrame 

data = [
    (1, "Alice", "Engineer"),
    (2, "Bob", "Doctor"),
    (3, "Charlie", "Teacher")
]

df = spark.createDataFrame(data, schema)

# Write the DataFrame to S3 

output_path = "arn:aws:s3:::test-aws-bucket-profession-ai-adi/from_emr"
df.write.mode("overwrite").csv(output_path)

# Stop the Spark Session
spark.stop()

"""
Questo scrip quindi va a creare questo Dataframe e lo stora in S3 ma questo lo fa attraverso
uso di spark quindi in maniera distribuita e questo lo notiamo anche dalla cartella
in cui viene salavto il file rom_emr erche contiene piu file e non uno singolo
Infatti quando si lavora con Spark, i dati vengono partizionati e distribuiti
tra i vari nodi del cluster, e quindi il risultato finale è composto da più file.
"""

# Dovro fare Upload di questo sprit nel bucket S3 