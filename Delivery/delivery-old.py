import calendar
import requests, json
import time
import math
import mysql.connector
from datetime import date, datetime, timedelta

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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # local mysql connection 
# dir = os.getcwd()
# dir = dir.split("bridge")[0]+"bridge"
# sys.path.append(dir)
# from bridge import settings  # type: ignore
# data = settings.SAPSESSION("core")

# mydb = mysql.connector.connect(
#   host=settings.DATABASES['default']['HOST'],
#   user=settings.DATABASES['default']['USER'],
#   password=settings.DATABASES['default']['PASSWORD'],
#   database=settings.DATABASES['default']['NAME']
# )

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='$Bridge@2022#',
    # password='root',
    # database='massead_pre'
    database='massead_pre'
)

# mycursor = mydb.cursor(dictionary=True, buffered=True)
mycursor = mydb.cursor()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# with open("../bridge/db1.json") as f:
    # db = f.read()
    # # print(db)
# data = json.loads(db)
# r = requests.post('http://157.241.48.182:50001/b1s/v1/Login', data=json.dumps(data), verify=False)
# token = json.loads(r.text)['SessionId']
# # print(token)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 
# 
# 
# 
# 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#  ODBC Connection with sap sql databse
import json
import pyodbc

server = '157.241.48.182' # to specify an alternate port
# database = 'VISION_SALE_SERVICE_P' 
database = 'massead_pre' 
username = 'sa' 
password = 'vision@1091'

url = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
# print(url)
conn = pyodbc.connect(url)

cursor = conn.cursor()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 
# 
# 
# 
# 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

sapDb = {"CompanyDB": "massead_pre", "UserName": "manager", "Password": "9090", "sapurl": "http://157.241.48.182:50001/b1s/v1"}
# sapDb = {"CompanyDB": "VISION_SALE_SERVICE_P", "UserName": "manager", "Password": "9090", "sapurl": "http://157.241.48.182:50001/b1s/v1"}
r = requests.post('http://157.241.48.182:50001/b1s/v1/Login', data=json.dumps(sapDb), verify=False)
# print(r)
token = json.loads(r.text)['SessionId']
# print('===== sap login token --dev-- =====')
# print(token)

# get delivery list form sap
# res = requests.get(data['sapurl']+'/DeliveryNotes/$count?$filter=UpdateDate ge 2022-10-27', headers={'Authorization': "Bearer "+data['SessionId']+""}, verify=False)
res = requests.get(sapDb['sapurl']+'/DeliveryNotes/$count?$filter=UpdateDate ge '+str(currentDate), cookies=r.cookies, verify=False)
# res = requests.get(sapDb['sapurl']+'/DeliveryNotes/$count?$filter=UpdateDate ge 2022-12-04', cookies=r.cookies, verify=False)
serInvoicesCount = int(res.text)
count = math.ceil(int(serInvoicesCount)/20)
print(count)

mycursor.execute("select * from Delivery_delivery")
mycursor.fetchall()
localInvoicesCount = mycursor.rowcount

print(f'local Delivery count: {localInvoicesCount} and server Delivery count {serInvoicesCount}')
# if localInvoicesCount < serInvoicesCount:
if count > 0:
# if True:
    skip=0
    for i in range(count):
        res = requests.get(sapDb['sapurl']+'/DeliveryNotes?$filter=UpdateDate ge '+str(currentDate)+' &$skip='+str(skip)+'', cookies=r.cookies, verify=False)
        # res = requests.get(sapDb['sapurl']+'/DeliveryNotes?$filter=UpdateDate ge 2022-12-04 &$skip='+str(skip)+'', cookies=r.cookies, verify=False)
        opts = json.loads(res.text)
        for opt in opts['value']:
            DocEntry = opt['DocEntry']
        
            docSelectQuery = f"select * from Delivery_delivery WHERE DocEntry = '{DocEntry}'"
            print(docSelectQuery)
            mycursor.execute(docSelectQuery)
            mycursor.fetchall()
            if mycursor.rowcount != 1:

                d = datetime.strptime(str(opt['DocTime']), "%H:%M:%S")
                DocTime = d.strftime("%I:%M:%S %p")

                e = datetime.strptime(str(opt['UpdateTime']), "%H:%M:%S")
                UpdateTime = e.strftime("%I:%M:%S %p")

                discountPercent = float(opt['DiscountPercent'])
                if discountPercent < 0:
                    discountPercent = 0

                # str(discountPercent)
                CardName = str(opt['CardName']).replace("'","\\'")
                OrderID = str(opt['U_PORTAL_NO']) # local order id

                ContactAddress = str(opt['Address'])
                
                ord_sql = "INSERT INTO `Delivery_delivery` (`TaxDate`, `DocDueDate`, `ContactPersonCode`, `DiscountPercent`, `DocDate`, `CardCode`, `Comments`, `SalesPersonCode`, `DocEntry`, `U_Term_Condition`, `CreateDate`, `CreateTime`, `UpdateDate`, `UpdateTime`, `CardName`, `CreationDate`, `DocCurrency`, `DocTotal`, `DocumentStatus`, `VatSum`, `BPLID`, `PaymentGroupCode`, `OrderId`, `ShippingAndHandling`) VALUES ('"+str(opt['TaxDate'])+"', '"+str(opt['DocDueDate'])+"', '"+str(opt['ContactPersonCode'])+"', '"+str(discountPercent)+"', '"+str(opt['DocDate'])+"', '"+str(opt['CardCode'])+"', '"+str(opt['Comments'])+"', '"+str(opt['SalesPersonCode'])+"', '"+str(opt['DocEntry'])+"', '', '"+str(opt['CreationDate'])+"', '"+str(DocTime)+"', '"+str(opt['UpdateDate'])+"', '"+str(UpdateTime)+"', '"+str(CardName)+"', '"+str(opt['CreationDate'])+"', '"+str(opt['DocCurrency'])+"', '"+str(opt['DocTotal'])+"', '"+str(opt['DocumentStatus'])+"', '"+str(opt['VatSum'])+"', '', '"+str(opt['PaymentGroupCode'])+"','"+str(OrderID)+"', '"+str(opt['U_Ship_Handling'])+"')"

                # print(ord_sql)
                mycursor.execute(ord_sql)
                mydb.commit()                
                DeliveryId = mycursor.lastrowid
                
                add = opt['AddressExtension']
                U_SCOUNTRY  = str(add['U_SCOUNTRYS'])
                U_SSTATE    = str(add['U_SSTATES'])
                U_SHPTYPB   = str(add['U_SHPTYPSS'])
                U_BSTATE    = str(add['U_BSTATEB'])
                U_BCOUNTRY  = str(add['U_BCOUNTRYB'])
                U_SHPTYPS   = str(add['U_SHPTYPBB'])
                

                ShipToBuilding = str(add['ShipToBuilding']).replace("'","\\'")
                BillToBuilding = str(add['BillToBuilding']).replace("'","\\'")
                ShipToStreet = str(add['ShipToStreet']).replace("'","\\'")
                BillToStreet = str(add['BillToStreet']).replace("'","\\'")

                add_sql = "INSERT INTO `Delivery_addressextension` (`DeliveryId`, `BillToBuilding`, `ShipToState`, `BillToCity`, `ShipToCountry`, `BillToZipCode`, `ShipToStreet`, `BillToState`, `ShipToZipCode`, `BillToStreet`, `ShipToBuilding`, `ShipToCity`, `BillToCountry`, `U_SCOUNTRY`, `U_SSTATE`, `U_SHPTYPB`, `U_BSTATE`, `U_BCOUNTRY`, `U_SHPTYPS`) VALUES ('"+str(DeliveryId)+"', '"+str(BillToBuilding)+"', '"+str(add['ShipToState'])+"', '"+str(add['BillToCity'])+"', '"+str(add['ShipToCountry'])+"', '"+str(add['BillToZipCode'])+"', '"+str(ShipToStreet)+"', '"+str(add['BillToState'])+"', '"+str(add['ShipToZipCode'])+"', '"+str(BillToStreet)+"', '"+str(ShipToBuilding)+"', '"+str(add['ShipToCity'])+"', '"+str(add['BillToCountry'])+"', '"+str(U_SCOUNTRY)+"', '"+str(U_SSTATE)+"', '"+str(U_SHPTYPB)+"', '"+str(U_BSTATE)+"', '"+str(U_BCOUNTRY)+"', '"+str(U_SHPTYPS)+"');"
                # print(add_sql)
                mycursor.execute(add_sql)
                mydb.commit()

                lines = opt['DocumentLines']
                # for line in opt['DocumentLines']:
            
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                
                sqlQuery = f"""
                Select
                d.DocNum [DeliveryChallanNumber]
                ,d.DocEntry [OrderID]
                ,a.ItemCode [ProductCode]
                ,a.ItemName [ProductName]
                ,ISNULL(c.SysNumber,r.SysNumber) [SystemSerialNumber]
                ,ISNULL(c.DistNumber,r.DistNumber) as [SerialNumber]
                ,k.ItmsGrpCod [GroupCode]
                ,k.ItmsGrpNam [GroupName]
                ,e.ShipDate [DeliveryDate]
                ,e."ItemCode"+'/'+COALESCE(c.DistNumber,"c".DistNumber,r.Distnumber)+'/'+ISNULL(Convert(varchar,c.GrntStart,105),'')+'/'+ISNULL(Convert(varchar,c.GrntExp,105),'')+'/'+ISNULL(Convert(varchar,c.U_EXWRNTY_STDT,105),'')+'/'+ISNULL(Convert(varchar,c.U_EXWRNTY_EDDT,105),'') [BarcodeNumber]
                ,'' [Warranty StartDate]
                ,'' [Warranty EndDate]
                ,c.U_EXWRNTY_STDT [ExtendedWarantyStartDate]
                ,c.U_EXWRNTY_EDDT [ExtendedWarrantyEndDate]
                ,i.U_FRMDT  [AMCCNCStartDate]
                ,i.U_TODT [AMCCNCEndDate]
                ,l.U_Zone  [Zone]
                ,d.CardCode [CardCode]
                ,d.CardName 
                ,ISNULL(n.FirstName,'') [ContactPerson]
                ,m.E_Mail [Mail]
                ,m.Cellular [PhoneNumber]
                ,d.Comments [Remarks]
                ,ISNULL(j.U_ITEMTYPE,'') [WarrantyType]

                    from OITL a inner join ITL1 b on a.LogEntry=b.LogEntry left Join OSRN c on b.SysNumber=c.SysNumber and b.ItemCode=c.itemCode
                    left Join OBTN r on b.SysNumber=r.SysNumber and b.ItemCode=r.itemCode

                    inner join DLN1 e on a.DocEntry=e.DocEntry and a.DocLine=e.LineNum
                    inner join ODLN d on d.DocEntry=a.DocEntry
                    left join INV1 f on e.TargetType=f.ObjType and e.TrgetEntry=f.DocEntry and e.LineNum=f.BaseLine
                    left join OINV h on f.DocEntry=h.DocEntry
                    left Join [@CIN_INV_C0] g on g.U_ITMCD=e.ItemCode and g.U_Line=e.LineNum and U_INVENT=h.DocEntry
                    Left Join [@CIN_INV_C1] i on g.DocEntry=i.DocEntry and ISNULL(i.U_ITMCD,'')!=''
                    left Join OITM j on e.ItemCode=j.ItemCode
                    left Join OITB k on j.ItmsGrpCod=k.ItmsGrpCod
                    left Join OCRD m on d.CardCode=m.CardCode
                    left Join CRD1 l on d.CardCode=l.CardCode and d.ShipToCode=l.Address2 and l.AddrType='S'
                    left Join OCPR n on n.CardCode=m.CardCode and d.CntctCode=n.CntctCode
                        Where e.DocEntry = '{DocEntry}'  And a.DocType='15'
                """
                # print(sqlQuery)
                cursor.execute(sqlQuery) 
                rows = cursor.fetchall()
                # print(rows)
                tempCount = 0
                for row in rows:

                    LineNum = lines[tempCount]["LineNum"]

                    BaseEntry = str(lines[tempCount]['BaseEntry']) # sap order id
                    
                    lDiscountPercent = 0.0
                    if lines[tempCount]['DiscountPercent'] == None or lines[tempCount]['DiscountPercent'] == 0:
                        lDiscountPercent = 0.0
                    else:
                        lDiscountPercent = float(lines[tempCount]['DiscountPercent'])
                    
                    str(lDiscountPercent)
        
                    # DeliveryID = 2289 #static
                    DeliveryChallanNumber = row[0]
                    # OrderID = row[1]
                    ProductCode = row[2]
                    ProductName = row[3]
                    SystemSerialNumber = row[4]
                    SerialNumber = row[5]
                    GroupCode = row[6]
                    GroupName = row[7]
                    DeliveryDate = row[8]
                    BarcodeNumber = row[9]
                    # WarStartDate = row[10]
                    # WarEndDate = row[11]
                    ExtendedWarantyStartDate = row[12]
                    ExtendedWarrantyEndDate = row[13]
                    AMCCNCStartDate = row[14]
                    AMCCNCEndDate = row[15]
                    Zone = row[16]
                    CardCode = row[17]
                    CardName = row[18]
                    ContactPerson = row[19]
                    Mail = row[20]
                    PhoneNumber = row[21]
                    Remarks = row[22]
                    WarrantyType = row[23]

                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    print('---- AMC UPDATE-----')
                    update_amc_order = f"UPDATE `Order_amcsalesorder` SET `ItemSerialNo`='{SerialNumber}' WHERE `OrderID` = '{OrderID}' and `LineNum` = '{LineNum}'"
                    print(update_amc_order)
                    mycursor.execute(update_amc_order)
                    mydb.commit()

                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # # print('============= service item ==================')
                    # sql_doc_entry = f"SELECT * FROM `Delivery_documentlines` WHERE `OrderId` = '{OrderID}' and `SerialNo` = '{SerialNumber}'"
                    # # print(sql_doc_entry)
                    # mycursor.execute(sql_doc_entry)
                    # docEntdata = mycursor.fetchall()
                    # if len(docEntdata) != 0:
                    #     continue
                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    
                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # print('============= service item ==================')
                    # sql_category = f"SELECT * FROM `Category_category` WHERE `Number`='{GroupCode}' and `IsService` = 'true'"
                    # # print(sql_category)
                    # mycursor.execute(sql_category)
                    # catdata = mycursor.fetchall()
                    # # print(catdata)
                    # if len(catdata) != 0:
                    #     continue

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    WarStartDate = currentDate # current date as warrenty start date
                    WarEndDate = currentDate + timedelta(days=365) # date after 1 year as warrenty start end date
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

                    tmpCMCSD = ""
                    tmpCMCED = ""
                    tmpAMCSD = ""
                    tmpAMCED = ""

                    if WarrantyType != "":
                        if WarrantyType == 1:
                            tmpCMCSD = AMCCNCStartDate
                            tmpCMCED = AMCCNCEndDate
                        
                        if WarrantyType == 2:
                            tmpAMCSD = AMCCNCStartDate
                            tmpAMCED = AMCCNCEndDate

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    sqlQueryDelivery = f'INSERT INTO `Delivery_documentlines`(`LineNum`, `DeliveryID`, `OrderId`, `DeliveryChallanNumber`, `Quantity`, `UnitPrice`, `DiscountPercent`, `TaxCode`, `BarCode`, `SerialNo`, `ItemCode`, `ItemName`, `ItemCategory`, `ItemDescription`, `U_FGITEM`, `CostingCode2`, `ProjectCode`, `FreeText`, `EstimatedDeliveryDate`, `WarrantyType`, `WarrantyStartDate`, `WarrantyDueDate`, `ExtWarrantyStartDate`, `ExtWarrantyDueDate`, `AMCStartDate`, `AMCDueDate`, `CMCStartDate`, `CMCDueDate`, `ManufacturingDate`, `ExpiryDate`, `Status`, `BaseEntry`, `TaxRate`) VALUES ("{LineNum}", "{DeliveryId}", "{OrderID}", "{DeliveryChallanNumber}", "{lines[tempCount]["Quantity"]}", "{lines[tempCount]["UnitPrice"]}", "{lDiscountPercent}", "{lines[tempCount]["TaxCode"]}", "{BarcodeNumber}", "{SerialNumber}", "{ProductCode}", "{ProductName}", "{lines[tempCount]["ProjectCode"]}", "{lines[tempCount]["ItemDescription"]}", "{lines[tempCount]["U_FGITEM"]}", "{lines[tempCount]["CostingCode2"]}", "{lines[tempCount]["ProjectCode"]}", "{lines[tempCount]["FreeText"]}", "{DeliveryDate}", "{WarrantyType}", "{WarStartDate}", "{WarEndDate}", "{ExtendedWarantyStartDate}", "{ExtendedWarrantyEndDate}", "{tmpAMCSD}", "{tmpAMCED}", "{tmpCMCSD}", "{tmpCMCED}", "NA", "NA", "NA", "{BaseEntry}", "{lines[tempCount]["TaxPercentagePerRow"]}")'
                    
                    # print(sqlQueryDelivery)
                    mycursor.execute(sqlQueryDelivery)
                    mydb.commit()
                    itemId = mycursor.lastrowid 
                    # # print(itemId)
                    # print(f'Item id :- {itemId}')

                    # static fields
                    TicketType = "Installation"
                    TicketTitle = "New Installation"
                    TicketPriority = "Medium" # low, medium, heigh
                    TicketStatus = "Pending"
                    TicketRequestStatus = "Pending"

                    closedDate = currentDate + timedelta(days=15)
                    dueDate = currentDate + timedelta(days=15)

                    assignTo = 52
                    tempZone = "North"

                    # print('---- BP ----')
                    bpSql = f"SELECT `id`, `CardCode`, `CardName`, `Zone`, `ContactPerson`, `EmailAddress`, `Phone1`, `CountryCode`  FROM `BusinessPartner_businesspartner` WHERE `CardCode` = '{opt['CardCode']}'"
                    # print(bpSql)
                    mycursor.execute(bpSql)
                    bpdata = mycursor.fetchall()
                    if len(bpdata) != 0:
                        tempZone = bpdata[0][3]
                        ContactPerson = bpdata[0][4]
                        Mail = bpdata[0][5]
                        PhoneNumber = bpdata[0][6]
                        CountryCode = bpdata[0][7]
                    # print(Zone)

                    # print('---- Employee ----')
                    empSql = f"SELECT `id`, `SalesEmployeeCode`, `firstName` FROM `Employee_employee` WHERE `role` = 'support manager' AND `zone` = '{tempZone}' AND `Active` = 'tYES'"
                    # print(empSql)
                    mycursor.execute(empSql)
                    empdata = mycursor.fetchall()
                    if len(empdata) != 0:
                        # assignTo = empdata[0][0] # for id
                        assignTo = empdata[0][1] # for SalesEmployeeCode

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    sqlQueryTickets = f"INSERT INTO `Tickets_tickets`(`DeliveryID`, `AssignTo`, `CreatedBy`, `Type`, `Title`, `BpCardCode`, `ContactName`, `ContactPhone`,`CountryCode`, `ContactEmail`, `ContactAddress`, `ProductSerialNo`, `ProductName`, `ProductCategory`, `ProductModelNo`, `Zone`, `Priority`, `Status`, `Description`, `DurationOfService`, `SignatureStatus`, `WarrantyStartDate`, `WarrantyDueDate`, `ExtWarrantyStartDate`, `ExtWarrantyDueDate`, `AMCStartDate`, `AMCDueDate`, `CMCStartDate`, `CMCDueDate`, `ManufacturingDate`, `ExpiryDate`, `CreateDate`,`ClosedDate`,`Datetime`, `DueDate`, `TicketStatus`, `CustomerPIR`, `TicketEndDate`, `TicketStartDate`, `AlternatePhone`, `SignatureFile`, `CustomerFeedback`) VALUES ('{DeliveryId}', '{assignTo}', '{assignTo}', '{TicketType}', '{TicketTitle}', '{opt['CardCode']}', '{ContactPerson}', '{PhoneNumber}','{CountryCode}',  '{Mail}', '{ContactAddress}', '{SerialNumber}', '{ProductName}', '{GroupCode}', '', '{Zone}', '{TicketPriority}', '{TicketStatus}', '{Remarks}', '', '', '{WarStartDate}', '{WarEndDate}', '{ExtendedWarantyStartDate}', '{ExtendedWarrantyEndDate}', '{tmpAMCSD}', '{tmpAMCED}', '{tmpCMCSD}', '{tmpCMCED}', '', '', '{serverDateTime}', '{closedDate}', '{serverDateTime}', '{dueDate}', '{TicketRequestStatus}', '','','','','','')"
                    # print(sqlQueryTickets)
                    mycursor.execute(sqlQueryTickets)
                    mydb.commit()
                    ticketId = mycursor.lastrowid
                    # print(f'Ticket id :- {ticketId}')

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    ListFor = 1 # Customer(0), Engineer(1)
                    # print('------------')
                    sql_fetch_checklist = f"SELECT id, Name FROM ItemsPIR_checklist WHERE CategoryId = '{GroupCode}' AND Type = '{TicketType}' AND ListFor = '{ListFor}'"
                    # print(sql_fetch_checklist)
                    mycursor.execute(sql_fetch_checklist)
                    checklist_rows = mycursor.fetchall()

                    # cursor.execute(sql_fetch_checklist)
                    # checklist_rows = cursor.fetchall()
                    if len(rows) != 0:
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
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    tempCount = tempCount+1

        # print('___')
        skip = skip+20
        # print(skip)


