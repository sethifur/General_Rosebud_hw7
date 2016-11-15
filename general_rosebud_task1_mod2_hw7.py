#!/usr/bin/env python3
'''
tests module one
'''
import sys
import general_rosebud_task1_mod1_hw7 as rose
import csv

def importData():
    '''
    Imports data to test module one
    Args:
        i is the name of the file
    '''
    fileToRead = open('./minivanData.csv')
    csvArray = csv.reader(fileToRead)
    arr = []
    for row in csvArray:
        arr.append(row)
    for row in range(1,6):
        print('Reading Record ', arr[row][0])
        rose.checkDoors(rose.getInputOverload(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])



# Main Function
def main():
    importData()

if __name__ == '__main__':
    #Call Main
    main()
    exit(0)
