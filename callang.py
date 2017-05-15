import subprocess

'''
subprocess.call(['executable path','filename']
subprocess.call(['C:\\Octave\\Octave-4.2.1\\bin\\octave-gui.exe','test2.m'])

octave has:
    -octave.exe
    -octave-cli.exe
    -octave-gui.exe

r has:
    -R.exe
    -Rscript.exe

'''

# Currently hardcoded paths
octave_cli_path = 'C:\\Octave\\Octave-4.2.1\\bin\\octave-cli.exe'
octave_gui_path = 'C:\\Octave\\Octave-4.2.1\\bin\\octave-gui.exe'

rscript_path = 'C:\\Program Files\\R\\R-3.3.2\\bin\\Rscript.exe'
r_cli_path = 'C:\\Program Files\\R\\R-3.3.2\\bin\\R.exe'
r_gui_path = 'C:\\Program Files\\RStudio\\bin\\rstudio.exe' # actually calling RStudio not R

def test():
    r_file = 'rtest.r'
    m_file = 'test2.m'


    sub_call_octave = [octave_cli_path,m_file]
    sub_call_r = [rscript_path,r_file]

    subprocess.call(sub_call_octave)

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
'''


def gui(lang):
    str_lang = str(lang).lower()
    if str_lang == 'help':
        print('help')
    elif str_lang == 'octave':
        subprocess.call(octave_gui_path)
    elif str_lang == 'r':
        subprocess.call(r_gui_path)
    else:
        print('Not a valid language...')

def cli(lang):
    str_lang = str(lang).lower()
    if str_lang == 'help':
        print('Current avaliable CLIs are: ')
        print('- Octave\n- R')
    elif str_lang == 'octave':
        subprocess.call(octave_cli_path)
    elif str_lang == 'r':
        subprocess.call(r_cli_path)
    else:
        print('Not a valid Command Line Interface name...')

def script(lang,filename):
    str_lang = str(lang).lower()
    if str_lang == 'help':
        print('help')
    elif str_lang == 'octave':
        lang_path = octave_cli_path
    elif str_lang == 'r':
        lang_path = rscript_path
    else:
        print('Not a valid language')
    print('Running:\n\n   ---File:     [ %s ]\n   ---Language: [ %s ]\n...'%(filename,str_lang.upper()))
    sub_call = [lang_path,filename]
    subprocess.call(sub_call)
