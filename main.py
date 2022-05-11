from src.Service.AutomateService import Automate
from src.Service.MainService import Main
if __name__ == '__main__':

    main = Main()
    main.readFile("#1")
    print(main.automate.to_string())
