import os
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preorderTraversal(self, root):
        order = []

        self.preorderTraversaltool(root, order)
        return order

    def preorderTraversaltool(self, root, order):
        if root is None:
            return 

        order.append(root.data)

        self.preorderTraversaltool(root.left, order)

        self.preorderTraversaltool(root.right, order)
        
    def postorderTraversal(self, root):
        order = []

        self.postorderTraversaltool(root, order)
        return order

    def postorderTraversaltool(self, root, order):
        if root is None:
            return

        self.postorderTraversaltool(root.left, order)

        self.postorderTraversaltool(root.right, order)

        order.append(root.data)

        return

    def inorderTraversal(self, root):
        answer = []

        self.inorderTraversalUtil(root, answer)
        return answer

    def inorderTraversalUtil(self, root, answer):
        if root is None:
            return

        self.inorderTraversalUtil(root.left, answer)
        answer.append(root.data)
        self.inorderTraversalUtil(root.right, answer)
        return

    def inputparent(self, data):
        if self.data:
            if self.left is None:
                self.left = Tree(data)
                print(f'{self.left.data} is a sub file of the main file ({self.data}).')
            else:
                if self.right is None:
                    self.right = Tree(data)
                    print(f'{self.right.data} is a sub file of the main file ({self.data}).')
                else:
                    print('Reached the maximum number of subfiles.')       
        else:
            self.data = data

    def inputchild(self, parent, child):
        if self.left.data == parent:
            if self.left.left is None:
                self.left.left = Tree(child)
                print(f'{self.left.left.data} is a sub file of the parent file ({self.left.data}).')
            else:
                if self.left.right is None:
                    self.left.right = Tree(child)
                    print(f'{self.left.right.data} is a sub file of the parent file ({self.left.data}).')
                else:
                    print('Reached the maximum number of subfiles.')
        elif self.right.data == parent:
            if self.right.left is None:
                self.right.left = Tree(child)
                print(f'{self.right.left.data} is a sub file of the parent file ({self.right.data}).')
            else:
                if self.right.right is None:
                    self.right.right = Tree(child)
                    print(f'{self.right.right.data} is a sub file of the parent file ({self.right.data}).')
                else:
                    print('Reached the maximum number of subfiles.')
        else:
            print('Parent file not found.')

print('=============================== Program to create folder structure based on binary tree ===============================')
while True:
    print('''\n
1. Input root (main file)
2. Input parent (sub file/child of the main file)
3. Input child (sub file/child of the parent)
4. Print file names using preorder traversal method
5. Print file names using postorder traversal method
6. Print file names using inorder traversal method
7. Exit \n''')
    inputmenu = int(input('Choose a menu option: '))
    if inputmenu == 1:
        mainfile = input('Enter the name of the main file: ')
        new_node = Tree(mainfile)
        os.system('cls')
        print(f'{new_node.data} is the name of the main file.')

    elif inputmenu == 2:
        parentfile = input(f'Enter the file to be the parent (subfile of the main file ({new_node.data})): ')
        os.system('cls')
        new_node.inputparent(parentfile)

    elif inputmenu == 3:
        parentfile, childfile = input('Enter the parent file and child file (parentfile, childfile): ').split(", ")
        os.system('cls')
        new_node.inputchild(parentfile, childfile)

    elif inputmenu == 4:
        os.system('cls')
        print(new_node.preorderTraversal(new_node))

    elif inputmenu == 5:
        os.system('cls')
        print(new_node.postorderTraversal(new_node))

    elif inputmenu == 6:
        os.system('cls')
        print(new_node.inorderTraversal(new_node))

    elif inputmenu == 7:
        print('\nThank you. Have a nice day. *smileyface\n')
        break
