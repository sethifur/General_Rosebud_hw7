#!/usr/bin/env python3
'''
Takes a zip code and changes it into a barcode
'''
import sys


def printDigit(d):
    '''
    Tests the print bar function with preset zipCodes
        Args:
            d is a zipcode
    '''
    print('Enter a zipcode: ',d)
    printBarCode(d)


def printBarCode(zipCode):
    '''
    Finds the offset of a zip code and prints a barcode
    Args:
        zipCode is a five digit string        
    '''

    sm = 0
    barCode = '|'
    convertBar = ['||:::',':::||','::|:|','::||:',':|::|',':|:|:',':||::','|:::|','|::|:','|:|::']
    for i in range(0,5):
        sm += int(zipCode[i])
        barCode += convertBar[int(zipCode[i])]

    sm = 10 - sm % 10 
    if sm == 10:
        sm = 0
    zipCode += str(sm)
    barCode += convertBar[sm]+'|'
    print(barCode)
    



def getInput():
    zipCode = input('Enter a zipcode: ')
    printBarCode(zipCode)



# Main Function
def main():
    getInput()
    return

if __name__ == '__main__':
    #Call Main
    main()

    exit(0)
