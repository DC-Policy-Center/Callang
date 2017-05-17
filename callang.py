'''
Callang calls other languages to run scripts while in python.
There are two languages being implemented now: Octave and R.
These languages have different executables associated with their calling processing

##### Executables used in python's subpocess call to run CLI, GUI, or Script

| <center> Use </center>         | Octave           | R           |
|:-------------------------------|:----------------:|:-----------:|
|Script execution                | octave.exe       | R.exe       |
|Command line interface (CLI)    | octave-cli.exe   | R.exe       |
|Graphical user interface (GUI)  | octave-gui.exe   | Rstudio.exe |


Dependencies: OS, subprocess, fnmatch;



|Signature-------------------------------------------|
|Written for DC Policy Center by Michael Watson; 2017|
|www.DCPolicyCenter.org / DC-Policy-Center.github.io |
|github:M-Watson & MW-DC-Policy-Center               |
|----------------------------------------------------|
'''

import subprocess
import fnmatch as fnm

import os
import sys

sys.path.append('./lib/')

import callangHelpers

#### Find the versions of the languages if installed in default windows locations ##
# Default R location with versioning in windows
r_abs_path = 'C:\\Program Files\\R\\'
r_version = callangHelpers.directoryClean('r')

# Default Octave location with versioning in windows
octave_abs_path = 'C:\\Octave\\'
octave_version = callangHelpers.directoryClean('octave')


### Currently semi-hardcoded paths, will only work in default install on windows ###
# Octave paths
octave_cli_path = '%s%s\\bin\\octave-cli.exe'%(octave_abs_path,octave_version)
octave_gui_path = '%s%s\\bin\\octave-gui.exe'%(octave_abs_path,octave_version)
# R Paths
rscript_path = '%s%s\\bin\\Rscript.exe'%(r_abs_path,r_version)
r_cli_path = '%s%s\\bin\\R.exe'%(r_abs_path,r_version)
# R Studio default path
r_gui_path = 'C:\\Program Files\\RStudio\\bin\\rstudio.exe' # actually calling RStudio not R

def test():
    r_file = '.\\Scripts\\rtest.r'
    m_file = '.\\Scripts\\test2.m'


    sub_call_octave = [octave_cli_path,m_file]
    sub_call_r = [rscript_path,r_file]

    subprocess.call(sub_call_octave)


def version(lang):
# Check the version of a language installed
    str_lang = str(lang).lower()
    if str_lang == 'help':
        print('version(lang) checks the version of the [lang] requsted')
        print('Current avaliable languages are: ')
        print('- Octave\n- R')
    elif str_lang == 'octave':
        print('You are working with Octave version: %s'%(octave_version))
    elif str_lang == 'r':
        print('You are working with R version: %s'%(r_version))
    else:
        print('Not a valid language...')

def gui(lang):
# gui(lang) Open the corresponding GUI for the requsted [lang]
    str_lang = str(lang).lower()
    if str_lang == 'help':
        print('gui(lang) Open the corresponding GUI for the requsted [lang]')
        print('Current avaliable GUIs are: ')
        print('- Octave\n- R (through R Studio)')
    elif str_lang == 'octave':
        print('Opening GUI for %s ...\n\n'%(str_lang))
        subprocess.call(octave_gui_path)
    elif str_lang == 'r':
        print('Opening GUI for %s ...\n\n'%(str_lang))
        subprocess.call(r_gui_path)
    else:
        print('Not a valid language...')

def cli(lang):
    str_lang = str(lang).lower()
    if str_lang == 'help':
        print('Current avaliable CLIs are: ')
        print('- Octave\n- R')
    elif str_lang == 'octave':
        print('Opening CLI for %s ...\n\n'%(str_lang))
        subprocess.call(octave_cli_path)
    elif str_lang == 'r':
        print('Opening CLI for %s ...\n\n'%(str_lang))
        subprocess.call(r_cli_path)
    else:
        print('Not a valid Command Line Interface name...')

def script(filename):
    if filename == 'help':
        print('help')
    elif fnm.fnmatch(filename,'*.m'):
        lang = 'Octave'
        lang_path = octave_cli_path
        #filename = 'source("%s")'%(filename)
    elif fnm.fnmatch(filename,'*.r'):
        lang = 'R'
        lang_path = rscript_path
    else:
        print('Not a valid language')
    print('Running:\n\n   ---File:     [ %s ]\n   ---Language: [ %s ]\n...'%(filename,lang))
    sub_call = [lang_path,filename]
    subprocess.call(sub_call)
