# Callang
Callang calls other languages to run scripts while in python.

## Currently implemented languages
- Octave
  * MatLab<sup>1</sup> clone with some reverse compatability
  * Used for matric processing and general analytics
- R
  * General statistical analysis language


##### Executables used in python's subpocess call to run CLI, GUI, or Script

| <center> Use </center>         | Octave           | R           |  
|:-------------------------------|:----------------:|:-----------:|
|Script execution                | octave.exe       | R.exe       |
|Command line interface (CLI)    | octave-cli.exe   | R.exe       |
|Graphical user interface (GUI)  | octave-gui.exe   | Rstudio.exe |


## Issues noticed

- Octave (.m) files will only run on relative paths if they are scripts, not functions
- <s>Different versions of R installed are located in different folders.  This can be solved by reading the directory with os rather than hardcoded.</s>
  - Solved, somewhat ugly but reads directory, creates a string of the folder name and version, and then appends as the directory absolute path.  Still only works on windows and in default installation location.
-GUI call leaves command line inoperable until the GUI is closed


## License


## Footnotes
<sup>1</sup> MatLab proprietary software is the registered trademark of [MathWorks, Inc.](https://www.mathworks.com/company/aboutus/policies_statements/trademarks.html?s_tid=gf_trd)
