import datetime

# https://docs.influxdata.com/influxdb/v1/concepts/key_concepts/

class DataJSONStructure():
    def __init__(self, complete_measurement_data):
        self.batch = list()

        self.measurement = complete_measurement_data['name'] # name of measurement
        self.tags = complete_measurement_data['tags'] # dictionary with
        self.fields = complete_measurement_data['fields'] # list of strings

        self.variableDictionary = complete_measurement_data.copy()
    
    def makeMeasurement(self, values):
        return {
            "measurement": self.measurement,
            "tags": self.tags,
            "fields": self.fillFields(values),
            "time": int(datetime.datetime.now().timestamp())
        }
    
    def fillFields(self, values):
        result = dict()
        i = 0
        for tags in self.fields:
            result[tags] = values[i]
            i += 1
        return result

        