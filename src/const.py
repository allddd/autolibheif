#
num_prompt = '''Type a number and confirm
==> '''
dir_prompt = '''
Type in full path to the photos folder and confirm
(leave blank to return to the main menu)
==> '''
def_prompt = '''Type a number and confirm 
(leave blank for default)
==> '''
enter = 'Press Enter to return to the main menu'

#
undef_errmsg = 'Something went wrong'
num_errmsg = 'Please enter a valid number'
dir_errmsg = 'Specified directory does not exist'
empty_errmsg = 'Specified directory is empty'
nofiles_errmsg = 'There are no files to convert in the specified directory'

#
new_row = '''
'''
dirchosen_txt = '''
Looking for files in'''
succesconv_txt = '''
Successfully converted'''
qty_txt = '''
Select the desired conversion quality'''

#
main_menu = ('''
[1] Decode (convert HEIC/HEIF image)
[2] Encode (convert image to HEIC/HEIF)
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
Help = ('''
Autolibheif is a CLI utility for encoding and 
decoding the HEIF/HEIC file format.

If you need help at any time, type "h" and confirm
to get instructions for each individual step.

Want to report a problem or request a feature ?
Select option [2] and visit the Github page.
''')

#
head = '''
 ▄▀▄ █ █ ▀█▀ ▄▀▄ █   █ ██▄ █▄█ ██▀ █ █▀
 █▀█ ▀▄█  █  ▀▄▀ █▄▄ █ █▄█ █ █ █▄▄ █ █▀
                                 v1.0.1'''
