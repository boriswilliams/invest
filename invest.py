import math

from print2d import print2d

multip = {
    # US
    'spy': 0.7,
    'voo': 0.7,
    # Total
    'vti': 1.3,
    # UK
    'isf.l': 1,
    # India
    'inda': 1,
    # Emerging
    'vwo': 0.4,
    'iemg': 0.4,
    # World
    'iefa': 0.6,
    # Europe
    'vgk': 0.5,
    # China
    'fxi': 0.5,
    # Japan
    'ewj': 0.5,
}

value = {
    'ewj': 211.92,
    'fxi': 224.15,
    'iefa': 257.20,
    'iemg': 175.52,
    'inda': 412.01,
    'isf.l': 428.44,
    'spy': 310.98,
    'vgk': 211.63,
    'voo': 310.90,
    'vti': 533.07,
    'vwo': 174.67
}

DELTA = 10

CASH = 277

def roundValue(x):
    return math.floor(x * 100) / 100

def calc(cash, stocks):
    num = cash
    den = 0
    for ticker in stocks:
        num += value[ticker]
        den += multip[ticker]
    target = num / den
    
    maxDiff = 0
    maxTicker = ''
    for ticker in stocks:
        if (diff := value[ticker] + DELTA - target * multip[ticker]) > maxDiff:
            maxTicker, maxDiff = ticker, diff
    if maxTicker:
        return calc(cash, [ticker for ticker in stocks if ticker != maxTicker])
    
    res = {}
    for ticker in stocks:
        res[ticker] = target * multip[ticker] - value[ticker]
    return res

def main():
    output = []

    res = calc(CASH, value.keys())

    for ticker in value:
        output.append([ticker, multip[ticker], value[ticker], roundValue(res[ticker] + value[ticker]) if ticker in res else 0, ticker, roundValue(res[ticker])if ticker in res else 0])

    print2d(output, columnHeaders=['ticker', 'multip', 'value', 'target', 'ticker', 'buy'])

if __name__ == '__main__':
    main()