import json, os, subprocess, sys

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def PromptList(Prompt):
    Value = input(Prompt).strip()
    if not Value:
        return []
    return [Item.strip() for Item in Value.split(",")]

def CreateItemFiles(Item):
    Title = Item.get("Title", "Untitled")

    DirBase = os.path.dirname(os.path.abspath(f"{__file__}../../../"))
    DirItems = os.path.join(DirBase, "Items")
    DirItem = os.path.join(DirItems, Title)

    os.makedirs(DirItem, exist_ok=True)

    DirJson = os.path.join(DirItem, f"{Title}.json")
    DirTxt = os.path.join(DirItem, f"{Title}.txt")

    with open(DirJson, "w", encoding="utf-8") as File:
        json.dump(Item, File, indent=4)

    Tags = Item.get("Tags", [])
    FormattedTags = " ".join(f"#{Tag}" for Tag in Tags)

    Content = (
        f"{FormattedTags}\n\n"
        f"{Item.get('Title', '')}\n\n"
        f"Appearance: {Item.get('Appearance', 'None')}\n"
        f"Description: {Item.get('Description', 'None')}\n"        
        f"Mechanic: {Item.get('Mechanic', 'None')}"
    )

    with open(DirTxt, "w", encoding="utf-8") as File:
        File.write(Content)

def RunTool(RelPath):
    PythonExe = sys.executable
    subprocess.call([PythonExe, RelPath])

def MainItem():
    Clear()

    Item = {
        "Title": input("Title: ").strip(),
        "Appearance": input("Appearance: ").strip(),
        "Description": input("Description: ").strip(),
        "Mechanic": input("Mechanic: ").strip(),
        "Tags": PromptList("Tags: "),
    }

    CreateItemFiles(Item)
    BackChoice = (input("\nReturn to main menu? (Y/n): ").strip()).capitalize()
    BackChoice = BackChoice[0]

    if BackChoice == "Y":
        RunTool("D:\Mistress.py")

while True:
    MainItem()