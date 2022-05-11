from src.Service.StateService import State
from src.Service.AutomateService import  Automate

class Main:
    def __init__(self):
        pass

    def readFile(self,file_name):
        automate_name = file_name
        file_name = f"src/Service/automates/{file_name}.txt"
        automate_states = []
        list_symbol = []
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()
        nb_symbols = int(lines[0])
        nb_states = int(lines[1])
        nb_initial_states = int(lines[2].split(" ")[0])
        nb_final_states = int(lines[3].split(" ")[0])
        initial_states = lines[2].strip().split(" ")[1::1]
        final_states = lines[3].split(" ")[1::1]
        nb_transitions = int(lines[4])
        transitions = []
        for i in range(5, 5 + nb_transitions):
            transitions.append(lines[i])
        for i in range(0, nb_states):
            is_initial = str(i) in initial_states
            is_final = str(i) in final_states
            automate_states.append(State(i, is_initial, is_final))
        for transition in transitions:
            start = int(transition[0])
            end = int(transition[2])
            symbol = transition[1]
            if symbol not in list_symbol:
                list_symbol.append(symbol)
            automate_states[start].addTransition({"symbol": symbol, "end": automate_states[end]})

        self.automate = Automate(name=automate_name, states=automate_states, initial_states=initial_states, final_states=final_states, transitions=transitions, symbols=list_symbol, nb_initial_states=nb_initial_states, nb_final_states=nb_final_states , nb_transitions=nb_transitions)
