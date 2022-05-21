'''Principal data
activity'''
import csv
import matplotlib.pyplot as plt

with open(r'D:\MAHARASHTRA\Maharashtra.csv', encoding='latin-1') as csv_file:
    csv_reader = csv.reader(csv_file)
    registration_dict = {}
    for line in csv_reader:
        if line[6] == 'DATE_OF_REGISTRATION':
            continue
        else:
            string = line[6]
            string = string[6:]
            if string == "2015":
                a = line[11]
                registration_dict[a] = registration_dict.get(a, 1)+1

if __name__ == '__main__':
    regis_date = []
    regis = []
    for k in registration_dict:
        regis_date.append(k)
        regis.append(registration_dict[k])

    plt.rcParams["figure.figsize"] = (20, 60)
    plt.bar(regis_date, regis)
    plt.title("Principal Business Activity")
    plt.xlabel("Business")
    plt.ylabel("Number of Companies")
    plt.xticks(rotation=85)
