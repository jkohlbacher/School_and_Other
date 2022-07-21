#####################################
#READ FIRST
# A.) change current date 
# B.) api key of account that needs sorting 
# C.) api key of the maturity date custom field 
# D.) change NO DATE stage id
# E.) change Import Stage ID
# F.) change pipeline stage id
# G.) change USER ID
#####################################


#ADD SO THAT IF THERE IS A DEAL WITH A CURRENT DATE DO NOT PUT IT WITH NO DATES

from pipedrive import Pipedrive
import datetime
from dateutil.relativedelta import relativedelta
import time

#0 Change all fields


pipedrive = Pipedrive('') #Enter API key of account that needs the sorting
MD_Custom_Api = ''
Current_date = datetime.datetime.strptime('','%Y-%m-%d')
Import_stage_id = 
NoDateStageID = 
PastDateID = 
UserID =  
PostFundingPipeID = 



global_request_counter = 0

def DealSort(DealID,StageID,DealDate):
    global global_request_counter
    if global_request_counter < 40:
        pipedrive.deals({'id': DealID,'stage_id':StageID,'user_id':UserID},method = 'PUT')
        global_request_counter += 1
    else:
        print('requests rate limit hit - sleeping 2 seconds')
        time.sleep(2)
        global_request_counter = 0
        pipedrive.deals({'id': DealID,'stage_id':StageID,'user_id':UserID},method = 'PUT')
        global_request_counter += 1
    if global_request_counter < 40:
        pipedrive.activities({'due_date':DealDate,'deal_id':DealID,'type':'anniversary_call','user_id':UserID},method = 'POST')
        global_request_counter +=1 
    else:
        print('request rate limit hit - sleeping 2 seconds')
        time.sleep(2)
        global_request_counter = 0
        pipedrive.activities({'due_date':DealDate,'deal_id':DealID,'type':'anniversary_call','user_id':UserID},method = 'POST')
        global_request_counter +=1



stage_id_response = pipedrive.stages({'pipeline_id':PostFundingPipeID},method = 'GET') #MAKE SURE PIPELINE ID IS CORRECT
global_request_counter += 1
stage_id_list = []

for x in range(len(stage_id_response['data'])):
    id = stage_id_response['data'][x]['id']
    stage_id_list.append(id)

on = 1
#1. Get all the deals
while on == 1:
    response = pipedrive.deals({'stage_id':Import_stage_id},method='GET') #MAKE SURE STAGE ID IS CORRECT
    global_request_counter += 1
    if response['data'] == None:
        print('Full Complete')
        break

    print('response recieved')
    print('Got ' + str(len(response['data'])) + ' Deals')

    id_list = []
    Mdate_list = []
    

# Puts the deal id and Mdate into two seperate lists. The order in the lists matters as the first entry into the id_list corresponds to the first entry into Mdate_list
    for x in range(len(response['data'])):
        id = response['data'][x]['id']
        Mdate = response['data'][x][MD_Custom_Api]
        id_list.append(id)
        Mdate_list.append(Mdate)

#Converts the format of the dates in Mdate from a string into a proper datetime object to make it easier to work with
    for x in range(len(Mdate_list)):
        if Mdate_list[x] != '' and Mdate_list[x] != None:
            w = datetime.datetime.strptime(Mdate_list[x],'%Y-%m-%d')
        else:
            w = 0
        Mdate_list[x] = w



#2. Sort through the deals based off the dates



    Y4 = []
    Y4D = []
    Y3 = []
    Y3D = []
    Y2 = []
    Y2D = []
    Y1 = []
    Y1D = []
    D30 = []
    D30D = []
    D90 = []
    D90D = []
    D180 = []
    D180D = []
    NoDate = []
    PastDate = []

    for q in range(len(Mdate_list)):
        Current_id = id_list[q]
        if Mdate_list[q] == 0:
            NoDate.append(Current_id)
        else:
            day = Mdate_list[q] - Current_date
            if day.days > 1460:
                Y4.append(Current_id)
                Y4D.append(Mdate_list[q]- relativedelta(years=4))
            elif day.days > 1095:
                Y3.append(Current_id)
                Y3D.append(Mdate_list[q]- relativedelta(years=3))
            elif day.days > 730:
                Y2.append(Current_id)
                Y2D.append(Mdate_list[q]- relativedelta(years=2))
            elif day.days > 365:
                Y1.append(Current_id)
                Y1D.append(Mdate_list[q]- relativedelta(years=1))
            elif day.days > 180:
                D180.append(Current_id)
                D180D.append(Mdate_list[q]- relativedelta(days=180))
            elif day.days > 90:
                D90.append(Current_id)
                D90D.append(Mdate_list[q]- relativedelta(days=90))
            elif day.days < 0:
                PastDate.append(Current_id)
            else:
                D30.append(Current_id)
                D30D.append(Mdate_list[q]- relativedelta(days=30))

    print('deals sorted')
    print('Y4 is len' + str(len(Y4)))
    print('Y3 is len' + str(len(Y3)))
    print('Y2 is len' + str(len(Y2)))
    print('Y1 is len' + str(len(Y1)))
    print('D180 is len' + str(len(D180)))
    print('D90 is len' + str(len(D90)))
    print('D30 is len' + str(len(D30)))
    print('NoDate is len' + str(len(NoDate)))
    print('PastDate is len' + str(len(PastDate)))

#3. Send the deals back into the correct stage

    for x in range(len(Y4)):
        DealSort(Y4[x],stage_id_list[1],Y4D[x])
    for x in range(len(Y3)):
        DealSort(Y3[x],stage_id_list[2],Y3D[x])
    for x in range(len(Y2)):
        DealSort(Y2[x],stage_id_list[3],Y2D[x])
    for x in range(len(Y1)):
        DealSort(Y1[x],stage_id_list[4],Y1D[x])
    for x in range(len(D180)):
        DealSort(D180[x],stage_id_list[5],D180D[x])
    for x in range(len(D90)):
        DealSort(D90[x],stage_id_list[6],D90D[x])
    for x in range(len(D30)):
        DealSort(D30[x],stage_id_list[7],D30D[x])
    for x in NoDate:
        if global_request_counter < 40:
            pipedrive.deals({'id': x,'stage_id': NoDateStageID,'user_id':UserID},method = 'PUT')
            global_request_counter += 1
        else:
            time.sleep(2)
            print('request rate limit hit - sleeping 2 seconds')
            global_request_counter = 0
            pipedrive.deals({'id': x,'stage_id': NoDateStageID,'user_id':UserID},method = 'PUT')
            global_request_counter += 1
    for x in PastDate:
        if global_request_counter < 40:
            pipedrive.deals({'id': x,'stage_id': PastDateID,'user_id':UserID},method = 'PUT')
            global_request_counter += 1
        else:
            time.sleep(2)
            print('request rate limit hit - sleeping 2 seconds')
            global_request_counter = 0
            pipedrive.deals({'id': x,'stage_id': PastDateID,'user_id':UserID},method = 'PUT')
            global_request_counter += 1
        

    print('completed this set of deals - starting loop again')

