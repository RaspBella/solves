#!/bin/python
import backend

solves = backend.file_in("3x3.csv") # make array of solve objects from file

PB = backend.solve(69, "DNF(4.20)", "Funny", "R U R\' U\'", "06-09-1969", 4.20) # make a solve object by hand

# print solve objects
backend.print_solve(solves[419])
backend.print_solve(PB)

# search function(uses previous print function)
backend.search(85550, solves) #using int x will print solve number x
backend.search(85555, solves) # same but a nice error message displays
backend.search(8.91, solves) #using float x.y(s) will print solve time x.y(s)
backend.search("DNF(8.59)", solves) #using str "x" will print stuff containing "x"

# Current examples of what you can do right now
