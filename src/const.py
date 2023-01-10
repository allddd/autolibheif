#
num_prompt = '''Type a number and confirm
==> '''
def_prompt = '''Type a number and confirm 
(leave blank for default)
==> '''
dir_prompt = '''
Type in full path to the photos folder and confirm
(leave blank to return to the main menu)
==> '''

#
undef_err = 'Something went wrong'
num_err = 'Please enter a valid number'
dir_err = 'Specified directory does not exist'
empty_err = 'Specified directory is empty'
nofiles_err = 'There are no files to convert in the specified directory'

#
row = '''
'''
enter = 'Press Enter to continue'
dir_txt = 'Looking for files in'
succ_txt = 'Successfully converted'
qty_txt = 'Select the desired conversion quality'

#
main_menu = ('''
[1] Decode (convert HEIC/HEIF file)
[2] Encode (convert file to HEIC/HEIF)
[3] Help
[4] Quit
''')
qty_menu = ('''
[1] Maximum (default)
[2] Decent
[3] Medium
[4] Low
[5] Exit to main menu
''')
dec_menu = ('''
[1] Convert to .jpg
[2] Convert to .png
[3] Exit to main menu
''')
enc_menu = ('''
[1] Convert to .HEIC
[2] Convert to .HEIF
[3] Exit to main menu
''')
help_menu = '''
[1] Exit to main menu (default)
[2] Visit the Github page
'''

#
help_main = ('''
Autolibheif is a Linux CLI utility for convenient
encoding and decoding of the HEIF/HEIC file format

If you need help at any time, type "h" and confirm
to get instructions for each individual step

Want to report a problem or request a feature ?
Select option [2] and visit the Github page
''')
help_decenc = ('''
Files will be converted to the file type you select here
''')
help_qty = ('''
The converted file retains a specific percentage of the 
original's quality, depending on what you select here

Maximum = 100%
Decent = 85%
Medium = 50%
Low = 25%
''')
help_dir = ('''
All compatible files in the folder specified
here will be converted to the desired file type

Other files and originals will remain intact

Enter the folder path in this format:
/home/user/Pictures
''')

#
github = 'https://github.com/allddd/autolibheif'
head = '''
 ▄▀▄ █ █ ▀█▀ ▄▀▄ █   █ ██▄ █▄█ ██▀ █ █▀
 █▀█ ▀▄█  █  ▀▄▀ █▄▄ █ █▄█ █ █ █▄▄ █ █▀
                                 v1.0.2'''
