import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
from time import time

# Consts
GREEN = 'g'
START = 'start'
END = 'end'

def showChart(CSVFile):
	x = []
	y = []

	for numbersList in CSVFile:
		for number in numbersList:
			x.append(numbersList.index(number))
			y.append(int(number))

	plt.xlabel('formulaResult')
	plt.ylabel('Number')
	plt.title(f'3N+1 for - {USER_INP}')
	plt.plot(x, y, color = GREEN, linewidth = 0.5)

	runTime(END)
	plt.show()

def isEven(number: int) -> bool:
    return True if number%2 == 0 else False

def formula(number: str) -> list:
	resultList = []

	while number != 1:
		if isEven(number):
			number = number / 2
		else:
			number = 3 * number + 1

		resultList.append(number)

	return resultList

def createCSV(numbersToCheck) -> list:
	return map(lambda number: formula(number), range(2, numbersToCheck))

def getUsersInput() -> int:
	ROOT = tk.Tk()
	ROOT.withdraw()
	global USER_INP
	USER_INP = simpledialog.askinteger(title="3N+1 Simulator",
										prompt="Please choose number to run with:")

	print(f'Claculating for {USER_INP} numbers')
	return USER_INP

def runTime(action: str) -> None:
	if action == START:
		global startTime
		startTime = time()
	elif action == END:
		endTime = time()
		print (f'Run Time = {endTime - startTime} seconds')

def main() -> None:
	print('-----------------  START ----------------')
	numbersToCheck = getUsersInput()
	runTime(START)
	CSVFile = createCSV(numbersToCheck)
	showChart(CSVFile)
	print('-----------------  END -----------------')


if __name__ == '__main__':
	main()


