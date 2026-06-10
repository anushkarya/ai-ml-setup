import csv
import math

values = []

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        values.append(float(row[0]))

# manual mean
total = 0
for x in values:
    total += x

mean = total / len(values)

# manual std
variance_sum = 0
for x in values:
    variance_sum += (x - mean) ** 2

variance = variance_sum / len(values)
std = math.sqrt(variance)

print("Manual Mean:", mean)
print("Manual Std:", std)

# built-ins
print("Built-in Mean:", sum(values) / len(values))
print("Built-in Std:", math.sqrt(sum((x - mean) ** 2 for x in values) / len(values)))

