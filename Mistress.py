import os, subprocess, sys

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def FindTools(BaseDir):
    Tools = []

    for Root, Dirs, Files in os.walk(BaseDir):
        Dirs[:] = [D for D in Dirs if not D.startswith(".")]

        for File in Files:
            if File.endswith(".py"):
                FullPath = os.path.join(Root, File)
                RelPath = os.path.relpath(FullPath, BaseDir)
                Tools.append((File.replace(".py", ""), RelPath))

    return Tools

def ChooseTool(Tools):
    while True:
        Clear()
        print("Select a tool:\n")

        for i, (Name, Path) in enumerate(Tools):
            Display = Path.replace(os.sep, " / ").replace(".py", "")
            print(f"{i}: {Display}")

        Choice = input("\nChoice: ").strip()

        if Choice.isdigit():
            Index = int(Choice)
            if 0 <= Index < len(Tools):
                return Tools[Index]

        for Name, Path in Tools:
            if Choice.lower() == Name.lower():
                return Name, Path

def RunTool(RelPath):
    PythonExe = sys.executable
    subprocess.call([PythonExe, RelPath])

def Main():
    DirBase = os.path.dirname(os.path.abspath(__file__))
    DirTools = os.path.join(DirBase, "Tools")

    while True:
        Tools = FindTools(DirTools)
        if not Tools:
            print("No tools found.")
            input("\nPress Enter...")
            return

        Name, Path = ChooseTool(Tools)
        FullPath = os.path.join(DirTools, Path)

        Clear()
        print(f"Running: {Name}\n")
        RunTool(FullPath)

if __name__ == "__main__":
    Main()
