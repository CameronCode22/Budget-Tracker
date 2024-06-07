import pandas as pd
import calendar
import os
from datetime import datetime

#get the current year and month
current_year = pd.Timestamp.now().year
current_month = pd.Timestamp.now().month
todays_date = datetime.now()
adjusted_date = todays_date.strftime('%Y-%m-%d')

#Get the number of days in the current month
num_days = calendar.monthrange(current_year, current_month)[1]

#create a DataFrame with the dates of the current month
dates_df = pd.DataFrame ({'Date':pd.date_range(start=f'{current_year}-{current_month}-01',periods=num_days)})

file_name = "This month budget.xlsx"
#find out if the excel has laready been created
if not (os.path.isfile(file_name)):

    #write the datframe to excel
    dates_df.to_excel(file_name, index=False)
    print(f"File {file_name} was created succesfully")
else:
    print(f"File {file_name} already exists")

#get user input, what was spent today?
today_spend = int(input("How much did you spend today?"))

#add the spend to the outgoing column

for idx, row in dates_df.iterrows():
    print(row['Date'])
    if row['Date'].strftime('%Y-%m-%d') == adjusted_date:
        dates_df.loc[idx, 'Cost'] = today_spend
# for dates in dates_df['Date']:
#     if dates == adjusted_date:
#         dates_df.loc[dates, 'Cost'] = today_spend

#dates_df[todays_date.strftime('%Y-%m-%d')] = today_spend

#write the updated Dataframe to excel

dates_df.to_excel(file_name, index=False)




