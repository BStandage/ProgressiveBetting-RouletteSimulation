import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

def progressive_betting():
    bet = 1
    prob = 18 / 38
    earnings = 1
    count = 0

    while earnings > -1000000 and earnings < 1000000:
        count += 1
        if random.random() < prob:
            earnings += abs(bet) * 2

        else:
            earnings -= abs(bet)
            bet = abs(bet) * 2

        plt.scatter(count, earnings)
        plt.plot(count, earnings, 'o')
        plt.pause(.1)
        print(" Earnings: " + str(earnings))

    plt.show()


if __name__ == '__main__':
    progressive_betting()