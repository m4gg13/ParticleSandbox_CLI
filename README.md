# ParticleSandbox

<img width="812" alt="Screenshot 2024-11-24 at 4 27 33 PM" src="https://github.com/user-attachments/assets/c04824ff-120b-4ef7-82e6-43115cac8d8c">

A tool with which a user may provide an initial state (including a set of particles to begin with and values for relevant variables associated with the beginning state) in order to simulate an evolution of that state using a quantum computer. The tool's output is a set of variables associated with the result of a time evolution of the provided initial state.

## Why?

Easily and rapidly experimenting with particle interactions may allow for experimenters to gain insight into new patterns in what may otherwise be the appearance of chaos.

Simulating interactions between particles is a task that requires detailed instructions on what to do in each possible case. Such a simulation should incorporate the way that different abstractions of matter like elementary particles, atoms, or molecules follow unique rulesets. This application attempts to implement that simulation.

## Features
- user interface (GUI)
    `python3 ./atom_editor.py`
- command line tool (CLI) at 
    `python3 ./particlesandbox.py`
- simplifies the simulation of particle interactions with multiple options for level of abstraction
    - elementary particle
    - atom
    - molecule

## Instructions

### How to install

#### Download the code

There are 2 ways you may go about this. 

##### Option 1 - Download binary

1. See the Github releases tab. https://github.com/m4gg13/ParticleSandbox/releases
2. Download the latest release's binary of your choosing between GUI and CLI

##### Option 2 - Python file

1. Clone down the repo with the command `git clone git@github.com:m4gg13/ParticleSandbox.git`
2. Move into the ParticleSandbox directory

#### Install the dependencies

1. First, you'll need the pyscf dependency `python3 -m pip install pyscf`
2. Next, you'll want to install all of the necessary Qiskit packages `python3 -m pip install qiskit_nature qiskit_algorithms` 

#### Start the app

##### Option 1 - Download binary

1. Execute the downloaded binary

##### Option 2 - Python file

1. Execute the run command of the type you choose, either `python3 ./atom_editor.py` for GUI or `python3 ./particlesandbox.py` for CLI

### How to use

#### GUI

`python3 ./atom_editor.py`

The large field on the top is the definition of the initial state. It is editable - you should enter information there that matches the displayed syntax and describes the initial state that you'd like to use in your evolution simulation. 

There is a group of smaller text boxes in the center third of the window. Each set of boxes has a label that indicates what variable each box's value is associated with in the simulation. 

Below the group of smaller text boxes there is a row of buttons. The RUN button evolves the state described in the boxes above. .... #TODO

At the bottom of the window there is a second large text box. This is where general output from the simulation will appear. Details of the result state are printed in this box upon execution of the simulation.

#### CLI

`python3 ./particlesandbox.py`

The program will prompt you for all of the values that you may provide to it for use during the simulation of the interaction. Input may be saved to the `initial_state.json` file before execution. The program will describe what its doing as it goes.
