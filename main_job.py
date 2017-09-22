# -*- coding: utf-8 -*-
tags=[]
with open("tags.txt") as tags_file: #fetch tags from the tags file
    for tag in tags_file.readlines():
        tags.append(tag)

tags=map(lambda x: str(x).strip(),tags)#strip unwanted whitespaces
#%%
from datetime import date
from time import strftime
from datetime import timedelta
import os
from grizzled.os import working_directory

ten_days=timedelta(days=10)#maximum date range to fetch from piconfig
#%%
def comm_file(tag, interval_start,interval_end):#function to create command files for piconfig
    if not os.path.exists(tag):
        os.makedirs(tag)
    
    filename=str(tag)+"_"+interval_start.strftime("%d-%b-%y")+"_"+interval_end.strftime("%d-%b-%y")
    with open(os.path.join(os.getcwd(),tag,filename+str(".txt")),"w") as comm_file:
        comm_file.writelines("@login FTHISTORIAN,pidemo\n")
        comm_file.writelines("@tabl piarc\n")
        comm_file.writelines("@mode list\n")
        comm_file.writelines("@output "+filename+".csv\n")
        comm_file.writelines("@timf9\n")
        comm_file.writelines("@sigd 9\n")
        comm_file.writelines("@istru tag, starttime, endtime, count\n")
        comm_file.writelines("@ostru tag, time, value\n")
        comm_file.writelines("@echo none\n")
        comm_file.writelines("@ostru ...\n")
        comm_file.writelines(str(tag)+","+interval_start.strftime("%d-%b-%y")+","+interval_end.strftime("%d-%b-%y")+", 1400000\n")
        comm_file.writelines("@ends\n")
    return tag,filename

#%%
def piconfig(tag,filename):#function to go in directory and pass arg file to piconfig
    with working_directory(str(os.path.join(os.getcwd(),tag))):
        os.system('piconfig < '+ filename +'.txt')

#%%

start_date=date(day=1,month=1,year=2016)#starting date for fetching data
end_date=date(day=1,month=1,year=2017)#ending date for fetching data

for tag in tags:
    current_date=start_date
    while current_date<end_date:
        interval_start=current_date
        interval_end=0
        if current_date==interval_end:
            interval_start=current_date+timedelta(days=1)    
        
        interval_end=current_date+ten_days
        
        if interval_end>end_date:
            interval_end=end_date
        tag,filename=comm_file(tag, interval_start,interval_end)
        piconfig(tag,filename)
        #os.system('piconfig < '+str(os.path.join(os.getcwd(),tag,filename))+".txt")
        #print("tag_"+interval_start.strftime("%d-%b-%y")+"_"+interval_end.strftime("%d-%b-%y"))
        current_date=interval_end
    

    
