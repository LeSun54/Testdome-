#A palindrome is a word that reads the same backward or forward.

#Write a function that checks if a given word is a palindrome. Character case should be ignored.

#For example, is_palindrome("Deleveled") should return True as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.class FileOwners:
class Palindrome:

    @staticmethod
    def group_by_owners(files):
        result = {}
        for filename in files.keys():
            owner = files[filename]
            if owner not in result:
                result[owner] = list()
            result[owner].append(filename)
        return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
