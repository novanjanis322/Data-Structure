import os

class Tree:
    def __init__(self, dataname, datanumber):
        self.dataname = dataname
        self.datanumber = datanumber
        self.left = None
        self.right = None

    def inputdata_man(self, name, phonenumber):
        if self.left is None:
            self.left = Tree(name, phonenumber)
            print(f'Successfully added {self.left.dataname} with number {self.left.datanumber} to male customer data.')  
        else:
            self.rekursive_inputdata_man(name, phonenumber, self.left)

    def rekursive_inputdata_man(self, name, phonenumber, node):
        if node.left is None:
            node.left = Tree(name, phonenumber)
            print(f"Successfully added {node.left.dataname} with number {node.left.datanumber} to male customer data.")
        else:
            if node.right is None:
                node.right = Tree(name, phonenumber)
                print(f"Successfully added {node.right.dataname} with number {node.right.datanumber} to male customer data.")
            else:
                self.rekursive_inputdata_man(name, phonenumber, node.left)

    def inputdata_woman(self, name, phonenumber):
        if self.right is None:
            self.right = Tree(name, phonenumber)
            print(f'Successfully added {self.right.dataname} with number {self.right.datanumber} to female customer data.') 
        else:
            self.rekursive_inputdata_woman(name, phonenumber, self.right)

    def rekursive_inputdata_woman(self, name, phonenumber, node):
        if node.right is None:
            node.right = Tree(name, phonenumber)
            print(f"Successfully added {node.right.dataname} with number {node.right.datanumber} to female customer data.")
        else:
            if node.left is None:
                node.left = Tree(name, phonenumber)
                print(f"Successfully added {node.left.dataname} with number {node.left.datanumber} to female customer data.")
            else:
                self.rekursive_inputdata_woman(name, phonenumber, node.right)               

    def simplesearchdata(self, val):
        if self.left is not None and self.left.dataname.upper() == val.upper():
            return f"Data {self.left.dataname} found in male customer data."
        if self.right is not None and self.right.dataname.upper() == val.upper():
            return f"Data {self.right.dataname} found in female customer data."
        elif self.left is None:
            if self.right is not None:
                return self.rekursive_simplesearchright(val, self.right)
        else:
            return self.rekursive_simplesearchleft(val, self.left)
        return " "

    def rekursive_simplesearchleft(self, val, node):
        if node.left is None:
            return self.rekursive_simplesearchright(val, self)
        elif node.left is not None and node.left.dataname.upper() == val.upper():
            return f"Data {node.left.dataname} found in male customer data."
        elif node.right is not None and node.right.dataname.upper() == val.upper():
            return f"Data {node.right.dataname} found in male customer data."
        return self.rekursive_simplesearchleft(val, node.left)

    def rekursive_simplesearchright(self, val, node):
        if node.right is None:
            return " "
        elif node.right is not None and node.right.dataname.upper() == val.upper():
            return f"Data {node.right.dataname} found in female customer data."
        elif node.left is not None and node.left.dataname.upper() == val.upper():
            return f"Data {node.left.dataname} found in female customer data."
        return self.rekursive_simplesearchright(val, node.right)
        
    def komplexsearchdata(self, val):
        if self.left is not None and val.upper() in self.left.dataname.upper():
            print(f"Complex search for {val} found in male customer data [{self.left.dataname}].")
        if self.left is not None:
            self.rekursive_komplexsearchleft(val, self.left)
        if self.right is not None and val.upper() in self.right.dataname.upper():
            print(f"Complex search for {val} found in female customer data [{self.right.dataname}].")
        if self.right is not None:
            self.rekursive_komplexsearchright(val, self.right)
       
    def rekursive_komplexsearchleft(self, val, node):
        if node.left is None:
            return
        if node.left is not None and val.upper() in node.left.dataname.upper():
            print(f"Complex search for {val} found in male customer data [{node.left.dataname}].")
        if node.right is not None and val.upper() in node.right.dataname.upper():
            print(f"Complex search for {val} found in male customer data [{node.right.dataname}].")
        return self.rekursive_komplexsearchleft(val, node.left)

    def rekursive_komplexsearchright(self, val, node):
        if node.right is None:
            return
        if node.right is not None and val.upper() in node.right.dataname.upper():
            print(f"Complex search for {val} found in female customer data [{node.right.dataname}].")
        if node.left is not None and val.upper() in node.left.dataname.upper():
            print(f"Complex search for {val} found in female customer data [{node.left.dataname}].")
        return self.rekursive_komplexsearchright(val, node.right)

    def customerdata_man(self):
        if self.left is not None:
            print("Name\t\t\t\t\t\tPhone Number")
            print(f"{self.left.dataname}\t\t\t\t\t\t{self.left.datanumber}")
            self.rekursif_customerdata_man(self.left)
        else:
            return
    
    def rekursif_customerdata_man(self, node):
        if node.left is not None:
            if node.right is not None:
                print(f"{node.left.dataname}\t\t\t\t\t\t{node.left.datanumber}")
                print(f"{node.right.dataname}\t\t\t\t\t\t{node.right.datanumber}")
            else:
                print(f"{node.left.dataname}\t\t\t\t\t\t{node.left.datanumber}")
            return self.rekursif_customerdata_man(node.left)
        elif node.left is None:
            return
            
    def customerdata_woman(self):
        if self.right is not None:
            print("Name\t\t\t\t\t\tPhone Number")
            print(f"{self.right.dataname}\t\t\t\t\t\t{self.right.datanumber}")
            self.rekursif_customerdata_woman(self.right)
        else:
            return
    
    def rekursif_customerdata_woman(self, node):
        if node.right is not None:
            if node.left is not None:
                print(f"{node.right.dataname}\t\t\t\t\t\t{node.right.datanumber}")
                print(f"{node.left.dataname}\t\t\t\t\t\t{node.left.datanumber}")
            else:
                print(f"{node.right.dataname}\t\t\t\t\t\t{node.right.datanumber}")
            return self.rekursif_customerdata_woman(node.right)
        elif node.right is None:
            return

tree = Tree("Contact Book", "Customers of Maju Jaya Store")
while True:
    print('''
=============================================================
Customer Data Program for "Maju Jaya Store"
=============================================================
1. Input Customer Data
2. "SIMPLE" Customer Data Search (specific name search)
3. "COMPLEX" Customer Data Search
4. View Customer Data
0. Exit ''')
    try:
        menu_choice = int(input('Choose a menu option: '))
        if menu_choice == 1:
            os.system('cls')
            print("=========================Input Data=========================")
            input_count = int(input('\nEnter the number of customer data entries: '))
            while input_count != 0:
                gender, name, number = input("\nEnter customer data [(male/female), name, number]: ").split(", ")
                if gender.upper() == "MALE":
                    tree.inputdata_man(name, number)
                    input_count -= 1
                elif gender.upper() == "FEMALE":
                    tree.inputdata_woman(name, number)
                    input_count -= 1
                else:
                    print("Make sure to input gender as male/female. Data not added.")
            
            print("\nData entry completed.")
        elif menu_choice == 2:
            search_name = input("Enter the name to search: ")
            os.system('cls')
            print("===================Simple Search Results===================")
            print(tree.simplesearchdata(search_name))
            back_to_main = input("\nPress any key to return to the main menu: ")
            os.system('cls')
            continue
        
        elif menu_choice == 3:
            complex_search_name = input("Enter the data to search: ")
            os.system('cls')
            print("==================Complex Search Results==================")
            tree.komplexsearchdata(complex_search_name)
            back_to_main = input("\nPress any key to return to the main menu: ")
            os.system('cls')
            continue
                    
        elif menu_choice == 4:
            os.system('cls')
            print(f"=============={tree.dataname} {tree.datanumber}===============\n")
            print("-----------------------------Male-------------------------------")
            tree.customerdata_man()
            print("----------------------------Female------------------------------")
            tree.customerdata_woman()
            back_to_main = input("\nPress any key to return to the main menu: ")
            os.system('cls')
            continue

        elif menu_choice == 0:
            confirm_exit = input("Are you sure (yes/no): ")
            if confirm_exit.upper() == "YES":
                os.system('cls')
                print("Data entry program has ended.")
                break
            elif confirm_exit.upper() == "NO":
                os.system('cls')
                print("Returning to main menu.")
            else:
                os.system('cls')
                print("Invalid input. Returning to main menu.")
        else:
            os.system('cls')
            print("Only numbers 1-3 and 0 are allowed. Returning to main menu.")
    except ValueError:
        os.system('cls')
        print("Invalid input. Returning to main menu.")
        continue
