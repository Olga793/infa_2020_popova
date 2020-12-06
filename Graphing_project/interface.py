import tkinter as tk
from tkinter import messagebox as mb
import hladni_theorprint
import hladni_model


def stactic_button_click(val_1, val_2):
    try:
        hor_mode = int(val_1)
        ver_mode = int(val_2)
        hladni_theorprint.hladni_theorprint(hor_mode, ver_mode)
    except ValueError:
        mb.showinfo('Input Error!',
                    'You have to insert one value into every box \nThe values MUST be INTEGER!')
        
def simulation_button_click(val):
    try:
        freq = float(val)
        hladni_model.hladni_model(freq)
    except ValueError:
        mb.showinfo('Input Error!',
                    'You have to insert one value into every box \nThe values MUST be FLOAT!')

def main():
    root = tk.Tk()
    interaction_frame = tk.Frame(root)
    
    instruction_label = tk.Label(interaction_frame, text = 'Here you can pick the mode')
    instruction_label.pack()
    
    heading_theory_mode = tk.Label(interaction_frame,
                                   text = 'Insert two integer values for static mode')
    heading_theory_mode.pack()
    
    entry_theory_1 = tk.Entry(interaction_frame)
    entry_theory_1.pack()
    
    entry_theory_2 = tk.Entry(interaction_frame)
    entry_theory_2.pack()
    
    theory_mode_button = tk.Button(interaction_frame, text = 'Static mode', 
                                   command = lambda: stactic_button_click(entry_theory_1.get(),
                                                                          entry_theory_2.get()))
    theory_mode_button.pack()
    
    entry_simulation = tk.Entry(interaction_frame)
    entry_simulation.pack()
    
    simulation_mode_button = tk.Button(interaction_frame, text = 'Simulation mode', 
                                   command = lambda: simulation_button_click(entry_simulation.get()))
    simulation_mode_button.pack()
    
    interaction_frame.pack()
    
    root.mainloop()
    
main()



