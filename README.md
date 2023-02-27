# Automating Spark's schema creation from Pandas Dataframe

* Read this file to understand how and for which cases this code was designed.

* The complete code is in the `src` folder.

---

## Study Case

While I was developing a Glue Job on AWS for a DaaS (DataBase as a service) project, I was using some python libraries, such as awswrangler to consume the data that was in the data lake (using AWS Athena as an intermediary to access the data).

When using [awsrangler](https://aws-sdk-pandas.readthedocs.io/en/stable/) we can send some SQL queries (using the [Presto](https://prestodb.io/docs/current/) Engine) to the database and have a Dataframe as a result, and guess what, a Pandas Dataframe.

Normally the conversion of a pandas dataframe to a spark data frame is very simple, just using a spark.CreateDataFrame(df), but in some cases we can't convert this way, because we need to define the [schema](https://sparkbyexamples.com/spark/spark-schema-explained-with-examples/) for the dataframe of spark and when we have many tables/views/dataframes to process this individual build it can take more time than necessary.

## Big Idea

The first step is to understand which [datatypes pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html) has and which are the same as [spark datatypes](https://spark.apache.org/docs/latest/sql-ref-datatypes.html).

With pandas dataframes, we can use the dataframe.dtypes code (without parentheses) to extract some information from the dataframe, such as column names and their types.

With the columns and their types in hand, we can simply start creating the spark schema that is based on tuples with [StructField()](https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.types.StructField.html).

~~~ python
StructField(columnName, sparkDataType, nullable)
~~~

## Application

I created a function to facilitate its use on a large scale, named 'defineSparkSchema' which will return a list with the tuples needed for the schema, with the following parameter:

- pandas_dataframe: pd.DataFrame

~~~python

def defineSparkSchema(pandas_dataframe) -> list:
    return []
~~~

The most important thing here is to understand what are the possible types that will come in your pandas DataFrame and how you will want them in spark, remember that you will always have to convert because at some point you may lose a column if you do not map the type of it and which one will put in the spark.

One of the uses of the code would be like this:

~~~python

def defineSparkSchema(pandas_dataframe) -> list:
    return []

df = spark.createDataFrame(data = my_pandas_dataframe,
                           schema = StructType(defineSparkSchema(my_pandas_dataframe)))
~~~