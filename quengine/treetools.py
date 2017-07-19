class TreeNode:
    """Parse tree."""

    def __init__(self, className, text, children, level):
        """Construct a tree.
        """
        self.className = className
        self.text = text
        self.children = children
        self.level = level
        pass

    def __str__(self):
        """To string (with tree structure parentheses)."""
        strlist = []
        for i in range(self.level):
            strlist.append('    ')
        strlist.extend(['(', self.className])
        if len(self.children) > 0:
            strlist.append('\n')
            for child in self.children:
                strlist.append(child.__str__())
            if len(self.text) > 0:
                for i in range(self.level + 1):
                    strlist.append('    ')
            else:
                for i in range(self.level):
                    strlist.append('    ')
        else:
            strlist.append(' ')
        strlist.append(self.text)
        strlist.append(')\n')
        return ''.join(strlist)

    def toSentence(self):
        """Unfold the tree structure into a string."""
        strlist = []
        for child in self.children:
            childSent = child.toSentence()
            if len(childSent) > 0:
                strlist.append(childSent)
        if len(self.text) > 0:
            strlist.append(self.text)
        return ' '.join(strlist)

    def relevel(self, level):
        """Re-assign level."""
        self.level = level
        for child in self.children:
            child.relevel(level + 1)

    def copy(self):
        """Clone a tree."""
        children = []
        for child in self.children:
            children.append(child.copy())
        return TreeNode(self.className, self.text, children, self.level)
