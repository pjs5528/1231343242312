#!/usr/bin/python

"""

File:        cmpsc443-ids.py
Descruption: This is the implementation of the 443 IDS system.
Author:      Patrick Sweeney
Date:        12/02/2018

"""

# Import statements 
import csv
import matplotlib.pyplot as plt
import numpy as np

# Global data
ids_training_data = []
class algorithm:
	def __init__(self):
		self.fp = 0.0
		self.tp = 0.0
		self.fn = 0.0
		self.tn = 0.0
		self.fpList = []
		self.tpList = []

# Read the training and test data
def readIDSData():

	# Variables
	global ids_training_data

	# Read the training data file
	fdesc = open("cmpsc443-ids-training.csv", "rt")
	datreader = csv.reader(fdesc, delimiter=',')
	for row in datreader:
		ids_training_data.append( [int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])] )


# Now compute the IDS performance
def testIDSsystem():

	# Variables
	global ids_training_data
	All = algorithm()
	Not_f0 = algorithm()
	Not_f1 = algorithm()
	Not_f2 = algorithm()
	Not_f3 = algorithm()
	Not_f4 = algorithm()

	# DO STUFF
	for i in range(500):
		All.tp = 0.0
		All.fp = 0.0
		All.tn = 0.0
		All.fn = 0.0

		Not_f0.tp = 0.0
		Not_f0.fp = 0.0
		Not_f0.tn = 0.0
		Not_f0.fn = 0.0
		
		Not_f1.tp = 0.0
		Not_f1.fp = 0.0
		Not_f1.tn = 0.0
		Not_f1.fn = 0.0

		Not_f2.tp = 0.0
		Not_f2.fp = 0.0
		Not_f2.tn = 0.0
		Not_f2.fn = 0.0

		Not_f3.tp = 0.0
		Not_f3.fp = 0.0
		Not_f3.tn = 0.0
		Not_f3.fn = 0.0

		Not_f4.tp = 0.0
		Not_f4.fp = 0.0
		Not_f4.tn = 0.0
		Not_f4.fn = 0.0

		for row in ids_training_data:
			if ((row[0] + row[1] + row[2] + row[3] + row[4]) <= i):
				if (row[5] == 0):
					All.fp += 1
				else:
					All.tp += 1

			else:
				if (row[5] == 0):
					All.tn += 1
				else:
					All.fn += 1
			
			if ((row[1] + row[2] + row[3] + row[4]) <= i):
				if (row[5] == 0):
					Not_f0.fp += 1
				else:
					Not_f0.tp += 1

			else:
				if (row[5] == 0):
					Not_f0.tn += 1
				else:
					Not_f0.fn += 1
			
			if ((row[0] + row[2] + row[3] + row[4]) <= i):
				if (row[5] == 0):
					Not_f1.fp += 1
				else:
					Not_f1.tp += 1

			else:
				if (row[5] == 0):
					Not_f1.tn += 1
				else:
					Not_f1.fn += 1

			if ((row[0] + row[1] + row[3] + row[4]) <= i):
				if (row[5] == 0):
					Not_f2.fp += 1
				else:
					Not_f2.tp += 1

			else:
				if (row[5] == 0):
					Not_f2.tn += 1
				else:
					Not_f2.fn += 1

			if ((row[0] + row[1] + row[2] + row[4]) <= i):
				if (row[5] == 0):
					Not_f3.fp += 1
				else:
					Not_f3.tp += 1

			else:
				if (row[5] == 0):
					Not_f3.tn += 1
				else:
					Not_f3.fn += 1

			if ((row[0] + row[1] + row[2] + row[3]) <= i):
				if (row[5] == 0):
					Not_f4.fp += 1
				else:
					Not_f4.tp += 1

			else:
				if (row[5] == 0):
					Not_f4.tn += 1
				else:
					Not_f4.fn += 1

		All.tpList.append(100 - (All.tp * 100.0) / (All.tp + All.fn))
		All.fpList.append(100 - (All.fp * 100.0) / (All.fp + All.tn))
		Not_f0.tpList.append(100 - (Not_f0.tp * 100.0) / (Not_f0.tp + Not_f0.fn))
		Not_f0.fpList.append(100 - (Not_f0.fp * 100.0) / (Not_f0.fp + Not_f0.tn))
		Not_f1.tpList.append(100 - (Not_f1.tp * 100.0) / (Not_f1.tp + Not_f1.fn))
		Not_f1.fpList.append(100 - (Not_f1.fp * 100.0) / (Not_f1.fp + Not_f1.tn))
		Not_f2.tpList.append(100 - (Not_f2.tp * 100.0) / (Not_f2.tp + Not_f2.fn))
		Not_f2.fpList.append(100 - (Not_f2.fp * 100.0) / (Not_f2.fp + Not_f2.tn))
		Not_f3.tpList.append(100 - (Not_f3.tp * 100.0) / (Not_f3.tp + Not_f3.fn))
		Not_f3.fpList.append(100 - (Not_f3.fp * 100.0) / (Not_f3.fp + Not_f3.tn))
		Not_f4.tpList.append(100 - (Not_f4.tp * 100.0) / (Not_f4.tp + Not_f4.fn))
		Not_f4.fpList.append(100 - (Not_f4.fp * 100.0) / (Not_f4.fp + Not_f4.tn))		

			

	# Setup the plot
	fig, ax = plt.subplots()
	ax.set(xlabel = 'False Positives', ylabel = 'Detection Rate',
		title = 'ROC Curve')
	ax.grid()
	ax.plot(All.fpList, All.tpList, '.-', label = 'All')
	ax.plot(Not_f0.fpList, Not_f0.tpList, '.-', label = 'Not_f0')
	ax.plot(Not_f1.fpList, Not_f1.tpList, '.-', label = 'Not_f1')
	ax.plot(Not_f2.fpList, Not_f2.tpList, '.-', label = 'Not_f2')
	ax.plot(Not_f3.fpList, Not_f3.tpList, '.-', label = 'Not_f3')
	ax.plot(Not_f4.fpList, Not_f4.tpList, '.-', label = 'Not_f4')
	ax.legend(loc = 'lower right')
	fig.tight_layout()



	# DO MORE STUFF
	fig.savefig('cmpsc443-ids-output.pdf')

# Main function
def main():
        readIDSData()
        testIDSsystem()

if __name__ == '__main__':
    main()
