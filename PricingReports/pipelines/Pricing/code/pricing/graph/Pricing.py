from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pricing.config.ConfigStore import *
from pricing.functions import *

def Pricing(spark: SparkSession) -> DataFrame:
    from spark_ai.webapps import WebUtils
    WebUtils().register_udfs(spark)
    df1 = spark.range(1)

    return df1\
        .withColumn("url", lit("https://docs.prophecy.io/sitemap.xml"))\
        .withColumn("content", expr("web_scrape(url)"))
