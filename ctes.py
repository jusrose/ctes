info = """
disclaimer: I am not resposible for illegal use of this product.
this program is meant for educational purpouses only.
what you do with this program is solely your responsibility.
version: 0.0.1
welcome to the custom text encryption system
illegal use might but is not limited to encrypted transmission over airwaves
"""
print(info)

#main class
class CryptControl:
    #class init method
    def __init__(self, keya="12345", keyb="abcdef", keyc="zyxwvut"):
        #import the key to the class and parse it
        self.ka = keya #table key 5 chars long
        self.kb = keyb #column key 6 chars long
        self.kc = keyc #row key 7 chars long
        #check key validity
        self.checkKeys()
        #translation dict variable
        self.translation = {
            "a": "{}{}{}".format(self.ka[0], self.kb[0], self.kc[0]),
            "e": "{}{}{}".format(self.ka[0], self.kb[1], self.kc[0]),
            "i": "{}{}{}".format(self.ka[0], self.kb[2], self.kc[0]),
            "o": "{}{}{}".format(self.ka[0], self.kb[0], self.kc[1]),
            "u": "{}{}{}".format(self.ka[0], self.kb[1], self.kc[1]),
            "y": "{}{}{}".format(self.ka[0], self.kb[2], self.kc[1]),
            "A": "{}{}{}".format(self.ka[1], self.kb[0], self.kc[0]),
            "E": "{}{}{}".format(self.ka[1], self.kb[1], self.kc[0]),
            "I": "{}{}{}".format(self.ka[1], self.kb[2], self.kc[0]),
            "U": "{}{}{}".format(self.ka[1], self.kb[0], self.kc[1]),
            "O": "{}{}{}".format(self.ka[1], self.kb[1], self.kc[1]),
            "Y": "{}{}{}".format(self.ka[1], self.kb[2], self.kc[1]),
            "b": "{}{}{}".format(self.ka[2], self.kb[0], self.kc[0]),
            "c": "{}{}{}".format(self.ka[2], self.kb[1], self.kc[0]),
            "d": "{}{}{}".format(self.ka[2], self.kb[2], self.kc[0]),
            "f": "{}{}{}".format(self.ka[2], self.kb[3], self.kc[0]),
            "g": "{}{}{}".format(self.ka[2], self.kb[4], self.kc[0]),
            "h": "{}{}{}".format(self.ka[2], self.kb[0], self.kc[1]),
            "j": "{}{}{}".format(self.ka[2], self.kb[1], self.kc[1]),
            "k": "{}{}{}".format(self.ka[2], self.kb[2], self.kc[1]),
            "l": "{}{}{}".format(self.ka[2], self.kb[3], self.kc[1]),
            "m": "{}{}{}".format(self.ka[2], self.kb[4], self.kc[1]),
            "n": "{}{}{}".format(self.ka[2], self.kb[0], self.kc[2]),
            "p": "{}{}{}".format(self.ka[2], self.kb[1], self.kc[2]),
            "q": "{}{}{}".format(self.ka[2], self.kb[2], self.kc[2]),
            "r": "{}{}{}".format(self.ka[2], self.kb[3], self.kc[2]),
            "s": "{}{}{}".format(self.ka[2], self.kb[4], self.kc[2]),
            "t": "{}{}{}".format(self.ka[2], self.kb[0], self.kc[3]),
            "v": "{}{}{}".format(self.ka[2], self.kb[1], self.kc[3]),
            "w": "{}{}{}".format(self.ka[2], self.kb[2], self.kc[3]),
            "x": "{}{}{}".format(self.ka[2], self.kb[3], self.kc[3]),
            "z": "{}{}{}".format(self.ka[2], self.kb[4], self.kc[3]),
            "B": "{}{}{}".format(self.ka[3], self.kb[0], self.kc[0]),
            "C": "{}{}{}".format(self.ka[3], self.kb[1], self.kc[0]),
            "D": "{}{}{}".format(self.ka[3], self.kb[2], self.kc[0]),
            "F": "{}{}{}".format(self.ka[3], self.kb[3], self.kc[0]),
            "G": "{}{}{}".format(self.ka[3], self.kb[4], self.kc[0]),
            "H": "{}{}{}".format(self.ka[3], self.kb[0], self.kc[1]),
            "J": "{}{}{}".format(self.ka[3], self.kb[1], self.kc[1]),
            "K": "{}{}{}".format(self.ka[3], self.kb[2], self.kc[1]),
            "L": "{}{}{}".format(self.ka[3], self.kb[3], self.kc[1]),
            "M": "{}{}{}".format(self.ka[3], self.kb[4], self.kc[1]),
            "N": "{}{}{}".format(self.ka[3], self.kb[0], self.kc[2]),
            "P": "{}{}{}".format(self.ka[3], self.kb[1], self.kc[2]),
            "Q": "{}{}{}".format(self.ka[3], self.kb[2], self.kc[2]),
            "R": "{}{}{}".format(self.ka[3], self.kb[3], self.kc[2]),
            "S": "{}{}{}".format(self.ka[3], self.kb[4], self.kc[2]),
            "T": "{}{}{}".format(self.ka[3], self.kb[0], self.kc[3]),
            "V": "{}{}{}".format(self.ka[3], self.kb[1], self.kc[3]),
            "W": "{}{}{}".format(self.ka[3], self.kb[2], self.kc[3]),
            "X": "{}{}{}".format(self.ka[3], self.kb[3], self.kc[3]),
            "Z": "{}{}{}".format(self.ka[3], self.kb[4], self.kc[3]),
            "0": "{}{}{}".format(self.ka[4], self.kb[0], self.kc[0]),
            "1": "{}{}{}".format(self.ka[4], self.kb[1], self.kc[0]),
            "2": "{}{}{}".format(self.ka[4], self.kb[2], self.kc[0]),
            "3": "{}{}{}".format(self.ka[4], self.kb[3], self.kc[0]),
            "4": "{}{}{}".format(self.ka[4], self.kb[4], self.kc[0]),
            "5": "{}{}{}".format(self.ka[4], self.kb[5], self.kc[0]),
            "6": "{}{}{}".format(self.ka[4], self.kb[0], self.kc[1]),
            "7": "{}{}{}".format(self.ka[4], self.kb[1], self.kc[1]),
            "8": "{}{}{}".format(self.ka[4], self.kb[2], self.kc[1]),
            "9": "{}{}{}".format(self.ka[4], self.kb[3], self.kc[1]),
            "`": "{}{}{}".format(self.ka[4], self.kb[4], self.kc[1]),
            "-": "{}{}{}".format(self.ka[4], self.kb[5], self.kc[1]),
            "=": "{}{}{}".format(self.ka[4], self.kb[0], self.kc[2]),
            "[": "{}{}{}".format(self.ka[4], self.kb[1], self.kc[2]),
            "]": "{}{}{}".format(self.ka[4], self.kb[2], self.kc[2]),
            "\\":"{}{}{}".format(self.ka[4], self.kb[3], self.kc[2]),
            ";": "{}{}{}".format(self.ka[4], self.kb[4], self.kc[2]),
            "'": "{}{}{}".format(self.ka[4], self.kb[5], self.kc[2]),
            ",": "{}{}{}".format(self.ka[4], self.kb[0], self.kc[3]),
            ".": "{}{}{}".format(self.ka[4], self.kb[1], self.kc[3]),
            "/": "{}{}{}".format(self.ka[4], self.kb[2], self.kc[3]),
            "~": "{}{}{}".format(self.ka[4], self.kb[3], self.kc[3]),
            "_": "{}{}{}".format(self.ka[4], self.kb[4], self.kc[3]),
            "{": "{}{}{}".format(self.ka[4], self.kb[5], self.kc[3]),
            "}": "{}{}{}".format(self.ka[4], self.kb[0], self.kc[4]),
            "|": "{}{}{}".format(self.ka[4], self.kb[1], self.kc[4]),
            ":": "{}{}{}".format(self.ka[4], self.kb[2], self.kc[4]),
            "\"":"{}{}{}".format(self.ka[4], self.kb[3], self.kc[4]),
            "<": "{}{}{}".format(self.ka[4], self.kb[4], self.kc[4]),
            ">": "{}{}{}".format(self.ka[4], self.kb[5], self.kc[4]),
            "?": "{}{}{}".format(self.ka[4], self.kb[0], self.kc[5]),
            "!": "{}{}{}".format(self.ka[4], self.kb[1], self.kc[5]),
            "@": "{}{}{}".format(self.ka[4], self.kb[2], self.kc[5]),
            "#": "{}{}{}".format(self.ka[4], self.kb[3], self.kc[5]),
            "$": "{}{}{}".format(self.ka[4], self.kb[4], self.kc[5]),
            "%": "{}{}{}".format(self.ka[4], self.kb[5], self.kc[5]),
            "^": "{}{}{}".format(self.ka[4], self.kb[0], self.kc[6]),
            "&": "{}{}{}".format(self.ka[4], self.kb[1], self.kc[6]),
            "*": "{}{}{}".format(self.ka[4], self.kb[2], self.kc[6]),
            "(": "{}{}{}".format(self.ka[4], self.kb[3], self.kc[6]),
            ")": "{}{}{}".format(self.ka[4], self.kb[4], self.kc[6]),
            "+": "{}{}{}".format(self.ka[4], self.kb[5], self.kc[6]),
        }
    #key checker function
    def checkKeys(self):
        if len(self.ka) == 5 and len(self.kb) == 6 and len(self.kc) == 7:
            used = []
            for c in self.ka:
                if c not in used:
                    used.append(c)
                else:
                    raise ValueError("Key A has duplicates")
            used = []
            for c in self.kb:
                if c not in used:
                    used.append(c)
                else:
                    raise ValueError("Key B has duplicates")
            used = []
            for c in self.kc:
                if c not in used:
                    used.append(c)
                else:
                    raise ValueError("Key C has duplicates")
            return
        raise ValueError("A keys length was invalid")
    #encryption method
    def encrypt(self, text="hello_world"):
        #predefine the output as empty string
        newText = ""
        #parse throughthe old text and using translation var translate it to the new text
        for i in text:
            newText = newText + "{}".format(self.translation[i])
        #return the new text
        return newText
    #decryption method
    def decrypt(self, text="4ay1bz3dy3dy1ay5ew4cw1ay3dx3dy3cz5bu"):
        #sets text to lowercase
        text = text.lower()
        #predefines the necessary vars
        textCode = []#result predefinition
        tempText = ""#temperary string
        count = 0#counter from 0 - 2 to keep track of where we are
        #parses text and seperates into 3 chars per string sets
        #and adding it to a var textCode that was prdefined
        for i in text:
            if count == 0:
                tempText = i
                count = count +1
            elif count == 1:
                tempText = tempText + i
                count = count +1
            elif count == 2:
                tempText = tempText + i
                textCode.append(tempText)
                count = 0
        #predefines output as empty string
        newText = ""
        #translates each 3 char string into the output
        for i in textCode:
            for k, v in self.translation.items():
                if v == i:
                    newText = newText + k
                    break
        #returns the output
        return newText

if __name__ == "__main__":
    
    def genCrypt():
        print("enter a 5 character long string with no duplicates")
        ka = input(">>>_")
        print("enter a 6 character long string with no duplicates")
        kb = input(">>>_")
        print("enter a 7 character long string with no duplicates")
        kc = input(">>>_")
        try:
            crypt = CryptControl(ka, kb, kc)
        except ValueError:
            print("failed to generate crypt, did you use duplicates or the right number of characters?")
            return genCrypt()
        return crypt
    
    def main():
        crypt = genCrypt()
        while True:
            m = input("1 for cnahge keys, 2 for encrypt, 3 for decrypt, 4 to quit\n>>>_")
            if m == "1":
                crypt = genCrypt()
            elif m == "2":
                try:
                    print(crypt.encrypt(input("what do you want encrypt:")))
                except:
                    print("error encrypting")
            elif m == "3":
                try:
                    print(crypt.decrypt(input("what is the enrypte text to decrypt")))
                except:
                    print("error decrypting")
            elif m == "4":
                quit()
            else:
                print("invalid input try again")
    
    main()