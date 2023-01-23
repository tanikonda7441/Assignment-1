#Program to sort ages, find max , min, median, average,range of ages

import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print('Ages : ', ages)
ages.sort()                                          #sorting ages
print('Sorted ages:', ages)

minimum = min(ages)                                  #finding min of ages
print('The minimum age is', minimum)

maximum=max(ages)                                    #finding max of ages
print('The maximum age is', maximum)

add= minimum + maximum                               #addition of max and min of ages
print('Addition of min and max age is', add)

median=statistics.median(ages)                       #median of ages
print('Median of ages is', median)

mean=statistics.mean(ages)                           #average of ages
print('Average of ages is', mean)

range=maximum-minimum                                #range of ages
print('Range of ages $is', range)
