#For any editors of this, i'm on the TAB gang, so any "pycharmed" out there who use four spaces, suffer ^_^
import tkinter as tk
import numpy as np

DIM = 32 #Radius of the screen in simulated cells
PXPERDIM = 10 #Size of one cell in pixels

class OptimizedPlate:
    def __init__(self, dim, attached = False, density = 20, friction = 0, tension = 1):
        '''
        dim - plate radius
        attached - if plate borders are attached
        density - mass of a simulation cell
        friction - percent of the speed to lose per tick
        tension - how strong forces among the plate are
        '''
        self.dim = dim
        self.coords = np.zeros((dim, dim), dtype=float)
        self.speeds = np.zeros((dim, dim), dtype=float) #coords and speeds of every simulated cell
        self.attached = attached
        self.tension = tension
        self.friction = friction
        self.density = density
    
    def tick(self, force, timestep = 1):
        '''
        This will desctibe the plate state at the moment.
        force - external force in the plate center
        timestep - how long the game tick is
        '''
        for i in range(self.dim):
            for j in range(self.dim):
                self.speeds[i][j] += self.force_calculate(i, j)*timestep/self.density #forces among the plate
                self.speeds[i][j] *= (1 - self.friction) #energy loss
        self.speeds[0][0] += force*timestep/self.density #external force
        self.coords += self.speeds*timestep #coords recalculation
    
    def force_calculate(self, i, j):
        '''
        Internal force among the plate for a certain simulated cell.
        i, j - coords of a cell we talk about
        '''
        if self.attached and (i == self.dim-1 or j == self.dim-1):
            return 0 #if the plate is attached, borders won't move
        else:
            all_sins = 0
            for k in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if (k[0] > self.dim-1 or k[1] > self.dim-1):
                    a = 0 #unattached borders don't receive a force from outside
                else:
                    a = self.getcoords(k[0], k[1]) - self.coords[i][j]
                all_sins += a
        return all_sins*self.tension
    
    def getcoords(self, i, j):
        '''
        Returns the deviation of a cell with coords (i, j), negatives are possible
        '''
        return self.coords[abs(i)][abs(j)]
    
    def getcolor(self, i, j, scale):
        '''
        Returns the colour to paint the cell (i, j) into for simulation purposes.
        '''
        value = self.getcoords(i, j)
        intensity = min(int(abs(value)*scale), 255)
    
        if value > 0:
            res = (intensity, 0, 0) #Positive deviation is painted as red
        else:
            res = (0, intensity, 0) #Negative deviation is painted as green
    
        return "#%02x%02x%02x" % res

class GameObjectsList:
    def __init__(self, canv, plate, pxscale = PXPERDIM, scale = 35500):
        '''
        Constructs the list of objects representating simulated cells.
        canv - canvas to draw them onto
        plate - what we are simulating
        pxscale - size of one simulated cell, pixels
        scale - is used for correct color representation, use bigger values for smaller fluctuations
        '''
        self.scale = scale
        self.dim = plate.dim
        self.objects_list = [] #here the cell IDs will be stored. Maybe rewrite to numpy array?
        for i in range(-self.dim+1, self.dim):
            temp = []
            for j in range(-self.dim+1, self.dim):
                (xpos, ypos) = self.coords_transform(i, j)
                color = plate.getcolor(i, j, scale)
                temp.append(canv.create_rectangle(xpos*pxscale, ypos*pxscale, (xpos+1)*pxscale, (ypos+1)*pxscale, fill = color))
            self.objects_list.append(temp)
    
    def coords_transform(self, i, j):
        '''
        Recalculates coordinates.
        Input: screen coords (0, 0 in the top left corner)
        Output: plate coords (0, 0 in the center)
        '''
        return(i+self.dim-1, j+self.dim-1)
    
    def update(self, canv, plate):
        '''
        Update the screen with the plate state
        '''
        for i in range(-self.dim+1, self.dim):
            for j in range(-self.dim+1, self.dim):
                (xpos, ypos) = self.coords_transform(i, j)
                color = plate.getcolor(i, j, self.scale)
                canv.itemconfig(self.objects_list[xpos][ypos], fill = color)
        canv.update()
    
def harmonic_force(time, frequency, force = 1):
        '''
        Calculates the force to punch the plate with at any given moment.
        time - given moment
        frequency - the frequency of fluctuations (2pi/period)
        force - amplitude of that force
        '''
        return force*np.sin(time*frequency)
    
def hladni_model(force_freq_value = 1):
    #Screen creation
    root = tk.Tk()
    gstr = str((2*DIM+1)*PXPERDIM)
    root.geometry(gstr+'x'+gstr)
    canv = tk.Canvas(root, bg='black')
    canv.pack(fill = tk.BOTH, expand=1)
    
    
    #Simulation initialisation
    plate = OptimizedPlate(DIM)
    screen = GameObjectsList(canv, plate)
    time = 0
    
    #Time management
    TIME = 1500
    timestep = 1
    frequency = 2*np.pi*force_freq_value/100
    
    for i in range(TIME): #Main cycle
        force = harmonic_force(time, frequency, 0.01)
        plate.tick(force, timestep)
        time += timestep
    
        screen.update(canv, plate)
        print(i)


