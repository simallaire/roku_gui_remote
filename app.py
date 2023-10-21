#!/bin/python3
import argparse

from PyQt6.QtWidgets import QApplication
from rokuapp import RokuApp

parse = argparse.ArgumentParser(description="Roku Remote")
parse.add_argument("--host", help="IP address of Roku device", required=True)
parse.add_argument("-p", "--port", help="Port of Roku device", default=8060)
parse.add_argument("-k", "--disable-keyboard", help="Disable keyboard shortcuts", action="store_true")
args = parse.parse_args()

app = QApplication([])
main = RokuApp(ip=f"{args.host}:{args.port}", kb_listener=not args.disable_keyboard)

app.exec()
