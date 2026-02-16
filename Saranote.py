import os, subprocess, sys

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def FindTools(ToolsDir):
    ToolList = []

    for Root, Dirs, Files in os.walk(ToolsDir):
        Dirs[:] = [D for D in Dirs if not D.startswith(".")]

        for File in Files:
            if File.endswith(".py"):
                FullPath = os.path.join(Root, File)
                RelPath = os.path.relpath(FullPath, ToolsDir)
                Name = RelPath.replace(".py", "")
                ToolList.append((Name, FullPath))

    return ToolList

def ChooseOption(Prompt, Options):
    while True:
        Clear()
        print(Prompt + "\n")

        for i, (Name, _) in enumerate(Options):
            Display = Name.replace(os.sep, " / ")
            print(f"{i}: {Display}")

        Choice = input("\nChoice: ").strip()

        if Choice.isdigit():
            Index = int(Choice)
            if 0 <= Index < len(Options):
                return Options[Index]

        for Name, Path in Options:
            if Choice.lower() == Name.lower():
                return (Name, Path)

def Main():
    DirBase = os.path.dirname(os.path.abspath(__file__))
    ToolsDir = os.path.join(DirBase, "Tools")

    while True:
        Tools = FindTools(ToolsDir)

        if not Tools:
            print("No tools found.")
            input("\nPress Enter...")
            return

        Name, Path = ChooseOption("Select tool:", Tools)

        Clear()
        print(f"Running: {Name}\n")

        subprocess.call([sys.executable, Path])

if __name__ == "__main__":
    Main()