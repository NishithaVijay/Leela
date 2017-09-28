#!/usr/bin/python3
import random #system choose the random numbers
count=0
r=0
while count<=100:
	roll=input("press r to roll the dice") #r is used to roll the dice 
	if roll=="r":
		r=random.randint(1,6) #it gives a radom number between 1 & 6
		count=count+r
		print("your random num is",r)
		print ("your on count",count)
		if count==8:
	       count=37
		print("climbed ladder",count)
	  elif count==40:
           count=68
        print("climbed ladder",count)
      elif count==13:
 		   count=34
 		print("climbed ladder",count)
 	  elif count==52:
           count=81
        print("climbed ladder",count)
      elif count==76:
           count=97
        print("climbed ladder",count)      	
