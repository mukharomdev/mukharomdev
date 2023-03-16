import pathlib
import sys
import os
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())




def get_random_ingredients(kind=None):
	return ['shells', 'gorgonzola', 'parsley']