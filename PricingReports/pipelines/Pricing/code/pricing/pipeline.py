from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pricing.config.ConfigStore import *
from pricing.functions import *
from prophecy.utils import *
from pricing.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Pricing = Pricing(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Pricing")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pricing")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Pricing", config = Config)(pipeline)

if __name__ == "__main__":
    main()
