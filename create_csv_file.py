import csv
class CreateCSVFile:
    def __init__(self, fileName, fields, rows):
        self.fileName = fileName
        self.fields = fields
        self.rows = rows
        self.createFile()
    def createFile(self):
        with open(self.fileName, "w") as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow(self.fields)
            csvWriter.writerows(self.rows)
        print("CSV file created")