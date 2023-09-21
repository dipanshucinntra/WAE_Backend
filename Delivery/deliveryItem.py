import json
import pyodbc

server = '157.241.48.182' # to specify an alternate port
# server = '103.234.187.253' # to specify an alternate port
#server = 'tcp:myserver.database.windows.net' 
# database = 'VISION_LIVE_160822' 
database = 'VISION_SERVICE' 
username = 'sa' 
password = 'vision@1091'

# database = 'VISION_DEV' 
# username = 'sa' 
# password = 'vision@1091'

url = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
print(url)
conn = pyodbc.connect(url)
cursor = conn.cursor()


#cursor.execute("SELECT @@version;")
#cursor.execute("SELECT * from OBPL")
# cursor.execute("SELECT BPLId, BPLName, Address, MainBPL, Disabled, UserSign2, UpdateDate, DflWhs, TaxIdNum, StreetNo, Building, ZipCode, City, State, Country from OBPL where Disabled='N'") 

sqlQuery = """
Select
d.DocNum [DeliveryChallanNumber]
,d.DocEntry [OrderID]
,a.ItemCode [ProductCode]
,a.ItemName [ProductName]
,c.SysNumber [SystemSerialNumber]
,c.DistNumber as [SerialNumber]
,k.ItmsGrpCod [GroupCode]
,k.ItmsGrpNam [GroupName]
,e.ShipDate [DeliveryDate]
,e."ItemCode"+'/'+COALESCE(c.DistNumber,"c".DistNumber)+'/'+ISNULL(Convert(varchar,c.GrntStart,105),'')+'/'+ISNULL(Convert(varchar,c.GrntExp,105),'')+'/'+ISNULL(Convert(varchar,c.U_EXWRNTY_STDT,105),'')+'/'+ISNULL(Convert(varchar,c.U_EXWRNTY_EDDT,105),'') [BarcodeNumber]
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

    from OITL a inner join ITL1 b on a.LogEntry=b.LogEntry inner Join OSRN c on b.SysNumber=c.SysNumber and b.ItemCode=c.itemCode

    inner join DLN1 e on a.DocEntry=e.DocEntry and a.DocLine=e.LineNum
    inner join ODLN d on d.DocEntry=a.DocEntry
    inner join INV1 f on e.TargetType=f.ObjType and e.TrgetEntry=f.DocEntry and e.LineNum=f.BaseLine
    inner join OINV h on f.DocEntry=h.DocEntry
    left Join [@CIN_INV_C0] g on g.U_ITMCD=e.ItemCode and g.U_Line=e.LineNum and U_INVENT=h.DocEntry
    Left Join [@CIN_INV_C1] i on g.DocEntry=i.DocEntry and ISNULL(i.U_ITMCD,'')!=''
    left Join OITM j on e.ItemCode=j.ItemCode
    left Join OITB k on j.ItmsGrpCod=k.ItmsGrpCod
    left Join OCRD m on d.CardCode=m.CardCode
    left Join CRD1 l on d.CardCode=l.CardCode and d.ShipToCode=l.Address2 and l.AddrType='S'
    left Join OCPR n on n.CardCode=m.CardCode and d.CntctCode=n.CntctCode
        Where e.DocEntry in (Select BaseEntry from INV1 Where DocEntry='2289'  And a.DocType='15')
"""

cursor.execute(sqlQuery) 
rows = cursor.fetchall()

if len(rows) != 0:
    for row in rows:
        print(row)
        DeliveryID = 2289 #static

        DeliveryChallanNumber = row[0]
        OrderID = row[1]
        ProductCode = row[2]
        ProductName = row[3]
        SystemSerialNumber = row[4]
        SerialNumber = row[5]
        GroupCode = row[6]
        GroupName = row[7]
        DeliveryDate = row[8]
        BarcodeNumber = row[9]
        StartDate = row[10]
        EndDate = row[11]
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

        # sqlQuery = f"INSERT INTO `delivery_documentlines`(`LineNum`, `DeliveryID`, `OrderId`, `DeliveryChallanNumber`, `Quantity`, `UnitPrice`, `DiscountPercent`, `TaxCode`, `BarCode`, `SerialNo`, `ItemCode`, `ItemName`, `ItemCategory`, `ItemDescription`, `U_FGITEM`, `CostingCode2`, `ProjectCode`, `FreeText`, `EstimatedDeliveryDate`, `WarrantyType`, `WarrantyStartDate`, `WarrantyDueDate`, `ExtWarrantyStartDate`, `ExtWarrantyDueDate`, `AMCStartDate`, `AMCDueDate`, `CMCStartDate`, `CMCDueDate`, `ManufacturingDate`, `ExpiryDate`, `Status`) VALUES (0, {DeliveryID}, {OrderID}, {DeliveryChallanNumber}, {DeliveryID},  0, 0, 0,)"



# columns = [column[0] for column in cursor.description]
# all = []
# i=0;


# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="$Bridge@2022#",
#   database="massead_pre"
# )
# mycursor = mydb.cursor()



# for row in rows:
#   sp_sql = "INSERT INTO `Company_branch` (`BPLId`, `BPLName`, `Address`, `MainBPL`, `Disabled`, `UserSign2`, `UpdateDate`, `DflWhs`, `TaxIdNum`, `StreetNo`, `Building`, `ZipCode`, `City`, `State`, `Country`) VALUES ('"+str(row[0])+"', '"+str(row[1])+"', '"+str(row[2])+"', '"+str(row[3])+"', '"+str(row[4])+"', '"+str(row[5])+"', '"+str(row[6])+"', '"+str(row[7])+"', '"+str(row[8])+"', '"+str(row[9])+"', '"+str(row[10])+"', '"+str(row[11])+"', '"+str(row[12])+"', '"+str(row[13])+"', '"+str(row[14])+"');"
#   print(sp_sql)
#   mycursor.execute(sp_sql)
#   mydb.commit()

