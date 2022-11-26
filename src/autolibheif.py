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
            decode_menu()
            break

        elif usr_inp == '2':
            encode_menu()
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
            print(num_errmsg)
            time.sleep(1)
            continue


def decode_menu():
    global wish_ext

    while True:

        clear()
        print(head)
        print(dec_menu)

        usr_inp = input(num_prompt)

        if usr_inp == '1':
            wish_ext = '.jpg'
            dec_qty()
            break

        elif usr_inp == '2':
            wish_ext = '.png'
            dec_qty()
            break

        elif usr_inp == '3':
            main()
            break

        else:
            print(num_errmsg)
            time.sleep(1)
            continue


def encode_menu():
    global wish_ext

    while True:

        clear()
        print(head)
        print(enc_menu)

        usr_inp = input(num_prompt)

        if usr_inp == '1':
            wish_ext = '.HEIC'
            enc_qty()
            break

        elif usr_inp == '2':
            wish_ext = '.HEIF'
            enc_qty()
            break

        elif usr_inp == '3':
            main()
            break

        else:
            print(num_errmsg)
            time.sleep(1)
            continue


def helpmenu():
    while True:

        clear()
        print(head)
        print(Help)
        print(help_menu)

        usr_inp = input(def_prompt)

        if (not usr_inp):
            main()
            break

        elif usr_inp == '1':
            main()
            break

        elif usr_inp == '2':
            webbrowser.open('https://github.com/allddd/autolibheif')
            main()
            break

        else:
            print(num_errmsg)
            time.sleep(1)
            continue


# Quality select
def dec_qty():
    global wish_qty

    while True:

        clear()
        print(head)
        print(qty_txt)
        print(qty_menu)

        usr_inp = input(def_prompt)

        if (not usr_inp):
            wish_qty = '100'
            dec_chosedir()
            break

        elif usr_inp == '1':
            wish_qty = '100'
            dec_chosedir()
            break

        elif usr_inp == '2':
            wish_qty = '85'
            dec_chosedir()
            break

        elif usr_inp == '3':
            wish_qty = '50'
            dec_chosedir()
            break

        elif usr_inp == '4':
            wish_qty = '25'
            dec_chosedir()
            break

        elif usr_inp == '5':
            main()
            break

        else:
            print(num_errmsg)
            time.sleep(1)
            continue


def enc_qty():
    global wish_qty

    while True:

        clear()
        print(head)
        print(qty_txt)
        print(qty_menu)

        usr_inp = input(def_prompt)

        if (not usr_inp):
            wish_qty = '-L'
            enc_chosedir()
            break

        elif usr_inp == '1':
            wish_qty = '-L'
            enc_chosedir()
            break

        elif usr_inp == '2':
            wish_qty = '85'
            enc_chosedir()
            break

        elif usr_inp == '3':
            wish_qty = '50'
            enc_chosedir()
            break

        elif usr_inp == '4':
            wish_qty = '25'
            enc_chosedir()
            break

        elif usr_inp == '5':
            main()
            break

        else:
            print(num_errmsg)
            time.sleep(1)
            continue


# Directory select
def dec_chosedir():
    global wish_dir

    while True:

        clear()
        print(head)
        wish_dir = input(dir_prompt)

        if (not wish_dir):
            main()
            break

        elif os.path.isdir(wish_dir):
            print(f'{dirchosen_txt} {wish_dir}{new_row}')

            if len(os.listdir(wish_dir)) == 0:
                print(empty_errmsg)
                time.sleep(2)
                continue

            else:
                for pht in os.listdir(wish_dir):
                    if pht.endswith('.HEIC'):
                        decode()
                        break

                    elif pht.endswith('.HEIF'):
                        decode()
                        break

                else:
                    print(nofiles_errmsg)
                    time.sleep(2)
                    continue

        else:
            print(f'{new_row}{dir_errmsg}')
            time.sleep(2)
            continue


def enc_chosedir():
    global wish_dir

    while True:

        clear()
        print(head)
        wish_dir = input(dir_prompt)

        if (not wish_dir):
            main()
            break

        elif os.path.isdir(wish_dir):
            print(f'{dirchosen_txt} {wish_dir}{new_row}')

            if len(os.listdir(wish_dir)) == 0:
                print(empty_errmsg)
                time.sleep(2)
                continue

            else:
                for pht in os.listdir(wish_dir):
                    if pht.endswith('.jpg'):
                        encode()
                        break

                    elif pht.endswith('.png'):
                        encode()
                        break

                else:
                    print(nofiles_errmsg)
                    time.sleep(2)
                    continue

        else:
            print(f'{new_row}{dir_errmsg}')
            time.sleep(2)
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

        elif pht.endswith('.HEIF'):
            name_wo = pht[:-5]
            print(f'Converting {pht} to {name_wo}{wish_ext}')
            subprocess.run(['heif-convert', '-q', wish_qty, '--quiet', pht, name_wo + wish_ext])
    else:
        new_fnum = len(os.listdir())
        conv_num = new_fnum - fnum

        if conv_num > 0:
            print(f'{succesconv_txt} {conv_num} files')
            os.chdir(cwd)
            goback()

        else:
            print(undef_errmsg)
            time.sleep(1)
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

        elif pht.endswith('.png'):
            name_wo = pht[:-4]
            print(f'Converting {pht} to {name_wo}{wish_ext}')
            subprocess.run(['heif-enc', '-q', wish_qty, pht, '-o', name_wo + wish_ext])
    else:
        new_fnum = len(os.listdir())
        conv_num = new_fnum - fnum

        if conv_num > 0:
            print(f'{succesconv_txt} {conv_num} files')
            os.chdir(cwd)
            goback()

        else:
            print(undef_errmsg)
            time.sleep(1)
            os.chdir(cwd)
            main()


# Other functions
def clear():
    os.system('clear')


def goback():
    print(enter)
    os.system('read')
    main()
