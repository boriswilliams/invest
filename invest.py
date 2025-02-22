import math

from print2d import print2d

multip = {
  # US
  'spy': 0.7,
  'voo': 0.7,
  # Total
  'vti': 1.2,
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
  'ewj': 114.87,
  'spy': 111.62,
  'vgk': 114.58,
  'inda': 102.87,
  'iemg': 42.25,
  'iefa': 41.06,
  'vwo': 40.28,
  'fxi': 47.85,
  'isf.l': 87.67,
  'vti': 101.41,
  'voo': 57.67
}

DELTA = 10

CASH = 300

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
  for ticker in res:
    output.append([ticker, multip[ticker], value[ticker], roundValue(res[ticker] + value[ticker]), roundValue(res[ticker])])

  for ticker in value:
    if ticker in res:
      continue
    output.append([ticker, multip[ticker], value[ticker], 0, 0])

  print2d(output, columnHeaders=['ticker', 'multip', 'value', 'target', 'buy'])

if __name__ == '__main__':
  main()