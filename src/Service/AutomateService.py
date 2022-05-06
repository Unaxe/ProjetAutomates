from src.Service.StateService import State
import numpy as np


class Automate:
    def __init__(self, name, file_name):
        self.automate_name = name
        self.file_name = f"src/Service/automates/{file_name}.txt"
        self.automate_states = []
        self.list_symbol = []
        file = open(self.file_name, "r")
        lines = file.readlines()
        file.close()
        self.nb_symbols = int(lines[0])
        self.nb_states = int(lines[1])
        self.nb_snitial_states = int(lines[2].split(" ")[0])
        self.nb_final_states = int(lines[3].split(" ")[0])
        self.initial_states = lines[2].split(" ")[1::1]
        self.final_states = lines[3].split(" ")[1::1]
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
            if symbol not in self.list_symbol:
                self.list_symbol.append(symbol)
            self.automate_states[start].addTransition({"symbol": symbol, "end": self.automate_states[end]})

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
        print("oui")

    def determinisation(self):
        a_traiter = []
        new = ""
        new_end = []
        for i in self.initial_states:
            new += i
            a_traiter.append(self.automate_states[int(i)])
            for a in a_traiter:
                for c in range(len(a.transitions)):
                    new_end[int(np.where(np.array(self.list_symbol) == a.transitions[c]["symbol"]))] = a.transitions[c][
                        "end"].state_name
        for i in range(len(self.list_symbol)):
            self.automate_states[int(new)].addTransition({"symbol": self.list_symbol[i], "end": new[i]})
            a_traiter.append(new_end[i])


    def lire_mot(self):
        list_mot = []
        x = input("Entrez un mot: ")
        while(x != "-1"):
            x = input("Entrez un mot: ")
            list_mot.append(x)
        return list_mot

    def reconnaitre_mot(self):
        list_mot = self.lire_mot()
        for mot in list_mot:
            mot.split("")
            for i in self.initial_states:
                for j in range(len(self.automate_states[int(i)].transitions)):
                    if mot[0] == self.automate_states[int(i)].transitions[j]["symbol"]:
                        first_etat = self.automate_states[int(i)]

            first_etat= self.automate_states[0]
            for i in range(len(mot)):
                for j in range(len(first_etat.transitions)):
                    if(mot[i] == first_etat.transitions[j]["symbol"]):
                        first_etat = first_etat.transitions[j]["end"]
            if(first_etat.is_final):
                print("Le mot est reconnu")
            else:
                print("Le mot n'est pas reconnu")






# La en gros je cherche dans les transition à regrouper les états  qui ont transité par a et puis par b depuis tout
# les état initiaux, faut créer deux nouvelles transistions avec comme nom l'éat initiale et transition a et b et les
# états récupérés au dessus A la fin faudra le généraliser dans une fonction
