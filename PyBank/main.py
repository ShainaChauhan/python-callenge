import pandas as pd

data = pd.read_csv('Resources/budget_data.csv')
data.head()

months = 0
total_amount = 0
for i  in data['Profit/Losses']:
    months =months +1
    total_amount +=i

months
total_amount

change = [data['Profit/Losses'][i] - data['Profit/Losses'][i-1] for i in range(1, len(data['Profit/Losses']))]
average = round(sum(change)/len(change),2)
average
data['Change_in_Profit'] = data['Profit/Losses'].diff()
max_profit = data['Change_in_Profit'].idxmax()
min_profit = data['Change_in_Profit'].idxmin()

max_date = data.loc[max_profit,'Date']
max_profit_amount = data.loc[max_profit,'Change_in_Profit']


min_date = data.loc[min_profit,'Date']
min_profit_amount = data.loc[min_profit,'Change_in_Profit']
print(max_date,max_profit_amount)
print(min_date,min_profit_amount)

print('Financial Analysis')
print('-------------------------------------')
print(f'Total Months: {months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {max_date} (${int(max_profit_amount)})')
print(f'Greatest Decrease in Profits: {min_date} (${int(min_profit_amount)})')

output_file = 'Analysis/pybank.txt'
with open(output_file,'a') as file:
    file.write('Financial Analysis\n')
    file.write('-------------------------------------\n')
    file.write(f'Total Months: {months}\n')
    file.write(f'Total: ${total_amount}\n')
    file.write(f'Average Change: ${average}\n')
    file.write(f'Greatest Increase in Profits: {max_date} (${int(max_profit_amount)})\n')
    file.write(f'Greatest Decrease in Profits: {min_date} (${int(min_profit_amount)})\n')
