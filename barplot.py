''' barplot
company registraion by year'''
import csv
import matplotlib.pyplot as plt

with open(r'D:\MAHARASHTRA\Maharashtra.csv', encoding='latin-1') as csv_file:
    csv_reader = csv.reader(csv_file)
    year_dict = {}
    for line in csv_reader:
        if line[6] == 'DATE_OF_REGISTRATION':
            continue
        else:
            string = line[6]
            string = string[6:]
            year_dict[string] = year_dict.get(string, 1) + 1
    # print(year_dict)
if __name__ == '__main__':
    year_array = []
    registrations = []
    for k in year_dict:
        year_array.append(k)
    year_array.sort()
    year_array.remove('')
    for i in year_array:
        registrations.append(year_dict[i])

    plt.rcParams["figure.figsize"] = (30, 10)
    plt.bar(year_array, registrations)
    plt.title("Company Registration by Year")
    plt.xlabel("Date_of_Registration")
    plt.ylabel("Number of Companies")
    plt.xticks(rotation=90)
