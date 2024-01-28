

import pandas as pd
data = pd.read_csv('Resources/election_data.csv')
data.head()

votes = data.shape[0]

vote_percent = data['Candidate'].value_counts().reset_index()
vote_percent.columns = ['Candidate','Count']
vote_percent['Percentage']= (vote_percent['Count']/len(data)*100).round(3)
max_percentage = vote_percent['Percentage'].idxmax()
winner = counts.loc[max_percentage,'Candidate']
ordered_candidates = vote_percent.sort_values(by='Candidate')

print('Election Results')
print('-------------------------------------------')
print('Total Votes: ',votes)
print('-------------------------------------------')
for i,r in ordered_candidates.iterrows():
    print(f"{r['Candidate']}: {r['Percentage']}%({r['Count']})")
print('-------------------------------------------')
print("Winner: ",winner)

output_file = 'Analysis/election_results.txt'
with open(output_file, 'a') as file:
    file.write('Election Results\n')
    file.write('-------------------------------------------\n')
    file.write(f'Total Votes: {votes}\n')
    file.write('-------------------------------------------\n')
    for i,r in ordered_candidates.iterrows():
        file.write(f'{r["Candidate"]}: {r["Percentage"]}% ({r["Count"]})\n')
    file.write('-------------------------------------------\n')
    file.write(f"Winner: {winner}\n")
