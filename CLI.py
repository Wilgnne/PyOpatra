from os import system, name

clear = lambda: system ("cls") if name == "nt" else system ("clear")