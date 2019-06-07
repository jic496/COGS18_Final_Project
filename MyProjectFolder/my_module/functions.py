"""A collection of function for doing my project."""

class File(object):
    def __init__(self):
        self.children = {}
        self.isFile = False
        self.files = {}  

        
class FileSystem(object):

    def __init__(self):
        self.root = File()        

    def ls(self, path):
        """
        List files / directories
        
        Input parameter:
        ----------
        path: str
        The path of file or directory
        
        Return:
        ----------
        List of files or directories: list of str
        """
        root = self.root
        path = path[1:]
        if not path:
            return sorted(root.children.keys())
        path = path.split('/')
        for p in path:
            n = root.children.get(p, None)
            if n:
                root = n
            else:
                break
        return sorted(root.files.keys())

    def mkdir(self, path):
        """
        Make a directory
        
        Input parameter:
        ----------
        path: str
        The path of directory
        
        Return:
        ----------
        None
        """
        root = self.root
        path = path[1:]
        path = path.split('/')
        for p in path:
            root.children[p] = root.children.get(p, File())
            root.files[p] = ""
            root = root.children[p]
        root.isFile = True
        
    def addContentToFile(self, filePath, content):
        """
        Add content to file
        
        Input parameter:
        ----------
        filePath: str
        The path of a file
        content: str
        The content wanted to add to the given file
        
        Return:
        ----------
        None
        """
        root = self.root
        
        self.mkdir(filePath)
        filePath = filePath[1:]
        path = filePath.split('/')
        for p in path:
            n = root.children.get(p, None)
            if not n:
                break
            root = n
        root.files[p] = root.files.get(p, "") + content
        root.children[p] = None

    def readContentFromFile(self, filePath):
        """
        Read content from given file
        
        Input parameter:
        ----------
        filePath: str
        The path of a file
        
        Return:
        ----------
        Content of the given file: str
        """
        root = self.root
        filePath = filePath[1:]
        path = filePath.split('/')
        for p in path:
            n = root.children.get(p, None)
            if not n:
                break
            root = n
        return root.files[p]
