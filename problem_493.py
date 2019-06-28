from utils import *

def main(balls = 70, colors = 7, draws = 20):
    def count_colors(draw_combination):
        return len(filter(lambda x: x > 0, draw_combination))

    balls_per_color = balls / colors

    draw_combinations = filter(lambda x: sum(x) == draws, product(xrange(balls_per_color + 1), repeat=colors))
    numerator = sum([reduce(multiply, [nCr(balls_per_color, x) for x in c]) * count_colors(c) for c in draw_combinations])
    denominator = nCr(balls, draws)
    answer = divide(numerator, denominator)
    print round(answer, 9)

main()
