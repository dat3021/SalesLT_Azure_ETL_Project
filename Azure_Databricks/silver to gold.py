# Databricks notebook source
dbutils.fs.ls('/mnt/silver/SalesLT')

# COMMAND ----------

from pyspark.sql.functions import col 

def rename_column(df):
    column_names = df.columns
    rename_map = {}

    for old_col_name in column_names:
        new_part_col_name = []
        for index, char in enumerate(old_col_name):
            if index != 0 and char.isupper() and not old_col_name[index - 1].isupper():
                new_part_col_name.append("_")
            new_part_col_name.append(char.lower())
        new_col_name = "".join(new_part_col_name).lstrip("_")

        rename_map[old_col_name] = new_col_name

    for old_col_name, new_col_name in rename_map.items():
        df = df.withColumnRenamed(old_col_name,new_col_name)

    return df
    

# COMMAND ----------

df = spark.read.format('delta').load('/mnt/silver/SalesLT/Customer/')
display(df)

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('/mnt/silver/SalesLT/'):
    table_name.append(i.name.split("/")[0])

table_name

# COMMAND ----------

for name in table_name:
    df = spark.read.format('delta').load('/mnt/silver/SalesLT/' + name)
    df = rename_column(df)

    df.write.format('parquet').mode('overwrite').save('/mnt/gold/SalesLT/' + name + '/')
