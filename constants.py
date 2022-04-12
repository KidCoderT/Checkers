import pygame

width, height = 720, 720

cell_width = width / 8
cell_height = height / 8

clock = pygame.time.Clock()

movement_offsets = (7, -7, 9, -9)

numSquaresToEdge = []

# Precomput the data
for file in range(8):
    for rank in range(8):
        numNorth = 7 - rank
        numSouth = rank
        numWest = file
        numEast = 7 - file

        # index = 8 * rank + file

        numSquaresToEdge.append(
            [
                min(numNorth, numWest),
                min(numSouth, numEast),
                min(numNorth, numEast),
                min(numSouth, numWest),
            ]
        )
