currentIndex = 0
currentToken = ''
fileText = open("fuente.txt", "r").read()
output_file = open("output_file.txt", "w")
errcount = 0

def getToken():
    global currentToken
    global currentIndex
    #print(currentToken)
    if(currentIndex < len(fileText)-1):
        currentToken = fileText[currentIndex]
        currentIndex += 1
        if(currentToken == ' ' or currentToken == '\t'  or currentToken == '\n'):
            getToken()
        return True
    else:
        currentToken = 'eof'
        return False

def tmatch (spectedToken):
    if(not spectedToken == currentToken):
        global errcount
        errcount += 1
        print("error en la posicion:" + str(currentIndex) + ", se esperaba >>" + spectedToken, "y se encontro >> " + currentToken)
    getToken()


def stringrp():
    if (currentToken == '"'):
        tmatch('"')
        output_file.write('STRING ')
    elif (currentToken == 'eof'):
        tmatch('"')
    else:
        getToken()
        stringrp()

def stringr():
    tmatch('"')
    stringrp()

def list():
    if (currentToken == '['):
        output_file.write('L_CORCHETE \n\t')
    tmatch('[')
    if (currentToken == '{'):
        obj()
    elif(currentToken == '{' 
        or currentToken == '[' 
        or currentToken == '"' 
        or currentToken.isnumeric()
        or currentToken == 't'
        or currentToken == 'f'
        or currentToken == 'n'):
        value()
    elif (currentToken == ','):
        output_file.write('COMA \n\t')
        tmatch(',')
        attr()
    if (currentToken == ']'):
        output_file.write('R_CORCHETE\n\t')
    tmatch(']')



def truer():
    if (currentToken == 't'):
        trueString = currentToken
        for number in range(3):
            getToken()
            trueString += currentToken
        if (trueString.lower() == 'true'):
            output_file.write('PR_TRUE ')
            getToken()

def nullr():
    if (currentToken == 'n'):
        nullStr = currentToken
        for number in range(3):
            getToken()
            nullStr += currentToken
            
        if (nullStr.lower() == 'null'):
            output_file.write('PR_NULL ')
            getToken()

def falser():
    if (currentToken == 'f'):
        falseString = currentToken
        for number in range(4):
            getToken()
            falseString += currentToken
        if (falseString.lower() == 'false'):
            output_file.write('PR_FALSE ')
            getToken()

def numberr():
    if (currentToken.isnumeric()):
        getToken()
        numberr()

def value():
    
    if (currentToken == '{'):
        obj()
    elif (currentToken == '['):
        list()
    elif (currentToken == '"'):
        stringr()
    elif (currentToken.lower() == 't'):
        truer()
    elif (currentToken.lower() == 'f'):
        falser()
    elif (currentToken.lower() == 'n'):
        nullr()
    elif (currentToken.isnumeric()):
        output_file.write('NUMBER ')
        numberr()
    else:
        tmatch("{,[,\",true,false")

def attr():
    stringr()
    if (currentToken == ':'):
        output_file.write('DOS_PUNTOS ')
    tmatch(':')
    value()
    if (currentToken == ','):
        output_file.write('COMA \n\t')
        tmatch(',')
        attr()


def obj():
    if (currentToken == '{'):
        output_file.write('L_LLAVE \n\t')
    tmatch('{')
    if (currentToken == '"'):
        output_file.write('STRING')
        attr()
    if (currentToken == '}'):
        output_file.write('R_LLAVE\n')
    tmatch('}')




def json():
    getToken()
    obj()
    if (errcount < 1):
        print("No se han encontrado errores de sintaxis.")
    output_file.close()


def main():
    json()

if __name__ == '__main__':
    main()