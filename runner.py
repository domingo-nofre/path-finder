import os

currentPath = os.getcwd()
print(currentPath)
cmd = "behave -v features -t @automated"
os.system(cmd)