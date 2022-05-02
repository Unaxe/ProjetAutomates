from src.Service.StateService import State
class Automate:
    def __init__(self, name, file_name):
        self.automate_name = name
        self.file_name = f"src/Service/automates/{file_name}.txt"
        self.automate_states = []
        file = open(self.file_name, "r")
        lines = file.readlines()
        file.close()
        self.nb_symbols = int(lines[0])
        self.nb_states = int(lines[1])
        self.nb_snitial_states = int(lines[2].split(" ")[0])
        self.nb_final_states = int(lines[3].split(" ")[0])
        self.initial_states = lines[2].split(" ")[1:-1]
        self.final_states = lines[3].split(" ")[1:-1]
        self.nb_transitions = int(lines[4])
        self.transitions = []
        for i in range(5, 5 + self.nb_transitions):
            self.transitions.append(lines[i])
        for i in range(0, self.nb_states):
            is_initial = str(i) in self.initial_states
            is_final = str(i) in self.final_states
            self.automate_states.append(State(i, is_initial, is_final))
        for transition in self.transitions:
            start = int(transition[0])
            end = int(transition[2])
            symbol = transition[1]
            self.automate_states[start].addTransition({"symbol":symbol, "end": self.automate_states[end]})

    def to_string(self):
        print(f"Automate {self.automate_name}")
        print(f"Nombre de symboles: {self.nb_symbols}")
        print(f"Nombre d'états: {self.nb_states}")
        print(f"Nombre d'états initiales: {self.nb_snitial_states}")
        print(f"Nombre d'états finaux: {self.nb_final_states}")
        print(f"Etats initiales: {self.initial_states}")
        print(f"Etats finaux: {self.final_states}")
        print(f"Nombre de transitions: {self.nb_transitions}")
        print(f"Transitions: {self.transitions}")
        for state in self.automate_states:
            state.to_string()
        print("\n")



