''' STANDARD LANG IF STATEMENTS
str_lang = str(lang).lower()
if str_lang == 'help':
    print('help')
elif str_lang == 'octave':
    DO OCTAVE THING
elif str_lang == 'r':
    DO R THING
else:
    print('Not a valid language...')

    still
'''
import os

def directoryClean(lang):
    str_lang = str(lang).lower()
    if str_lang == 'help':
        print('help')
        version = 'none'
    elif str_lang == 'octave':
        octave_abs_path = 'C:\\Octave\\'
        octave_directories = []
        for item in os.walk(octave_abs_path):
            octave_directories.append(item)
            octave_version_raw = octave_directories[0][1]
            string_version = str(octave_version_raw)
        list_version = []
        for letter in string_version:
            list_version.append(letter)
        list_version.pop(0)
        list_version.pop(0)
        list_version.pop(len(list_version)-1)
        list_version.pop(len(list_version)-1)
        octave_version = ''.join(list_version)
        version = octave_version

    elif str_lang == 'r':
        r_abs_path = 'C:\\Program Files\\R\\'
        r_directories = []
        for item in os.walk(r_abs_path):
            r_directories.append(item)
            r_version_raw = r_directories[0][1]
            string_version = str(r_version_raw)
        list_version = []
        for letter in string_version:
            list_version.append(letter)
        list_version.pop(0)
        list_version.pop(0)
        list_version.pop(len(list_version)-1)
        list_version.pop(len(list_version)-1)
        r_version = ''.join(list_version)
        version = r_version
    else:
        print('Not a valid language...')
        version = 'none'
    return(version)
