currentIndex = 0
currentToken = ''
fileText = open("fuente.txt", "r").read()
output_file = open("output_file.txt", "w")
def getToken():
    global currentToken
    global currentIndex
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
        print("error en la posicion:" + str(currentIndex) + ",se esperaba:" + spectedToken, "y se encontró:" + currentToken)
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
    else:
        attr()

    tmatch(']')
    if (currentToken == ']'):
        output_file.write('L_CORCHETE\n\t')


def truer():
    if (currentToken == 't'):
        trueString = currentToken
        for number in range(3):
            getToken()
            trueString += currentToken
        if (trueString.lower() == 'true'):
            output_file.write('PR_TRUE ')
            getToken()

def falser():
    if (currentToken == 'f'):
        trueString = currentToken
        for number in range(4):
            getToken()
            trueString += currentToken
        if (trueString.lower() == 'false'):
            output_file.write('PR_FALSE ')
            getToken()

def numberr():
    if (currentToken.isnumeric()):
        getToken()
        numberr()
    else:
        value()

def value():
    if (currentToken == '{'):
        obj()
    elif (currentToken == '['):
        list()
    elif (currentToken == '"'):
        stringr()
    elif (currentToken == 't'):
        truer()
    elif (currentToken == 'f'):
        falser() 
    elif (currentToken.isnumeric()):
        output_file.write('NUMBER ')
        numberr()
    elif (currentToken == ','):
        output_file.write('COMA \n\t')
        tmatch(',')
        value()
    else:
        tmatch('inicio de un valor: ({,[,",true, false, number o una coma)')

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
    attr()
    if (currentToken == '}'):
        output_file.write('R_LLAVE\n')
    tmatch('}')
    if (currentToken == ','):
        output_file.write('COMA \n\t')
        tmatch(',')
        obj()



def json():
    getToken()
    obj()
    output_file.close()


def main():
    json()

if __name__ == '__main__':
    main()