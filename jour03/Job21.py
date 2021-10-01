import matplotlib.pyplot as plt
import re

file = open("data.txt", "r")
line = file.read()
file.close()
line.lower()
x = "abcdefghijklmnopqrstuvwxyz"
alph = sorted(x)

split = line.split()


tab = []

