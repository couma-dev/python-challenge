# import os and csv modules
import csv

# create emty lists to add hold the values

month_count = []
profit_list = []
profit_change_list = []




# set file path

budgetpath = '../Resources/budget_data.csv'

#read the budget file

with open(budgetpath, 'r') as budgetcsv:

    budgetreader = csv.reader(budgetcsv, delimiter = ',')

    # read the header for the budget file

    budget_header = next(budgetcsv)

    #loop through the budget file and count the months and profit and add them to the empty list we created above
    # month_count = 0
    for row in budgetreader:   
        month_count.append(row[0])
        profit_list.append(int(row[1]))

    #loop through the profit list to determine the change in profit between previous and current month
    for j in range(len(profit_list)-1):
        profit_change_list.append(profit_list[j+1] - profit_list[j])
        
# calculate maximum and mininum profit increase/decrease in the profit_change_List

max_profit_increase = max(profit_change_list)

min_profit_decrease = min(profit_change_list)

# storing the index of the min and max values from profit change list
increase_index = profit_change_list.index(max(profit_change_list)) + 1
decrease_index = profit_change_list.index(min(profit_change_list)) + 1

#Pritning the Analysis

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {len(month_count)}")
print(f"Total: {sum(profit_list)}")
print(f"Average  Change: ${round(sum(profit_change_list)/int(len(month_count)),2)}")
print(f"Greatest Increase in Profits: {month_count[increase_index]} (${(str(max_profit_increase))})")
print(f"Greatest Decrease in Profits: {month_count[decrease_index]} (${(str(min_profit_decrease))})")

# outfile
budgetoutput_filepath = "../Resources/Analysis.txt"
with open(budgetoutput_filepath, 'w') as Analysistxt:
    Analysistxt.write("Financial Analysis")
    Analysistxt.write("\n")
    Analysistxt.write("-------------------------------")
    Analysistxt.write("\n")
    Analysistxt.write(f"Total Months: {len(month_count)}")
    Analysistxt.write("\n")
    Analysistxt.write(f"Total: {sum(profit_list)}")
    Analysistxt.write("\n")
    Analysistxt.write(f"Average  Change: ${round(sum(profit_change_list)/int(len(month_count)),2)}")
    Analysistxt.write("\n")
    Analysistxt.write(f"Greatest Increase in Profits: {month_count[increase_index]} (${(str(max_profit_increase))})")
    Analysistxt.write("\n")
    Analysistxt.write(f"Greatest Decrease in Profits: {month_count[decrease_index]} (${(str(min_profit_decrease))})")
