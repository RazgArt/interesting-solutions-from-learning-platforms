"""To give credit where credit is due: This problem was taken from the ACMICPC-Northwest
Regional Programming Contest. Thank you problem writers.
You are helping an archaeologist decipher some runes. He knows that this ancient society used a Base 10 system,
and that they never start a number with a leading zero. He's figured out most of the digits as well as a few
operators, but he needs your help to figure out the rest.
The professor will give you a simple math expression, of the form
[number][op][number]=[number]
He has converted all of the runes he knows into digits. The only operators he knows are addition (+),
subtraction(-), and multiplication (*), so those are the only ones that will appear.
Each number will be in the range from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a
leading -, and maybe a few ?s. If there are ?s in an expression, they represent a digit rune that the professor
doesn't know (never an operator, and never a leading -).
All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other
given digits in the expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.
Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works, give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong. output -1 in that case.
Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a paramater repressenting the expression and will return an int value representing the unknown rune or -1 if no such rune exists."""
import re


def solve_runes(runes):
    for numb in sorted(set("0123456789") - set(runes)):
        string = runes.replace("?", str(numb))
        list_numbers = re.findall(r'[-]?\d+', string)
        if "00" in list_numbers:
            continue
        one, two, answer = list(map(lambda x: int(x), list_numbers))
        znak = re.search(r'(?<=\d)[*+-]', string)[0]
        operation = {
            "*": one * two,
            "-": one - two,
            "+": one + two
                    }
        if operation[znak] == answer:
            return int(numb)

    return -1
if __name__ == '__main__':
    solve_runes("19--4?==6?")
