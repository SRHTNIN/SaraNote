import os, json, subprocess, platform

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def OpenFile(Path):
    system = platform.system()
    if system == "Windows":
        os.startfile(Path)
    elif system == "Darwin":
        subprocess.call(["open", Path])
    else:
        subprocess.call(["xdg-open", Path])

def LoadParametersJson(DirPath):
    ParamPath = os.path.join(DirPath, "Parameters.json")
    if not os.path.isfile(ParamPath):
        return None

    try:
        with open(ParamPath, "r", encoding="utf-8") as F:
            return json.load(F)
    except:
        return None

def ListValidFolders(BaseDir):
    All = []
    for Item in os.listdir(BaseDir):
        if Item.startswith("."):
            continue
        Path = os.path.join(BaseDir, Item)
        if os.path.isdir(Path):
            if LoadParametersJson(Path) is not None:
                All.append(Item)
    return All

def ChooseOption(Prompt, Options):
    while True:
        Clear()
        print(Prompt)
        for i, Option in enumerate(Options):
            print(f"{i}: {Option}")

        Choice = input("\nChoice: ").strip()

        if Choice.isdigit():
            Index = int(Choice)
            if 0 <= Index < len(Options):
                return Options[Index]

        if Choice in Options:
            return Choice

def SearchEntries(BasePath, Param, Value):
    Matches = []

    for Item in os.listdir(BasePath):
        Folder = os.path.join(BasePath, Item)
        if not os.path.isdir(Folder):
            continue
        if Item.startswith("."):
            continue

        JsonPath = None
        for F in os.listdir(Folder):
            if F.lower().endswith(".json"):
                JsonPath = os.path.join(Folder, F)
                break

        if not JsonPath:
            continue

        try:
            with open(JsonPath, "r", encoding="utf-8") as File:
                Data = json.load(File)
        except:
            continue

        if Param not in Data:
            continue

        Field = Data[Param]
        Found = False

        if isinstance(Field, list):
            for X in Field:
                if Value.lower() in X.lower():
                    Found = True
                    break
        else:
            if Value.lower() in str(Field).lower():
                Found = True

        if Found:
            Matches.append((Item, JsonPath))

    return Matches

def Main():
    Clear()
    BaseDir = os.path.dirname(os.path.abspath(f"{__file__}../../"))

    Folders = ListValidFolders(BaseDir)
    if not Folders:
        print("No valid content folders found.")
        input("\nPress Enter...")
        return

    ChosenFolder = ChooseOption("Select category:", Folders)
    DirFolder = os.path.join(BaseDir, ChosenFolder)

    ParamsJson = LoadParametersJson(DirFolder)
    if not ParamsJson or "Parameters" not in ParamsJson:
        print("No Parameters.json found or invalid format.")
        input("\nPress Enter...")
        return

    ParamList = ParamsJson["Parameters"]

    ChosenParam = ChooseOption("Select parameter to search by:", ParamList)

    SearchValue = input(f"\nSearch value for {ChosenParam}: ").strip()
    if not SearchValue:
        print("Empty search value.")
        input("\nPress Enter...")
        return

    Matches = SearchEntries(DirFolder, ChosenParam, SearchValue)

    if not Matches:
        print("\nNo results found.")
        input("\nPress Enter...")
        return

    Clear()
    print("Results:\n")
    for i, (Name, Path) in enumerate(Matches):
        print(f"{i}: {Name}")

    Choice = input("\nSelect result number or name: ").strip()

    Selected = None
    if Choice.isdigit():
        Index = int(Choice)
        if 0 <= Index < len(Matches):
            Selected = Matches[Index][1]
    else:
        for Name, Path in Matches:
            if Name.lower() == Choice.lower():
                Selected = Path
                break

    if not Selected:
        print("Invalid choice.")
        input("\nPress Enter...")
        return

    TxtPath = Selected.replace(".json", ".txt")

    print("\nOpening:", TxtPath)
    OpenFile(TxtPath)

    input("\nPress Enter to return to the menu...")

while True:
    Main()