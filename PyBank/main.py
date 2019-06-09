# Import os module to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#Empty lists for month and revenue
total_month = 0
monthly_change = 0
prior_month_rev = 0
total_monthly_change = 0
greatest_monthly_increase = 0
greatest_monthly_decrease = 0
total_revenue = 0

#Reading csv file

with open(csvpath, newline="") as csvfile:
    #csv reader specifies delimiter and variable that holds contents
    budget = csv.reader(csvfile, delimiter=",")
    #read the header row first
    budget_header = next(budget)
    
    #
    for row in budget:
        #find total number of monthss
        total_month +=1
        date = row[0]
        total_revenue +=float(row[1])

        if budget.line_num == 2:
            monthly_change = 0
        else:
            monthly_change = float(row[1]) - prior_month_rev
        total_monthly_change += monthly_change

        if monthly_change >= greatest_monthly_increase:
            greatest_monthly_increase = monthly_change
            date_greatest_inc = date
        elif monthly_change <= greatest_monthly_decrease:
            greatest_monthly_decrease = monthly_change
            date_greatest_dec = date

        prior_month_rev = float(row[1])


#find average monthly change
average_change = round(total_monthly_change/(total_month-1),2)

output_path = os.path.join("PyBank_Report.txt" )

#write summary report
with open(output_path,"w") as output_file:
    output_file.writelines("Financial Analysis\n")
    output_file.writelines("___________________________________________________\n")
    output_file.writelines(f"Total Months: {total_month}\n")
    output_file.writelines(f"Total Revenue: ${total_revenue}\n")
    output_file.writelines(f"Average Change: ${average_change}\n")
    output_file.writelines(f"Greatest Increase in Revenue: {date_greatest_inc} (${greatest_monthly_increase})\n")
    output_file.writelines(f"Greatest Decrease in Revenue: {date_greatest_dec} (${greatest_monthly_decrease})\n")
    output_file.writelines("___________________________________________________\n")
#read summary report
with open(output_path,"r") as result_file:
        print(result_file.read())



        
