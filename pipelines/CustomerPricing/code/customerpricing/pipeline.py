from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from customerpricing.config.ConfigStore import *
from customerpricing.functions import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("CustomerPricing")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/CustomerPricing")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/CustomerPricing", config = Config)(pipeline)

if __name__ == "__main__":
    main()
