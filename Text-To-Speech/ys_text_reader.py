# ys_text_reader.py
# Read a text file and make it speak with espeak
from subprocess import call

BOOK="alice.txt"
REPORT_EXCEPTION = False

try:
    with open(BOOK) as f:
        book = f.readlines()
except  Exception as e:
    if REPORT_EXCEPTION:
        print(str(e))

try:
    for parag in book:
        print(parag,flush=True)
        call(["espeak", "-ven", "-s160", parag])
except  Exception as e:
    if REPORT_EXCEPTION:
        print(str(e))

parag=f"""Reading {BOOK} is complete. See you soon!"""
print(parag,flush=True)
call(["espeak", "-ven", parag])
