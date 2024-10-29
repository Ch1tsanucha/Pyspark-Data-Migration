from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("webtoon") \
    .master("spark://spark-master:7077") \
    .config("spark.executor.memory", "2g") \
    .config("spark.driver.memory", "2g") \
    .config("spark.jars.packages", "com.mysql:mysql-connector-j:9.1.0,org.postgresql:postgresql:42.7.4") \
    .getOrCreate()


postgredf = spark.read.format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/root_db") \
    .option("driver", "org.postgresql.Driver") \
    .option("dbtable", "employees") \
    .option("user", "root") \
    .option("password", "1234")\
    .load()

postgredf.write \
    .format("jdbc") \
    .option("driver","com.mysql.cj.jdbc.Driver") \
    .option("url", "jdbc:mysql://db:3306/root_db") \
    .option("dbtable", "employees") \
    .option("user", "root") \
    .option("password", "1234") \
    .mode("overwrite") \
    .save()

spark.stop()