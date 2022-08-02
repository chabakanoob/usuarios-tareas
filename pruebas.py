wordd = "shark"

#cesar con aritmetica modular
def encriptador(word,key):
    
    word = word.upper()

    #con ascii
    new_word = ""
    for letter in word:
        if letter.isalpha():
            print(letter)

            posicion = ord(letter) + key

            if posicion > ord("Z"):

                diferencia = posicion % ord("Z")

                new_word += chr(ord("A")+diferencia-1)
                continue
            
            new_word +=chr(posicion)

        else:
            new_word+=letter
    
    return new_word

print(encriptador("yyy",2))

wordd +="sss"
print(wordd)
