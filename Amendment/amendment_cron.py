from ctypes import sizeof
import requests, json
import time
import math
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="$Bridge@2022#",
database="wae_pre"
#   password="",
#   password="root",
)
mycursor = mydb.cursor()
from datetime import datetime
from pytz import timezone
print("dada")
condition_apply = 'WHERE approval_status="Approved" OR approval_status="Process" OR approval_status="Pending"'
sqlSelectAmendment = "SELECT `id`, `order_id`, `ops_revision`, `client_name`, `ops_number`, `amendment`, `reason`, `open_date`, `close_date`, `approval_status`, `created_by` FROM `Amendment_amendment` "+condition_apply
mycursor.execute(sqlSelectAmendment)
allRow = mycursor.fetchall()
print('Approved',allRow)
for amendment in allRow:
    print('----- amendment data -----')
    print(amendment)
    amendmentId = amendment[0]
    amendmentIdate = amendment[7]
    amendmentIclosedate = amendment[8]
    amendment_status = amendment[9]
    amendmentOrderId = amendment[1]
    print("amnedment......",amendmentId, amendmentIdate, amendmentIclosedate)
    d1 = datetime.strptime(amendmentIdate, '%Y-%m-%dT%H:%M')
    print(type(d1))
    datetimeformate = '%Y-%m-%d %H:%M:%S'
    serverDateTime = datetime.now(timezone("Asia/Kolkata")).strftime(datetimeformate)
    # d1 = datetime.strptime(amendmentIdate, datetimeformate)
    d2 = datetime.strptime(serverDateTime, datetimeformate)
    d3 = datetime.strptime(amendmentIclosedate, '%Y-%m-%dT%H:%M')
    if d1<d2 and amendment_status=="Approved":
        print("expired", amendmentId)
        amdorderidupdate = f'WHERE id="{amendmentId}"'
        amendmentquery = "UPDATE `Amendment_amendment` SET `approval_status`='Process' "+amdorderidupdate
        mycursor.execute(amendmentquery)
        print(amendmentquery)
        amdorderid = f'WHERE id="{amendmentOrderId}"'
        amendmentOrderquery = "UPDATE `Order_order` SET `amendment_status`='Active' "+amdorderid
        mycursor.execute(amendmentOrderquery)
        
    if d2>d3 and amendment_status=="Process":
        print("hhhhh")
        amdorderidupdate = f'WHERE id="{amendmentId}"'
        amendmentquery = "UPDATE `Amendment_amendment` SET `approval_status`='Closed' "+amdorderidupdate
        mycursor.execute(amendmentquery)
        print(amendmentquery)
        amdorderid = f'WHERE id="{amendmentOrderId}"'
        amendmentOrderquery = "UPDATE `Order_order` SET `amendment_status`='Inactive' "+amdorderid
        mycursor.execute(amendmentOrderquery)
    if d2>d3 and amendment_status=="Pending":
        print("hhhhh")
        amdorderidupdate = f'WHERE id="{amendmentId}"'
        amendmentquery = "UPDATE `Amendment_amendment` SET `approval_status`='Request Time Out' "+amdorderidupdate
        mycursor.execute(amendmentquery)
        print(amendmentquery)
        amdorderid = f'WHERE id="{amendmentOrderId}"'
        amendmentOrderquery = "UPDATE `Order_order` SET `amendment_status`='Inactive' "+amdorderid
        mycursor.execute(amendmentOrderquery)
mydb.commit() # this method will confirm and save changes in database 