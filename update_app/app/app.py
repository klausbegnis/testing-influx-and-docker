from time import sleep
import datetime
import random
import json

from influxdb import InfluxDBClient

from DataJSONStructure import DataJSONStructure

## Points to be relevated
# 1 - Amount / size of bashes, how mucht should be stored in RAM
#       how much should it start saving o tmp files -> directly on storage
# 2 - Fastest way to achive the same code output without losing any insertions

# Creates or check existing database
DB_NAME = 'little_project_db'
DB_DICT = {'name' : DB_NAME}
client = InfluxDBClient(host='localhost', port=8086)

# Creates data structure of the data base
MEASUREMENT_STANDARD = json.load(open(r"./configurations/wind_speed.json"))
json_data_structure = DataJSONStructure(MEASUREMENT_STANDARD)

if (DB_DICT not in client.get_list_database()):
    client.create_database(DB_NAME)

if __name__ == '__main__':
    while(True):
        sleep(5)
        client.write(json_data_structure.makeMeasurement(
            random.randint(0,22),
            random.randint(0,22),
            random.randint(0,22)
        ))