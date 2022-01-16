
import pynput
import shutil
import os
import sys
import subprocess
from pynput.keyboard import Listener

def write_to_persian(key):
    letter = str(key)
    letter = letter.replace("Key.shiftKey.alt_l", " ")

    letter = letter.replace("'", "")

    letter = letter.replace("u", "")

    letter = letter.replace("a", "ش")

    #letter = letter.replace("B", "ذ")
    letter = letter.replace("b", "ذ")

    letter = letter.replace("c", "ز")

    #letter = letter.replace("D", "ی")
    letter = letter.replace("d", "ی")

    #letter = letter.replace("E", "ث")
    letter = letter.replace("e", "ث")

    #letter = letter.replace("F", "ب")
    letter = letter.replace("f", "ب")

    #letter = letter.replace("G", "ل")
    letter = letter.replace("g", "ل")

    #letter = letter.replace("H", "ا")
    letter = letter.replace("h", "ا")

    #letter = letter.replace("I", "ه")
    letter = letter.replace("i", "ه")

    #letter = letter.replace("J", "ت")
    letter = letter.replace("j", "ت")

    #letter = letter.replace("K", "ن")
    letter = letter.replace("k", "ن")

    #letter = letter.replace("L", "م")
    letter = letter.replace("l", "م")

    #letter = letter.replace("M", "پ")
    letter = letter.replace("m", "پ")

    #letter = letter.replace("N", "د")
    letter = letter.replace("n", "د")

    #letter = letter.replace("O", "خ")
    letter = letter.replace("o", "خ")

    #letter = letter.replace("P", "ح")
    letter = letter.replace("p", "ح")

    #letter = letter.replace("Q", "ض")
    letter = letter.replace("q", "ض")

    #letter = letter.replace("R", "ق")
    letter = letter.replace("r", "ق")

    #letter = letter.replace("S", "س")
    letter = letter.replace("s", "س")

    #letter = letter.replace("T", "ف")
    letter = letter.replace("t", "ف")

    #letter = letter.replace("U", "ع")
    letter = letter.replace("u", "ع")

    #letter = letter.replace("V", "ر")
    letter = letter.replace("v", "ر")

    #letter = letter.replace("W", "ص")
    letter = letter.replace("w", "ص")

    #letter = letter.replace("X", "ط")
    letter = letter.replace("x", "ط")

    #letter = letter.replace("Y", "غ")
    letter = letter.replace("y", "غ")

    #letter = letter.replace("Z", "ظ")
    letter = letter.replace("z", "ظ")

    # [
    letter = letter.replace("[", "ج")

    # ]
    letter = letter.replace("]", "چ")

    #;
    letter = letter.replace(";" ,"ک")

    #''
    letter = letter.replace("''", "گ")

    # ,
    letter = letter.replace(",","و")


    # space
    letter = letter.replace("Kثغ.سحacث", " ")


    # shift
    letter = letter.replace("Kثغ.ساهبف", " ")
    letter = letter.replace("Kثغ.سحشزث", " ")
    # shift + alt
    letter = letter.replace("Kثغ.ساهبفKثغ.aمف_م", " ")

    # shift + alt
    letter = letter.replace("Kثغ.شمف_م","")

    # alt
    letter = letter.replace("Kثغ.aمف_م", "")

    # back space
    letter = letter.replace("Kثغ.ذacنسحacث", "/")
    letter = letter.replace("Kثغ.ذشزنسحشزث", "/")

    # control
    letter = letter.replace("Kثغ.cفقم_م", "")

    # fn
    letter = letter.replace("Kثغ.cفقم_م", "")

    #winky
    letter = letter.replace("Kثغ.cپی", "")

    #caps lock
    letter = letter.replace("Kثغ.caحس_مخcن","")

    letter = letter.replace("Kثغ.ثدفثق", "\n")

    with open("persian.txt", 'a',encoding="utf-8") as f:
        f.write(letter)

with Listener(on_press=write_to_persian) as l:
    l.join()
write_to_persian()



