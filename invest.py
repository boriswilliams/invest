import math

from print2d import print2d

multip = {
  # US S&P
  'spy': 0.6,
  'voo': 0.6,
  # Total
  'vti': 1.3,
  # UK
  'isf.l': 0.8,
  # India
  'inda': 0.9,
  # Emerging
  'vwo': 0.4,
  'iemg': 0.4,
  # World
  'iefa': 0.6,
  'vxus': 0.23,
  # Europe
  'vgk': 0.5,
  # China
  'fxi': 0.5,
  # Japan
  'ewj': 0.5,
}

value = {
  'ewj': 472.60,
  'fxi': 442.15,
  'iefa': 543.33,
  'iemg': 374.11,
  'inda': 760.55,
  'isf.l': 776.21,
  'spy': 551.23,
  'vgk': 453.84,
  'voo': 541.16,
  'vti': 1179.37,
  'vwo': 343.80,
  'vxus': 174.66
}

DELTA = 10

CASH = 284

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
