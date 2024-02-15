import csv

with open("test.csv", 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['cos', 'tasm', 'temu'])