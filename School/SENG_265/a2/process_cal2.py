#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Josh Kohlbacher
SENG 265 A2

I copy pasted the parse_xml file because it was included so I figured it was fair use. 
"""

from posixpath import split
import sys
import re
import datetime as dt

def parse_xml(filename,no_atr):
    # define the collections to be used
    broadcasters_list = []
    filtered_lines = []
    # read the file line by line
    with open(filename) as file:
        for line in file:
            # use regular expressions to collect relevant data
            line = re.findall(r'<(.*?)>(.*?)</\1>', line)
    #         # only include tags with information
            if len(line) > 0:
                filtered_lines.append(line[0])
    broadcaster_dic = {}
    # create the dictionaries
    for i in range(len(filtered_lines)):
        tup = filtered_lines[i]
        broadcaster_dic[tup[0]] = tup[1]
        # separate the information for each broadcaster
        if (i+1)%no_atr == 0 and i>0:
            broadcasters_list.append(broadcaster_dic)
            broadcaster_dic = {}
    # print the list of dictionaries
    return(broadcasters_list)

def removesemicolon(list_of_dict,key_value):
    
    for y in list_of_dict:
        splitter = y[key_value]
        splitter = splitter.replace(':','')
        y[key_value] = splitter


def addsemicolon(t):
    return t[:2] + ':' + t[2:]

def splitbroadcaster(t):
    return t.split(",")


def main():

    #get sys arguments
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    event_file = sys.argv[3]
    circuits_file = sys.argv[4]
    broad_file = sys.argv[5]

    #get the correct dates and filenames
    start_date = start_date.replace("--start=","",1)
    end_date = end_date.replace("--end=","",1)
    event_file = event_file.replace("--events=","",1)
    circuits_file = circuits_file.replace("--circuits=","",1)
    broad_file = broad_file.replace("--broadcasters=","",1)
    
    #remove the / from the input dates
    end_date = end_date.split('/')
    start_date = start_date.split('/')

    #use the provided parse_xml method to convert the input files into lists of dictionaries
    event_list = parse_xml(event_file,9)
    circuit_list = parse_xml(circuits_file,5)
    broad_list = parse_xml(broad_file,3)

    
   #get all events within the date range given in the input
    sorted_event_list = []
    
    for x in event_list:
        if int(x['year']) >= int(start_date[0]) and int(x['year']) <= int(end_date[0]):
            if int(x['month']) > int(start_date[1]) and int(x['month']) < int(end_date[1]):
                sorted_event_list.append(x)
            elif (int(x['month']) == int(start_date[1]) and int(x['day']) >= int(start_date[2])) or (int(x['month']) == int(end_date[1]) and int(x['day']) <= int(end_date[2])):
                sorted_event_list.append(x)

    #simple method to temporarily remove the : in the time eg 09:30 -> 0930 to make it easier to work with
    removesemicolon(sorted_event_list,"start")
    removesemicolon(sorted_event_list,"end")

    #this sorted + lamda function line will sort the event list so that the earliest dates appear first in the list 
    sorted_event_list = sorted(sorted_event_list,key = lambda z: (int(z['month']),int(z['day']),int(z['start'])))
    
    #open and create the output.yaml file 
    f = open("output.yaml","w")

    # begin writing to the output file
    f.write('events:\n')

    #make sure the sorted event list is not empty
    if len(sorted_event_list) != 0:
        for x in range(len(sorted_event_list)):
            #print the date header, automatically prints the first date at x = 0 and for future events checks if its date matches the last event printed, if not then print a new date header
            if x == 0 or (sorted_event_list[x]['year'] != sorted_event_list[x-1]['year'] or sorted_event_list[x]['month'] != sorted_event_list[x-1]['month'] or sorted_event_list[x]['day'] != sorted_event_list[x-1]['day']):
                f.write("  - %s-%s-%s:\n" % (sorted_event_list[x]['day'],sorted_event_list[x]['month'],sorted_event_list[x]['year']))
            
            f.write("    - id: %s\n" % (sorted_event_list[x]['id']))
            f.write("      description: %s\n"%(sorted_event_list[x]['description']))

            #this creates a list of the circuits with an id that matches the location value in the event list
            circuit_filter = list(filter(lambda i: i['id'] == sorted_event_list[x]['location'],circuit_list))

            f.write("      circuit: %s (%s)\n"%(circuit_filter[0]['name'],circuit_filter[0]['direction']))
            f.write("      location: %s\n"%(circuit_filter[0]['location']))
            
            #create datetime objects so that printing the required fields becomes much easier
            event_obj1 = dt.datetime(int(sorted_event_list[x]['year']),int(sorted_event_list[x]['month']),int(sorted_event_list[x]['day']))
            event_obj2 = dt.datetime(int(sorted_event_list[x]['year']),int(sorted_event_list[x]['month']),int(sorted_event_list[x]['day']))
            start_obj = dt.datetime.strptime(sorted_event_list[x]['start'],"%H%M").time()
            end_obj = dt.datetime.strptime(sorted_event_list[x]['end'],"%H%M").time()
            combined_obj_start1 = dt.datetime.combine(event_obj1, start_obj)
            combined_obj_start2 = dt.datetime.combine(event_obj2, end_obj)

            f.write("      when: %s %s - %s %s %s, %s %s, %s (%s)\n"%(combined_obj_start1.strftime("%I:%M"),combined_obj_start1.strftime("%p"),combined_obj_start2.strftime("%I:%M"),combined_obj_start2.strftime("%p"),combined_obj_start1.strftime("%A"),combined_obj_start1.strftime("%B"),combined_obj_start1.strftime("%d"),combined_obj_start1.strftime("%Y"),circuit_filter[0]['timezone']))
            f.write("      broadcasters:\n")
            
            #simple method to turn the value in broadcaster from one string 'B01,B02,B03' into a list  
            sorted_event_list[x]['broadcaster'] = splitbroadcaster(sorted_event_list[x]['broadcaster'])
            
            #gets all the required broadcasters for the event and returns them as list of list of dict, eg -> [[{dict:info}],[{dict:info}]]
            broad_filter = []
            for y in range(len(sorted_event_list[x]['broadcaster'])):
                broad_filter.append(list(filter(lambda i: i['id'] == sorted_event_list[x]['broadcaster'][y],broad_list))) 

            #iterate through the list of required broadcasters and print the name while being careful not to end the file with \n
            y = 0
            while y < len(broad_filter):
                f.write("        - %s"%(broad_filter[y][0]["name"]))
                if x+1 != len(sorted_event_list):
                    f.write("\n")
                else:
                    if y+1 != len(broad_filter):
                        f.write("\n")
                y+=1

    #close the file and finished
    f.close()


if __name__ == '__main__':
    main()
