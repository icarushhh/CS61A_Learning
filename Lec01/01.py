# run in a interpreter

# Numeric expressions
2022
2000 + 22
1 + 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Functions
abs(-2)

# Values
"Go Bears"

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open("/Users/icarus/Library/Mobile Documents/com~apple~CloudDocs/2022秋季学期/CS61A_Learning/Lec01/shakespeare.txt")
text = shakes.read().split()
print(len(text))
print(text[:25])
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets
# something in a set only shows up once
words = set(text)
print(len(words))

# Combinations 
'draw'
print('draw'[0])
print({w[0] for w in words})        # {} represent a set

# Data
print('draw'[::-1])        # reverse a word
print({w for w in words if w == w[::-1] and len(w)>4})
print({w for w in words if w[::-1] in words and len(w) == 4})
print({w for w in words if w[::-1] in words and len(w) > 6})
