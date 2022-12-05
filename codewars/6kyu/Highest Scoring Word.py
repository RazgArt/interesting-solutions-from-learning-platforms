"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""
"My solution"
def high(x:str)->str:
   x = x.split()
   arr = x.copy()
   for ind,word in enumerate(x):
      x[ind] = sum([ord(letter)-96  for letter in word])
   return arr[x.index(max(x))]
if __name__ == '__main__':
    print(high("man i need a taxi up to ubud"))
