from utils import *

def main(balls = 70, colors = 7, draws = 20, decimal_places = 9):
    balls_per_color = balls / colors

    # let p = probability of a red ball existing in a draw
    # let pc = probability of a red ball NOT existing in a draw

    # out of 60 non-red balls, pick 20
    # divide by total number of combinations (70 pick 20)
    pc = divide(nCr(balls - balls_per_color, draws), nCr(balls, draws))
    p = 1 - pc

    # expected value is 7 * (probability of 1 color existing) = 7p
    answer = colors * p

    # round to 9 decimal places
    print round(answer, decimal_places)

main()
