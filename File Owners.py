class FileOwners:

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
