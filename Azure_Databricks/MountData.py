# Databricks notebook source
dbutils.fs.unmount("/mnt/bronze")

# COMMAND ----------

dbutils.fs.unmount("/mnt/silver")


# COMMAND ----------

configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": "49c88c11-2513-4a59-935c-4ac4658a033f",
    "fs.azure.account.oauth2.client.secret": '~UU8Q~BY_qGtKtBBwuqDcgFJcRDO.Cfk91npLbMY',
    "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/4150d5a0-6540-4251-bea3-960daba3060a/oauth2/token"
}

# COMMAND ----------

dbutils.fs.mount(
    source = "abfss://bronze@adventure2810.dfs.core.windows.net/",
    mount_point = "/mnt/bronze",
    extra_configs = configs
)

# COMMAND ----------

dbutils.fs.mount(
    source = "abfss://silver@adventure2810.dfs.core.windows.net/",
    mount_point = "/mnt/silver",
    extra_configs = configs
)

# COMMAND ----------

dbutils.fs.mount(
    source = "abfss://gold@adventure2810.dfs.core.windows.net/",
    mount_point = "/mnt/gold",
    extra_configs = configs
)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls "mnt/bronze/SalesLT/"
