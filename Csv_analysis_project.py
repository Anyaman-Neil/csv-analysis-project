import csv
from collections import Counter

input_file = r'C:\Users\DELL\OneDrive\Desktop\Data ML\Expanded_data_with_more_features.csv'

# Step 1: Read and clean data (remove rows with '' or '0')
with open(input_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # read header
    data = list(reader)    # read all rows

cleaned_data = []
for row in data:
    if '' in row or '0' in row:
        # Skip rows with missing or zero values
        continue     # By using 'continue', the loop ignores such data and proceeds to the next item without processing the current one.
    cleaned_data.append(row)
# Step 2: Group rows based on EthnicGroup
eth_index = header.index("EthnicGroup")
group_A = []
group_B = []
group_C = []
group_D = []
group_E = []

for row in cleaned_data:
    eth_value = row[eth_index]
    if 'group A' in eth_value:
        group_A.append(row)
    elif 'group B' in eth_value:
        group_B.append(row)
    elif 'group C' in eth_value:
        group_C.append(row)
    elif 'group D' in eth_value:
        group_D.append(row)
    else:
        group_E.append(row)

# Combine all groups back into one list 
grouped_data = group_A + group_B + group_C + group_D + group_E

# Step 3: Calculate Total, Average, Highest, and Lowest scores per row
math_index = header.index("MathScore")
reading_index = header.index("ReadingScore")
writing_index = header.index("WritingScore")

totals = []
averages = []
highs = []
lows = []

for row in grouped_data:
    scores = [float(row[math_index]), float(row[reading_index]), float(row[writing_index])]
    total_score = sum(scores)
    avg_score = total_score / len(scores)
    high_score = max(scores)
    low_score = min(scores)

    totals.append(total_score)
    averages.append(avg_score)
    highs.append(high_score)
    lows.append(low_score)

# Step 4: Add new headers for the calculated columns
header.extend(['Total Score', 'Average Score', 'Highest Score', 'Lowest Score'])

# Step 5: Append calculated values to each row
for i, row in enumerate(grouped_data):
    row.extend([
        str(totals[i]),
        str(averages[i]),
        str(highs[i]),
        str(lows[i])
    ])
al5=[]
ag10=[]
af5t10=[]
bl5=[]
bg10=[]
bf5t10=[]
cl5=[]
cg10=[]
cf5t10=[]
dl5=[]
dg10=[]
df5t10=[]
el5=[]
eg10=[]
ef5t10=[]
for row in grouped_data:
    eth_value = row[eth_index]
    stdh = header.index("WklyStudyHours")
    if 'group A' in eth_value:
        if '< 5' in row[stdh]:
            al5.append(row)
        elif "> 10" in row[stdh]:
            ag10.append(row)
        else:
            af5t10.append(row)       
    elif 'group B' in eth_value:
        if '< 5' in row[stdh]:
            bl5.append(row)
        elif "> 10" in row[stdh]:
            bg10.append(row)
        else:
            bf5t10.append(row) 
    elif 'group C' in eth_value:
        if '< 5' in row[stdh]:
            cl5.append(row)
        elif "> 10" in row[stdh]:
            cg10.append(row)
        else:
            cf5t10.append(row) 
    elif 'group D' in eth_value:
        if '< 5' in row[stdh]:
            dl5.append(row)
        elif "> 10" in row[stdh]:
            dg10.append(row)
        else:
            df5t10.append(row)  
    elif 'group E' in eth_value:
        if '< 5' in row[stdh]:
            el5.append(row)
        elif "> 10" in row[stdh]:
            eg10.append(row)
        else:
            ef5t10.append(row) 
new_data=[]
ar=al5+ag10+af5t10+bl5+bg10+bf5t10+cl5+cg10+cf5t10+dl5+dg10+df5t10+el5+eg10+ef5t10
new_data.extend(ar)

for row in new_data:
    stdh = header.index("WklyStudyHours")    
    if '5 - 10' in row[stdh]:
        row[stdh]='5 to 10'

Total=header.index("Total Score")
stdh = header.index("WklyStudyHours")
total = {
    'group A': {'<5': 0, '5-10': 0, '>10': 0},
    'group B': {'<5': 0, '5-10': 0, '>10': 0},
    'group C': {'<5': 0, '5-10': 0, '>10': 0},
    'group D': {'<5': 0, '5-10': 0, '>10': 0},
    'group E': {'<5': 0, '5-10': 0, '>10': 0}}
l5=[]
g10=[]
f5t10=[]
for row in new_data:
    hour=row[stdh]
    t=float(row[Total])
    eth = row[eth_index]
    if eth in total:
        if '< 5' in hour:
           total[eth]['<5'] += t
        elif '> 10' in hour:
            total[eth]['>10'] += t
        else:
            total[eth]['5-10'] += t
for group in total:
    l5.append(total[group]['<5'])
    f5t10.append(total[group]['5-10'])
    g10.append(total[group]['>10'])
groups = list(total.keys())
for i in range(len(new_data)):
    if i < len(groups):
        new_data[i].extend([groups[i], l5[i], f5t10[i], g10[i]])
    else:
        new_data[i].extend(['', '', '', ''])
header.extend(['Groups','Stdh <5', 'Stdh 5-10', 'Stdh >10'])
# Step 6: Write the final cleaned, grouped, and enriched data to new CSV
output_file = r'C:\Users\DELL\OneDrive\Desktop\Data ML\New_Data_1.csv'
with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(new_data)

print(f"✅ Data processed and saved to: {output_file}")