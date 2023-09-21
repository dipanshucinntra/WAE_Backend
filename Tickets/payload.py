{
    "DeliveryID": 2,
    "AssignTo": 1,
    "CreatedBy": 1,
    "Type": "Installation",
    "Title": "Test Ticket",
    "BpCardCode": 2,
    "ContactName": "Abhi",
    "ContactPhone": "9871271138",
    "ContactEmail": "abhi@gmail.com",
    "ContactAddress": "test delhi",
    "ProductSerialNo": "1234567890",
    "ProductName": "test",
    "ProductCategory": "110",
    "ProductModelNo": "12312",
    "Zone": "North West",
    "Priority": "Standerd",
    "Status": "New",
    "Description": "test",
    "DurationOfService": "NA",
    "SignatureStatus": "",
    "WarrantyDueDate": "19-15-2022",
    "AMCDueDate": "19-15-2022",
    "CMCDueDate": "19-15-2022",
    "WarrantyStartDate": "9/16/2022",
    "WarrantyDueDate": "9/16/2022",
    "ExtWarrantyStartDate": "9/16/2022",
    "ExtWarrantyDueDate": "9/16/2022",
    "AMCStartDate": "9/16/2022",
    "AMCDueDate": "9/16/2022",
    "CMCStartDate": "9/16/2022",
    "CMCDueDate": "9/16/2022",
    "ManufacturingDate": "9/16/2022",
    "ExpiryDate": "9/16/2022",
    "CreateDate": "9-15-2022",
    "ClosedDate": "9-15-2022",
    "DueDate": "9-15-2022"
}



# assign ticket
{
    "TicketId": 1,
    "EmployeeId": 2
}

# history
{
    "id":1,
    "TicketId": 2,
    "Type": "New",
    "Remarks": "hwloo hs hasdasdsass test"
}

# Conversation
{
    "TicketId_id": 2,
    "OwnerId": 2,
    "OwnerType": "Employee",
    "Message": "Hello Sir",
    "Type": "Private/Public"
}

# equipments parts
{
    "TicketId": 2,
    "OwnerId": 2,
    "ItemCode": '006010000',
    "ItemQty": 1,
    "Comments": "Test",
    "Status": "Delivered",
    "BillToAddress": "Test Address",
    "Discount": "NA"
}
[
    {
        "TicketId": 1,
        "OwnerId": 2,
        "ItemCode": "006010000",
        "ItemQty": 1,
        "Comments": "Test",
        "BillToAddress": "Test Address"
    },
    {
        "TicketId": 1,
        "OwnerId": 2,
        "ItemCode": "006010000",
        "ItemQty": 1,
        "Comments": "Test",
        "BillToAddress": "Test Address"
    }
]

#service check list 
{
    "TicketId": 2,
    "TaskId": 1,
    "Comment": "Hi There",
    "Status": "Open",
    "Duration": "NA"
}


# INSERT INTO `Tickets_status`(`Status`) VALUES ("New"),("Assigned"),("In Progress"),("Pending"),("Resolved");
# INSERT INTO `Tickets_ticketstatus`(`TicketStatus`) VALUES ("Pending"),("Accepted"),("Rejected");
# INSERT INTO `Tickets_type`(`Type`) VALUES ("Installation"),("Maintenance"),("Complaints");
# INSERT INTO `Tickets_zone`(`Zone`) VALUES ("North"),("East"),("West"),("South");
# INSERT INTO `Tickets_priority`(`Priority`) VALUES ("Low"),("Medium"),("High");