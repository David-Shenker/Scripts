
from time import sleep
from turtle import width
import matplotlib.pyplot as plt
import csv

def showChart():
	x = []
	y = []

	with open('csvFile.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter = ',')

		for row in plots:
			for value in row:
				x.append(row.index(value))
				y.append(int(value))
	plt.xlabel('formulaResult')
	plt.ylabel('Number')
	plt.title('3N+1')
	plt.plot(x, y, color = 'g', linewidth = 0.5)
	plt.show()

def isEven(number: int) -> bool:
    return True if number%2 == 0 else False

def formula(numbersToCheck):
	csvFile = ''
	print('-----------------  START ----------------')
	for currentNumber in range(2, numbersToCheck):
		if currentNumber != 2:
			csvFile += '\n'
		number = currentNumber
		csvFile += str(number)
		# print(f'Running with - {number}')
		while number != 1:
			csvFile += ','
			if isEven(number):
				number = number / 2
			else:
				number = 3 * number + 1

			csvFile += str(number).split('.')[0]
			# print(number)
	# print (csvFile)
	with open('csvFile.csv','w') as csvfile:
		csvfile.write(csvFile)
	print('-----------------  END ----------------')


def main() -> None:
	numbersToCheck = 100
	formula(numbersToCheck)
	showChart()





if __name__ == '__main__':
	main()


