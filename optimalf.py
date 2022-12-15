from typing import List
import numpy as np


def optimalf(trades: List[int]):
    """
    If there is a positive expected return, then there is an optimal fixed
    fraction to reinvest of your total stake.

    trade: List[int]
        profit or loss on the ith trade

    returns
    -------
    f: int
        the optimal best size given the track record of the system
    """
    # calculate the holding period return
    fspace = np.linspace(0.01, 1.0, num=100)
    res = [geometric_mean(f, trades) for f in fspace]
    i = np.argmax(res)
    return min(trades) / -fspace[i]
    

def geometric_mean(f, trades):
    """
    trade is a numpy array
    """
    n = len(trades)
    biggest_loss = min(trades)
    return np.cumprod(1.0 + f * (-trades / biggest_loss))[-1] ** (1.0 / n)


if __name__ == "__main__":
    my_trades = np.array([100, -50, 20, 87, -55])
