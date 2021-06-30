from collections import Counter
words = [
  'look',
  'hello',
  'hello',
  'hello',
  'look',
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
print(word_counts)
print(word_counts['hello'])