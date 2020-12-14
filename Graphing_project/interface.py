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
        
def simulation_button_click(freq_val, discretization_val, borders_attached_val):
    try:
        freq = float(freq_val)
        hladni_model.hladni_model(freq, discretization_val, borders_attached_val)
    except ValueError:
        mb.showinfo('Input Error!',
                    'You have to insert one value into every box \nThe values MUST be FLOAT!')

def main():
    root = tk.Tk()
    interaction_frame = tk.Frame(root)
    
    instruction_label_theory = tk.Label(interaction_frame, text = 'Here you can pick the mode')
    instruction_label_theory.pack()
    
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
    
    '''entry_simulation = tk.Entry(interaction_frame)
    entry_simulation.pack()'''
    
    instruction_label_model = tk.Label(interaction_frame,
                                       text = 'Use scales to pick frequency\nand discretization')
    instruction_label_model.pack()
    
    force_scale = tk.Scale(interaction_frame, orient = 'horizontal', resolution = 1, from_ = 10, to = 20)
    force_scale.pack()
    
    discretization_scale = tk.Scale(interaction_frame, orient = 'horizontal', resolution = 1, from_ = 20, to = 40)
    discretization_scale.pack()
    
    borders_attached_val = False 
    
    borders_attached_check = tk.Checkbutton(interaction_frame, text = 'Borders attached', var = borders_attached_val)
    borders_attached_check.pack()
    
    simulation_mode_button = tk.Button(interaction_frame, text = 'Simulation mode', 
                                   command = lambda: simulation_button_click(force_scale.get(),
                                                                             discretization_scale.get(),
                                                                             borders_attached_val))
    simulation_mode_button.pack()
    
    interaction_frame.pack()
    
    root.mainloop()
    
main()



