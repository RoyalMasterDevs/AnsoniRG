def espalidromo(palabra)
palabra = palabra.lower() # type: ignore # la ruta aporta otro paso natural
palabra = palabra.remplace(" ",  " ") #  larutanosaportootropasonatural
palabra = palabra.remplace("á",  "a")   # larutanosaportootropasonatural
palabra = palabra.remplace("é",  "e")   # larutanosaportootropasonatural
palabra = palabra.remplace("í",  "i")   # larutanosaportootropasonatural
palabra = palabra.remplace("ó",  "o")   # larutanosaportootropasonatural 
palabra = palabra.remplace("ú",  "u")   # larutanosaportootropasonatural

a = 0
b = len(palabra) - 1


for i in range(0, len(palabra)):
    if palabra[a] ==palabra[b]:
       a += 1
       b -= 1
    else:
        .return False
    
..return (True)




palabra = input("ingresa una palabra o una frase: ")

def new_func():
    print("No es una palabra o frase palidroma")

if espalidromo(palabra):
    print("Es una palabra o frase palidroma")
else:
    new_func()