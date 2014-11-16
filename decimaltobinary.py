def decimal_to_binary(decimal_number):
    """
    Converts decimal numbers to binary representation. Uses recursion. 
    """
    if decimal_number < 0:
        return 'No decimal representation for negative numbers'
    elif decimal_number == 0:
        return ''

    if decimal_number:
        quotient = decimal_number/2
        remainder = decimal_number % 2
        return str(decimal_to_binary(quotient)) + str(remainder)

if(__name__=="__main__"):
    #1010
    print decimal_to_binary(10)

    #1111
    print decimal_to_binary(15)

    #1100
    print decimal_to_binary(12)

    #10100
    print decimal_to_binary(20)

    #11001
    print decimal_to_binary(25)
