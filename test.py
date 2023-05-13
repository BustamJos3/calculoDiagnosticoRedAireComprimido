import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

tuberias = {}
codos = {}
Tes = {}
VALVULAS = {}
contador_tubos = 0
contador_codo = 0
contador_Te = 0
contador_Valvulas = 0
propiedades = {}


class SideMenu:
    def __init__(self, master, bg_color):
        self.master = master
        self.frame = tk.Frame(self.master, width=200, bg=bg_color)
        Propipunto_finales = tk.Button(self.frame, text='Propiedades del sistema', width=20, bg=bg_color, fg='white', command=self.Priopiedades_sys )
        Propipunto_finales.pack(pady=10)
        Accesorios = tk.Button(self.frame, text='CREAR', width=20, bg=bg_color, fg='white', command=self.accesorios )
        Accesorios.pack(pady=10)
        Valvulas = tk.Button(self.frame, text='Válvulas', width=20, bg=bg_color, fg='white',command=self.Valvulas )
        Valvulas.pack(pady=10)
        
        Resultados = tk.Button(self.frame, text='Resultados', width=20, bg=bg_color, fg='white', )
        Resultados.pack(pady=10)

        self.frame2 = tk.Frame(self.frame,  bg=bg_color)
        self.frame_propiedades = tk.Frame(self.frame2,  bg=bg_color)
        self.frame_valvulas = tk.Frame(self.frame2,  bg=bg_color)
       
        
        self.frame3 = tk.Frame(self.frame, width=300, height=300,  bg=bg_color)
        self.frame4 = tk.Frame(self.frame3,  bg=bg_color)
        self.frame5 = tk.Frame(self.frame3, width=300, height=300,  bg=bg_color)
        self.frame6 = tk.Frame(self.frame3, width=300, height=300,  bg=bg_color)

     

        img1 = tk.PhotoImage(file="calculoDiagnosticoRedAireComprimido/imagenes/tubo.png", master=self.master)
        self.button1 = tk.Button(self.frame2, image=img1, command=self.tuberia)
        self.button1.image = img1  # asignar la imagen al atributo del botón

        img2 = tk.PhotoImage(file="calculoDiagnosticoRedAireComprimido/imagenes/t.png", master=self.master)
        self.button2 = tk.Button(self.frame2, image=img2, command=self.Te)
        self.button2.image = img2  # asignar la imagen al atributo del botón
        
        img3 = tk.PhotoImage(file="calculoDiagnosticoRedAireComprimido/imagenes/codo.png", master=self.master)
        self.button3 = tk.Button(self.frame2, image=img3, command=self.Codo)
        self.button3.image = img3  # asignar la imagen al atributo del botón

        # Crear etiquetas y campos de entrada
        tk.Label(self.frame4 ,width=12, text="Posición inicial:", bg=bg_color, fg='white').grid(row=0, column=0)
        self.punto_inicio = tk.Entry(self.frame4,width=12 )
        self.punto_inicio.grid(row=0, column=1,)
        tk.Label(self.frame4, width=12,text="Posición final:",bg=bg_color, fg='white').grid(row=1, column=0)
        self.punto_final = tk.Entry(self.frame4,width=12,)
        self.punto_final.grid(row=1, column=1)
        tk.Label(self.frame4,width=12, text="Material:",bg=bg_color, fg='white').grid(row=2, column=0)
        materiales = ["Acero", "Aluminio", "Bronce", "Cobre", "PVC"]
        self.combo = ttk.Combobox(self.frame4,width=12,state='readonly',values=materiales)
        self.combo.current(0) 
        self.combo.grid(row=2,column=1,padx=5)
        tk.Label(self.frame4, text="Delta de presión:",bg=bg_color, fg='white').grid(row=3, column=0)
        self.D_Presion = tk.Entry(self.frame4,width=12 )
        self.D_Presion.grid(row=3,column=1)
        self.var = tk.IntVar(value=1)
        self.chk = tk.Checkbutton(self.frame4,width=12,text="Tubería primaria:", bg=bg_color,fg='green',variable=self.var, justify='right')
        self.chk.grid(row=4,column=0 )
        self.boton_enviar = tk.Button(self.frame4, text="Enviar", bg=bg_color, fg='white',command=self.tubo )
        self.boton_enviar.grid(row=5, column=1)

        
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        metric_checkbox = tk.Checkbutton(self.frame_propiedades, text="Sistema Métrico",  bg=bg_color,fg='green',variable=self.var1, command=self.select_metric)
        metric_checkbox.grid(row=0,column=0, )
        imperial_checkbox = tk.Checkbutton(self.frame_propiedades, text="Sistema Imperial", bg=bg_color,fg='green', variable=self.var2, command=self.select_imperial)
        imperial_checkbox.grid(row=1, column=0)
        tk.Label(self.frame_propiedades,width=16, text="Presión atmosferica:",bg=bg_color, fg='white').grid(row=2, column=0)
        self.A_mar = tk.Entry(self.frame_propiedades,width=10 )
        self.A_mar.grid(row=2,column=1, padx=6)
        self.boton_enviar_P = tk.Button(self.frame_propiedades, text="Enviar", bg=bg_color, fg='white',command=self.enviar_Pro )
        self.boton_enviar_P.grid(row=3, column=1)

       



    def select_metric(self):
        self.var2.set(0)

    def select_imperial(self):
        self.var1.set(0)
    
    def enviar_Pro(self):
        if self.var1.get()==1:
            P_atm = self.A_mar.get()
            propiedades['Propiedades'] = [P_atm,'Métrico']
        
        else:
            P_atm = self.A_mar.get()
            propiedades['Propiedades'] = [P_atm,'Imperial']
        
        print(propiedades)
    
    def enviar_val(self):
        global contador_Valvulas 
        P_ubicacion = self.P_valvu.get()
        rotacion = self.rotaciones_Valvu.get()
        VALVULAS['Válvula'+str(contador_Valvulas)] = [P_ubicacion,rotacion, self.var_val.get()]
        contador_Valvulas += 1
        print(VALVULAS)
    
    

    def Priopiedades_sys(self):
        
        self.frame_valvulas.pack_forget()
        self.frame3.pack_forget()
        self.button1.pack_forget()
        self.button2.pack_forget()
        self.button3.pack_forget()
        if self.frame2.winfo_manager():
            self.frame2.pack_forget()
            
        else:
            self.frame2.pack()
            self.frame_propiedades.pack()
            print('somenthing')

    def Valvulas(self):
        
        self.frame_propiedades.pack_forget()
        self.frame3.pack_forget()
        self.button1.pack_forget()
        self.button2.pack_forget()
        self.button3.pack_forget()
        if self.frame2.winfo_manager():
            self.frame2.pack_forget()
            
        else:
            self.frame2.pack()
            self.frame_valvulas.pack()
            print('válvulas')
            tk.Label(self.frame_valvulas, text="Tipo de válvula:",bg='#2c2f33', fg='white').grid(row=0, column=0)
            list_valvulas = ["Globo", "Compuerta", "Diafragma", "Guillotina"]
            combo_v = ttk.Combobox(self.frame_valvulas,width=12,state='readonly',values=list_valvulas)
            combo_v.current(0) 
            combo_v.grid(row=0,column=1,padx=5)
            tk.Label(self.frame_valvulas,width=12, text="Elemento:",bg='#2c2f33', fg='white').grid(row=1, column=0)
            variable_mienbros = tk.StringVar(self.frame_valvulas)
            mienbros = [hp for hp in tuberias]
            tubos_already = ttk.Combobox(self.frame_valvulas,width=12,textvariable=variable_mienbros, state='readonly')
            tubos_already.configure(values=mienbros)
            tubos_already.current(len(tuberias)-1)
            tubos_already.grid(row=1,column=1,)
            tk.Label(self.frame_valvulas, text="Punto final(N. tubo):",bg='#2c2f33', fg='white').grid(row=2, column=0)
            P_codo = tk.Entry(self.frame_valvulas,width=12 )
            P_codo.grid(row=2,column=1)

            tk.Label(self.frame_valvulas, text="Material:",bg='#2c2f33', fg='white').grid(row=3, column=0)
            materiales = ["Acero", "Aluminio", "Bronce", "Cobre", "PVC"]
            combo = ttk.Combobox(self.frame_valvulas,width=12,state='readonly',values=materiales)
            combo.current(0) 
            combo.grid(row=3,column=1,padx=5)

            tk.Label(self.frame_valvulas, text="Delta de presión:",bg='#2c2f33', fg='white').grid(row=4, column=0)
            D_Presion = tk.Entry(self.frame_valvulas,width=12 )
            D_Presion.grid(row=4,column=1)

            var_c = tk.IntVar(value=1)
            chk_c = tk.Checkbutton(self.frame_valvulas,width=12,text="Tubería primaria:", bg='#2c2f33',fg='green',variable=var_c, justify='right')
            chk_c.grid(row=5,column=0 )
            def enviar_VALVULA():
                global contador_Valvulas, contador_tubos
                P_ubicacion = P_codo.get().split(',')
                tubo_alr = tubos_already.get()
                VALVULAS['valvula'+str(contador_Valvulas)] = [P_ubicacion,tubo_alr,var_c.get(),combo.get(),D_Presion.get()]
                print(VALVULAS)
                contador_Valvulas += 1

                P_inicial =  tuberias[tubo_alr][1]
                P_final =  P_ubicacion
                tuberias['tubo'+str(contador_tubos)] = [P_inicial,P_final,var_c.get(), combo.get(), D_Presion.get()] 
                print(tuberias)
                contador_tubos += 1

                #actualizar mienbros
                mienbros_ = [hp for hp in tuberias]
                tubos_already.configure(values=mienbros_)
                tubos_already.current(len(tuberias)-1)

            
            boton_enviar_ = tk.Button(self.frame_valvulas, text="Enviar", bg='#2c2f33', fg='white',command=enviar_VALVULA)
            boton_enviar_.grid(row=6, column=1)

    def borrar(self):
        global tuberias
        print(tuberias.keys())
    
    def accesorios(self):
        
        self.frame_valvulas.pack_forget()
        self.frame_propiedades.pack_forget()
        if self.frame2.winfo_manager():
            self.frame2.pack_forget()
            self.frame3.pack_forget()
            self.frame4.pack_forget()
            self.button1.pack_forget()
            self.button2.pack_forget()
            self.button3.pack_forget()
               
        else:
            self.frame4.pack_forget()
            self.frame2.pack()
            self.button1.pack(side=tk.LEFT, padx=5, pady=5)
            self.button2.pack(side=tk.RIGHT, padx=5, pady=5)
            self.button3.pack( padx=5, pady=5)

    def tuberia(self):
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        if self.frame3.winfo_manager():
            self.frame3.pack_forget()
            self.frame4.pack_forget()
            
        else:
            self.frame3.pack()
            self.frame4.pack()

    def Codo(self):
        if self.frame3.winfo_manager():
            self.frame3.pack_forget()
            self.frame4.pack_forget()
            self.frame5.pack_forget()
            self.frame6.pack_forget()
           
        else:
            self.frame3.pack()
            self.frame5.pack()
            tk.Label(self.frame5,width=12, text="Elemento:",bg='#2c2f33', fg='white').grid(row=0, column=0)
            variable_mienbros = tk.StringVar(self.frame5)
            mienbros = [hp for hp in tuberias]
            tubos_already = ttk.Combobox(self.frame5,width=12,textvariable=variable_mienbros, state='readonly')
            tubos_already.configure(values=mienbros)
            tubos_already.current(len(tuberias)-1)
            tubos_already.grid(row=0,column=1,)
            tk.Label(self.frame5, text="Punto final(N. tubo):",bg='#2c2f33', fg='white').grid(row=1, column=0)
            P_codo = tk.Entry(self.frame5,width=12 )
            P_codo.grid(row=1,column=1)

            tk.Label(self.frame5, text="Material:",bg='#2c2f33', fg='white').grid(row=2, column=0)
            materiales = ["Acero", "Aluminio", "Bronce", "Cobre", "PVC"]
            combo = ttk.Combobox(self.frame5,width=12,state='readonly',values=materiales)
            combo.current(0) 
            combo.grid(row=2,column=1,padx=5)

            tk.Label(self.frame5, text="Delta de presión:",bg='#2c2f33', fg='white').grid(row=3, column=0)
            D_Presion = tk.Entry(self.frame5,width=12 )
            D_Presion.grid(row=3,column=1)

            var_c = tk.IntVar(value=1)
            chk_c = tk.Checkbutton(self.frame5,width=12,text="Tubería primaria:", bg='#2c2f33',fg='green',variable=var_c, justify='right')
            chk_c.grid(row=4,column=0 )
            def enviar_codo():
                global contador_codo, contador_tubos
                P_ubicacion = P_codo.get().split(',')
                tubo_alr = tubos_already.get()
                codos['codo'+str(contador_codo)] = [P_ubicacion,tubo_alr,var_c.get()]
                print(codos)
                contador_codo += 1

                P_inicial =  tuberias[tubo_alr][1]
                P_final =  P_ubicacion
                tuberias['tubo'+str(contador_tubos)] = [P_inicial,P_final,var_c.get(), combo.get(), D_Presion.get()] 
                print(tuberias)
                contador_tubos += 1

                #actualizar mienbros
                mienbros_ = [hp for hp in tuberias]
                tubos_already.configure(values=mienbros_)
                tubos_already.current(len(tuberias)-1)

            
            boton_enviar_ = tk.Button(self.frame5, text="Enviar", bg='#2c2f33', fg='white',command=enviar_codo )
            boton_enviar_.grid(row=5, column=1)
    
    def Te(self):
        if self.frame3.winfo_manager():
            self.frame3.pack_forget()
            self.frame4.pack_forget()
            self.frame5.pack_forget()
            self.frame6.pack_forget()
           
        else:
            self.frame3.pack()
            self.frame6.pack()
            tk.Label(self.frame6,width=12, text="Elemento:",bg='#2c2f33', fg='white').grid(row=0, column=0)
            variable_mienbros = tk.StringVar(self.frame6)
            mienbros = [hp for hp in tuberias]
            tubos_already = ttk.Combobox(self.frame6,width=12,textvariable=variable_mienbros, state='readonly')
            tubos_already.configure(values=mienbros)
            tubos_already.current(len(tuberias)-1)
            tubos_already.grid(row=0,column=1,)
            tk.Label(self.frame6, text="Punto final 1(N. tubo):",bg='#2c2f33', fg='white').grid(row=1, column=0)
            P_Te = tk.Entry(self.frame6,width=12 )
            P_Te.grid(row=1,column=1)
            tk.Label(self.frame6, text="Punto final 2(N. tubo):",bg='#2c2f33', fg='white').grid(row=2, column=0)
            P_Te_2 = tk.Entry(self.frame6,width=12 )
            P_Te_2.grid(row=2,column=1)

            tk.Label(self.frame6, text="Material:",bg='#2c2f33', fg='white').grid(row=3, column=0)
            materiales = ["Acero", "Aluminio", "Bronce", "Cobre", "PVC"]
            combo = ttk.Combobox(self.frame6,width=12,state='readonly',values=materiales)
            combo.current(0) 
            combo.grid(row=3,column=1,padx=5)

            tk.Label(self.frame6, text="Delta de presión:",bg='#2c2f33', fg='white').grid(row=4, column=0)
            D_Presion = tk.Entry(self.frame6,width=12 )
            D_Presion.grid(row=4,column=1)

            var_c = tk.IntVar(value=1)
            chk_c = tk.Checkbutton(self.frame6,width=12,text="Tubería primaria:", bg='#2c2f33',fg='green',variable=var_c, justify='right')
            chk_c.grid(row=5,column=0 )
            def enviar_Te():
                global contador_Te, contador_tubos
                P_ubicacion = P_Te.get().split(',')
                P_ubicacion_2 = P_Te_2.get().split(',')
                tubo_alr = tubos_already.get()
                Tes['Te'+str(contador_Te)] = [P_ubicacion,tubo_alr,var_c.get(),P_ubicacion_2]
                print(Tes)
                contador_Te += 1

                P_inicial =  tuberias[tubo_alr][1]
                P_final =  P_ubicacion
                P_final_2 =  P_Te_2.get().split(',')
                tuberias['tubo'+str(contador_tubos)] = [P_inicial,P_final,var_c.get(), combo.get(), D_Presion.get()] 
                contador_tubos += 1
                tuberias['tubo'+str(contador_tubos)] = [P_inicial,P_final_2,var_c.get(), combo.get(), D_Presion.get()] 
                contador_tubos += 1
                print(tuberias)

                #actualizar mienbros
                mienbros_ = [hp for hp in tuberias]
                tubos_already.configure(values=mienbros_)
                tubos_already.current(len(tuberias)-1)

            
            boton_enviar_ = tk.Button(self.frame6, text="Enviar", bg='#2c2f33', fg='white',command=enviar_Te )
            boton_enviar_.grid(row=6, column=1)

    
    

    def tubo(self):
        global contador_tubos
        P_inicial =  self.punto_inicio.get().split(',')
        P_final =  self.punto_final.get().split(',')
        tuberias['tubo'+str(contador_tubos)] = [P_inicial,P_final,self.var.get(), self.combo.get(), self.D_Presion.get()] 

        print(tuberias)
        contador_tubos += 1
    
class Application:
    def __init__(self, master, theme='light'):
        self.master = master
        self.master.title('Red de aire comprimido')
        self.master.iconbitmap("calculoDiagnosticoRedAireComprimido/imagenes/logo.ico")
        self.master.geometry('700x540')
        self.master.minsize(700, 530)
        

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
        self.editar_sistema = tk.Button(self.master, text="Editar sistema",width=20, height=2, bg=bg_color, fg=fg_color, command=self.edit_sistem)
        
        
        self.graficador = tk.Frame(self.master, width=300, height=300, bg='red')
        self.graficador.pack( fill=tk.BOTH, expand=True)
        self.frame_general = tk.Frame(self.graficador,)
        self.frame_general.pack(fill=tk.BOTH, expand=True)
        

        self.editar_sys = tk.Frame(self.graficador, width=300, height=300, bg='red')
        

        self.img = Figure(figsize=(3, 3), dpi=120)
        ax = self.img.add_subplot(111, projection='3d')
        self.canvas_ = FigureCanvasTkAgg(self.img, master=self.frame_general)
        self.canvas_.draw()
        self.canvas_.get_tk_widget().pack(side='right', fill=tk.BOTH, expand=True)

        

    def toggle_menu(self):
        if self.menu_visible:
            self.side_menu.frame.pack_forget()
            self.actualizar.pack_forget()
            self.editar_sistema.pack_forget()
            self.show_menu_button.config(text='Mostrar el menú')
        else:
            self.side_menu.frame.pack(side='left',  fill=tk.BOTH, )
            self.graficador.pack( side='right', fill=tk.BOTH, expand=True)
            self.editar_sistema.pack(side='bottom', fill=tk.X, expand=True, after=self.graficador)
            self.actualizar.pack(side='bottom', fill=tk.X, expand=True, after=self.editar_sistema)
            
            self.show_menu_button.config(text='Ocultar el menú')

        self.menu_visible = not self.menu_visible

    def edit_sistem(self):

        self.frame_general.pack_forget()
        
        if self.editar_sys.winfo_manager():
            self.editar_sys.pack_forget()
            self.frame_general.pack(fill=tk.BOTH, expand=True)
        else:
            self.editar_sys.pack(fill=tk.BOTH, expand=True)
            for widget in self.editar_sys.winfo_children():
                widget.destroy()
            # Creamos un widget Canvas
            canvas_sc = tk.Canvas(self.editar_sys)
            canvas_sc.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Creamos un widget Scrollbar y lo asociamos con el Canvas
            scrollbar = tk.Scrollbar(self.editar_sys, command=canvas_sc.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            # Configuramos el Canvas para que use el Scrollbar vertical
            canvas_sc.configure(yscrollcommand=scrollbar.set)

            # Creamos un Frame para poner dentro del Canvas
            frame_f_ = tk.Frame(canvas_sc, bg='green')
            
            frame_tubos = tk.Frame(frame_f_, bg='red')
            frame_tubos.grid(column=0, row=0, padx=5 )
            
            i = 0
            for hp in tuberias.keys():
                tk.Label(frame_tubos, text=hp, bg='white', fg='black').grid(row=i, column=0)
                #botones editar
                self.borrar_b = tk.Button(frame_tubos,width=6, text='Borrar', bg='#2c2f33', fg='red', command=self.borrar)
                self.update = tk.Button(frame_tubos,width=7, text='Actualizar',  bg='#2c2f33', fg='green', command=self.borrar)
                self.borrar_b.grid(row=i, column=2)
                self.update.grid(row=i, column=1)
                i += 1
            frame_codos = tk.Frame(frame_f_, bg='blue')
            frame_codos.grid(column=1, row=0, padx=5)
            i = 0
            for hp in codos.keys():
                tk.Label(frame_codos, text=hp, bg='white', fg='black').grid(row=i, column=0)
                #botones editar
                self.borrar_co = tk.Button(frame_codos, width=6,text='Borrar', bg='#2c2f33', fg='red', command=self.borrar)
                self.update_co = tk.Button(frame_codos,width=7, text='Actualizar',  bg='#2c2f33', fg='green', command=self.borrar)
                self.borrar_co.grid(row=i, column=2)
                self.update_co.grid(row=i, column=1)
                i += 1
            frame_tes = tk.Frame(frame_f_, bg='red')
            frame_tes.grid(column=2, row=0, padx=5,)
            
            i = 0
            for hp in Tes.keys():
                tk.Label(frame_tes, text=hp, bg='white', fg='black').grid(row=i, column=0, )
                #botones editar
                self.borrar_te = tk.Button(frame_tes,width=6, text='Borrar', bg='#2c2f33', fg='red', command=self.borrar)
                self.update_te = tk.Button(frame_tes, width=7,text='Actualizar',  bg='#2c2f33', fg='green', command=self.borrar)
                self.borrar_te.grid(row=i, column=2)
                self.update_te.grid(row=i, column=1)
                i += 1
            
            # Colocamos el Frame dentro del Canvas
            canvas_sc.create_window((0, 0), window=frame_f_, anchor="center",)

            # Configuramos el tamaño del Canvas
            frame_f_.update_idletasks()
            frame_f_.pack_configure(fill='x')
            canvas_sc.configure(scrollregion=canvas_sc.bbox("all"))
            print('edit')      

    def borrar(self):
        global tuberias
        print(tuberias.keys())
           
    def actualizar(self):
        self.editar_sys.pack_forget()
        self.frame_general.pack(fill=tk.BOTH, expand=True)
        
        
        self.img.clf()
        ax = self.img.add_subplot(111, projection='3d')
        for hp in tuberias:
            P_inicial = [int(tuberias[hp][0][0]),int(tuberias[hp][0][1]),int(tuberias[hp][0][2])]
            P_final = [int(tuberias[hp][1][0]),int(tuberias[hp][1][1]),int(tuberias[hp][1][2])]
            x_line = np.array([P_inicial[0], P_final[0]])
            y_line = np.array([P_inicial[1], P_final[1]])
            z_line = np.array([P_inicial[2], P_final[2]])
            x_point, y_point, z_point = np.mean(x_line), np.mean(y_line), np.mean(z_line)
            texto = hp
            if tuberias[hp][2]==1: #tuberia primaria
                ax.plot(x_line, y_line, z_line,color='blue')
                
                ax.text(x_point, y_point, z_point, texto, color='black', fontsize=12)
            else: #tuberia secundaria
                ax.plot(x_line, y_line, z_line,color='red')       
    
                ax.text(x_point, y_point, z_point, texto, color='black', fontsize=12)
            
        for hp in codos:
            P_ubicacion = codos[hp][0]
            mienbro = codos[hp][1]
            P_mienbro = tuberias[mienbro][1]
            P_mienbro_i = tuberias[mienbro][0]
            P_inicial_m = np.array([int(P_mienbro_i[0]),int(P_mienbro_i[1]),int(P_mienbro_i[2])])
            P_inicial = np.array([int(P_mienbro[0]),int(P_mienbro[1]),int(P_mienbro[2])])
            P_final = np.array([int(P_ubicacion[0]),int(P_ubicacion[1]), int(P_ubicacion[2])])
            
            P_inicial_re = [P_inicial_m[0]+(P_inicial[0]-P_inicial_m[0])*0.9, P_inicial_m[1]+(P_inicial[1]-P_inicial_m[1])*0.9, P_inicial_m[2]+(P_inicial[2]-P_inicial_m[2])*0.9 ]
            P_final_re = [P_inicial[0]+(P_final[0]-P_inicial[0])*0.1, P_inicial[1]+(P_final[1]-P_inicial[1])*0.1, P_inicial[2]+(P_final[2]-P_inicial[2])*0.1]
            

            if codos[hp][2]==1: #tuberia primaria
                ax.plot([P_inicial[0],P_inicial_re[0]],[P_inicial[1],P_inicial_re[1]],[P_inicial[2],P_inicial_re[2]],color='black',linewidth=4)
                ax.plot([P_final_re[0],P_inicial[0]],[P_final_re[1],P_inicial[1]],[P_final_re[2],P_inicial[2]],color='black',linewidth=4)
                
            else: #tuberia secundaria
                ax.plot([P_inicial[0],P_inicial_re[0]],[P_inicial[1],P_inicial_re[1]],[P_inicial[2],P_inicial_re[2]],color='black',linewidth=4)
                ax.plot([P_final_re[0],P_inicial[0]],[P_final_re[1],P_inicial[1]],[P_final_re[2],P_inicial[2]],color='black',linewidth=4)

        for hp in Tes:
            P_ubicacion = Tes[hp][0]
            P_ubicacion_2 = Tes[hp][3]
            mienbro = Tes[hp][1] 
            P_mienbro = tuberias[mienbro][1]
            P_mienbro_i = tuberias[mienbro][0]
            P_inicial_m = np.array([int(P_mienbro_i[0]),int(P_mienbro_i[1]),int(P_mienbro_i[2])])
            P_inicial = np.array([int(P_mienbro[0]),int(P_mienbro[1]),int(P_mienbro[2])])
            P_final = np.array([int(P_ubicacion[0]),int(P_ubicacion[1]), int(P_ubicacion[2])])
            P_final_2 = np.array([int(P_ubicacion_2[0]),int(P_ubicacion_2[1]), int(P_ubicacion_2[2])])
            
            P_inicial_re = [P_inicial_m[0]+(P_inicial[0]-P_inicial_m[0])*0.9, P_inicial_m[1]+(P_inicial[1]-P_inicial_m[1])*0.9, P_inicial_m[2]+(P_inicial[2]-P_inicial_m[2])*0.9 ]
            P_final_re = [P_inicial[0]+(P_final[0]-P_inicial[0])*0.1, P_inicial[1]+(P_final[1]-P_inicial[1])*0.1, P_inicial[2]+(P_final[2]-P_inicial[2])*0.1]
            P_3 = [P_inicial[0]+(P_final_2[0]-P_inicial[0])*0.1, P_inicial[1]+(P_final_2[1]-P_inicial[1])*0.1, P_inicial[2]+(P_final_2[2]-P_inicial[2])*0.1]

            if Tes[hp][2]==1: #tuberia primaria
                ax.plot([P_inicial[0],P_inicial_re[0]],[P_inicial[1],P_inicial_re[1]],[P_inicial[2],P_inicial_re[2]],color='black',linewidth=4)
                ax.plot([P_inicial[0],P_3[0]],[P_inicial[1],P_3[1]],[P_inicial[2],P_3[2]],color='black',linewidth=4)
                ax.plot([P_final_re[0],P_inicial[0]],[P_final_re[1],P_inicial[1]],[P_final_re[2],P_inicial[2]],color='black',linewidth=4)
                
            else: #tuberia secundaria
                ax.plot([P_inicial[0],P_inicial_re[0]],[P_inicial[1],P_inicial_re[1]],[P_inicial[2],P_inicial_re[2]],color='black',linewidth=4)
                ax.plot([P_inicial[0],P_3[0]],[P_inicial[1],P_3[1]],[P_inicial[2],P_3[2]],color='black',linewidth=4)
                ax.plot([P_final_re[0],P_inicial[0]],[P_final_re[1],P_inicial[1]],[P_final_re[2],P_inicial[2]],color='black',linewidth=4)

            for hp in VALVULAS:
                P_inicial = tuberias[VALVULAS[hp][1]][1]
                print(P_inicial)
                if VALVULAS[hp][2]==1:#tuberia primaria
                    ax.plot(P_inicial[0],P_inicial[1],P_inicial[2],color='black',linewidth=10)
                    
        self.canvas_.draw()



               

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root, theme='dark')
    root.mainloop()


