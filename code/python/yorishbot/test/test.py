import pyaml
import sys
import os

os.chdir(sys.path[1])

def main():
	with open("config.yaml") as f:
		config = f.read()
		data   = pyaml.dump(config)
		print("------------")
		print(data)
		print("-----------")
		name_app = data.split("\n")
		print(name_app)
##		print(dir(list))

if __name__ == '__main__':
	main()
