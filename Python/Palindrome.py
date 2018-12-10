class Palindrome:

    @staticmethod
    def is_palindrome(word):
        lower = word.lower()
        return lower == lower[::-1]

print(Palindrome.is_palindrome('Deleveled'))
