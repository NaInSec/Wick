#!/usr/bin/env python

# Tools Name : Wick  - Python Brute Force Password Generator.
# Description : Ini adalah skrip Python yang digunakan untuk menghasilkan semua kemungkinan kombinasi kata sandi untuk Crack WAP dan file login atau kata sandi lainnya. Program ini adalah open source. Jika Anda melihat kebutuhan untuk memperbaiki atau mengubah sesuatu dengan segala cara, lakukanlah, tetapi bagikan temuan Anda. itu hanya benar.
# Author : XSVS_Cyb3r
# Sites : https://xsvscyb3r.id
# Email : xsvscyb3r@proton.me
# Github : github.com/XSVSCyb3rID

from __future__ import print_function 
__NAME__ = "wick.py - Python Brute Force Password Generator"
__VERSION_MAJOR__ = 1
__VERSION_MINOR__ = 0

import sys, os
import argparse  
import itertools  
import gzip  
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description = """
Penggunaan Dengan Aircrack-Ng :
./wick.py -o stdout -A | aircrack-ng -b XX:XX:XX:XX:XX:XX -w - file.cap
Penggunaan Dengan Medusa :
./wick.py | xargs -L 1 medusa -h 192.168.1.1 -u admin -M web-form -p
""",formatter_class=RawTextHelpFormatter)

parser.add_argument("-o", "--output", dest = "output",
	help = "(wajib) Nama keluaran file .gz atau gunakan kata kunci 'stdout'.")

parser.add_argument("-min", dest = "min_size", type = int, default = 8,
	help = "(opsional) Ukuran minimum kata-kata; pingsan: 8")

parser.add_argument("-max", dest = "max_size", type = int, default = 8,
	help = "(opsional) Ukuran maximal kata-kata; pingsan: 8")

group = parser.add_argument_group("jenis kata; Gunakan setidaknya satu.")

group.add_argument("-N", dest = "has_numbers", action = "store_true", default = False,
	help = "(Opsional) Jika disetel, kata-kata yang dihasilkan akan menyertakan angka.")

group.add_argument("-L", dest = "has_lowercase_letters", action = "store_true", default = False,
	help = "(Opsional) Jika disetel, kata-kata yang dihasilkan akan menyertakan huruf kecil.")

group.add_argument("-U", dest = "has_uppercase_letters", action = "store_true", default = False,
	help = "(Opsional) Jika disetel, kata-kata yang dihasilkan akan menyertakan huruf besar.")

group.add_argument("-S", dest = "has_special_characters", action = "store_true", default = False,
	help = "(Opsional) Jika disetel, kata-kata yang dihasilkan akan menyertakan karakter khusus.")

group.add_argument("-A", "--all", dest = "has_all_characters", action = "store_true", default = False,
	help = "(Opsional) Jika disetel, kata-kata yang dihasilkan akan mencakup semua karakter.")

parser.add_argument("-v", "--version", dest = "show_version", action = "store_true", default = False,
	help = "(Opsional) Jika disetel, akan menampilkan versi program lalu keluar.")

args = parser.parse_args()

if (args.show_version):
	print("%s %d.%d" % (__NAME__, __VERSION_MAJOR__, __VERSION_MINOR__))
	sys.exit(0)

def error (msg):
	print("ERROR: %s" % msg, file = sys.stderr)
	sys.exit(1)

if (not args.output):
	error("Nama file outfile atau 'stdout' harus disediakan\r\nketik wick.py --help untuk info lebih lanjut.")

if (args.min_size < 1):
	error("Nilai tidak valid untuk -min: %d\r\nketik wick.py --help untuk info lebih lanjut." % args.min_size)

if (args.max_size < 1):
	error("Nilai tidak valid untuk -max: %d\r\nKetik wick.py --help untuk info lebih lanjut." % args.max_size)

if (args.min_size > args.max_size):
	error("-min tidak bisa lebih besar dari -max\r\nKetik wick.py --help untuk info lebih lanjut.")

if (args.has_numbers + args.has_lowercase_letters + args.has_uppercase_letters + args.has_special_characters + args.has_all_characters == 0):
	error("Setidaknya satu dari (-n), (-l), (-u), (-s), atau (-a) diperlukan\r\ntype wordpie.py --help untuk info lebih lanjut.")

if(args.output != "stdout"):
        print("* Menghasilkan kata-kata ukuran %d hingga %d" % (args.min_size, args.max_size))

SPECIAL_CHARACTERS = range(33, 48) + range(58, 65) + range(91, 97) + range(123, 127)
NUMBERS = range(48, 58)
UPPERCASE_LETTERS = range(65, 91)
LOWERCASE_LETTERS = range(97, 123)

CHARACTER_SET = ""

def ascii_to_chr (codes):
	return ''.join([chr(i) for i in codes])

if (args.has_special_characters):
	CHARACTER_SET += ascii_to_chr(SPECIAL_CHARACTERS)

if (args.has_numbers):
	CHARACTER_SET += ascii_to_chr(NUMBERS)

if (args.has_uppercase_letters):
	CHARACTER_SET += ascii_to_chr(UPPERCASE_LETTERS)

if (args.has_lowercase_letters):
	CHARACTER_SET += ascii_to_chr(LOWERCASE_LETTERS)

if (args.has_all_characters):
	CHARACTER_SET += ascii_to_chr(LOWERCASE_LETTERS)
	CHARACTER_SET += ascii_to_chr(UPPERCASE_LETTERS)
	CHARACTER_SET += ascii_to_chr(NUMBERS)
	CHARACTER_SET += ascii_to_chr(SPECIAL_CHARACTERS)
       

if(args.output != "stdout"):
        print("* menghasilkan kata-kata dengan karakter dari\n  " + CHARACTER_SET)

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::      

# OPEN FILE FOR WRITING GZ WORDLIST

if(args.output != "stdout"):
        fh = gzip.open(args.output, "wb")


# GENERATE THE WORDPIE! 

for size in range(args.min_size, args.max_size + 1):
	n_words = len(CHARACTER_SET) ** size
	if(args.output != "stdout"):
              print("* Menghasilkan kata-kata ukuran %d (%d kata total)" % (size, n_words))
	i = 0

	for word in itertools.product(CHARACTER_SET, repeat = size):
              if(args.output == "stdout"):
                     print(''.join(word))
              else:
	    	     print(''.join(word), file = fh)
		     i += 1
		     if (i % 100000 == 0):
		          print("  %d/%d Kata-kata yang dihasilkan" % (i, n_words))

	      if (i % 100000 > 0):
                     if(args.output != "stdout"):
		          print("  %d/%d Kata-kata yang dihasilkan" % (i, n_words))

if(args.output != "stdout"):
        fh.close()
        print("* Pai disajikan!")