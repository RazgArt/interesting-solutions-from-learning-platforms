"""You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

This is a simplified version of the Between Markers mission.

The initial and final markers are always different.
The initial and final markers are always 1 char size.
The initial and final markers always exist in a string and go one after another.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:

assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

How it is used: For text parsing.

Precondition: There can't be more than one final and one initial markers."""

"My solution"
import re
def between_markers(text: str, start: str, end: str) -> str:
    if start in "[\/.]":
        parser = f'(?<=\{start}).+(?=\{end})'
    else:
        parser = f'(?<={start}).*(?={end})'
    return re.search(parser,text)[0]




assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"


if __name__ == '__main__':
    print(between_markers("What is >apple<", ">", "<"))
