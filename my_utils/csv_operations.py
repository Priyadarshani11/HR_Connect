import csv

class HandleCSV:

    filename = "C:\\Users\\priya\\PycharmProjects\\HRConnect\\employee\\employees.csv"

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            result = csv.DictReader(foo)
            data = []
            for item in result:
                data.append(item)
            return data

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename, 'r') as bar:
            yield bar.readline()

# TODO - ADD MORE SUCH METHODS HERE
# TODO - UNDERSTAND USAGE OF `classmethod` HERE

if __name__=="__main__":
    new = HandleCSV()
    print(new.read_entire_csv())


