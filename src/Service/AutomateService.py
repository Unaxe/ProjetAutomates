from src.Service.StateService import State



class Automate:
    """
    Class that represents the automate
    an automate needs :
    - a name
    - a list of states
    - a list of initials states
    - a list of finals states
    - a list of transitions
    - a list of symbols
    - the numb of symbols
    - the numb of states
    - the states
    """
    def __init__(self, name, states, initial_states, final_states, transitions, symbols, nb_initial_states,
                 nb_final_states , nb_transitions):
        self.automate_name = name
        self.automate_states = []
        self.list_symbol = symbols
        self.nb_symbols = symbols
        self.nb_states = len(states)
        self.nb_initial_states = nb_initial_states
        self.nb_final_states = nb_final_states
        self.initial_states = initial_states
        self.final_states = final_states
        self.nb_transitions = nb_transitions
        self.transitions = transitions
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
        print(f"Nombre d'états initiales: {self.nb_initial_states}")
        print(f"Nombre d'états finaux: {self.nb_final_states}")
        print(f"Etats initiales: {self.initial_states}")
        print(f"Etats finaux: {self.final_states}")
        print(f"Nombre de transitions: {self.nb_transitions}")
        print(f"Transitions: {self.transitions}")
        for state in self.automate_states:
            state.to_string()
        print("\n")

    def determinisation(self):

        if self.est_un_automate_asynchrone():
            print("L'automate est assynchrone")
            self.determinisation_automate_asynchrone()
        elif self.est_un_automate_deterministe():
            self.determinisation_automate_synchrone()
        else:
            # TODO Déterminisation
            self.completion()
        #Afficher automate

    def est_un_automate_asynchrone(self):
        for state in self.automate_states:
            for transition in state.transitions:
                if transition["symbol"] == '*':
                    return True
        return False

    def est_un_automate_deterministe(self): #TODO : à compléter
        for state in self.automate_states:
            for transition in state.transitions:
                if transition["symbol"] != "*":
                    if len(transition["end"].transitions) > 1:
                        return False
        return True

        pass

    def est_un_automate_complet(self): #TODO : à compléter
        # prendre tous les etats
        for state in self.automate_states:

            # Vérifier que chaque etat a une transition par chaque symbole
            for symbol in self.list_symbol:
                if symbol not in state.transitions:
                    return False
        return True
            # retourner le resultat
        pass

    def completion(self): #TODO : à compléter
        if est_un_automate_détérministe(self) == true or est_un_automate_complet(self) == false:

        # Nouvel etat : Poubelle
        # Nouvelle transition : Poubelle -> Poubelle pour tous les symboles
        # Pour chaque etat
            # Pour chaque symbole
                # Si l'etat n'a pas de transition avec ce symbole
                    # Ajouter une transition avec le symbole et l'etat Poubelle
        pass

    def determinisation_automate_asynchrone(self): #TODO : à compléter
        pass

    def determinisation_automate_synchrone(self): #TODO : à compléter
        # I est l'ensemble des états initiaux de l'automate non déterministe. C'est donc bien un sous-ensemble de Q.
        a = Automate(self.name, 1, "1", "final_states", "", self.symbols, 1,"nb_final_states" , 0)
        #"tant que l'ensemble des états à traiter n'est pas vide"
        states_to_process = []
        for state in a.automate_states:
            states_to_process.append(state)
        while(len(states_to_process) >0 ):
            state = states_to_process.pop()
            # On considère tous les éléments de l'alphabet, les uns après les autres, et on calcule les transitions
            # sortantes, si elle existent. Les états cibles sont créés s'ils n'existent pas déjà dans l'automate déterministe.
            for symbol in a.list_symbol:
                # On considère tous les éléments p de p' pour lesquels il existe, dans l'automate non déterministe,
                # une transition sortante (p,x,q).
                # On calcule ainsi q' qui est l'ensemble des états de l'automate non déterministe accessibles (dans l'automate non
                # déterministe) par une transition étiquetée 'x' partant d'un état (de l'automate non déterministe) appartenant à p'.
                # La transition (p',x,q') est ajoutée à l'automate déterministe
                # Si l'état q' n'est pas déjà présent dans l'automate déterministe, il y est ajouté. Il est alors marqué "à traiter".
                pass
            # l'etat est marqué déjà traité
        # Les états terminaux de l'automate déterministes sont tous les états contenant au moins un état terminal dans l'automate non déterministe.
        return a


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
                    if mot[i] == first_etat.transitions[j]["symbol"] or mot[i] == "*":
                        first_etat = first_etat.transitions[j]["end"]
            if(first_etat.is_final):
                print(f"Le mot: {mot} est reconnu")
            else:
                print(f"Le mot : {mot} n'est pas reconnu")

    def reconnaitre_mot_asynchrone(self):
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
                    if mot[i] == first_etat.transitions[j]["symbol"] or mot[i] == "*":
                        first_etat = first_etat.transitions[j]["end"]
            if(first_etat.is_final):
                print(f"Le mot: {mot} est reconnu")
            else:
                print(f"Le mot : {mot} n'est pas reconnu")








# La en gros je cherche dans les transition à regrouper les états  qui ont transité par a et puis par b depuis tout
# les état initiaux, faut créer deux nouvelles transistions avec comme nom l'éat initiale et transition a et b et les
# états récupérés au dessus A la fin faudra le généraliser dans une fonction
