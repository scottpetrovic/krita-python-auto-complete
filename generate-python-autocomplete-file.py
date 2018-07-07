import glob, os, re  #re allows for regular expression patterns

# SETUP
# ---------------------------
# change current directory to the libkis folder in the krita source code
# this is where all the python API files are at that we will read
#os.chdir("C:\\dev\\krita\\libs\\libkis")  # possible Windows OS dir. need to have two "\" symbols
os.chdir("/home/scottpetrovic/krita/src/libs/libkis")




# YOU SHOULDN'T HAVE TO TOUCH ANYTHING BELOW HERE
#----------------------------------------------

# create new file to save to. "w+" means write and create a file. saves in directory specified above
exportFile = open("PyKrita.py", "w+")

# a bit of a readme for what this does
exportFile.write("# Auto-generated file that reads from H files in the libkis folder \n" +
"# The purpose is to use as auto-complete in Python IDEs \n" )


# grab all h files and iterate through them
for file in glob.glob("*.h"):
    currentFile = open(file)


    exportFile.write("\n# auto-generated from: "  +  currentFile.name   +   " \n" )

    allFileLines = currentFile.readlines() # readlines creates a list of the lines
    #exportFile.write(allFileLines[1])

    # find all classes that need to be exported
    classPattern = re.compile("KRITALIBKIS_EXPORT")

    lineWithClassFile = -1 # used later to also help with finding class comments

    # in a .h file, this will grab what class things are a part of
    for i, line in enumerate(allFileLines):

        for match in re.finditer(classPattern, line):

            lineWithClassFile = i

            # first order of business is to get the class name from the file
            # currently only one class per file, so this will probably
            # break if there are more
            bracesPrecursor = ""

            # sometimes braces are cuddled and have stuff in it

            if len(allFileLines[i]) <= 2:
                lineWithClassFile = lineWithClassFile - 1

            bracesPrecursor = allFileLines[lineWithClassFile]
            className = bracesPrecursor.split(' ')[2]

            # start getting the format ready for the class
            exportFile.write("class " + className + ":\n")




    # now let's find the comments that exist for the class and append it to the botom
    #after we find the lines that have the class comments, we can concatenate the lines and clean them up

    # we are now checking the next 3 lines above to see if there are comments for the class
    # if there aren't don't try to grab the comments later
    classCommentsEnd = -1
    if "*/" in allFileLines[lineWithClassFile]:
        classCommentsEnd = lineWithClassFile;

    if "*/" in allFileLines[lineWithClassFile - 1]:
            classCommentsEnd = lineWithClassFile - 1;

    if "*/" in allFileLines[lineWithClassFile - 2]:
        classCommentsEnd = lineWithClassFile - 2;


    # if we see some comments for the class, so try to read them...
    if classCommentsEnd != -1:

        classCommentsStartIndex = -1

        for a in range(classCommentsEnd, 0, -1 ) :   #go in decreasing order
            if "/*" in allFileLines[a]:
                classCommentsStartIndex = a
                break


        if classCommentsStartIndex != -1:
            classCommentsStart = classCommentsStartIndex + 1
            classCommentsOutput = "" # concatenate everything in here for the comments

            for x in range (classCommentsStart, classCommentsEnd ):
                classCommentsOutput +=  allFileLines[x].strip() + "\n   "

            classCommentsOutput = classCommentsOutput.replace("*", "")
        else:
            classCommentsOutput = "Trouble Parsing class comments"
    else:
        classCommentsOutput = "Class not documented"



    exportFile.write("    \"\"\"" +  classCommentsOutput   +  "    \"\"\""  +   "\n\n")





    # 2nd thing to do.....find the functions for the class
    # find all the functions and output them.
    # need to add some spaces for proper indenting
    # this just looks for things that have () and

    #we save the line of the previous function to get exactly range between signatures of the methods
    previousFunctionLineNumber = -1

    fnPattern = re.compile("\(.*\)")
    for j, line in enumerate(allFileLines):

        line  = line.strip() # strip white beginning and trailing white space

        for match in re.finditer(fnPattern, line):
            if line.strip()[0][0] != "*": # this means it is part of a comments

                #these aren't functions we can call

                if "Q_" not in line and "~" not in line and "operator" not in line:

                    # if we made it this far that means we are a valid function
                    # now we need to figure out how to parse this and format it for python
                    isVirtual = False
                    returnType = "void"
                    isExplicit = False

                    functionLineNumber = j
                    functionList = line.split("(")[0]
                    functionList = functionList.replace("*", "").replace("const", "").replace(" >", ">")

                    if "virtual" in functionList:
                        isVirtual = True
                        functionList = functionList.split("virtual")[1]

                    if "explicit" in functionList:
                        isExplicit = True
                        functionList = functionList.split("explicit")[1]


                    functionList = functionList.strip() # extra spaces at the beginning need to be removed

                    #first word is usually the return type
                    if " " in functionList:
                        returnType = functionList.split(' ')[0]
                        functionList = functionList.split(' ')[1]


                    # save off the parameters elsewhere as we have to parse each differently
                    # we need to clean it up a bit since it is loose and doesn't need variable names and types. we will just keep the types
                    paramsList = "(" + line.split("(")[1]
                    paramsList = paramsList.replace("const", "").replace("&", "").replace("*", "").replace(";", "") # remove const stuff
                    paramsList = paramsList.replace("(", "").replace(")", "").strip()

                    # clean up parameters with multiple
                    if "," in paramsList:

                        multipleParamsList = []

                        # break it apart and clear everything after the first word
                        for p in paramsList.split(","):
                            multipleParamsList.append(p.strip().split(" ")[0])

                        paramsList = ",".join(multipleParamsList )

                    elif paramsList != "":
                        paramsList = paramsList.strip().split(" ")[0]
                        #Only one parameter. remove everything after the first word

                    exportFile.write("    def " + functionList + "(" + paramsList + "):" "\n")





                    # now let's figure out what comments we have. we figured out the return type above. but we need to scrape the h file for comments
                    #functionLineNumber
                    functionCommentsEnd = functionLineNumber - 1;
                    functionCommentsStartIndex = previousFunctionLineNumber

                    for b in range(functionCommentsEnd, functionCommentsStartIndex+1, -1 ) :   #go in decreasing order
                        if "/*" in allFileLines[b]:
                            functionCommentsStartIndex = b
                            break

                    if functionCommentsStartIndex != -1:
                        classCommentsStart = classCommentsStartIndex +1 # first line just has "/*", so we can skip that

                        functionCommentsOutput = "" # concatenate everything in here for the comments
                        for x in range (functionCommentsStartIndex, functionCommentsEnd ):
                            functionCommentsOutput +=  allFileLines[x].strip()

                            functionCommentsOutput = functionCommentsOutput.replace("*", "").replace("/ ", "")
                    else:
                        functionCommentsOutput = "Missing function documentation"


                    # finally export the final file
                    exportFile.write("        \"\"\"Return Type: " + returnType + "\n        " + functionCommentsOutput + "\"\"\" \n\n" )




    # file is done. add some spacing for readability
    exportFile.write("\n")

    # close the file that we are done with it
    currentFile.close()

exportFile.close()
