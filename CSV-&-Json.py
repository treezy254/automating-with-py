# The csv module
import csv
from urllib import response
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num)+ ' ' + str(row))
    
#writer Objects
import csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])

outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])

outputWriter.writerow([1, 2, 3.142, 4])
outputFile.close()


#JSON and APIs
stringOfJsonData = {"name": "Zophie", "isCat": true, 
 "miceCaught": 0, "napsTaken":37, "felineIQ": null}

#json module
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue

#writing json with the dumps() func
stringOfJsonData = json.dunps(pythonValue)
stringOfJsonData

#PRoject: Fetching Current Weather Data
APPID = 1
import json, requests, sys
# Compute location from command line arguements
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = "httpsL//url" % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-',w[0]['weather'][0]['description'])
print()
print('Tommorow')
print(w[1]['weather'][0]['main'], '-',w[1]['weather'][0]['description'])
print()
print("Day after tomorrow:")
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])

