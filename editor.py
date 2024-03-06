import tkinter as tk

window = tk.Tk()
window.geometry("800x800")

# MARK: State Visualization section
# MARK: Variable Configuration section

state_row = 1
tk.Label(window, text="INITIAL").grid(row = state_row, column = 2)
tk.Label(window, text="FINAL").grid(row = state_row, column = 3)

energy_row = 2
tk.Label(window, text="ENERGY").grid(row = energy_row, column = 1)
e1 = tk.Entry(window, width = 20)
e1.grid(row = energy_row, column = 2)
e2 = tk.Entry(window)
e2.grid(row = energy_row, column = 3)

spin_row = 3
tk.Label(window, text="SPIN").grid(row = spin_row, column = 1)
s1 = tk.Entry(window, width = 20)
s1.grid(row = spin_row, column = 2)
s2 = tk.Entry(window)
s2.grid(row = spin_row, column = 3)

particle_number_row = 4
tk.Label(window, text="PARTICLE #").grid(row = particle_number_row, column = 1)
p1 = tk.Entry(window, width = 20)
p1.grid(row = particle_number_row, column = 2)
p2 = tk.Entry(window)
p2.grid(row = particle_number_row, column = 3)

# MARK: Action Button Section
action_button_row = 8
tk.Button(window, text='RUN').grid(row=action_button_row, column=1)
tk.Button(window, text='RESET').grid(row=action_button_row, column=2)
tk.Button(window, text='QUIT').grid(row=action_button_row, column=3)

# MARK: State Chooser dropdown section
# MARK: Console section

window.mainloop()

# notes
#from tkinter import *
#from tkinter import messagebox
#top = Tk()
#top.geometry("100x100")
#def helloCallBack():
#   msg=messagebox.showinfo( "Hello Python", "Hello World")
#B = Button(top, text ="Hello", command = helloCallBack)
#B.place(x=50,y=50)
#top.mainloop()
