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

def replaceSpecificUsecaseForDirectors(string):
    index = string.find(r'"Directors": "') + 14  # Find the starting index of the substring
    if index > 15:
        indexNextComma = string.find(',', index) - 1  # Find the index of the next comma after the substring
        # Replacing double quotes with single quotes in the specified substring
        return string[:index] + string[index:indexNextComma].replace('"', "'") + string[indexNextComma:]
    return string



listFile = ['logt21.txt', 'logt22.txt','logt23.txt','logt24.txt','logt25.txt','logt31.txt','logt32.txt']
testListFile = ['test.txt']

for i in listFile:
    with open(f'data/raw/{i}', 'r') as file:
        data = file.readlines()


extracted_data = []

# Define the keys to extract
keys_to_extract = ['Mac', 'SessionMainMenu', 'AppName', 'LogId', 'Event', 'ItemId', 'RealTimePlaying']



# Clean all the logs file
for line in data:
    line = remove_escape_sequences(line)
    line = line.replace("u'", "\"").replace("'", "\"").replace("u\"", "\"").replace("\t","").replace("SessionMainMen","SessionMainMenu").replace("N\A","None")
    line = line.replace(r'"ItemName": "O"LEARYS 2"', '"ItemName": "O\'LEARYS 2"').replace('"Title": "M"gladbach - FC Cologne"', '"Title": "M\'gladbach - FC Cologne"').replace('"Hamburger - M"Gladbach"', '"Hamburger - M\'Gladbach"')
    line = replaceSpecificUsecaseForDirectors(line)
    json_data = json.loads(line)
    extracted_data.append({key: json_data.get(key, None) for key in keys_to_extract})

#


# Create a DataFrame from the extracted data
df = pd.DataFrame(extracted_data)
df.to_csv('./data/cleanCSV/extractedData.csv')

dfUser_info = pd.read_csv('./data/raw/user_info.txt', delimiter='\t')
dfUser_info.to_csv('./data/cleanCSV/user_info.csv')

# Display the DataFrame
print(df[['Mac','RealTimePlaying']])

df['RealTimePlaying'] = pd.to_numeric(df['RealTimePlaying'], errors='coerce')

filtered_df = df.count([df['RealTimePlaying'] > 0])

print(filtered_df)


