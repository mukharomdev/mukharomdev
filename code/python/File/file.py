import pathlib
import sys

print(sys.path)
print(__file__)
print(pathlib.Path(__file__).parents[2].resolve().as_posix())
# sys.path.insert(0,pathlib.Path(__file__))
# 
# print(dir(pathlib.Path(__file__)))