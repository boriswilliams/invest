import math

from print2d import print2d

multip = {
  # World
  'iefa': 0.6,
  'vxus': 0.3,
  # Europe
  'vgk': 0.5,
  # Emerging
  'vwo': 0.4,
  'iemg': 0.4,
  # USA
  'vti': 1.3,
  # S&P
  'spy': 0.6,
  'voo': 0.6,
  # UK
  'isf.l': 0.8,
  # China
  'fxi': 0.5,
  # India
  'inda': 0.8,
  # Japan
  'ewj': 0.5,
}

value = {
  'ewj': 533.86,
  'fxi': 533.62,
  'iefa': 634.59,
  'iemg': 430.47,
  'inda': 848.90,
  'isf.l': 850.70,
  'spy': 649.47,
  'vgk': 527.02,
  'voo': 645.85,
  'vti': 1395.13,
  'vwo': 429.49,
  'vxus': 319.13
}

DELTA = 10

CASH = -500

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
  if cash > 0:
    for ticker in stocks:
      if (diff := value[ticker] + DELTA - target * multip[ticker]) > maxDiff:
        maxTicker, maxDiff = ticker, diff
  else:
    for ticker in stocks:
      if (diff := target * multip[ticker] - value[ticker]) > maxDiff:
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
