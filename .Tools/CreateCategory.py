import os, shutil

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def FindDefaults(DefaultsDir):
    DefaultsList = []

    for Root, Dirs, Files in os.walk(DefaultsDir):
        Dirs[:] = [D for D in Dirs if not D.startswith(".")]

        for File in Files:
            FullPath = os.path.join(Root, File)
            RelPath = os.path.relpath(FullPath, DefaultsDir)
            DefaultsList.append((RelPath, FullPath))

    return DefaultsList

def CreateCategory(CategoryName, CategoriesPath, DefaultsPath):
    CategoryPath = os.path.join(CategoriesPath, CategoryName)
    if not os.path.exists(CategoryPath):
        os.makedirs(CategoryPath, exist_ok=True)

        ItemsPath = os.path.join(CategoryPath, "Items")
        os.makedirs(ItemsPath, exist_ok=True)

        DataPath = os.path.join(CategoryPath, ".Data")
        os.makedirs(DataPath, exist_ok=True)    

        Defaults = FindDefaults(DefaultsPath)

        for Default in Defaults:
            shutil.copy(Default[1], f"{DataPath}/{Default[0]}")
        
        print(f"\nCreated: {CategoryPath}")
    
    else:
        print(f"\n{CategoryPath} already exists.")

    input("\nPress Enter to return...")


def Main():
    DirBase = os.path.dirname(os.path.abspath(__file__))
    DirRoot = os.path.dirname(DirBase)
    PathDefaults = os.path.join(DirRoot, ".Defaults")
    PathCategory = os.path.join(DirRoot, "Categories")

    NameCategory = str(input("Category name: "))
    if NameCategory:
        CreateCategory(NameCategory, PathCategory, PathDefaults)
    else:
        print("\nCategory name not accepted.")
        input("\nPress Enter to return...")

while True:
    Main()