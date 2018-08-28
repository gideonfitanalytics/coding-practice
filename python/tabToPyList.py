# sourceFile: determines which file is used
# inputTable: stores the part of the file that still needs to be processed
# oneRow: stores the current row being processed
# finalList: stores the part of the file that has successfully been processed
# nextRow: used to check if any rows are left over
# whileCount: keeps track of the number of rows processed

import fileFinder

sourceFile = "testinput.tsv"
# sourceFile = "testinputCell.tsv"
# sourceFile = "testinputRow.tsv"
# sourceFile = "testinputColumn.tsv"
fileFound = 0
fileFound = fileFinder.findFile(sourceFile, fileFound)
if fileFound == 1:
    with open(sourceFile, 'r') as f:
        inputTable = f.read()
    print "Original Table\n", inputTable
    whileCount = 0
    if '\n' in inputTable:
        oneRow = inputTable.split('\n', 1)[0]
        inputTable = inputTable.split('\n', 1)[1]
        oneRow = oneRow.split('\t')
        oneRow = [oneRow]
        finalList = oneRow
        nextRow = 1
        while nextRow == 1:
            if '\n' in inputTable:
                oneRow = inputTable.split('\n')[0]
                inputTable = inputTable.split('\n', 1)[1]
                oneRow = oneRow.split('\t')
                finalList.append(oneRow)
            else:
                oneRow = inputTable.split('\t')
                if inputTable != "":
                    finalList.append(oneRow)
                nextRow = 0
            whileCount += 1
        print "Converted:\n", finalList
    else:
        inputTable = inputTable.split('\t')
        print inputTable
    print "\n---\n"
    if whileCount == 1:
        print "Completed one l" + u"\u00F6" + u"\u00F6" + "p!"
    elif whileCount <= 0:
        print "No l" + u"\u00F6" + u"\u00F6" + "ps for you!"
    else:
        print "Completed", whileCount, "l" + u"\u00F6" + u"\u00F6" + "ps!"
    print "\n---\n"
else:
    raw_input("Press ENTER to close")
