import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


tuberias = {}
contador_tubos = 0

class SideMenu:
    def __init__(self, master, bg_color):
        self.master = master
        self.frame = tk.Frame(self.master, width=200, bg=bg_color)
        # self.frame.pack(side='left', fill='y')
        self.sections = ['Accesorios', 'Valvulas', 'Propipunto_finales del fluido', 'Editar sistema', 'Resultados']
        
        Accesorios = tk.Button(self.frame, text='Accesorios', width=20, bg=bg_color, fg='white', command=self.accesorios )
        Accesorios.pack(pady=10)
        Valvulas = tk.Button(self.frame, text='Valvulas', width=20, bg=bg_color, fg='white',command=lambda:print(len(tuberias)) )
        Valvulas.pack(pady=10)
        Propipunto_finales = tk.Button(self.frame, text='Propipunto_finales del fluido', width=20, bg=bg_color, fg='white', )
        Propipunto_finales.pack(pady=10)
        Editar = tk.Button(self.frame, text='Editar sistema', width=20, bg=bg_color, fg='white', )
        Editar.pack(pady=10)
        Resultados = tk.Button(self.frame, text='Resultados', width=20, bg=bg_color, fg='white', )
        Resultados.pack(pady=10)

        self.frame2 = tk.Frame(self.frame,  bg=bg_color)
        self.frame3 = tk.Frame(self.frame, width=200, height=200,  bg=bg_color)

        img1 = tk.PhotoImage(file="./imagenes/tubo.png", master=self.master)
        self.button1 = tk.Button(self.frame2, image=img1, command=self.tuberia)
        self.button1.image = img1  # asignar la imagen al atributo del botón

        img2 = tk.PhotoImage(file="./imagenes/t.png", master=self.master)
        self.button2 = tk.Button(self.frame2, image=img2, command=lambda: print('dfgd'))
        self.button2.image = img2  # asignar la imagen al atributo del botón
        
        img3 = tk.PhotoImage(file="./imagenes/codo.png", master=self.master)
        self.button3 = tk.Button(self.frame2, image=img3, command=lambda: print('dfgd'))
        self.button3.image = img3  # asignar la imagen al atributo del botón

        # Crear etiquetas y campos de entrada
        tk.Label(self.frame3 , text="Posición inicial:", bg=bg_color, fg='white').grid(row=0, column=0)
        self.punto_inicio = tk.Entry(self.frame3 )
        self.punto_inicio.grid(row=0, column=1,)
        tk.Label(self.frame3, text="Posición final:",bg=bg_color, fg='white').grid(row=1, column=0)
        self.punto_final = tk.Entry(self.frame3)
        self.punto_final.grid(row=1, column=1)
        self.boton_enviar = tk.Button(self.frame3, text="Enviar", bg=bg_color, fg='white',command=self.tubo )
        self.boton_enviar.grid(row=3, column=1)

    def accesorios(self):
        if self.frame2.winfo_manager():
            self.frame2.pack_forget()
            self.frame3.pack_forget()
            self.button1.pack_forget()
            self.button2.pack_forget()
            self.button3.pack_forget()
        else:
            self.frame2.pack()
            self.button1.pack(side=tk.LEFT, padx=5, pady=5)
            self.button2.pack(side=tk.RIGHT, padx=5, pady=5)
            self.button3.pack( padx=5, pady=5)

    def tuberia(self):
        if self.frame3.winfo_manager():
            self.frame3.pack_forget()
        else:
            self.frame3.pack()

    def tubo(self):
        global contador_tubos
        P_inicial =  self.punto_inicio.get().split(' ')
        P_final =  self.punto_final.get().split(' ')
        tuberias['tubo'+str(contador_tubos)] = [P_inicial,P_final] 
        print(tuberias)
        contador_tubos += 1
    
class Application:
    def __init__(self, master, theme='light'):
        self.master = master
        self.master.title('Red de aire comprimido')
        self.master.iconbitmap("imagenes/logo.ico")
        self.master.geometry('600x440')
        self.master.minsize(500, 430)
        

        if theme == 'dark':
            bg_color = '#2c2f33'
            fg_color = 'white'
        else:
            bg_color = 'white'
            fg_color = 'black'

        self.master.configure(background=bg_color)

        self.show_menu_button = tk.Button(self.master, text='Mostrar el menú', command=self.toggle_menu, bg=bg_color, fg=fg_color)
        self.show_menu_button.pack(side='top', fill='x')

        self.side_menu = SideMenu(self.master, bg_color=bg_color)

        
        self.menu_visible = False

        self.actualizar = tk.Button(self.master, text="actualizar",width=20, height=2, bg='green', command=self.actualizar )
        
        self.graficador = tk.Frame(self.master, width=300, height=300, bg='red')
        self.graficador.pack( fill=tk.BOTH, expand=True)

        

        self.img = Figure(figsize=(3, 3), dpi=120)
        ax = self.img.add_subplot(111, projection='3d')
        self.canvas = FigureCanvasTkAgg(self.img, master=self.graficador)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='right', fill=tk.BOTH, expand=True)

        

    def toggle_menu(self):
        if self.menu_visible:
            self.side_menu.frame.pack_forget()
            self.actualizar.pack_forget()
            self.show_menu_button.config(text='Mostrar el menú')
        else:
            self.side_menu.frame.pack(side='left',  fill=tk.BOTH, )
            self.graficador.pack( side='right', fill=tk.BOTH, expand=True)
            self.actualizar.pack(side='bottom', fill=tk.X, expand=True, after=self.graficador)
            self.show_menu_button.config(text='Ocultar el menú')

        self.menu_visible = not self.menu_visible

          
        
    def actualizar(self):
        self.img.clf()
        ax = self.img.add_subplot(111, projection='3d')
        for hp in tuberias:
            ax.plot([int(tuberias[hp][0][0]),int(tuberias[hp][1][0])], [int(tuberias[hp][0][1]),int(tuberias[hp][1][1])], [int(tuberias[hp][0][2]),int(tuberias[hp][1][2])],color='blue')
        self.canvas.draw()

               

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root, theme='dark')
    root.mainloop()


