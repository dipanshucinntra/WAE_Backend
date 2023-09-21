from ctypes import sizeof
import requests, json
import time
import math
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="$Bridge@2022#",
#   password="root",
  database="standalone_new"
)

mycursor = mydb.cursor(dictionary=True)

userList = []

# sqlSelectCamSet = "SELECT * FROM `Campaign_campaignset` WHERE `id` = 38"
sqlSelectCamSet = "SELECT `id`, `CampaignSetName`, `CampaignAccess`, `Description`, `LeadSource`, `LeadPriority`, `LeadStatus`, `LeadFromDate`, `LeadToDate`, `OppType`, `OppSalePerson`, `OppStage`, `OppFromDate`, `OppToDate`, `BPType`, `BPSalePerson`, `BPCountry`, `BPState`, `BPIndustry`, `BPFromDate`, `BPToDate`, `MemberList`, `Status`, `CreateDate`, `CreateTime`, `CampaignSetOwner_id`, `CreateBy_id`, `BPCountryCode`, `BPStateCode`, `AllBP`, `AllLead`, `AllOpp` FROM `Announcement_campaignset` WHERE Status = 1"
mycursor.execute(sqlSelectCamSet)
allRow = mycursor.fetchall()
for campaign in allRow:
    print('----- campset data -----')
    print(campaign)
    camSetId = campaign['id']

    AllBPCheck = campaign['AllBP']
    AllLeadCheck = campaign['AllLead']
    AllOppCheck = campaign['AllOpp']

    # ----------------------------------
    # -------Filter for Lead -----------
    # ----------------------------------
    leadFlag = False;

    if AllLeadCheck == 1:
        leadwhere = ''
        leadFlag = True;
    else:
        leadwhere = 'WHERE 1 '
        LeadSource = campaign['LeadSource'].strip()
        LeadPriority = campaign['LeadPriority'].strip()
        LeadStatus = campaign['LeadStatus'].strip()
        LeadFromDate = campaign['LeadFromDate'].strip()
        LeadToDate = campaign['LeadToDate'].strip()

        if LeadSource != "":
            leadwhere += 'and `source` in("'+ LeadSource.replace(',','","') +'") '
            leadFlag = True;

        if LeadPriority != "":
            leadwhere += 'and `leadType` in("'+ LeadPriority.replace(',','","') +'") '
            leadFlag = True;

        if LeadStatus != "":
            leadwhere += 'and `status` in("'+ LeadStatus.replace(',','","') +'") '
            leadFlag = True;

        if LeadFromDate != "" and LeadToDate != "":
            leadwhere += 'and `date` <= "'+ LeadFromDate + '" and `date` >= "'+  LeadToDate +'" '
            leadFlag = True;

    if leadFlag:
        sqlSelectLead = "SELECT `id`, `contactPerson`, `phoneNumber`,`CountryCode`, `email`, `leadType`, `status` FROM `Lead_lead` " + leadwhere
        print('----- lead data -----')
        print(sqlSelectLead)
        mycursor.execute(sqlSelectLead)
        allLead = mycursor.fetchall()
        # print(len(allLead))
        for contactPrson in allLead:
            userData = {
                'Name': contactPrson['contactPerson'],
                'Phone': contactPrson['phoneNumber'],
                'CountryCode': contactPrson['CountryCode'],
                'Email': contactPrson['email']
            }
            userList.append(userData)
        
    
    # ----------------------------------------
    # --------- Oppertunity data -------------
    # ----------------------------------------
    oppFlag = False;

    if AllOppCheck == 1:
        oppwhere = ''
        oppFlag = True;
    else:   
        oppwhere = 'WHERE 1 '
        OppType = campaign['OppType'].strip()
        OppSalePerson = campaign['OppSalePerson'].strip()
        # OppStage = campaign['OppStage'].strip()
        OppFromDate = campaign['OppFromDate'].strip()
        OppToDate = campaign['OppToDate'].strip()


        if OppType != "":
            oppwhere += 'and `U_TYPE` = "'+ OppType +'" '
            oppFlag = True;

        if OppSalePerson != "":
            oppwhere += 'and `SalesPerson` in("'+ OppSalePerson.replace(',','","') +'") '
            oppFlag = True;


        if OppFromDate != "" and OppToDate != "":
            oppwhere += 'and `StartDate` <= "'+ OppFromDate + '" and `ClosingDate` >= "'+  OppToDate +'" '
            oppFlag = True;

    if oppFlag:
        sqlSelectOpp = "SELECT DISTINCT ContactPerson, ContactPersonName,id FROM Opportunity_opportunity " + oppwhere
        print('----- opp data -----')
        print(sqlSelectOpp)
        mycursor.execute(sqlSelectOpp)
        allLead = mycursor.fetchall()
        # print(allLead)
        # print(len(allLead))
        for oppData in allLead:
            # print(oppData)
            ContactPersonId = oppData['id']
            sqlSelectBpEmp = "SELECT `id`,`FirstName`, `MobilePhone`,`CountryCode`, `E_Mail` FROM `BusinessPartner_bpemployee` WHERE `id` = "+ str(ContactPersonId)
            mycursor.execute(sqlSelectBpEmp)
            empData = mycursor.fetchall()
            for bpEmp in empData:
                # print('-----Emp data----')
                # print(data)
                userData = {
                    'Name': bpEmp['FirstName'],
                    'Phone': bpEmp['MobilePhone'],
                    'CountryCode': bpEmp['CountryCode'],
                    'Email': bpEmp['E_Mail']
                }
                userList.append(userData)
            
    
    # ----------------------------------------
    # ----------- Customer data --------------
    # ----------------------------------------
    bpFlag = False

    if AllBPCheck == 1:
        bpwhere = ''
        bpFlag = True;
    else: 
        bpwhere = 'WHERE 1 '
        BPType = campaign['BPType'].strip()
        BPSalePerson = campaign['BPSalePerson'].strip()
        BPCountry = campaign['BPCountry'].strip()
        BPState = campaign['BPState'].strip()
        BPIndustry = campaign['BPIndustry'].strip()
        BPFromDate = campaign['BPFromDate'].strip()
        BPToDate = campaign['BPToDate'].strip()

        BPCountryCode = campaign['BPCountryCode'].strip()
        BPStateCode = campaign['BPStateCode'].strip()

        if BPType != "":
            bpwhere += 'and BusinessPartner_businesspartner.U_TYPE = "'+ BPType +'" '
            bpFlag = True

        if BPSalePerson != "":
            bpwhere += 'and BusinessPartner_businesspartner.SalesPersonCode in("'+ BPSalePerson.replace(',','","') +'") '
            bpFlag = True

        if BPFromDate != "" and BPToDate != "":
            bpwhere += 'and BusinessPartner_businesspartner.CreateDate <= "'+ BPFromDate + '" and BusinessPartner_businesspartner.CreateDate >= "'+  BPToDate +'" '
            bpFlag = True

        if BPIndustry != "":
            bpwhere += 'and BusinessPartner_businesspartner.Industry in("'+ BPIndustry.replace(',','","') +'") '
            bpFlag = True
        
        if BPCountry != "":
            bpwhere += 'and BusinessPartner_bpaddresses.Country = "'+ BPCountry +'" '
            bpFlag = True
        
        if BPState != "":
            bpwhere += 'and BusinessPartner_bpaddresses.State = "'+ BPState +'" '
            bpFlag = True

    if bpFlag:
        sqlSelectBP = "SELECT BusinessPartner_businesspartner.id FROM BusinessPartner_businesspartner JOIN BusinessPartner_bpaddresses ON BusinessPartner_businesspartner.id = BusinessPartner_bpaddresses.BPID " + bpwhere
        print('----- Customer data -----')
        print(sqlSelectBP)
        mycursor.execute(sqlSelectBP)
        allBp = mycursor.fetchall()
        # print(allBp)
        # print(len(allBp))
        for bp in allBp:
            # print(oppData)
            ContactPersonId = bp['id']
            sqlSelectBpEmp = "SELECT `id`,`FirstName`, `MobilePhone`,`CountryCode`, `E_Mail` FROM `BusinessPartner_bpemployee` WHERE `id` = "+ str(ContactPersonId)
            mycursor.execute(sqlSelectBpEmp)
            empData = mycursor.fetchall()
            for bpEmp in empData:
                # print('-----Emp data----')
                # print(data)
                userData = {
                    'Name': bpEmp['FirstName'],
                    'Phone': bpEmp['MobilePhone'],
                    'CountryCode': bpEmp['CountryCode'],
                    'Email': bpEmp['E_Mail']
                }
                userList.append(userData)


    print('----All User----')
    # print(userList)
    for user in userList:
        Name = user['Name']
        Phone = user['Phone']
        CountryCode = user['CountryCode']
        Email = user['Email']

        if Phone != "" and Email != "":
            sqlSelectCamSet = "SELECT * FROM `Announcement_campaignsetmembers` WHERE `CampSetId_id` = '"+str(camSetId)+"' AND `Phone` = "+ str(Phone) +"  AND `CountryCode` = "+ str(CountryCode) +"   And `Email` = '"+str(Email)+"'"
            # print(sqlSelectCamSet)
            mycursor.execute(sqlSelectCamSet)
            allRow = mycursor.fetchall()
            
            if not allRow:
                insertCamSetMember ="INSERT INTO `Announcement_campaignsetmembers`(`Name`, `Phone`,`CountryCode`, `Email`, `CampSetId_id`) VALUES ('"+str(Name)+"', '"+str(Phone)+"', '"+str(CountryCode)+"', '"+str(Email)+"', '"+str(camSetId)+"')"
                # print(insertCamSetMember)
                mycursor.execute(insertCamSetMember)
            mydb.commit() # this method will confirm and save changes in database
    
    userList = []