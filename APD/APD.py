def PushOrPop(state,ch,stack,APD):
    if not stack:
        end = 0
        return(state,end)
    end = 0
    inStack = stack.pop()
    if ch not in APD[state].keys():
        end = 1
        return(state,end)
    else:
        if inStack not in APD[state][ch].keys():
            end = 1
            return(state,end)
        else:
            if APD[state][ch][inStack][0] == 'push':
                stack.append(inStack)
                stack.append(ch)
                end = 0
            else:
                if APD[state][ch][inStack][0] =='continue':
                    stack.append(inStack)
                    if len(APD[state][ch][inStack]) == 2:
                        if APD[state][ch][inStack][1]== 'pop':
                            stack.pop()
                            end = 0
                    if state == '0':
                        state = '1'
                        end = 0
                    else:
                        if state == '1':
                            state = '2'
                            end = 0
                else:
                    if APD[state][ch][inStack][0] == 'pop':
                        end = 0
                        return(state,end)
                    else:
                        if APD[state][ch][inStack][0] == 'end':
                            end = 1
    return (state,end)

def isWordAccepted(word, APD,symbols):
    state = '0'
    stack = ['z0']
    end = 0
    for ch in word:
        if ch not in symbols:
            print("Character not in symbols!!")
            break
        else:
            state,end = PushOrPop(state,ch,stack,APD)

    if end == 1 and not stack:
        print("Word accepted!")
    else:
        print("Word not accepted!")

def readFile(fileName):
    f = open(fileName,"r")
    lines = f.readlines()
    lines = [line.strip("\n") for line in lines]
    nrOfStates = lines[0]
    nrOfSymbols = lines[1]
    symbols = lines[2]
    symbols = symbols.split(" ")
    nrOfTransitions = lines[3]
    APD = {}
    linesTrans = [line.split() for line in lines[4:]]
    for line in linesTrans:
        if line[0] not in APD.keys():
            APD[line[0]] = {}
            if line[1] not in APD[line[0]].keys():
                APD[line[0]][line[1]] = {}
                if line[2] not in APD[line[0]][line[1]].keys():
                    APD[line[0]][line[1]][line[2]] = []
                    APD[line[0]][line[1]][line[2]].append(line[3])

                else:
                    APD[line[0]][line[1]][line[2]].append(line[3])
            else:
                if line[2] not in APD[line[0]][line[1]].keys():
                    APD[line[0]][line[1]][line[2]] = []
                    APD[line[0]][line[1]][line[2]].append(line[3])
                else:
                    APD[line[0]][line[1]][line[2]].append(line[3])
        else:
            if line[1] not in APD[line[0]].keys():
                APD[line[0]][line[1]] = {}
                if line[2] not in APD[line[0]][line[1]].keys():
                    APD[line[0]][line[1]][line[2]] = []
                    APD[line[0]][line[1]][line[2]].append(line[3])
                else:
                    APD[line[0]][line[1]][line[2]].append(line[3])
            else:
                if line[2] not in APD[line[0]][line[1]].keys():
                    APD[line[0]][line[1]][line[2]] = []
                    APD[line[0]][line[1]][line[2]].append(line[3])
                else:
                    APD[line[0]][line[1]][line[2]].append(line[3])

    word = '001c100&'
    isWordAccepted(word,APD,symbols)


def main():
    readFile("date.in")
if __name__ == "__main__":
    main()