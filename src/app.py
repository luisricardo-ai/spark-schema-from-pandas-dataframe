from pyspark.sql.types import StructType, StructField, StringType, BooleanType, LongType, TimestampType, DoubleType

def defineSparkSchema(pandas_dataframe) -> list:
    schema_tuples = []
    for col in range(len(pandas_dataframe.columns)):
 
        if pandas_dataframe.dtypes[col] == 'object':
            schema_tuples.append(StructField(pandas_dataframe.columns[col], StringType(), True))
        
        elif pandas_dataframe.dtypes[col] == 'int32' or pandas_dataframe.dtypes[col] == 'Int64':
            schema_tuples.append(StructField(pandas_dataframe.columns[col], LongType(), True))
            
        elif pandas_dataframe.dtypes[col] == 'float32' or pandas_dataframe.dtypes[col] == 'float64':
            schema_tuples.append(StructField(pandas_dataframe.columns[col], DoubleType(), True))

        elif pandas_dataframe.dtypes[col] == 'string':
            schema_tuples.append(StructField(pandas_dataframe.columns[col], StringType(), True))     
            
        elif pandas_dataframe.dtypes[col] == 'datetime64[ns]':
            schema_tuples.append(StructField(pandas_dataframe.columns[col], TimestampType(), True))     

    return schema_tuples