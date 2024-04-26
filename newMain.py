from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark with Delta Lake and Iceberg") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.1.0,org.apache.iceberg:iceberg-spark3-runtime:0.12.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog") \
    .config("spark.sql.catalog.spark_catalog.type", "hive") \
    .enableHiveSupport() \
    .getOrCreate()
