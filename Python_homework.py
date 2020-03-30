#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import os

os.chdir('/Users/huiyingzheng/Desktop/GT Databootcamp/python-homework/PyBank')
os.getcwd()

# Need to read in bank data, first set the path, I think this is only a pointer, where the file should begin
bdgt_path = os.path.join("Resources","budget_data.csv")

#set initial number of months
n_months = 0
total_sum = 0

#set initial changes over the entire period
month = []
profit_loss = []

dev_diff = []

profit_change = []


# set the next pointer for where the file starts
with open(bdgt_path) as bank:
    bankdata = csv.reader(bank, delimiter=",")
    
    # Because there are headers in the dataset, need to read the header row 
    bankdata_header = next(bankdata)
    print("Bankdata Header:" + str(bankdata_header))

    for row in bankdata:
        month.append(row[0])
        profit_loss.append(float(row[1]))
        
    averg_prof = round(sum(profit_loss)/len(profit_loss))
    
    profit_change.append(0)
    
    for i in range(len(profit_loss)):
        dev_diff.append(profit_loss[i]-averg_prof)
        if i > 0:
            profit_change.append(profit_loss[i] - profit_loss[i-1])
    
    temp_max = max(profit_change)
    max_index = profit_change.index(temp_max)
    
    
    temp_min = min(profit_change)
    min_index = profit_change.index(temp_min)
    
    
    
    average_change = round(sum(profit_change)/(len(profit_change)-1),2)
    total_month = len(month)
    
    print(f'Total Months: {total_month}')
    print(f'Total Months: {int(sum(profit_loss))}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {month[max_index]} (${int(profit_change[max_index])})')
    print(f'Greatest Increase in Profits: {month[min_index]} (${int(profit_change[min_index])})')

                           
                           


# In[2]:


import csv
import os

os.getcwd()
os.chdir('/Users/huiyingzheng/Desktop/GT Databootcamp/python-homework/PyPoll')
os.getcwd()

# Need to read in bank data, first set the path, I think this is only a pointer, where the file should begin
vote_path = os.path.join("Resources","election_data.csv")


#set initial lists 
vid = []
vcounty = []
vcad = []

cad_dis = []

votes_count = []
votes_pert = []

#dev_diff = []

#profit_change = []


# set the next pointer for where the file starts
with open(vote_path) as votedata:
    votefile = csv.reader(votedata, delimiter=",")
    
    # Because there are headers in the dataset, need to read the header row 
    votefile_header = next(votefile)
    print("Bankdata Header:" + str(votefile_header))
    
    for row in votefile:
        vid.append(row[0])
        vcounty.append(row[1])
        vcad.append(row[2])
    
    cad_dis = list(set(vcad))

    n = len(vid)
    m = len(cad_dis)

    for i in range(m):
        votes_count.append(0)
    
    for i in range(n):
        for j in range(m):
            if vcad[i] == cad_dis[j]: 
                votes_count[j] = votes_count[j]+1
                

    votes_max = max(votes_count)
    winner_index = votes_count.index(votes_max)


    print("------------------------------")
    print(f'Total Votes: {len(vid)}')
    print("------------------------------")
    for p in range(m):
        votes_pert.append(votes_count[p]/n)
        print(cad_dis[p] +": " +"{:.3%}".format(votes_pert[p]) + " (" + str(votes_count[p]) + ")")
    # print(f'{cad_dis[p]}: {:.2%}.{format(votes_pert[p]) ({votes_count[p]})')

    print("------------------------------")
    print("Winner is: " + str(cad_dis[winner_index]))
    print("------------------------------")


# In[ ]:




