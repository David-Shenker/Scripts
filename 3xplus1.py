import matplotlib.pyplot as plt

# Consts
GREEN = 'g'

def showChart(CSVFile):
	x = []
	y = []

	for numbersList in CSVFile:
		for number in numbersList:
			x.append(numbersList.index(number))
			y.append(int(number))

	plt.xlabel('formulaResult')
	plt.ylabel('Number')
	plt.title('3N+1')
	plt.plot(x, y, color = GREEN, linewidth = 0.5)
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

def createCSV(numbersToCheck):
	return map(lambda number: formula(number), range(2, numbersToCheck))

def main() -> None:
	print('-----------------  START ----------------')
	numbersToCheck = 100
	CSVFile = createCSV(numbersToCheck)
	showChart(CSVFile)
	print('-----------------  END ----------------')


if __name__ == '__main__':
	main()


