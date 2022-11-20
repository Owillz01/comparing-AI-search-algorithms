import pygame, sys, random
from pygame.locals import *

class DrawBoard:
    TILESIZE = 80
    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    FPS = 30
    BLANK = None

    #                 R    G    B
    BLACK =         (  0,   0,   0)
    WHITE =         (255, 255, 255)
    BRIGHTBLUE =    (  0,  50, 255)
    DARKTURQUOISE = (  3,  54,  73)
    GREEN =         (  0, 204,   0)

    BGCOLOR = DARKTURQUOISE
    TILECOLOR = GREEN
    TEXTCOLOR = WHITE
    BORDERCOLOR = BRIGHTBLUE
    BASICFONTSIZE = 20

    
    BUTTONCOLOR = WHITE
    BUTTONTEXTCOLOR = BLACK
    MESSAGECOLOR = WHITE

    XMARGIN = 0
    YMARGIN = 0

    

    def __init__(self, dimension, _board ):
        print(_board, "_board")
        self.BOARDWIDTH = dimension
        self.BOARDHEIGHT = dimension
        self.board = _board
        self.XMARGIN = int((self.WINDOWWIDTH - (self.TILESIZE * dimension + (dimension - 1))) / 2)
        self.YMARGIN = int((self.WINDOWHEIGHT - (self.TILESIZE * dimension + (dimension - 1))) / 2)
        self.main()

    def main(self):
        global FPSCLOCK, DISPLAYSURF, BASICFONT
        # , RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption('Slide Puzzle')
        BASICFONT = pygame.font.Font('freesansbold.ttf', self.BASICFONTSIZE)
        while True:
            self.drawBoard()
            pygame.display.update()
            FPSCLOCK.tick(self.FPS)

    def drawBoard(self):
        DISPLAYSURF.fill(self.BGCOLOR)
        # if message:
        #     textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
        #     DISPLAYSURF.blit(textSurf, textRect)

        for tilex in range(len(self.board)):
            for tiley in range(len(self.board[0])):
                if self.board[tilex][tiley]:
                    self.drawTile(tilex, tiley, self.board[tilex][tiley])

        # left, top = getLeftTopOfTile(0, 0)
        # width = BOARDWIDTH * TILESIZE
        # height = BOARDHEIGHT * TILESIZE
        # pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)

        # DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
        # DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
        # DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)

    def drawTile(self, tilex, tiley, number, adjx=0, adjy=0):
        # draw a tile at board coordinates tilex and tiley, optionally a few
        # pixels over (determined by adjx and adjy)
        left, top = self.getLeftTopOfTile(tilex, tiley)
        pygame.draw.rect(DISPLAYSURF, self.TILECOLOR, (left + adjx, top + adjy, self.TILESIZE, self.TILESIZE))
        textSurf = BASICFONT.render(str(number), True, self.TEXTCOLOR)
        textRect = textSurf.get_rect()
        textRect.center = left + int(self.TILESIZE / 2) + adjx, top + int(self.TILESIZE / 2) + adjy
        DISPLAYSURF.blit(textSurf, textRect)

    def getLeftTopOfTile(self, tileX, tileY):
        left = self.XMARGIN + (tileX * self.TILESIZE) + (tileX - 1)
        top = self.YMARGIN + (tileY * self.TILESIZE) + (tileY - 1)
        return (left, top)

# board = [[1, 0] ,[2, 3]]
# DrawBoard(2,board)