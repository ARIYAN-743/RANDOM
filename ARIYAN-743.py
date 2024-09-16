import os, sys
os.system("git pull")
try:
    __import__("Ranx").__MR_FARHAN__()
except Exception as e:
    exit(str(e))
