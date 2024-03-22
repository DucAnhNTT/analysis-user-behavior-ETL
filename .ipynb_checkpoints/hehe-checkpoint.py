# import os
# import sys
# from pyspark.sql import SparkSession
# from pyspark.sql.types import StructType, StructField, StringType
import pandas as pd
import json


# os.environ['PYSPARK_PYTHON'] = sys.executable
# os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
#
# # Initialize Spark session
# spark = SparkSession.builder \
#     .appName("hehe") \
#     .getOrCreate()

def remove_escape_sequences(string):
    return string.encode('utf-8').decode('unicode_escape')

def replaceSpecificUsecase(string):
    return string.replace("Chris O\"Donnell", "Chris O\'Donnell").replace("Kevin O\"Neill", "Kevin O\'Neill").replace("Renzil D\"Silva", "Renzil D\'Silva")

listFile = ['log21.txt', 'log22.txt','log23.txt','log24.txt','log25.txt','log31.txt','log32.txt']

for file in listFile:
    with open(file, 'r') as file:
        data = file.readlines()

extracted_data = []

# Define the keys to extract
keys_to_extract = ['Mac', 'SessionMainMenu', 'AppName', 'LogId', 'Event', 'ItemId', 'RealTimePlaying']



for line in data:
    line = remove_escape_sequences(line)
    line = line.replace("u'", "\"").replace("'", "\"").replace("u\"", "\"").replace("\t","").replace("SessionMainMen","SessionMainMenu")
    line = replaceSpecificUsecase(line)
    print(line)
    json_data = json.loads(line)
    extracted_data.append({key: json_data.get(key, None) for key in keys_to_extract})


# Create a DataFrame from the extracted data
df = pd.DataFrame(extracted_data)

# Display the DataFrame
print(df[['Mac','RealTimePlaying']])

df['RealTimePlaying'] = pd.to_numeric(df['RealTimePlaying'], errors='coerce')

filtered_df = df.count([df['RealTimePlaying'] > 0])

print(filtered_df)




# # Define schema for DataFrame
# schema = StructType([
#     StructField(key, StringType(), True) for key in keys_to_extract
# ])
#
# # Create PySpark DataFrame
# df = spark.createDataFrame(parsed_data, schema=schema)
#
# # Show DataFrame
# df.show()
#
# Stop SparkSession
# spark.stop()
