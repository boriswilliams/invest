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
  'vxus': 0.2,
  # Europe
  'vgk': 0.5,
  # China
  'fxi': 0.5,
  # Japan
  'ewj': 0.5,
}

value = {
  'ewj': 497.50,
  'fxi': 410.87,
  'iefa': 577.53,
  'iemg': 391.19,
  'inda': 773.47,
  'isf.l': 789.98,
  'spy': 532.10,
  'vgk': 481.33,
  'voo': 530.69,
  'vti': 1150.28,
  'vwo': 360.27,
  'vxus': 100.09
}

DELTA = 10

CASH = 270

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
