import argparse
#Caesar cipher
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet_shift = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Adjust alphabet shift according to given number
def shift(number):
    while number > 0:
        place_holder = alphabet_shift[0]
        alphabet_shift.pop(0)
        alphabet_shift.append(place_holder)
        number -= 1
        
  

def change_char(phrase_list):
    output_list = []
    print("Your input phrase is: {}".format(phrase_list))
    for i in range(len(phrase_list)):
        for n in range(len(alphabet)):
            if phrase_list[i].isupper():
                if phrase_list[i] == alphabet[n].upper():
                    output_list.append(alphabet_shift[n].upper())
            else:
                if phrase_list[i] == alphabet[n]:
                    output_list.append(alphabet_shift[n])
            

    return print("Your output is: {}".format(output_list))
        


def main():

    #Adding a parser
    descStr = "This program performs a simple Caeser Cypher shift"
    parser = argparse.ArgumentParser(description=descStr)
    #Expected arguments
    parser.add_argument('--string', dest='phrase', required=True)
    parser.add_argument('--shift', dest='shift_number', required=True)
    parser.add_argument('--show-output', dest='show_output', required=False)
    
    #Parsing the args
    args = parser.parse_args()
    
    phrase = str(args.phrase)
    shift_number = int(args.shift_number)
    
    shift(shift_number)
    phrase_list = list(phrase.strip())

    if args.show_output:
        print("Your given phrase list is: {}".format(phrase_list))
        print("The alphabet shift is: {}".format(alphabet_shift))


    change_char(phrase_list)

if __name__ == '__main__':
    main()