''' Authorized
Cap'''
import csv
import matplotlib.pyplot as plt
# matplotlib.use('TkAgg')

with open(r'D:\MAHARASHTRA\Maharashtra.csv', 'r', encoding='latin-1') as csv_file:
    csv_reader = csv.reader(csv_file)
    capital = ['<=1L', '1L to 10L', '10L to 1Cr', '1Cr to 10Cr', '>10Cr']
    list_data = []
    for line in csv_reader:
        if line[8] is not None:
            list_data.append(line[8])

if __name__ == '__main__':
    list_data.remove('AUTHORIZED_CAP')
    companies_with_capital = [0, 0, 0, 0, 0]

    for i in list_data:
        if int(float(i)) <= 100000:
            companies_with_capital[0] += 1
        elif int(float(i)) > 100000 and int(float(i)) < 1000000:
            companies_with_capital[1] += 1
        elif int(float(i)) >= 1000000 and int(float(i)) < 10000000:
            companies_with_capital[2] += 1
        elif int(float(i)) >= 1000000 and int(float(i)) <= 100000000:
            companies_with_capital[3] += 1
        else:
            companies_with_capital[4] += 1

    plt.bar(capital, companies_with_capital)
    plt.title("Authorized Capital")
    plt.xlabel("Capital")
    plt.ylabel("Number of Companies")
