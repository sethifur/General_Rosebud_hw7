#!/usr/bin/env python3
'''
tests module one
'''
import sys
import general_rosebud_task1_mod1_hw7 as rose
import csv

def testFun():
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
        print('Reading Record ', row)
        arr[row][9] = arr[row][9].replace(' ','')
        value = rose.getInputOverload(int(arr[row][1]),int(arr[row][2]),int(arr[row][3]),int(arr[row][4]),int(arr[row][5]),int(arr[row][6]),int(arr[row][7]),int(arr[row][8]),arr[row][9])
        rose.checkDoors(value)
        print('\n\n\n')


# Main Function
def main():
    testFun()

if __name__ == '__main__':
    #Call Main
    main()
    exit(0)
