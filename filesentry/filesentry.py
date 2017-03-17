#!/usr/bin/env python

import filecmp
import os
import sys

from colorama import init, Fore, Back, Style
init(autoreset=True)
from filecmp import dircmp

def print_diff_files(dcmp):

    errStyle = Fore.RED + Style.BRIGHT
    endLeft = Style.DIM + dcmp.left
    endRight = Style.DIM + dcmp.right

    # Files both a and b, whose contents differ
    for name in dcmp.diff_files:
        print errStyle + "Different " + Style.RESET_ALL + name + " found in " + \
        endLeft + Style.RESET_ALL + " and " + endRight


    # Names in both a and b, such that the type differs between the directories,
    # or names for which os.stat() reports an error.
    for name in dcmp.common_funny:
        print errStyle + "Common funny " + Style.RESET_ALL + name + " found in " + \
        endLeft + Style.RESET_ALL + " and " + endRight

    # Files which are in both a and b, but could not be compared.
    for name in dcmp.funny_files:
        print errStyle + "Funny files " + Style.RESET_ALL + name + " found in " + \
        endLeft + Style.RESET_ALL + " and  " + endRight


    # Checks for files and subdirectories not found in both a and b
    extraStyle = errStyle + "Extra" + Style.RESET_ALL + Style.DIM + " ... " + Style.RESET_ALL
    for name in dcmp.left_only:
        print extraStyle + name + " found in " + endLeft
    for name in dcmp.right_only:
        print extraStyle + name + " found in " + endRight


    # Recurses down through all subdirectories
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)


# Initialize dcmp with directories from terminal input
dcmp = dircmp(sys.argv[1], sys.argv[2])
print_diff_files(dcmp)
