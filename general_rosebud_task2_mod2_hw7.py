#!/usr/bin/env python3
import sys
import general_rosebud_task2_mod1_hw7 as rose


def testingZip():
    text = open('./barCodeData.txt')
    zips = text.read()
    for i in range(0,21,6):
        rose.printDigit(zips[i:i+5])


# Main Function
def main():
    testingZip()
    return

if __name__ == '__main__':
    #Call Main
    main()

    exit(0)
