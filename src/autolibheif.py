import os
import time
import subprocess
import webbrowser
from .const import *


dec_ext = ('.heif', '.HEIF', '.heic', '.HEIC')
enc_ext = ('.jpg', '.JPG', '.png', '.PNG')


# Menus
def main():
    while True:

        clear()
        print(head)
        print(main_menu)

        usr_inp = input(num_prompt)

        if usr_inp == '1':
            decode(ext=decodemenu(), qty=decqty(), dirr=decdir())
            break

        elif usr_inp == '2':
            encode(ext=encodemenu(), qty=encqty(), dirr=encdir())
            break

        elif usr_inp == '3':
            helpmenu()
            break

        elif usr_inp == 'h':
            helpmenu()
            break

        elif usr_inp == '4':
            clear()
            quit()

        else:
            print(num_err)
            time.sleep(1)
            continue


def decodemenu():
    while True:

        clear()
        print(head)
        print(dec_menu)

        usr_inp = input(num_prompt)

        if usr_inp == '1':
            ext = '.jpg'
            return ext

        elif usr_inp == '2':
            ext = '.png'
            return ext

        elif usr_inp == '3':
            main()
            break

        elif usr_inp == 'h':
            print(help_decenc)
            ent()
            continue

        else:
            print(num_err)
            time.sleep(1)
            continue


def encodemenu():
    while True:

        clear()
        print(head)
        print(enc_menu)

        usr_inp = input(num_prompt)

        if usr_inp == '1':
            ext = '.HEIC'
            return ext

        elif usr_inp == '2':
            ext = '.HEIF'
            return ext

        elif usr_inp == '3':
            main()
            break

        elif usr_inp == 'h':
            print(help_decenc)
            ent()
            continue

        else:
            print(num_err)
            time.sleep(1)
            continue


def helpmenu():
    while True:

        clear()
        print(head)
        print(help_main)
        print(help_menu)

        usr_inp = input(def_prompt)

        if (not usr_inp):
            main()
            break

        elif usr_inp == '1':
            main()
            break

        elif usr_inp == '2':
            webbrowser.open(github)
            main()
            break

        else:
            print(num_err)
            time.sleep(1)
            continue


# Quality select
def decqty():
    while True:

        clear()
        print(head)
        print(f'{row}{qty_txt}')
        print(qty_menu)

        usr_inp = input(def_prompt)

        if (not usr_inp):
            qty = '100'
            return qty

        elif usr_inp == '1':
            qty = '100'
            return qty

        elif usr_inp == '2':
            qty = '85'
            return qty

        elif usr_inp == '3':
            qty = '50'
            return qty

        elif usr_inp == '4':
            qty = '25'
            return qty

        elif usr_inp == '5':
            main()
            break

        elif usr_inp == 'h':
            print(help_qty)
            ent()
            continue

        else:
            print(num_err)
            time.sleep(1)
            continue


def encqty():
    while True:

        clear()
        print(head)
        print(f'{row}{qty_txt}')
        print(qty_menu)

        usr_inp = input(def_prompt)

        if (not usr_inp):
            qty = '-L'
            return qty

        elif usr_inp == '1':
            qty = '-L'
            return qty

        elif usr_inp == '2':
            qty = '85'
            return qty

        elif usr_inp == '3':
            qty = '50'
            return qty

        elif usr_inp == '4':
            qty = '25'
            return qty

        elif usr_inp == '5':
            main()
            break

        elif usr_inp == 'h':
            print(help_qty)
            ent()
            continue

        else:
            print(num_err)
            time.sleep(1)
            continue


# Directory select
def decdir():
    while True:

        clear()
        print(head)
        dirr = input(dir_prompt)

        if (not dirr):
            main()
            break

        elif dirr == 'h':
            print(help_dir)
            ent()
            continue

        elif os.path.isdir(dirr):
            print(f'{row}{dir_txt} {dirr}{row}')

            if len(os.listdir(dirr)) == 0:
                print(empty_err)
                ent()
                continue

            else:
                for pht in os.listdir(dirr):
                    if pht.endswith(dec_ext):
                        return dirr

                else:
                    print(nofiles_err)
                    ent()
                    continue

        else:
            print(f'{row}{dir_err}')
            ent()
            continue


def encdir():
    while True:

        clear()
        print(head)
        dirr = input(dir_prompt)

        if (not dirr):
            main()
            break

        elif dirr == 'h':
            print(help_dir)
            ent()
            continue

        elif os.path.isdir(dirr):
            print(f'{row}{dir_txt} {dirr}{row}')

            if len(os.listdir(dirr)) == 0:
                print(empty_err)
                ent()
                continue

            else:
                for pht in os.listdir(dirr):
                    if pht.endswith(enc_ext):
                        return dirr

                else:
                    print(nofiles_err)
                    ent()
                    continue

        else:
            print(f'{row}{dir_err}')
            ent()
            continue


# Converting
def decode(ext, qty, dirr):
    cwd = os.getcwd()
    os.chdir(dirr)
    fnum = len(os.listdir())

    for pht in os.listdir():
        if pht.endswith(dec_ext):
            name_wo = pht[:-5]
            print(f'Converting {pht} to {name_wo}{ext}')
            subprocess.run(['heif-convert', '-q', qty, '--quiet', pht, name_wo + ext])

    else:
        new_fnum = len(os.listdir())
        conv_num = new_fnum - fnum

        if conv_num > 0:
            print(f'{row}{succ_txt} {conv_num} files')
            os.chdir(cwd)
            ent()
            main()

        else:
            print(undef_err)
            ent()
            os.chdir(cwd)
            main()


def encode(ext, qty, dirr):
    cwd = os.getcwd()
    os.chdir(dirr)
    fnum = len(os.listdir())

    for pht in os.listdir():
        if pht.endswith(enc_ext):
            name_wo = pht[:-4]
            print(f'Converting {pht} to {name_wo}{ext}')
            subprocess.run(['heif-enc', '-q', qty, pht, '-o', name_wo + ext])

    else:
        new_fnum = len(os.listdir())
        conv_num = new_fnum - fnum

        if conv_num > 0:
            print(f'{row}{succ_txt} {conv_num} files')
            os.chdir(cwd)
            ent()
            main()

        else:
            print(undef_err)
            ent()
            os.chdir(cwd)
            main()


# Other functions
def clear():
    os.system('clear')


def ent():
    print(enter)
    os.system('read -s')
