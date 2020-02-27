"""
MORSE CODE TRANSLATOR

The syntax is written in Python 3.7.

Warning: The syntax will create three new files if the print statements are
uncommented.

Code can be run 
-in IDE where the main() function will also be processed.
or 
-in cmd (python.exe) by writing 'import morse_code' followed by 
'morse_code.function_name', where function_name can be 
eg. morse_code.toMorse("hello").
"""

morse_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}



def toMorse(message):
    """
    This function takes in a string of text and outputs its morse equivalent
    It cannot take other characters than alphanumerical.
    """
    if not isinstance(message, str):
        raise TypeError("Message has to be a string!")
    if not message.replace(" ","").isalnum():
        raise ValueError("Message in string can only contain the letters of the alphabet!")
  
    message = message.lower().split()
    code = ""
    for words in message:
        for letter in words:
            code += morse_dict.get(letter) + " "
        code += " "
    return code


def toText(code):
    """
    This function takes a Morse code, consisting of '.' and '-' and outputs
    it as a text. Separation between letters is one space ' ' and between words,
    two spaces '  '. If an unidentified symbol is read, it outputs 
    '{Unidentified Symbol}' for that symbol.
    """
    inv_morse = {v: k for k, v in morse_dict.items()}
    words = code.split("  ") # Separates code into intended words
    #code = code.split() # Separates each snippet into letters
    message = ""
    for word in words:
        letters = word.split()
        for sym in letters:
            if inv_morse.get(sym) == None:
                message += "{Unidentified Symbol}"
            else:
                message += inv_morse.get(sym)
        message += " "
    return message


def messageToMorseFile(message, file):
    """Function allowes user to directly write an alphanumeric message, which
    convers into Morse code before it is saved to a file of choice."""
    text_file = open(str(file)+".txt","wt")
    text_file.write(toMorse(message))
    text_file.close()
    
def messageFileToMorseFile(message_file, morse_file):
    """Function allowes user to load an alphanumeric message in a file, which
    convers into Morse code before it is saved to a file of choice."""
    
    input_file = open(str(message_file)+".txt","r")
    output_file = open(str(morse_file)+".txt","w")
    with input_file as text:
        message = text.read().replace('\n', ' ')
    
    output_file.write(toMorse(message))
    input_file.close()
    output_file.close()
    
def morseFileToMessageFile(morse_file, message_file):
    """Function allowes user to load a Morse code message in a file, which
    convers into text before it is saved to a file of choice."""
    
    input_file = open(str(morse_file)+".txt","r")
    output_file = open(str(message_file)+".txt","w")
    with input_file as code:
        morseCode = code.read()#.replace('\n', '')
    
    output_file.write(toText(morseCode))
    input_file.close()
    output_file.close()
    
        
print("\n\t", 21*"_", "\n\t MORSE CODE TRANSLATOR\n\t", 21*"_",
    "\nFunctions: \n-'toMorse(message)'\n-'toText(code)'\n-'messageToMorseFile(message, morseFile)'",
    "\n-'messageFileToMorseFile(messageFile, morseFile)'\n-'morseFileToMessageFile(morseFile, messageFile)'\n",
    "*** All inputs have to be in string format***\n", "If not in IDE, write 'import morse_code' followed\n by 'morse_code.toMorse('hello')' for example.\n\t", 21*"_","\n\n")

def main():

    message = "Hello this is now in morse code 1 2 339"
    print("\nExamples:\n")
    print("* Message: \n", message)
    print("* Message in Morse Code: \n", toMorse(message))
    print("* Message from Morse Code: \n", toText(toMorse(message)))
    print("* Testing function handling w/ unidentified symbols: \n",toText(".... .-.... .-.. .-.. ---"))
    
    # Will create file with the message 'Hello World' translated into Morse code
    messageToMorseFile("Hello World","morse")
    
    # Uncomment this and write something in a .txt file, then insert its name
    # in 'messageFile1'. This will generate a file with its Morse equivalent
    # and a new file with the translated Morse file to text again, to see how it worked.
    messageFileToMorseFile("messageFile1", "morseFile")
    morseFileToMessageFile("morseFile", "messageFile2")

if __name__ == '__main__':
    main()
