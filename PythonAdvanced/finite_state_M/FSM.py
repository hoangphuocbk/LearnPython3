#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from StateMachine import StateMachine

positive_adjectives = ["great","super", "fun", "entertaining", "easy"]
negative_adjectives = ["boring", "difficult", "ugly", "bad"]

def start_transitions(txt):
	splitted_txt = txt.split(None, 1)
	word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
	if word == "Python":
		new_state = "Python_state"
	else:
		new_state = "Error_state"
	return (new_state, txt)

def python_state_transitions(txt):
	splitted_txt = txt.split(None, 1)
	word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
	if word == "is":
		new_state = "Is_state"
	else:
		new_state = "Error_state"
	return (new_state, txt)

def is_state_transitions(txt):
	splitted_txt = txt.split(None, 1)
	word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
	if word == "not":
		new_state = "Not_state"
	elif word in positive_adjectives:
		new_state = "Pos_state"
	elif word in negative_adjectives:
		new_state = "Neg_state"
	return (new_state, txt)

def not_state_transitions(txt):
	splitted_txt = txt.split(None, 1)
	word, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
	if word in positive_adjectives:
		new_state = "Neg_state"
	elif word in negative_adjectives:
		new_state = "Pos_state"
	else:
		new_state = "Error_state"
	return (new_state, txt)

def Neg_state(txt):
    print("Hallo")
    return ("neg_state", "")

if __name__== "__main__":
	m = StateMachine()
	m.add_state("Start", start_transitions, end_state=0)
	m.add_state("Python_state", python_state_transitions, end_state=0)
	m.add_state("is_state", is_state_transitions, end_state=0)
	m.add_state("not_state", not_state_transitions, end_state=0)
	m.add_state("neg_state", None, end_state=1)
	m.add_state("pos_state", None, end_state=1)
	m.add_state("error_state", None, end_state=1)
	m.set_start("Start")
	m.run("Python is great")
	m.run("Python is difficult")
	m.run("Perl is ugly")
