from optparse import OptionParser
import random

TEST_IIN = '514728'

decimal_decoder = lambda s: int(s, 10)
decimal_encoder = lambda i: str(i)

def luhn_sum_mod_base(string, base=10, decoder=decimal_decoder):
    # Adapted from http://en.wikipedia.org/wiki/Luhn_algorithm
    digits = map(decoder, string)
    return (sum(digits[::-2]) +
        sum(map(lambda d: sum(divmod(2*d, base)), digits[-2::-2]))) % base

#Copied from Baluhn
def generate(string, base=10, encoder=decimal_encoder,
    decoder=decimal_decoder):
    """
    Calculates the Luhn mod N check character for the given input string. This
    character should be appended to the input string to produce a valid Luhn
    mod N string in the given base.
    
    >>> value = '4205092350249'
    >>> generate(value)
    '1'
    
    When operating in a base other than decimal, encoder and decoder callables
    should be supplied. The encoder should take a single argument, an integer,
    and return the character corresponsing to that integer in the operating
    base. Conversely, the decoder should take a string containing a single
    character and return its integer value in the operating base. Note that
    the mapping between values and characters defined by the encoder and
    decoder should be one-to-one.
    
    For example, when working in hexadecimal:
    
    >>> hex_alphabet = '0123456789abcdef'
    >>> hex_encoder = lambda i: hex_alphabet[i]
    >>> hex_decoder = lambda s: hex_alphabet.index(s)
    >>> value = 'a8b56f'
    >>> generate(value, base=16, encoder=hex_encoder, decoder=hex_decoder)
    'b'
    >>> verify('a8b56fb', base=16, decoder=hex_decoder)
    True
    >>> verify('a8b56fc', base=16, decoder=hex_decoder)
    False
    
    """
    
    d = luhn_sum_mod_base(string+encoder(0), base=base, decoder=decoder)
    if d != 0:
        d = base - d
    return encoder(d)

def generate_random_number_as_strina(length_random=9):
    """
    Generates a random string with 9 digits
    """
    rand = []
    for i in xrange(0, length_random):
        random_int = random.randint(0, 9)
        rand.append(random_int)

    ret_val = ''.join(str(x) for x in rand)

    return ret_val

def generate_card_numbers(number_of_cards=1):
    """
    Generates a random card number that passes the Luhn check algorithm. Generates one card number if no arguments passed.
    The first six digits of a card number (including the initial MII digit) are known as the issuer identification number (IIN). 
    These identify the institution that issued the card to the card holder. The rest of the number is allocated by the issuer.
    The card number is 16 digits long. We already have the TEST_IIN which is 6 digits long and we need to generate a random
    number that is 9 digits long. That makes 15 digits. The last remaining digit is generated using the luhn check.
    Why re-invent the when when baluhn already did this:-
    https://github.com/benhodgson/baluhn - truly open source
    """
    card_numbers = []

    for i in range(0, number_of_cards): #No xrange in Python3
        random_num_nine_digit = generate_random_number_as_strina()
        partial_card_num = TEST_IIN + random_num_nine_digit
        check_digit = generate(partial_card_num)
        card_numbers.append(partial_card_num + check_digit)

    return card_numbers

if __name__ == "__main__":
    parser = OptionParser(usage="python scripts/%prog -n <number_cards>")
    parser.add_option("-n", action="store", dest="num_cards", default=False, help='Number of card numbers to generate.')

    options = parser.parse_args()[0]

    #Generate one card number
    card_numbers = generate_card_numbers()

    print card_numbers

    #Generate 10 card numbers
    card_numbers = generate_card_numbers(int(options.num_cards))
    
    #The generated card numbers above could be verified here:-http://www.freeformatter.com/credit-card-number-generator-validator.html

    print card_numbers

