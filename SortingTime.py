import matplotlib.pyplot as plt
import os
from random import choice
from string import ascii_uppercase
import random
import timeit

# function to calculate sort times
def SortingTimePrint(stringsArray):
	start_time = timeit.default_timer()
	stringsArray.sort()
	elapsed = timeit.default_timer() - start_time
	print "Time Taken",elapsed
        return elapsed
	
#function to store random strings of different sizes
def RandomStringWriting(n):
	target = open("rajitha.txt", 'w')
	for j in range(1,n):
		string=''.join(choice(ascii_uppercase) for i in range(random.randint(1,20)))
		if(j%10==0):
	 		target.write(string+"\n")
		else:
			target.write(string+" ")
        target.close()

#function to plot a graph

def plotGraph(sizeArray,sortTimes):
	plt.plot(sizeArray, sortTimes, linewidth=2.0)
	plt.xlabel('WordsCount', fontsize=18)
	plt.ylabel('SortTime (seconds)', fontsize=16)
	plt.show()
# Reading words from file
def readFromFile():
	array =[]
	with open('rajitha.txt') as f:
		x = f.read()
		array.append(x)
	f.close()
	arrayOfStrings= array[0].split()
	return arrayOfStrings

# Main function

def mainFunction(m):
	n=100 #initial file size
	#Stores File sizes and their corrosponding Sort times
	sortTimes=[] 
	sizeArray=[]
	while(n<m):
		RandomStringWriting(n)
		inputfile=open("rajitha.txt","r")
		#------------------------------
		statinfo = os.stat('rajitha.txt')
		print "Sorted file size : ",statinfo.st_size,"B",n,"Words"
		sizeArray.append(n)
		#------------------------------
		
		arrayOfStrings= readFromFile()
		sortTimes.append(SortingTimePrint(arrayOfStrings))
		arrayofStrings=[]	
		n=int(n*1.2)
	plotGraph(sizeArray,sortTimes)
	
#input here
print "Size vs SortTime"
m=input("Enter Maximum number of words to sort :")
mainFunction(m)



