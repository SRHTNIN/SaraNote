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

def CreateCharFiles(Character):
    Title = Character.get("Title", "Untitled")

    DirBase = os.path.dirname(os.path.abspath(f"{__file__}../../../"))
    DirChars = os.path.join(DirBase, "Characters")
    DirChar = os.path.join(DirChars, Title)

    os.makedirs(DirChar, exist_ok=True)

    DirJson = os.path.join(DirChar, f"{Title}.json")
    DirTxt = os.path.join(DirChar, f"{Title}.txt")

    with open(DirJson, "w", encoding="utf-8") as File:
        json.dump(Character, File, indent=4)

    Tags = Character.get("Tags", [])
    Powers = Character.get("Powers", [])

    FormattedTags = " ".join(f"#{Tag}" for Tag in Tags)
    FormattedPowers = ", ".join(Powers)

    Content = (
        f"{FormattedTags}\n\n"
        f"{Character.get('Name', '')} ({Character.get('Age', '')}, {Character.get('Gender', '')})\n"
        f"{Character.get('Pronouns', '')}\n\n"
        f"{Character.get('Alignment', '')}\n\n"
        f"Powers: {FormattedPowers}\n\n"
        f"{Character.get('Appearance', '')}\n\n"
        f"{Character.get('Description', '')}\n"
    )

    with open(DirTxt, "w", encoding="utf-8") as File:
        File.write(Content)

def RunTool(RelPath):
    PythonExe = sys.executable
    subprocess.call([PythonExe, RelPath])

def MainChar():
    Clear()

    Character = {
        "Title": input("Title: ").strip(),
        "Name": input("Name: ").strip(),
        "Age": input("Age: ").strip(),
        "Gender": input("Gender: ").strip(),
        "Pronouns": input("Pronouns: ").strip(),
        "Alignment": input("Alignment: ").strip(),
        "Powers": PromptList("Powers: "),
        "Appearance": input("Appearance: ").strip(),
        "Description": input("Description: ").strip(),
        "Tags": PromptList("Tags: ")
    }

    CreateCharFiles(Character)
    BackChoice = (input("\nReturn to main menu? (Y/n): ").strip()).capitalize()
    BackChoice = BackChoice[0]

    if BackChoice == "Y":
        RunTool("D:\Mistress.py")

while True:
    MainChar()