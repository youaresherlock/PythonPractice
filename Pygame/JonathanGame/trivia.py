import sys
import pygame
from pygame import locals

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Trivia Game")
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)
white = 255, 255, 255
black = 0, 0, 0
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0

class Trivia(object):
    def __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white, white, white, white]

        # read trivia data from file
        with open(filename, "r") as file:
            trivia_data = file.readlines()

        # count and clean up trivia data
        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total +=1

    def print_text(self, font, x, y ,text, color=white, shadow=True):
        if shadow:
            imgText = font.render(text, True, black)
            screen.blit(imgText, (x - 2, y - 2))
        imgText = font.render(text, True, color)
        screen.blit(imgText, (x, y))

    def show_question(self):
        self.print_text(font1, 210, 5, "TRIVIA GAME")
        self.print_text(font2, 190, 500 - 20, "Press Keys (1-4) To Answer", purple)
        self.print_text(font2, 530, 5, "SCORE", purple)
        self.print_text(font2, 550, 25, str(self.score), purple)

        # get correct answer out of data(first)
        self.correct = int(self.data[self.current + 5])

        # display question
        question = self.current
        self.print_text(font1, 5, 80, "QUESTION " + str(question))
        self.print_text(font2, 20, 120, self.data[self.current], yellow)


        # response to correct answer
        if self.scored:
            self.colors = [white, white, white, white]
            self.colors[self.correct-1] = green
            self.print_text(font1, 230, 380, "CORRECT!", green)
            self.print_text(font2, 170, 420, "Press Enter For Next Question", green)
        elif self.failed:
            self.colors = [white, white, white, white]
            self.colors[self.wronganswer - 1] = red
            self.colors[self.correct - 1] = green
            self.print_text(font1, 220, 380, "INCORRECT!", red)
            self.print_text(font2, 170, 420, "Press Enter For Next Question", red)

        # display answers
        self.print_text(font1, 5, 170, "ANSWERS")
        self.print_text(font2, 20, 210, "1 - " + self.data[self.current + 1], self.colors[0])
        self.print_text(font2, 20, 240, "2 - " + self.data[self.current + 2], self.colors[1])
        self.print_text(font2, 20, 270, "3 - " + self.data[self.current + 3], self.colors[2])
        self.print_text(font2, 20, 300, "4 - " + self.data[self.current + 4], self.colors[3])

    def handle_input(self, number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else :
                self.failed = True
                self.wronganswer = number

    def next_question(self):
        if self.scored or self.failed:
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [white, white, white, white]
            self.current += 6
            if self.current >= self.total:
                while True:
                    ret = input("do you want play again? (q/y)")
                    if ret.strip().startswith("q"):
                        sys.exit()
                    else :
                        self.current = 0
                        break

# load the trivia data file
trivia = Trivia("trivia_data.txt")
# repeating the loop
while True:
    for event in pygame.event.get():
        if event.type == locals.QUIT:
            sys.exit()
        elif event.type == locals.KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                trivia.handle_input(1)
            elif event.key == pygame.K_2:
                trivia.handle_input(2)
            elif event.key == pygame.K_3:
                trivia.handle_input(3)
            elif event.key == pygame.K_4:
                trivia.handle_input(4)
            elif event.key == pygame.K_RETURN:
                trivia.next_question()
    # clean the screen
    screen.fill((0, 0, 200))

    # display trivia data
    trivia.show_question()

    # update the display
    pygame.display.update()

