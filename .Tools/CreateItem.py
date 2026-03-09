import os, json

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def LoadJson(Path):
    try:
        with open(Path, "r", encoding="utf-8") as F:
            return json.load(F)
    except:
        return None

def LoadText(Path):
    try:
        with open(Path, "r", encoding="utf-8") as F:
            return F.read()
    except:
        return None

def ListCategories(BaseDir):
    Categories = []
    for Item in os.listdir(BaseDir):
        if Item.startswith("."):
            continue
        Path = os.path.join(BaseDir, Item)
        if os.path.isdir(Path):
            DataPath = os.path.join(Path, ".Data")
            if os.path.isdir(DataPath):
                Categories.append(Item)
    return Categories

def ChooseOption(Prompt, Options):
    while True:
        Clear()
        print(Prompt + "\n")
        for i, Option in enumerate(Options):
            print(f"{i}: {Option}")

        Choice = input("\nChoice: ").strip()

        if Choice.isdigit():
            Index = int(Choice)
            if 0 <= Index < len(Options):
                return Options[Index]

        if Choice in Options:
            return Choice

def PromptValue(Field):
    Value = input(f"{Field}: ").strip()
    if "," in Value:
        return [X.strip() for X in Value.split(",") if X.strip()]
    return Value

def ApplyFormat(Template, Data):
    Output = Template
    for Key, Value in Data.items():
        Placeholder = f"%{Key}%"
        if isinstance(Value, list):
            Replacement = ", ".join(Value)
        else:
            Replacement = str(Value)
        Output = Output.replace(Placeholder, Replacement)
    return Output

def CreateItem(CategoryPath):
    DataPath = os.path.join(CategoryPath, ".Data")
    ItemsPath = os.path.join(CategoryPath, "Items")

    Params = LoadJson(os.path.join(DataPath, "Parameters.json"))
    Template = LoadText(os.path.join(DataPath, "Format.md"))

    if not Params or not Template:
        print("Missing Parameters.json or Format.md")
        input("\nPress Enter...")
        return

    Fields = Params.get("Parameters", [])

    ItemData = {}
    Clear()

    for Field in Fields:
        ItemData[Field] = PromptValue(Field)

    FileName = ItemData.get("FileName", "UnFileNamed")
    OutputPath = os.path.join(ItemsPath, f"{FileName}.md")

    os.makedirs(ItemsPath, exist_ok=True)

    Content = ApplyFormat(Template, ItemData)

    with open(OutputPath, "w", encoding="utf-8") as F:
        F.write(Content)

    print(f"\nCreated: {OutputPath}")
    input("\nPress Enter to return...")

def Main():
    DirBase = os.path.dirname(os.path.abspath(__file__))
    DirRoot = os.path.dirname(DirBase)
    DirCategories = os.path.join(DirRoot, "Categories")

    Categories = ListCategories(DirCategories)

    if not Categories:
        print("No categories found.")
        input("\nPress Enter...")
        return

    Chosen = ChooseOption("Select category:", Categories)
    CategoryPath = os.path.join(DirCategories, Chosen)

    CreateItem(CategoryPath)

while True:
    Main()