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

def CreateGameFiles(Game):
    Title = Game.get("Title", "Untitled")

    DirBase = os.path.dirname(os.path.abspath(f"{__file__}../../../"))
    DirGames = os.path.join(DirBase, "Games")
    DirGame = os.path.join(DirGames, Title)

    os.makedirs(DirGame, exist_ok=True)

    DirJson = os.path.join(DirGame, f"{Title}.json")
    DirTxt = os.path.join(DirGame, f"{Title}.txt")

    with open(DirJson, "w", encoding="utf-8") as File:
        json.dump(Game, File, indent=4)

    Tags = Game.get("Tags", [])
    FormattedTags = " ".join(f"#{Tag}" for Tag in Tags)

    Content = (
        f"{FormattedTags}\n\n"
        f"{Game.get('Title', '')}\n"
        f"Dimension: {Game.get('Dimension', 'None')}\n"
        f"Viewpoint: {Game.get('Viewpoint', 'None')}\n"
        f"Mechanic: {Game.get('Mechanic', 'None')}\n"
        f"Main Character: {Game.get('MainChar', 'None')}\n\n"
        f"Gameplay Loop:\n{Game.get('GameplayLoop', 'None')}\n\n"
        f"Description:\n{Game.get('Description', 'None')}\n"
    )

    with open(DirTxt, "w", encoding="utf-8") as File:
        File.write(Content)

def RunTool(RelPath):
    PythonExe = sys.executable
    subprocess.call([PythonExe, RelPath])

def MainGame():
    Clear()

    Game = {
        "Title": input("Title: ").strip(),
        "Dimension": input("Dimension: ").strip(),
        "Viewpoint": input("Viewpoint: ").strip(),
        "Mechanic": input("Mechanic: ").strip(),
        "MainChar": input("Main Character: ").strip(),
        "GameplayLoop": input("Gameplay Loop: ").strip(),
        "Description": input("Description: ").strip(),
        "Tags": PromptList("Tags: "),
    }

    CreateGameFiles(Game)
    BackChoice = (input("\nReturn to main menu? (Y/n): ").strip()).capitalize()
    BackChoice = BackChoice[0]

    if BackChoice == "Y":
        RunTool("D:\Mistress.py")

while True:
    MainGame()