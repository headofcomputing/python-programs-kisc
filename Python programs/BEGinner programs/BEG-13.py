#ask the user for value of distance
distanceKM = int(input("How many kilometers would you like to convert?: "))

#convert kilometer into meter, centimeter and millimeter
distanceM = distanceKM * 1000
distanceCM = distanceM * 100
distanceMM = distanceCM * 10

#Also ask the user for value of memory
memoryGB = int(input("How much in GB would you like to convert?: "))

#convert gigabyte into megabyte, kilobyte and bytes
memoryMB = memoryGB * 1024
memoryKB = memoryMB * 102.4
memoryB = memoryKB * 1024

#print converted values of distance
print(distanceKM, "KMs is equal to", distanceM,"m")
print(distanceKM, "KMs is equal to", distanceCM,"cm")
print(distanceKM, "KMs is equal to", distanceMM,"mm")

#optional
print("\n")

#print converted values of memory
print(memoryGB, "GBs is equal to", memoryMB, "MB")
print(memoryGB, "GBs is equal to", memoryKB, "KB")
print(memoryGB, "GBs is equal to", memoryB, "B")


