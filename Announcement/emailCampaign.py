from ctypes import sizeof
from datetime import date, datetime
import calendar
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import os
import smtplib
import requests, json
import time
import math
import mysql.connector

from urllib.parse import urlparse

currentDate = date.today()
currentDay = calendar.day_name[currentDate.weekday()]  # this will return the day of a week
currentTime = datetime.today().strftime("%I:%M %p")

#print("Today date is: ", currentDate)
#print("Today day is: ", currentDay)
#print("Today Current time: ", currentTime)


import sys
sys.path.append('/home/www/b2b/standalone_new/bridge_support/')
# sys.path.append('../../bridge')
from global_fun_core import sendMail


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="$Bridge@2022#",
#   password="root",
  database="standalone_new"
)

mycursor = mydb.cursor(dictionary=True)

# -------------------
# Email Campaign Body  
# -------------------
def sendCampaignToMember(subject, Message, members, Attachments, campId):
    for member in members:
        email = member['Email']
        if email !="":
            # print('in mail functions')
            # print(email, subject, Message)
            res = sendMail(email, subject, Message, Attachments)
            print(res)
            if Frequency == 'Once':
                # update send status 1 in campaign
                sqlUpdateCampaign = "UPDATE `Announcement_campaign` SET `Sent` = 1 WHERE `id` = "+ str(campId)
                mycursor.execute(sqlUpdateCampaign)
                mydb.commit()

userList = []

# sqlSelectCamSet = "SELECT * FROM `Campaign_campaignset` WHERE `id` = 38"
sqlSelectCamSet = "SELECT * FROM `Announcement_campaignset` WHERE Status = 1"
mycursor.execute(sqlSelectCamSet)
allRow = mycursor.fetchall()
for campaign in allRow:
    camSetId = campaign['id']
    # -----------------------
    # campain set member list
    # -----------------------
    allMembersArr = []
    #print("SELECT * FROM `Announcement_campaignsetmembers` WHERE `CampSetId_id` = "+ str(camSetId))
    sqlSelectMember = "SELECT * FROM `Announcement_campaignsetmembers` WHERE `CampSetId_id` = "+ str(camSetId)
    mycursor.execute(sqlSelectMember)
    allMembers = mycursor.fetchall()
    if len(allMembers) != 0:
        for member in allMembers:
            userData = {
                'Name': member['Name'],
                'Phone': member['Phone'],
                'CountryCode': member['CountryCode'],
                'Email': member['Email']
            }
            allMembersArr.append(userData)

    # -----------------------
    # --- campain list ------
    # -----------------------
    mailSubject = ""
    mailbody = ""

    print('---Campaign---')
    sqlSelectCam = "SELECT * FROM `Announcement_campaign` WHERE `RunTime` = '"+str(currentTime)+"' AND `Status` = 1 AND `Sent` = 0 AND `Type` = 'E-Mail' AND `StartDate` <= '"+str(currentDate)+"' AND `EndDate` >= '"+str(currentDate)+"' AND `CampaignSetId_id` = "+ str(camSetId)
    # sqlSelectCam = "SELECT * FROM `Campaign_campaign` WHERE `Status` = 1 AND `Sent` = 0 AND `Type` = 'E-Mail' AND `StartDate` <= '"+str(currentDate)+"' AND `EndDate` >= '"+str(currentDate)+"' AND `CampaignSetId_id` = "+ str(camSetId)
    print(sqlSelectCam)
    mycursor.execute(sqlSelectCam)
    allCampaign = mycursor.fetchall()
    print(len(allCampaign))
    if len(allCampaign) != 0:
        for campaign in allCampaign:
            print(campaign)
            print(campaign['id'])
            camp_id = campaign['id']
            
            Frequency = campaign['Frequency']
            mailbody = campaign['Message']
            MonthlyDate = campaign['MonthlyDate']
            WeekDay = campaign['WeekDay']
            mailSubject = campaign['Subject']
            RunTime = campaign['RunTime']
            Attachments = campaign['Attachments']
            
            #print("Frequency, mailbody, MonthlyDate, WeekDay, mailSubject, RunTime, Attachments")
            #print(Frequency, mailbody, MonthlyDate, WeekDay, mailSubject, RunTime, Attachments)

            if Frequency == 'Daily':
                if RunTime == currentTime:
                    sendCampaignToMember(mailSubject, mailbody, allMembersArr, Attachments, camp_id)
                    
            elif Frequency == 'Weekly':
                days = WeekDay.split(",")
                if currentDay in days:
                    sendCampaignToMember(mailSubject, mailbody, allMembersArr, Attachments, camp_id)

            elif Frequency == 'Monthly':
                dates = MonthlyDate.split(",")
                if currentDate in dates:
                    sendCampaignToMember(mailSubject, mailbody, allMembersArr, Attachments, camp_id)

            elif Frequency == 'Once':
                sendCampaignToMember(mailSubject, mailbody, allMembersArr, Attachments, camp_id)

