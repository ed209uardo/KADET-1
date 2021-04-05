#!/usr/bin/env python
import os
import sys
# importing Criteria importing model for Criteria
from criteria.models import Criteria
from useraccess.models import SchedulerUser


def main():
    all_Criteria = Criteria.objects.all() 
    all_Users = SchedulerUser.objects.all()
    checkResidentAvailability(all_Criteria, all_Users)



def checkResidentAvailability(Criteria, Users):
    #not sure how to import criteria
    
    for criterion in Criteria:
        int numWeek = getWeek(criterion)

        int pgy = criterion.ResidentYear #not sure how to get this but should be accessible

        int eligibleResidents = 0

        int residentsNeeded = criterion.MinResident #not sure how to get this

        #not sure how to import residents
        for resident in residents:
            content = resident.weeks[numWeek]
            if content != "BLACKOUT" and resident.pgy == pgy: #not sure how to get resident.pgy
                eligibleResidents++

            if eligibleResidents >= residentsNeeded:
                break
        
        if eligibleResidents < residentsNeeded:
            #alert user here that we don't have enough residents
            break

def getWeek(Criteria):
    #assume that every criterion and the schedule itself starts on monday
    startDate = criterion.StartRotation

    scheduleStart = schedule.StartDate #not sure how to get starting date of schedule model

    #the idea is that both of these variables should be DateTimeField objects and we should be able to get the difference in days
    #this syntax is a compelte guess from internet searches
    delta = datetime.datetime.strptime(scheduleStart, datetimeFormat) - datetime.datetime.strptime(startDate, datetimeFormat)
    delta = delta.days

    weeks = delta / 7
    return weeks

def algorithm():
    #very tentative
    #currently this creates a table of all eligible residents per week
    #however, i noticed that this is really similar to checkResidentAvailability
    #it's possible that we can combine this with cehckResidentAvailability to make the table the first time around
    #still not sure exactly what tricks we can do with this table

    eligibleTotal = [] #this will be a 2darray

    for i in range(criteria.length): #length is a bit of a guess here, acting like criteria is an array 
        criterion = criteria[i]

        int numWeek = getWeek(criterion)

        int pgy = criterion.ResidentYear

        for resident in residents:
            content = resident.weeks[numWeek]

            eligibleWeek = []

            if content != "BLACKBOUT" and resident.pgy == pgy:
                eligibleWeek.append(resident)

        eligibleTotal.append(eligibleWeek)

        