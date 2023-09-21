# */2 * * * * /usr/bin/python3 /home/www/b2b/massead_pre/bridge/Tickets/service-contract-cron.py
# */60 * * * * /usr/bin/python3 /home/www/b2b/massead_pre/bridge/Tickets/service-contract-cron.py
import requests, json
import time
import math
import mysql.connector

from datetime import datetime
from datetime import date, datetime, timedelta
import calendar

import sys, os

import pytz
# get the standard UTC time
UTC = pytz.utc

# tz = pytz.timezone('Asia/Kolkata')
currentDate = date.today()
currentDay = calendar.day_name[currentDate.weekday()]  # this will return the day of a week
currentTime = datetime.today().strftime("%I:%M %p")
currentDateTime = f"{currentDate} {currentTime}"
# serverDateTime = datetime.now(UTC)
serverDateTime = datetime.now(UTC).strftime('%Y-%m-%d %H:%M:%S.%f')

# print("Today date is: ", currentDate)
# print("Today day is: ", currentDay)
# print("Today Current time: ", currentTime)
print("Today Current serverDateTime: ", serverDateTime)

# dir = os.getcwd()
# dir = dir.split("bridge")[0]+"bridge"
# sys.path.append(dir)
# from bridge import settings
# data = settings.SAPSESSION("core")
# mydb = mysql.connector.connect(
#   host=settings.DATABASES['default']['HOST'],
#   user=settings.DATABASES['default']['USER'],
#   password=settings.DATABASES['default']['PASSWORD'],
#   database=settings.DATABASES['default']['NAME']
# )
# mycursor = mydb.cursor()

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='$Bridge@2022#',
    # password='root',
    database='massead_pre'
)
# mycursor = mydb.cursor()
mycursor = mydb.cursor(dictionary=True, buffered=True)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
DutationStartDate = currentDate - timedelta(days=15)
DutationEndDate = currentDate + timedelta(days=15)

print(">>>>>>>>>>>>>>> Service Contract Item <<<<<<<<<<<<<<<")
# SELECT * FROM `Order_servicecontractsitem` WHERE `FromDate` >= '2022-12-01' AND `FromDate` <= '2022-12-15'
sqlServiceContractItem = f"SELECT * FROM `Order_servicecontractsitem` WHERE `TicketGen`='False' AND `FromDate` >= '{str(DutationStartDate)}' AND `FromDate` <= '{str(DutationEndDate)}'"
print(sqlServiceContractItem)
mycursor.execute(sqlServiceContractItem)
contract_rows = mycursor.fetchall()
if len(contract_rows) != 0:
    for contractItem in contract_rows:

        ServiceContractItemId = contractItem['id']
        SerialNumber = contractItem['ItemSerialNo']
        ItemCode = contractItem['ItemCode']
        ProductName = contractItem['ItemName']
        FromDate = contractItem['FromDate']
        Todate = contractItem['Todate']
        
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        itemSql = f"SELECT * FROM `Item_item` WHERE `ItemCode` = '{ItemCode}'"
        mycursor.execute(itemSql)
        item_rows = mycursor.fetchall()
        GroupCode = item_rows[0]['ItemsGroupCode_id']
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        print(" >>>>>>> Service Contract Details <<<<<<<<<<<")
        sqlServiceContractDetails = f"SELECT * FROM `Order_servicecontracts` WHERE `id` = {contractItem['ServiceContractsId']}"
        print(sqlServiceContractDetails)
        mycursor.execute(sqlServiceContractDetails)
        contractDetails_rows = mycursor.fetchall()
        contractDetails = contractDetails_rows[0]

        CardCode = contractDetails['CardCode']
        ContactAddress = contractDetails['ShipAddr']
        ContractType = contractDetails['ContractType']

        assignTo = 52
        tempZone = "North"

        # print('---- BP ----')
        bpSql = f"SELECT `id`, `CardCode`, `CardName`, `Zone`, `ContactPerson`, `EmailAddress`, `Phone1` FROM `BusinessPartner_businesspartner` WHERE `CardCode` = '{CardCode}'"
        # print(bpSql)
        mycursor.execute(bpSql)
        bpdata = mycursor.fetchall()
        if len(bpdata) != 0:
            tempZone = bpdata[0]['Zone']
            ContactPerson = bpdata[0]['ContactPerson']
            Mail = bpdata[0]['EmailAddress']
            PhoneNumber = bpdata[0]['Phone1']
        # print(Zone)

        # print('---- Employee ----')
        empSql = f"SELECT `id`, `SalesEmployeeCode`, `firstName` FROM `Employee_employee` WHERE `role` = 'support manager' AND `zone` = '{tempZone}' AND `Active` = 'tYES'"
        # print(empSql)
        mycursor.execute(empSql)
        empdata = mycursor.fetchall()
        if len(empdata) != 0:
            assignTo = empdata[0]['SalesEmployeeCode'] # for SalesEmployeeCode

        # static fields
        TicketType = "Maintenance"
        TicketTitle = "New Maintenance"
        TicketPriority = "Medium" # low, medium, heigh
        TicketStatus = "Pending"
        TicketRequestStatus = "Pending"

        closedDate = currentDate + timedelta(days=15)
        dueDate = currentDate + timedelta(days=15)

        DeliveryId = 0
        Remarks = ""
        WarStartDate = ""
        WarEndDate = ""
        ExtendedWarantyStartDate = ""
        ExtendedWarrantyEndDate = ""
        tmpAMCSD = ""
        tmpAMCED = ""
        tmpCMCSD = ""
        tmpCMCED = ""

        if ContractType == '1':
            ExtendedWarantyStartDate = FromDate
            ExtendedWarrantyEndDate = Todate
        elif ContractType == '2':
            tmpCMCSD = FromDate
            tmpCMCED = Todate
        elif ContractType == '3':
            tmpAMCSD = FromDate
            tmpAMCED = Todate

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        sqlQueryTickets = f"INSERT INTO `Tickets_tickets`(`DeliveryID`, `AssignTo`, `CreatedBy`, `Type`, `Title`, `BpCardCode`, `ContactName`, `ContactPhone`, `ContactEmail`, `ContactAddress`, `ProductSerialNo`, `ProductName`, `ProductCategory`, `ProductModelNo`, `Zone`, `Priority`, `Status`, `Description`, `DurationOfService`, `SignatureStatus`, `WarrantyStartDate`, `WarrantyDueDate`, `ExtWarrantyStartDate`, `ExtWarrantyDueDate`, `AMCStartDate`, `AMCDueDate`, `CMCStartDate`, `CMCDueDate`, `ManufacturingDate`, `ExpiryDate`, `CreateDate`,`ClosedDate`,`Datetime`, `DueDate`, `TicketStatus`, `CustomerPIR`, `TicketEndDate`, `TicketStartDate`, `AlternatePhone`, `SignatureFile`, `CustomerFeedback`) VALUES ('{DeliveryId}', '{assignTo}', '{assignTo}', '{TicketType}', '{TicketTitle}', '{CardCode}', '{ContactPerson}', '{PhoneNumber}', '{Mail}', '{ContactAddress}', '{SerialNumber}', '{ProductName}', '{GroupCode}', '', '{tempZone}', '{TicketPriority}', '{TicketStatus}', '{Remarks}', '', '', '{WarStartDate}', '{WarEndDate}', '{ExtendedWarantyStartDate}', '{ExtendedWarrantyEndDate}', '{tmpAMCSD}', '{tmpAMCED}', '{tmpCMCSD}', '{tmpCMCED}', '', '', '{serverDateTime}', '{closedDate}', '{serverDateTime}', '{dueDate}', '{TicketRequestStatus}', '','','','','','')"
        # print(sqlQueryTickets)
        mycursor.execute(sqlQueryTickets)
        mydb.commit()
        ticketId = mycursor.lastrowid
        # print(f'Ticket id :- {ticketId}')
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        sqlUpdateServiceContract = f"UPDATE `Order_servicecontractsitem` SET `TicketGen`='True' WHERE `id` = {ServiceContractItemId}"
        mycursor.execute(sqlUpdateServiceContract)
        mydb.commit()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        ListFor = 1 # Customer(0), Engineer(1)
        # print('------------')
        sql_fetch_checklist = f"SELECT id, Name FROM ItemsPIR_checklist WHERE CategoryId = '{GroupCode}' AND Type = '{TicketType}' AND ListFor = '{ListFor}'"
        # print(sql_fetch_checklist)
        mycursor.execute(sql_fetch_checklist)
        checklist_rows = mycursor.fetchall()
        if len(checklist_rows) != 0:
            # print('----- Check List ---------')
            for row in checklist_rows:
                TaskName = row[1]
                sql_insertChecklist = f"INSERT INTO `Tickets_servicechecklist`(`TaskName`, `Comment`, `Status`, `Duration`, `Datetime`, `TicketId_id`) VALUES ('{TaskName}', '', 'False', '', '{serverDateTime}', '{ticketId}')"
                # print(sql_insertChecklist)
                mycursor.execute(sql_insertChecklist)
                mydb.commit()
                checklistId = mycursor.lastrowid
                # print(checklistId)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        ticketHistoryType = "Service"
        ticketHistoryRemarks = "New Installation Tickets Created"
        sqlQueryTicketHistory = f"INSERT INTO `Tickets_history`( `Type`, `Remarks`, `Datetime`, `TicketId_id`) VALUES ('{ticketHistoryType}', '{ticketHistoryRemarks}', '{serverDateTime}', '{ticketId}')"
        print(sqlQueryTicketHistory)
        mycursor.execute(sqlQueryTicketHistory)
        mydb.commit()
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # tempCount = tempCount+1
else:
    print("No data found")