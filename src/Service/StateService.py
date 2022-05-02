class State :
    def __init__(self,state_name, is_final_state, is_initial_state):
        self.state_name = str(state_name)
        self.transitions = []
        self.is_final = is_final_state
        self.is_initial = is_initial_state

    def addTransition(self,transition):
        self.transitions.append(transition)

    def to_string(self):
        print("State: " + self.state_name)
        print("Transitions: ")
        for transition in self.transitions:
            print(transition["symbol"] + " -> " + transition["end"].state_name)
        print("Is Final: " + str(self.is_final))
        print("Is Initial: " + str(self.is_initial))
        print("\n")



