numeros = "13 9 3 8 5 12 7 1 20 1 15"
letras = ""

if(numeros.__contains__("13")):
    letras += "M"
    if(numeros.__contains__("9")):
        letras += "I"
        if(numeros.__contains__("3")):
            letras += "C"
            if(numeros.__contains__("8")):
                letras += "H"
                if(numeros.__contains__("5")):
                    letras += "E"
                    if(numeros.__contains__("12")):
                        letras += "L"
                        if(numeros.__contains__("7")):
                            letras += "G"
                            if(numeros.__contains__("1")):
                                letras += "A"
                                if(numeros.__contains__("20")):
                                    letras += "T"
                                    if(numeros.__contains__("1")):
                                        letras += "A"
                                        if(numeros.__contains__("15")):
                                            letras += "O"

print(letras)

