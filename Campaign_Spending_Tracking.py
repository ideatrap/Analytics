import csv
from datetime import date
import datetime
import re


rows =[]

AID = set()
DollarSoFar = dict()
Born = dict()
CampaignSoFar = dict()
LastCampaign = dict()
strheading = str()
strrow = str()
DateMap = dict()
SpendMap = dict()




with open('AID_CID.csv', 'rU') as f:
    reader = csv.reader(f, delimiter=',')
# read in the csv file
    headings = next(reader)
    for row in reader:
        rows.append(row)
        if row[0]== '':
            pass
            # if the string is empty, don't operate
        elif(row[0] in AID):
            # has been logged before
            AID.add(row[0])

            basedate = date(int(row[4]),1,1)
            thisCampaign = basedate + datetime.timedelta(weeks=int(row[5]))
            CampaignSoFar[row[0]].add(row[3])
            
            
            
            DollarSoFar[row[0]] = float(row[6][1:].replace(",",""))+DollarSoFar[row[0]]
            
            if thisCampaign > LastCampaign[row[0]]:
                LastCampaign[row[0]] = thisCampaign
                
            
        else:
            #first time appear
            AID.add(row[0])
            basedate = date(int(row[4]),1,1)
            #print basedate
            
            #initialize a set and pass in the first CID
            dummy = set()
            dummy.add(row[3])
            CampaignSoFar[row[0]] = dummy

            DollarSoFar[row[0]] = float(row[6][1:].replace(',',''))
            Born[row[0]] = basedate + datetime.timedelta(weeks=int(row[5]))
            LastCampaign[row[0]] = basedate + datetime.timedelta(weeks=int(row[5]))
            
            ## buid tree on which date spend on how much - date is a list, spending is dict

#Output, write down the AD Profile

OutFile = open('AIDprofile_current.txt','w')
OutFile.write("AID|Born|SpendSoFar|#CIDSoFar|LastCampaign\n")

OutFileFull = open('AID_CID_$.txt','w')

# print out items in the list
for x in headings:
    strheading = strheading + x +"|"
    
OutFileFull.write(strheading + "|SpendByDate\n")

AIDlist = list(AID)
#set cannot be iterated, change set to a list

for aid in AIDlist:
    # bornOut = str(Born[aid].year)+"-"+str(Born[aid].month)+"-"+str(Born[aid].day)
    bornOut = str(Born[aid])
    SpendOut = str(DollarSoFar[aid])
    CIDOut = str(len(CampaignSoFar[aid]))
    lastCampaignOut = str(LastCampaign[aid])

    OutFile.write(aid+'|'+bornOut+'|'+SpendOut+'|'+CIDOut+'|'+lastCampaignOut+'\n')


print "======printing header==========="
print headings
#print rows
## sdfdsf 



#reference: 
# set: https://docs.python.org/2/library/sets.html
# dictionary: https://docs.python.org/2/library/stdtypes.html#typesmapping