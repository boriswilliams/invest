from math import floor
from collections import defaultdict
from typing import List

from print2d import print2d

multip = {
  # World
  'iefa': 0.6,
  'vxus': 0.6,
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

values = {
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

CASH = 500

def roundValue(x: float) -> int | float:
  if x == 0: return 0
  return floor(x * 100) / 100

def calcUnitTarget(cash: int, stocks) -> float:
  value = cash
  units = 0
  for ticker in stocks:
    value += values[ticker]
    units += multip[ticker]
  return value / units

def calcDiffs(cash: int | float, stocks: List[str]) -> dict[str, float]:

  unitTarget = calcUnitTarget(cash, stocks)

  # Filter out stocks past targets
  maxDiff = 0
  maxTicker = ''
  if cash > 0:
    for ticker in stocks:
      if (diff := values[ticker] + DELTA - unitTarget * multip[ticker]) > maxDiff:
        maxTicker, maxDiff = ticker, diff
  else:
    for ticker in stocks:
      if (diff := unitTarget * multip[ticker] - values[ticker]) > maxDiff:
        maxTicker, maxDiff = ticker, diff
  if maxTicker:
    return calcDiffs(cash, [ticker for ticker in stocks if ticker != maxTicker])
  
  # Return diffs to targets
  diffs = defaultdict(int)
  for ticker in stocks:
    diffs[ticker] = unitTarget * multip[ticker] - values[ticker]
  return diffs

def main():
  output = []

  diffs = calcDiffs(CASH, values.keys())

  for ticker in values:
    output.append([
      ticker,
      multip[ticker],
      values[ticker],
      roundValue(diffs[ticker] + values[ticker]),
      ticker,
      roundValue(diffs[ticker])
    ])

  print2d(output, columnHeaders=['ticker', 'multip', 'values', 'target', 'ticker', 'buy'])

if __name__ == '__main__':
  main()
