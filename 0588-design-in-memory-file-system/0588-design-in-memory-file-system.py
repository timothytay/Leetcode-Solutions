class FileSystem:

    def __init__(self):
        self.root = {}


    def ls(self, path: str) -> List[str]:
        cur = self.root
        path_vars = path[1:].split('/')
        if path_vars != [""]:
            for var in path_vars:
                cur = cur[var]
        if isinstance(cur, str):
            return [path_vars[-1]]
        else:
            names = list(cur.keys())
            names.sort()
            return names

    def mkdir(self, path: str) -> None:
        path_vars = path[1:].split('/')
        cur = self.root
        for direc in path_vars:
            if direc not in cur:
                cur[direc] = {}
            cur = cur[direc]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_vars = filePath[1:].split('/')
        cur = self.root
        for i in range(len(path_vars) - 1):
            if path_vars[i] not in cur:
                cur[path_vars[i]] = {}
            cur = cur[path_vars[i]]
        if path_vars[-1] not in cur:
            cur[path_vars[-1]] = ""
        cur[path_vars[-1]] += content

    def readContentFromFile(self, filePath: str) -> str:
        path_vars = filePath[1:].split('/')
        cur = self.root
        for direc in path_vars:
            cur = cur[direc]
        return cur


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)