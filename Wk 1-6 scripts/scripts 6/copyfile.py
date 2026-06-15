sourceName = input("Enter the source file name: ")
targetName = input("Enter the target file name: ")

sourceFile = open(sourceName, "r")
targetFile = open(targetName, "w")

for line in sourceFile:
    targetFile.write(line)

sourceFile.close()
targetFile.close()

print("File copied successfully.")
