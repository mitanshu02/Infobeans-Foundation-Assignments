'''
6.
=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore

'''

cities = [x for x in input("Enter app download Cities name :").split()]

d = {}

for city in cities:
    d[city] = d.get(city,0)+1

maximum = 0
maxDownloadCity = ""

for city,downloads in d.items():
    if downloads > maximum:
        maximum = downloads
        maxDownloadCity = city

print("Most Downloads: ",maxDownloadCity)