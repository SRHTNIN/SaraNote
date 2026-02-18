# Saranote
 A format-agnostic, FOSS, category-based note-taking program.
 It's made by Sarah, hence the name. :3

# Useful tips
All the default files, like the format and parameters, are in .Defaults.
You may change the default format file to any type of file, like .md, html or .txt.

HOWEVER, the variables need to stay in the same format.
You can't change the variable wrapping to not be percentage symbols.

Format.md -> Format.html
Works.

%Variable% -> #Variable#
Breaks the program.

Also, do note that Parameters.json need to mirror the Format files.
This means that while you don't NEED to have every parameter into your Format file,
you do can't make new variables in your Format file without having that variable in Parameters.json.