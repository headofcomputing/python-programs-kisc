#ask the user for the length and width of the rectangle
rectangleLength = int(input("What is the length of the rectangle?: "))
rectangleWidth = int(input("What is the width of the rectangle?: "))

#ask the user for the length of the square
squareLength = int(input("What is the length of the square?: "))

#ask the user for the length of the circle
circleRadius = int(input("What is the radius of the circle?: "))

#Calculate the area for each shape
rectangleArea = rectangleLength * rectangleWidth #length * width
squareArea = squareLength * squareLength         #length ^ 2
circleArea = 3.14 * circleRadius * circleRadius  #pi(in this case, 3.14) * radius ^ 2

#Print the area of each shape
print("The area of the rectangle is:", rectangleArea)
print("The area of the square is:", squareArea)
print("The area of the circle is:", circleArea)

