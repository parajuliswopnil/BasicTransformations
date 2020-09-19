import pygame
import sys
from pygame.locals import QUIT
import pygame.gfxdraw
import math

pygame.init()

colorBlack = (0, 0, 0)
colorRed = (255, 0, 0)
colorGreen = (0, 255, 0)
colorWhite = (255, 255, 255)

coordinatesOfFigure = []
transformationVector = []
originalFigure = []

figureSides = int(input("Enter the total number of sides of the figure: "))
for i in range(figureSides):
    x1 = int(input("Enter the x coordinate of the side " + str(i) + ": "))
    y1 = int(input("Enter the y coordinate of the side " + str(i) + ": "))
    originalFigure.append((x1, y1))
    coordinatesOfFigure.append([x1, y1, 1])

scalingFactorX = int(input("Enter the scaling factor in x: "))
scalingFactorY = int(input("Enter the scaling factor in y: "))
transformationVector.append((scalingFactorX, 0, 0))
transformationVector.append((0, scalingFactorY, 0))
transformationVector.append((0, 0, 1))

transposedCoordinate = [[0 for i in range(len(coordinatesOfFigure))] for j in range(len(coordinatesOfFigure[0]))]
for i in range(len(coordinatesOfFigure[0])):
    for j in range(len(coordinatesOfFigure)):
        transposedCoordinate[i][j] = coordinatesOfFigure[j][i]

finalTransformedCoordinate = [[0 for i in range(len(transposedCoordinate[0]))] for j in
                              range(len(transformationVector))]

for i in range(len(transformationVector)):
    for j in range(len(transposedCoordinate[0])):
        for k in range(len(transposedCoordinate)):
            finalTransformedCoordinate[i][j] += int(transformationVector[i][k] * transposedCoordinate[k][j])

transposedFinalCoordinate = [[0 for i in range(len(finalTransformedCoordinate))] for j in
                             range(len(finalTransformedCoordinate[0]))]
for i in range(len(finalTransformedCoordinate[0])):
    for j in range(len(finalTransformedCoordinate)):
        transposedFinalCoordinate[i][j] = finalTransformedCoordinate[j][i]

# print(finalTransformedCoordinate)


print(coordinatesOfFigure)
print(transposedCoordinate)
print(finalTransformedCoordinate)
print(transposedFinalCoordinate)

for i in range(len(transposedFinalCoordinate)):
    transposedFinalCoordinate[i].remove(1)

print(transposedFinalCoordinate)

drawingSurface = pygame.display.set_mode((900, 900))
drawingSurface.fill(colorWhite)
pygame.display.set_caption("2D Translation")
pygame.draw.polygon(drawingSurface, colorGreen, transposedFinalCoordinate)
pygame.draw.polygon(drawingSurface, colorRed, originalFigure)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
# print(transformationVector)
