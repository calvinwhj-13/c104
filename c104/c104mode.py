import csv 
from collections import Counter
with open('SOCR-HeightWeight.csv', newline = '') as f : 
    reader = csv.reader(f)
    filedata  = list(reader)
filedata.pop(0)
newdata = []
for i in range(len(filedata)) :
    num = filedata[i][1]
    newdata.append(float(num))
data = Counter(newdata)
mode_dataforRange = {
    "50-60" : 0,
    "60-70" : 0,
    "70-80" : 0
} 

for height, occurance in data.items() :
    if 50<float(height)<60 :
        mode_dataforRange['50-60'] += occurance
    elif 60<float(height)<70 :
        mode_dataforRange['60-70'] += occurance
    elif 70<float(height)<80 :
        mode_dataforRange['70-80'] += occurance 

mode_range, mode_occurance = 0, 0
for range, occurance in mode_dataforRange.items() :
    if occurance>mode_occurance : 
        mode_range, mode_occurance = [int(range.split('-')[0]), int(range.split('-')[1])], occurance

mode =  float((mode_range[0] + mode_range[1])/2) 
print(f'mode is -> {mode : 2f}') 