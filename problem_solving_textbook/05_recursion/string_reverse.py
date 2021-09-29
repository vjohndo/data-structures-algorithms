"""
Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.

Lesson learned:
"""

def reverse(expression):
    
    # BASE CASE -> A single string is the same when reversed
    # Remember to cover edge cases with the reverse
    if len(expression) <= 1:
        return expression

    # PROGRESS TO BASE -> MANIPULATE STRING... SLICE
    else:
        return expression[-1] + reverse(expression[0:-1])
    
print(reverse("hello"), "olleh")
print(reverse("l"), "l")
print(reverse("follow"), "wollof")
print(reverse(""), "")

