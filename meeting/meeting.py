"""
condense_meeting_times
[(20, 22), (21, 22), (25, 30)] => [[(20,22), (25,30)]]
1472782903 
"""

#contains parse function which is used to parse ISO-8601 strings into datetime
from dateutil.parser import *


#Assigned function
#Determines the format of input, calling the appropriate function.
#Returns what the called function returns.
def condense_meeting_times(times):
    if not type(times) is list:
        return []
    elif not times:
        return []
    elif type(times[0]) is tuple:
        first = times[0]
        if type(first[0]) is str:
            return condense_ISO_8601_timestamps(times)
        elif type(first[0]) is int:
            return condense_simple_or_Unix_timestamps(times)
    else:
        return []
    
    
#Takes in time pair tuples containing ints.
#Returns tuples containing overlapping times combined.
def condense_simple_or_Unix_timestamps(times):
    results = []

    #For each of the tuples
    for time in times:
        added = False

        #If results is emplty add time to it and continue
        if not results:
            results.append(time)
            continue

        #For each item in results
        for result in results:
            #Compare to see if either number in test is between the numbers in
            #results
            if (result[0] <= time[0] <= result[1]
                    or result[0] <= time[1] <= result[1]):
                #If it is combine the tuples and replace the one in results
                results.remove(result)
                result = (min(result[0], time[0]),
                          max(result[1], time[1]))
                results.append(result)
                added = True

        #time has not been combined with an element of results
        #add it to results
        if not added:
            results.append(time)
    
    return results


#Takes in time pair tuples containing ISO-8601 strings.
#Returns tuples containing overlapping times combined.
def condense_ISO_8601_timestamps(times):
    results = []

    #For each of the tuples
    for time in times:
        added = False

        #If results is emplty append time to it and continue
        if not results:
            results.append(time)
            continue

        #For each item in results
        for result in results:
            #Compare to see if either number in test is between the numbers in
            #results.
            if (
                    parse(result[0])
                    <= parse(time[0])
                    <= parse(result[1])
                    or parse(result[0])
                    <= parse(time[1])
                    <= parse(result[1])):
                #If it is combine the tuples and replace the one in results
                results.remove(result)
                result = (min([parse(result[0]), parse(time[0])]).isoformat(),
                          max([parse(result[1]), parse(time[1])]).isoformat())
                results.append(result)
                added = True

        #time has not been combined with an element of results
        #add it to results        
        if not added:
            results.append(time)
            
    return results
