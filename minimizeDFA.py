from pythomata import SimpleDFA
import graphviz
import tempfile
import webbrowser
import os

def get_user_input():
    alphabet = input("Enter the alphabet (comma-separated): ").split(',')
    states = input("Enter the states (comma-separated): ").split(',')
    initial_state = input("Enter the initial state: ")
    accepting_states = input("Enter the accepting states (comma-separated): ").split(',')
    
    print("Enter the transition function:")
    transition_function = {}
    for state in states:
        transitions = {}
        for symbol in alphabet:
            next_state = input(f"Transition from state '{state}' on symbol '{symbol}': ")
            if next_state:
                transitions[symbol] = next_state
        if transitions:
            transition_function[state] = transitions
    
    return alphabet, states, initial_state, accepting_states, transition_function

def create_dfa(alphabet, states, initial_state, accepting_states, transition_function):
    dfa = SimpleDFA(set(states), set(alphabet), initial_state, set(accepting_states), transition_function)
    return dfa

def minimize_and_trim_dfa(dfa):
    dfa_minimized = dfa.minimize()
    dfa_trimmed = dfa_minimized.trim()
    return dfa_trimmed

def render_dfa_to_browser(dfa):
    graph = dfa.to_graphviz()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".svg") as temp_file:
        temp_file_path = temp_file.name

    graph.render(filename=temp_file_path, format="svg", cleanup=True)
    svg_file_path = f"{temp_file_path}.svg"
    webbrowser.open(f"file://{svg_file_path}")

def main():
    alphabet, states, initial_state, accepting_states, transition_function = get_user_input()
    dfa = create_dfa(alphabet, states, initial_state, accepting_states, transition_function)
    dfa_trimmed = minimize_and_trim_dfa(dfa)
    render_dfa_to_browser(dfa_trimmed)

if __name__ == "__main__":
    main()
