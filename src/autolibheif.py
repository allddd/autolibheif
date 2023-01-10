import os
import time
import subprocess
import webbrowser
from .const import *

wish_ext = None
wish_qty = None
wish_dir = None


# Menus
def main():
    while True:

        clear()
        print(head)
        print(main_menu)

        usr_inp = input(num_prompt)

        if usr_inp == '1':
            decodemenu()
            break

        elif usr_inp == '2':
            encodemenu()
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
    global wish_ext

    while True:

        clear()
        print(head)
        print(dec_menu)

        usr_inp = input(num_prompt)

        if usr_inp == '1':
            wish_ext = '.jpg'
            decqty()
            break

        elif usr_inp == '2':
            wish_ext = '.png'
            decqty()
            break

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
    global wish_ext

    while True:

        clear()
        print(head)
        print(enc_menu)

        usr_inp = input(num_prompt)

        if usr_inp == '1':
            wish_ext = '.HEIC'
            encqty()
            break

        elif usr_inp == '2':
            wish_ext = '.HEIF'
            encqty()
            break

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
    global wish_qty

    while True:

        clear()
        print(head)
        print(f'{row}{qty_txt}')
        print(qty_menu)

        usr_inp = input(def_prompt)

        if (not usr_inp):
            wish_qty = '100'
            decdir()
            break

        elif usr_inp == '1':
            wish_qty = '100'
            decdir()
            break

        elif usr_inp == '2':
            wish_qty = '85'
            decdir()
            break

        elif usr_inp == '3':
            wish_qty = '50'
            decdir()
            break

        elif usr_inp == '4':
            wish_qty = '25'
            decdir()
            break

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
    global wish_qty

    while True:

        clear()
        print(head)
        print(f'{row}{qty_txt}')
        print(qty_menu)

        usr_inp = input(def_prompt)

        if (not usr_inp):
            wish_qty = '-L'
            encdir()
            break

        elif usr_inp == '1':
            wish_qty = '-L'
            encdir()
            break

        elif usr_inp == '2':
            wish_qty = '85'
            encdir()
            break

        elif usr_inp == '3':
            wish_qty = '50'
            encdir()
            break

        elif usr_inp == '4':
            wish_qty = '25'
            encdir()
            break

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
    global wish_dir

    while True:

        clear()
        print(head)
        wish_dir = input(dir_prompt)

        if (not wish_dir):
            main()
            break

        elif wish_dir == 'h':
            print(help_dir)
            ent()
            continue

        elif os.path.isdir(wish_dir):
            print(f'{row}{dir_txt} {wish_dir}{row}')

            if len(os.listdir(wish_dir)) == 0:
                print(empty_err)
                ent()
                continue

            else:
                for pht in os.listdir(wish_dir):
                    if pht.endswith('.HEIC'):
                        decode()
                        break

                    elif pht.endswith('.heic'):
                        decode()
                        break

                    elif pht.endswith('.HEIF'):
                        decode()
                        break

                    elif pht.endswith('.heif'):
                        decode()
                        break

                else:
                    print(nofiles_err)
                    ent()
                    continue

        else:
            print(f'{row}{dir_err}')
            ent()
            continue


def encdir():
    global wish_dir

    while True:

        clear()
        print(head)
        wish_dir = input(dir_prompt)

        if (not wish_dir):
            main()
            break

        elif wish_dir == 'h':
            print(help_dir)
            ent()
            continue

        elif os.path.isdir(wish_dir):
            print(f'{row}{dir_txt} {wish_dir}{row}')

            if len(os.listdir(wish_dir)) == 0:
                print(empty_err)
                ent()
                continue

            else:
                for pht in os.listdir(wish_dir):
                    if pht.endswith('.jpg'):
                        encode()
                        break

                    elif pht.endswith('.JPG'):
                        encode()
                        break

                    elif pht.endswith('.png'):
                        encode()
                        break

                    elif pht.endswith('.PNG'):
                        encode()
                        break

                else:
                    print(nofiles_err)
                    ent()
                    continue

        else:
            print(f'{row}{dir_err}')
            ent()
            continue


# Converting
def decode():
    cwd = os.getcwd()
    os.chdir(wish_dir)
    fnum = len(os.listdir())

    for pht in os.listdir():
        if pht.endswith('.HEIC'):
            name_wo = pht[:-5]
            print(f'Converting {pht} to {name_wo}{wish_ext}')
            subprocess.run(['heif-convert', '-q', wish_qty, '--quiet', pht, name_wo + wish_ext])

        elif pht.endswith('.heic'):
            name_wo = pht[:-5]
            print(f'Converting {pht} to {name_wo}{wish_ext}')
            subprocess.run(['heif-convert', '-q', wish_qty, '--quiet', pht, name_wo + wish_ext])

        elif pht.endswith('.HEIF'):
            name_wo = pht[:-5]
            print(f'Converting {pht} to {name_wo}{wish_ext}')
            subprocess.run(['heif-convert', '-q', wish_qty, '--quiet', pht, name_wo + wish_ext])

        elif pht.endswith('.heif'):
            name_wo = pht[:-5]
            print(f'Converting {pht} to {name_wo}{wish_ext}')
            subprocess.run(['heif-convert', '-q', wish_qty, '--quiet', pht, name_wo + wish_ext])

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


def encode():
    cwd = os.getcwd()
    os.chdir(wish_dir)
    fnum = len(os.listdir())

    for pht in os.listdir():
        if pht.endswith('.jpg'):
            name_wo = pht[:-4]
            print(f'Converting {pht} to {name_wo}{wish_ext}')
            subprocess.run(['heif-enc', '-q', wish_qty, pht, '-o', name_wo + wish_ext])

        elif pht.endswith('.JPG'):
            name_wo = pht[:-4]
            print(f'Converting {pht} to {name_wo}{wish_ext}')
            subprocess.run(['heif-enc', '-q', wish_qty, pht, '-o', name_wo + wish_ext])

        elif pht.endswith('.png'):
            name_wo = pht[:-4]
            print(f'Converting {pht} to {name_wo}{wish_ext}')
            subprocess.run(['heif-enc', '-q', wish_qty, pht, '-o', name_wo + wish_ext])

        elif pht.endswith('.PNG'):
            name_wo = pht[:-4]
            print(f'Converting {pht} to {name_wo}{wish_ext}')
            subprocess.run(['heif-enc', '-q', wish_qty, pht, '-o', name_wo + wish_ext])

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
