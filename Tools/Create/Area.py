import os, json, subprocess, sys

def PromptList(Prompt):
    V = input(Prompt).strip()
    if not V:
        return []
    return [X.strip() for X in V.split(",")]

def CreateAreaFiles(Area):
    Title = Area.get("Title", "Untitled")
    Parent = Area.get("Parent", "").strip()

    DirBase = os.path.dirname(os.path.abspath(f"{__file__}../../../"))

    if Parent:
        DirParent = os.path.join(DirBase, "Areas", *Parent.split("/"))
    else:
        DirParent = os.path.join(DirBase, "Areas")

    DirArea = os.path.join(DirParent, Title)
    os.makedirs(DirArea, exist_ok=True)

    DirJson = os.path.join(DirArea, f"{Title}.json")
    DirTxt = os.path.join(DirArea, f"{Title}.txt")

    with open(DirJson, "w", encoding="utf-8") as F:
        json.dump(Area, F, indent=4)

    Tags = Area.get("Tags", [])
    FormattedTags = " ".join(f"#{Tag}" for Tag in Tags)

    FormattedContent = (
        f"{FormattedTags}\n\n"
        f"{Area.get('Name', '')} ({Area.get('Size', '')}, {Area.get('Temperature', '')} temperature)\n\n"
        f"{Area.get('Appearance', '')}\n\n"
        f"{Area.get('Description', '')}\n"
    )

    with open(DirTxt, "w", encoding="utf-8") as F:
        F.write(FormattedContent)

    print(f"Area created at: {DirArea}")

def RunTool(RelPath):
    PythonExe = sys.executable
    subprocess.call([PythonExe, RelPath])

def MainArea():
    Area = {
        "Title": input("Title: ").strip(),
        "Name": input("Name: ").strip(),
        "Parent": input("Parent: ").strip(),
        "Size": input("Size: ").strip(),
        "Temperature": input("Temperature: ").strip(),
        "Appearance": input("Appearance: ").strip(),
        "Description": input("Description: ").strip(),
        "Tags": PromptList("Tags: ")
    }

    CreateAreaFiles(Area)
    BackChoice = (input("\nReturn to main menu? (Y/n): ").strip()).capitalize()
    BackChoice = BackChoice[0]

    if BackChoice == "Y":
            RunTool("D:\Mistress.py")

while True:
    MainArea()