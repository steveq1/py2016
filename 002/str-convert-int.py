#!/bin/bash python
import sys

def check_is_negative(listInputValue):
    if listInputValue[0] == '-':
        print ('- number')
        return -1;
    else:
        print ('+ number')
        return 1;
def check_is_decimal(inputValue):

    print( '. number ')

def add(listValue):
    number1 = 0
    number2 = 0
    size = len(listValue)
    index = 0
    valueMap = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    decimalIndex = 0
    for i in listValue:
        if i != '.':
          if decimalIndex == 0:
            number1 = number1 + valueMap[i]*pow(10,size-index-1)
          else:
            number2 = number2 + valueMap[i]*pow(10,-index)
        else:
            decimalIndex = size - index
            index = 1
            continue
        index = index+1
    number = number1 / pow(10,decimalIndex) + number2
#    print decimalIndex
#    print number
    return number
if __name__ == "__main__":
	args = sys.argv
	if len(args) == 1 :
	    print ('args too less ')
	elif len(args) == 2:
	    inputValue = args[1]
	    listInputValue = list(inputValue)
	    listSize = len(listInputValue)
	    negativeTag = check_is_negative(listInputValue)
	    if negativeTag == -1:
	        listInputValue = listInputValue[1:listSize]
	        print (listInputValue)
	    intValue = add(listInputValue)
	    if negativeTag == -1:
	        intValue = intValue * -1
	    print (intValue)
	else :
	    print ('args can not more than 2')


