import pyaml
import sys
import os

def main():
##	os.chdir('yorishbot')
        lists = os.listdir()
        syspath = sys.path
        os.chdir('..')
        lists = os.listdir()
        os.chdir('yorishbot')
        lists = os.listdir()
        try:
                from yorishbot import core
                from yorishbot.core.config import config

                
        except ImportError as im:
                print(im)
##        print(lists)
##        print(core)
##        print(config)
##        
##        print(os.getcwd())
##        config = config.Config('oke')
##        config()

if __name__ == '__main__':
    main()
    print(type(main))
    dir(main)
