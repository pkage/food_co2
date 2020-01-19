import json

data = {}

files = [
        "./carcsv/MY2019 Fuel Consumption Ratings.csv",
        "./carcsv/MY2018 Fuel Consumption Ratings.csv",
        "./carcsv/MY2017 Fuel Consumption Ratings.csv",
        "./carcsv/MY2016 Fuel Consumption Ratings.csv",
        "./carcsv/MY2015 Fuel Consumption Ratings (5-cycle).csv"
        ]

for f in files:
    with open (f, "r", encoding = "ascii", errors="ignore") as infile:
        line = infile.readline()
        while line:
            csv = line.split(',')
            if csv[0] == "Model" or csv[0] == "Year" \
                or csv[0] == "MODEL" or csv[0] == "YEAR":
                line = infile.readline()
                continue
            if csv[12] == '':
                line = infile.readline()
                continue
            if not csv[0] in data:
                data[csv[0]] = {}
            if not csv[1] in data[csv[0]]:
                data[csv[0]][csv[1]] = {}
            if not csv[2] in data[csv[0]][csv[1]]:
                data[csv[0]][csv[1]][csv[2]] = {"co2":0, "count": 0}
            data[csv[0]][csv[1]][csv[2]]["co2"] += int(csv[12])
            data[csv[0]][csv[1]][csv[2]]["count"] += 1
            
            line = infile.readline()

# reparse
for year in data.keys():
    for make in data[year].keys():
        for model in data[year][make].keys():
            co2 =  data[year][make][model]["co2"]
            count = data[year][make][model]["count"]
            data[year][make][model] = {
                    "avg_co2": (co2/count)
                    }

jsond = json.dumps(data)
print (jsond)

