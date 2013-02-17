def decimal_to_binary(decimal_number=None, ret_val=None):
  """Converts decimal numbers to binary representation """
	if(decimal_number is not None):
		quotient = decimal_number/2
		remainder = decimal_number % 2
		ret_val.append(remainder)
		if(quotient >= 2):
			decimal_to_binary(quotient, ret_val)
		else:
			retval_size = len(ret_val)
			ret_val.append(quotient)
	return ret_val


if(__name__=="__main__"):
	l=list()
	ret_val = decimal_to_binary(10, l)
	print ret_val[::-1]
