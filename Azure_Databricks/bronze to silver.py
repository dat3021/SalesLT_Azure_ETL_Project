# Databricks notebook source
from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType


# COMMAND ----------

dbutils.fs.ls("mnt/bronze/SalesLT/")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Delete Null Column

# COMMAND ----------

df = spark.read.format('parquet').load('/mnt/bronze/SalesLT/Address/')
df = df.drop("AddressLine2")
df.write.mode("overwrite").parquet("/mnt/bronze/SalesLT/Address/")

# COMMAND ----------

df = spark.read.format('parquet').load('/mnt/bronze/SalesLT/Product/')
df = df.drop("DiscontinuedDate")
df.write.mode("overwrite").parquet("/mnt/bronze/SalesLT/Product/")
#df.select("DiscontinuedDate").distinct().show()

# COMMAND ----------

df = spark.read.format('parquet').load('/mnt/bronze/SalesLT/SalesOrderHeader/')
df = df.drop("Comment","CreditCardApprovalCode")
df.write.mode("overwrite").parquet("/mnt/bronze/SalesLT/SalesOrderHeader/")
#df.select("Comment").distinct().show()
#display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Change Date format

# COMMAND ----------

table_name = []
for i in dbutils.fs.ls("/mnt/bronze/SalesLT/"):
    table_name.append(i.name.split('/')[0])

table_name

# COMMAND ----------

for i in table_name:
    df = spark.read.format('parquet').load('/mnt/bronze/SalesLT/' + i + '/')
    for column in df.columns :
        if "date" in column or "Date" in column:                                                                    
            df = df.withColumn(column, df[column].cast(TimestampType()))
            df = df.withColumn(column, date_format(from_utc_timestamp(df[column], "Asia/Ho_Chi_Minh"), "dd-MM-yyyy"))
            
    df.write.format('delta').mode('overwrite').save("/mnt/silver/SalesLT/" + i + "/")
