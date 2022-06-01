"""
Debes utilizar todo lo que sabes sobre los strings, las listas y sus métodos o funciones 
para transformar el siguiente texto: 

    thor lanzó su  martillo#flash ha fallado por  un pie!  -gritó Loki Laufeyson#dos 
    pies -le corrigió Hulk#flash menea la cabeza como disgustado... -agrega el 
    comentarista 

En:
 
    Thor lanzó su martillo... 
    - ¡Flash ha fallado por un pie! -gritó Loki Laufeyson. 
    - Dos pies le corrigió Hulk. 
    - Flash menea la cabeza como disgustado... -agrega el comentarista. 
    
Es prohibido modificar directamente el texto.
"""

# Initial text
text = "thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos \
pies -le corrigió Hulk#flash menea la cabeza como disgustado... -agrega el \
comentarista"
print(text)
print()

# Separate text in lines
## Create string list with the different lines of the text
separate_text_for_lines = text.split("#")

## Separate each list items in a string variable
line_1 = separate_text_for_lines[0]
line_2 = separate_text_for_lines[1]
line_3 = separate_text_for_lines[2]
line_4 = separate_text_for_lines[3]

# Modify each line
## Line 1 
line_1 = line_1.capitalize()
line_1 = line_1 + "...\n"

## Line 2 
aux_line = line_2.split("-")
line_2 = "- ¡" + aux_line[0].capitalize() + "-" + aux_line[1] + ".\n"

## Line 3 
aux_line = line_3.split("-")
line_3 = "- ¡" + aux_line[0].capitalize() + aux_line[1] + ".\n"

## Line 4 
line_4 = "- " + line_4.capitalize() + "."

# Join all lines into a single string
final_text = line_1 + line_2 + line_3 + line_4

# Print the corrected text
print(final_text)