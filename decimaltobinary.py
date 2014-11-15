def decimal_to_binary(decimal_number):
    """
    Converts decimal numbers to binary representation 
    """
    
    if decimal_number < 0:
        return 'No decimal representation for negative numbers'

    if decimal_number == 0:
        return ''

    if decimal_number:
        quotient = decimal_number/2
        remainder = decimal_number % 2
        return str(decimal_to_binary(quotient)) + str(remainder)
    else:
        print 'Provide a valid decimal number'

if(__name__=="__main__"):
    print decimal_to_binary(20)
