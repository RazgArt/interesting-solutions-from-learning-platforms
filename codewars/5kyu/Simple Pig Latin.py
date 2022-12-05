"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""
"My solution"
def pig_it(s:str)->str:
    return " ".join([word[1:]+word[0]+"ay" if word.isalpha() else word for word in s.split()])
if __name__ == '__main__':
    print(pig_it('Hello world !'))
