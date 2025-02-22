data = {
  2020: 62.15,
  2021: 16.08,
  2022: 29.53,
  2023: 47.84,
  2024: 35.58,
}

total = 1
for year in data:
  total *= 1 + data[year] / 100

print((total ** (1/len(data)) - 1) * 100)