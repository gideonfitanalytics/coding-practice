# sourceFile: determines which file is used
# inputTable: stores the part of the file that still needs to be processed
# oneRow: stores the current row being processed
# finalList: stores the part of the file that has successfully been processed
# nextRow: used to check if any rows are left over
# whileCount: keeps track of the number of rows processed

import os.path

# sourceFile = "testinput.tsv"
# sourceFile = "testinputCell.tsv"
# sourceFile = "testinputRow.tsv"
sourceFile = "testinputColumn.tsv"

if os.path.exists(sourceFile):
    with open(sourceFile, 'r') as f:
        inputTable = f.read()
    print "\nConverting", sourceFile, "...\n"
else:
    raw_input("\nFile Not Found\nPress ENTER to use the sample table: ")
    inputTable = "id\tname\tvalue\n0\tName1\tValue1\n1\tName2\tValue2\n2\tName3\
\tValue3\n3\tName4\tValue4\n4\tName5\tValue5"
    print "\nConverting Sample Table ...\n"

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
