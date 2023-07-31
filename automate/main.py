from datetime import date, datetime
import dateutil
import pandas as pd
from sendEmail import sendEmail
# from deta import app
import cronitor
cronitor.api_key = '4e715437e6b74934a7d5c801126bb768'

# Public GoogleSheets
sheetID = '10SwSiXd6ZsXMW6aCxB66vP-Mnlk1DPYAFuUgZbsRcX8'
sheetName = 'invoice_data'
url =f"https://docs.google.com/spreadsheets/d/{sheetID}/gviz/tq?tqx=out:csv&sheet={sheetName}"

def loadUrl(url):
    parse_dates = ["due_date", "reminder_date"]
    df = pd.read_csv(url,parse_dates=parse_dates)
    return df


def check(df):
    now = date.today()
    emailCounter =0
    for _, row in df.iterrows(): 
        if (now >= row["reminder_date"].date()) and (row["has_paid"] == "no"):
            sendEmail(subject=f'Reminder Invoice: {row["invoice_no"]}',name=row["name"],receiver_email=row["email"], dDate=row["due_date"].strftime("%d, %b %Y"), invoice_no=row["invoice_no"],amount= row["amount"])
            emailCounter +=1
    print(f"Emails sent: {emailCounter}")


@cronitor.job('B4NpFT')
def example_task():
    df= loadUrl(url)
    check(df)
    print('running background job')

example_task()

monitor = cronitor.Monitor('B4NpFT')

# the job has started
monitor.ping(state='run')

# the job has completed successfully
monitor.ping(state='complete')

# the job has failed
monitor.ping(state='fail')
