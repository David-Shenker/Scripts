#!/usr/bin/env python3

import os
import argparse
import string
import random
from time import sleep


# Consts
MAIN_FOLDER_NAME: str = '__linuxCourse__'
WRITE_TO_FILE = 'w'
LOW_PRIVILEGES = '111'
MAX_RANDOM_INT_SIZE: int = 10
FILE_NAME_LENGTH: int = 3
FOLDER_NAME_LENGTH: int = 5
NUMBER_OF_FILES: int = 5
NUMBER_OF_FOLDERS: int = 5
RETRY: int = 5
LARGE: int = 10000
MEDIUM: int = 7000
SMALL: int = 1000
SPACES = '\n!\n!\n'
FINAL_MESSAGE = ['Congratulations', 'You have finnished', 'The official linux course', '#d4v5he']

# Files
README = 'readme'
HIDDEN_README = '.readme'
COPY_THIS_FILE = 'copy.me'
TXT_FILE = 'grate_work_readme.txt'
FIND_ME_PATH = 'DAshe/sheDA'
HIDDEN_CLUES = '.clues'

# Exercises
EX1 = 'exercise_1'
EX2 = 'exercise_2'
EX3 = 'exercise_3'
EX4 = 'exercise_4'
EX5 = 'exercise_5'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trainees', dest='trainees', required=False, default='test')
    parser.add_argument('--mode', dest='mode', required=False, default='readme')
    parser.add_argument('--dest', dest='dest', required=False, default='.')
    return parser.parse_args()


#################################### Exercises ######################################

def initEX1(path: str, traineeName: str) -> str:
    text = f"""\n\n\n
			Hi {traineeName} and welcome to the Linux course!

			This is a basic practical course in Linux.
			You will complete some exercises during this course.

			Let's get started and start with:
			Please go to {EX1} folder and read the {EX1} file

			Best of luck to you! =]


			** You can find {HIDDEN_CLUES} in the {MAIN_FOLDER_NAME} folder **
		\n\n\n"""
    createFile(fileName=README, path=path, content=text)

    createFolder(folderName=EX1, path=path)
    path = f'{path}/{EX1}'

    text = f"""\n\n\n
			In this dir ({EX1}), find a file with the name '{README}'
		\n\n\n"""
    createFile(fileName=EX1, path=path, content=text)

    text = f"""\n\n\n
			Grate work!
			{EX1} completed successfully!
			Please go to {EX2} folder
		\n\n\n"""
    createFile(fileName=HIDDEN_README, path=path, content=text)

    createRandomFiles(NUMBER_OF_FILES, path)

    return path


def initEX2(path: str) -> str:
    createFolder(folderName=f'.{EX2}', path=path)
    path = f'{path}/.{EX2}'

    verifyFolderExists(path=path)
    zipFileExists = int(os.popen(f'ls {path} | grep {EX2} | wc -l').read().strip())
    if zipFileExists == 0:
        text = f"""\n\n\n
				YOU ARE THE BEST!!

				Your next mission is to duplicate the file with the name '{COPY_THIS_FILE}'
				And then, move it to {EX3} folder

				Good luck!
			\n\n\n"""
        createFile(fileName=EX2, path=path, content=text)
        os.popen(f'gzip {path}/{EX2}')

    createFile(fileName=COPY_THIS_FILE, path=path)

    return path


def initEX3(path: str) -> str:
    createFolder(folderName=EX3, path=path)
    path = f'{path}/{EX3}'

    text = f"""\n\n\n
			You are awesome!

			1. Please edit the file, and write you name here: _____.
			2. Edit the name of the file to your own name.
			3. Go to {EX4}

			See you there...
		\n\n\n"""
    createFile(fileName=EX3, path=path, content=text)
    os.popen(f'chmod {LOW_PRIVILEGES} {path}/{EX3}')

    return path


def initEX4(path: str) -> str:
    createFolder(folderName=EX4, path=path)
    path = f'{path}/{EX4}'

    text = f"""\n\n\n
			Under this directory find a file with '.txt' suffix

			clue - use the 'find <path> -name <name>' command
		\n\n\n"""
    createFile(fileName=EX4, path=path, content=text)

    createRandomFiles(numOfFiles=NUMBER_OF_FILES*3, path=path)
    createRandomFolders(numOfFolders=NUMBER_OF_FOLDERS*3, path=path)
    createFolder(folderName=FIND_ME_PATH, path=path)
    path = f'{path}/{FIND_ME_PATH}'
    createFile(fileName=TXT_FILE, path=path)

    return path


def initEX5(path: str) -> str:
    text = f"""\n\n\n
			In the {EX5} file, please find all exclamation marks (!)
		\n\n\n"""
    createFile(fileName=TXT_FILE, path=path, content=text)

    text = f'{getRandomParagraph(size=LARGE)}{SPACES}'
    for word in FINAL_MESSAGE:
        text += f'\n{word}  !\n'
        text += getRandomParagraph(size=MEDIUM)
    text += f'{SPACES}{getRandomParagraph(size=LARGE)}'

    os.popen(f'rm -rf {path}{EX5}')
    createFile(fileName=EX5, path=path, content=text)

    return path


##################################### Utils #########################################

def createCluesFile():
    text = f"""\n\n\n
			Useful Commands:
				cd, ls (ls -la), cat, mv, cp, vim, gzip (gzip -d), chmod, grep, |, find

			{EX1}: cat .{README}
			{EX2}: gzip -d {EX2}.gz ; cat {EX2}
			{EX3}: chmod 777 {EX3} ; vim {EX3}
			{EX4}: find . -name *.txt
			{EX5}: cat {EX5} | grep !
		\n\n\n"""
    createFile(fileName=HIDDEN_CLUES, path=MAIN_FOLDER_NAME, content=text)


def createRandomFiles(numOfFiles: int, path: str) -> None:
    for file in range(numOfFiles):
        fileName = getRandomString(FILE_NAME_LENGTH)
        createFile(fileName, path)


def createRandomFolders(numOfFolders: int, path: str) -> None:
    for folder in range(numOfFolders):
        folderName = getRandomString(FOLDER_NAME_LENGTH)
        createFolder(folderName, path)


def createFile(fileName: str, path: str = '.', content: str = '') -> None:
    try:
        verifyFolderExists(path=path)
        if content:
            with open(f'{path}/{fileName}', WRITE_TO_FILE) as f:
                f.write(content)
        else:
            os.popen(f'touch {path}/{fileName}')
    except FileNotFoundError:
        sleep(2)  # second
        os.popen(f'touch {path}/{fileName}')


def createFolder(folderName: str, path: str = '.') -> None:
    os.popen(f'mkdir -p {path}/{folderName}')


def getRandomString(length: int) -> str:
    letters = string.ascii_letters
    return (''.join(random.choice(letters) for letter in range(length)))


def getRandomInteger() -> int:
    return random.randint(1, MAX_RANDOM_INT_SIZE)


def getRandomParagraph(size: int = 1) -> str:
    return getRandomString(length=getRandomInteger() * size)


def verifyFolderExists(path: str) -> None:
    if 'exist' not in os.popen(f"if test -d {path}; then echo 'exist'; else echo 'false';fi").read():
        sleep(2)  # Wait to folder to init

################################## main functions #################################


def readme():
    print("""\n\n\n
		This script will create a Linux introduction course ('capture the flag').

		Acceptable Flags:
			--mode [readme / create / delete]
				create - Will create a folder for a trainee with the traning
				delete - Will delete a folder of a trainee

			--trainees 'name1,name2,name3...'
	\n\n\n""")


def deleteCourse():
    os.popen(f'rm -rf {MAIN_FOLDER_NAME}')
    print('\n\nAll files were deleted successfully =]\n\n')


def createCourse(count: int = 0):
    try:
        if count < RETRY:
            createFolder(MAIN_FOLDER_NAME)

            createCluesFile()

            traineesList = args['trainees'].split(',')
            for trainee in traineesList:
                print(f'Creating folder for {trainee}')
                createFolder(folderName=trainee, path=MAIN_FOLDER_NAME)
                verifyFolderExists(path=f'{MAIN_FOLDER_NAME}/{trainee}')

                path = f'./{MAIN_FOLDER_NAME}/{trainee}'
                path = initEX1(path, trainee)
                path = initEX2(path)
                path = initEX3(path)
                path = initEX4(path)
                path = initEX5(path)

            print('\n\nDone =]\nWe are ready to go!\n\n')
    except FileNotFoundError:
        count += 1
        print('Failed to init course. Retry...')
        createCourse(count)

################################## main #############################


def main():

    if args['mode'] == 'create':
        createCourse()

    elif args['mode'] == 'delete':
        deleteCourse()

    else:
        readme()


if __name__ == "__main__":
    args = vars(parse_args())
    main()
