#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Script Name:     voucher_pdf
# CreationDate:    15.10.2022
# Last Modified:   16.10.2022 18:32:32
# Copyright:       Michael N. (c)2022
# Purpose:         Erstellt Voucher im Format DIN A6 Querformat als PDF
#
from fpdf import FPDF
import re
import sys
from datetime import date
from argparse import ArgumentParser

aktuellesDatum = date.today()

def create_pdf(Lines, ssid):
    count_pdf = 0
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF('P', 'mm', (148, 105))
    for line in Lines:
        count_pdf += 1
        if count_pdf > 7:
            line = line.replace(" ", "").strip()
            line = line.replace("\"", "").strip()
            # Add a page
            pdf.add_page()
            # set style and size of font
            # that you want in the pdf
            pdf.set_font("Arial", size=20)
            # create WLAN image
            pdf.image("wlan.png", x = 5, y = 5, w = 20, h = 20, type = 'png', link = '')
            # create a cell
            pdf.cell(50, 10, txt="SSID:", ln=0, align='R', border=0)
            pdf.cell(60, 10, txt=ssid, ln=1, align='C', border=0)
            pdf.cell(50, 5, txt=" ", ln=2, align='C', border=0)
            pdf.cell(50, 5, txt=" ", ln=2, align='C', border=0)
            pdf.cell(50, 10, txt="Voucher:", ln=0, align='C', border=0)
            pdf.set_font("Courier", size=20)
            pdf.cell(60, 10, txt=line, ln=1, align='C', border=0)
            pdf.cell(50, 5, txt=" ", ln=2, align='C', border=0)
            pdf.set_font("Arial", size=20)
            pdf.cell(40, 10, txt="gültig:", ln=0, align='R', border=0)
            pdf.cell(64, 10, txt="8 Stunden", ln=1, align='C', border=0)
            pdf.set_font("Arial", size=15)
            pdf.cell(20, 9, txt="", ln=2, align='C', border=0)
            pdf.cell(10, 10, txt="", ln=0, align='C', border=0)
            pdf.multi_cell(120, 10, txt="Dieser Voucher ist für mehrere Geräte nutzbar.\nGültigkeit startet mit 1. Anwendung.", border = 0,align='J', fill= False)
        # save the pdf with name .pdf
    pdf.output("voucher_"+ aktuellesDatum.strftime("%Y-%m-%d") + ".pdf")
    print ("Anzahl der Voucher: %d" % (count_pdf-7))

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",help="read voucher list from FILE", metavar="FILE")
parser.add_argument("-s", "--ssid", dest="ssid",help="read SSID", metavar="SSID")
try:
    args = parser.parse_args()
    print("args:", args)
    # Using readlines()
    file1 = open(args.filename, 'r')
    Lines = file1.readlines()
    create_pdf(Lines, args.ssid)
except:
    parser.print_help(sys.stderr)
    sys.exit(0)
