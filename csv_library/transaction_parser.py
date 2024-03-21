import csv

def parse_transactions(filename):
    transactions = []
    sum = 0
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            posting_date = row[1]
            description = row[2]
            amount = float(row[3])
            balance = row[5]

            sum += amount

            transaction = (posting_date, description, amount, balance)

            transactions.append(transaction)
    
    return header, transactions, sum

#if __name__ == '__main__':
header, transactions, sum = parse_transactions('transactions.csv')
print(header)
print(transactions)
print(f'{sum:.2f}')