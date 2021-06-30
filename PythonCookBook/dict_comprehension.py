prices = {
  'ACME': 45.23,
  'APPL': 621.78,
  'IBM': 205.55,
  'HPQ': 37.20,
  'FB': 10.75
}

subset_1 = { k:v for k,v in prices.items() if v > 50}
print(prices)
print(subset_1)
"""
{'ACME': 45.23, 'APPL': 621.78, 'IBM': 205.55, 'HPQ': 37.2, 'FB': 10.75}
{'APPL': 621.78, 'IBM': 205.55}
"""