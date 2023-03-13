import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class SideMenu:
    def __init__(self, master, bg_color):
        self.master = master
        self.frame = tk.Frame(self.master, width=200, bg=bg_color)
        self.frame.pack(side='left', fill='y')

        self.sections = ['Accesorios', 'Valvulas', 'Propiedades del fluido', 'Editar sistema', 'Resultados']
        for section in self.sections:
            tk.Button(self.frame, text=section, width=20, bg=bg_color, fg='white').pack(pady=10)

class Application:
    def __init__(self, master, theme='light'):
        self.master = master
        self.master.title('Red de aire comprimido')
        self.master.geometry('600x400')
        self.master.minsize(500, 300)

        if theme == 'dark':
            bg_color = '#2c2f33'
            fg_color = 'white'
        else:
            bg_color = 'white'
            fg_color = 'black'

        self.side_menu = SideMenu(self.master, bg_color=bg_color)

        self.show_menu_button = tk.Button(self.master, text='Ocultar el menú', command=self.toggle_menu, bg=bg_color, fg=fg_color)
        self.show_menu_button.pack(side='top', fill='x')

        self.menu_visible = True

        self.graficador = tk.Frame(self.master, width=300, )
        self.graficador.pack( fill=tk.BOTH, expand=True)
        
        self.fig = Figure(figsize=(3, 3), dpi=120)
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        self.ax.plot([0,40], [0,60], [0,20],color='red')
        self.ax.plot([40,100], [60,100], [20,100],color='red')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graficador)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def toggle_menu(self):
        if self.menu_visible:
            self.side_menu.frame.pack_forget()
            self.show_menu_button.config(text='Mostrar el menú')
        else:
            self.side_menu.frame.pack(side='left',  fill=tk.BOTH, )
            self.graficador.pack( side='right', fill=tk.BOTH, expand=True)
            self.show_menu_button.config(text='Ocultar el menú')

        self.menu_visible = not self.menu_visible

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root, theme='dark')
    root.mainloop()