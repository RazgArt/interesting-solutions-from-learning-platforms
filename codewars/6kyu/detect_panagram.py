"""A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z
at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is,
False if not. Ignore numbers and punctuation."""
"My solution"
def is_pangram(s:str)->bool:
    if all(chr(num) in s.lower() for num in range(97,123)):
        return True
    return False
if '__main__' == __name__:
    print(is_pangram("The quick brown fox jumps over the lazy dog"))