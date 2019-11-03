from lab2_backend import *

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk

class LabGUI(tk.Frame):
    
    def __init__(self, parent):
        
        tk.Frame.__init__(self, parent)
        self.parent = parent
        
        parent.geometry('1450x700+50+50')
        parent.title('approximation')
                        
        self.init_input_filename()
        self.init_label_filename()
        
        self.init_x_leng()
        self.init_y_leng()
        
        self.init_choose_polynomial()
        self.init_create_pads()
        
        self.init_polynomial_degrees()
        self.init_function_weight()
        self.init_y_coord()
        
        self.init_run_button()
        self.init_default_checkbutton()
        self.init_all_labels()
        self.init_output_label()
        self.init_graph_canvas()
        
        self.first_run = True
        
    def init_label(self, text, column, row, columnspan=1, rowspan=1, height=1):
        
        label = tk.Label(self.parent, text=text, height=height)
        label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan)
        
        
    def init_variable_label(self, variable, column, row, columnspan=1, rowspan=1):
        
        label = tk.Label(self.parent, textvariable=variable)
        label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan)
        
        
    def init_entry(self, variable, text, column, row, columnspan=1, rowspan=1, width=4):
        
        entry = tk.Entry(
            self.parent, text=text,
            textvariable=variable, width=width)    
        
        entry.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=tk.W)
    
    
    def init_label_with_entry(self, text, column, row, variable, columnspan=1, rowspan=1, entry_width=4):
        
        self.init_label(text=text, column=column, row=row)       
        self.init_entry(text=text, column=column+1, row=row, variable=variable, width=entry_width)
 

    def init_radiobutton(self, text, column, row, variable, value, columnspan=1):
        
        rdbutton = tk.Radiobutton(self.parent, text=text, value=value, variable=variable)
        rdbutton.grid(row=row, column=column, columnspan=columnspan, sticky=tk.W)
        
        
    def init_pads(self, row=1, column=1, width=0, height=0):
        
        label = tk.Frame(self.parent, width=width, height=height)
        label.grid(column=column, row=row)
    
    
    def init_button(self, text, column, row, width, height, columnspan=1, rowspan=1, command=None):
        butt = tk.Button(self.parent, text=text, width=width, height=height, command=command)
        butt.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan)
    
    #Buttons
    
    def init_run_button(self):
        self.init_button(text = 'Розрахувати', width=10, height=1, 
                         column=11, row=5, rowspan=2, columnspan=2,
                         command=self.run)
    
    
    def init_default_checkbutton(self):
        self.default_data = tk.BooleanVar(value=True)
        checkbutton = tk.Checkbutton(
            self.parent, text='Стандартні значення', variable=self.default_data)
        checkbutton.grid(column=1, row=4)
    
    # Labels
    
    def init_create_pads(self):
        
        self.init_pads(column=2, width=35)
        self.init_pads(column=5, width=35)
        self.init_pads(column=7, width=20)
        self.init_pads(column=10, width=35)
        self.init_pads(row=7, height=30)
        self.init_pads(row=9, height=8)
    
    def init_all_labels(self):
        
        self.init_label(text = 'Ваги цільових функцій', column=11, row=0, columnspan=1, rowspan=2)
        
        self.init_label(text = 'Вибірка', column=0, row=0,columnspan=2, rowspan=2)
        self.init_label(text = 'Вектори', column=3, row = 0, columnspan=2, rowspan=2)
        self.init_label(text = 'Поліноми', column=6, row=0, columnspan=4, height=2)
        self.init_label(text = 'Вид', column=6, row=1)
        self.init_label(text = 'Степінь', column=8, row=1)
        
        self.init_label(text = 'Результат', column=0, row=8, columnspan=6)
        self.init_label(text = 'Графік', column=7, row=8, columnspan=6)  
        
    
    def init_output_label(self):
        
        self.scrolled_text = ScrolledText(
            master=self.parent, wrap='word', width=80, height=24, font=('TkDefaultFont', 11))
        
        self.scrolled_text.grid(column=0, row=10, columnspan=7)
        self.set_output_text('Натисніть на кнопку "Розрахувати"')
        self.scrolled_text.config(state=tk.DISABLED)
    
    
    def init_graph_canvas(self):
        self.canvas_size = (700, 450)
        self.graph_canvas = tk.Canvas(self.parent, bg="#fff", height=self.canvas_size[1], width=self.canvas_size[0])
        self.graph_canvas.grid(column=8, row=10, columnspan=6, sticky=tk.NW)
    
    # RadioButtons   
    
    def init_choose_polynomial(self):
        self.polynomial_type = tk.StringVar(value='chebyshev_first')
        self.init_radiobutton(text = 'Чебишева 1-го порядку', row=2, column=6, value='chebyshev_first', variable=self.polynomial_type)
        self.init_radiobutton(text = 'Чебишева 2-го порядку', row=3, column=6, value='chebyshev_second', variable=self.polynomial_type)
        self.init_radiobutton(text = 'Лежандра', row=4, column=6, value='legendre', variable=self.polynomial_type)
        self.init_radiobutton(text = 'Лагерра', row=5, column=6, value='laguerre', variable=self.polynomial_type)
        self.init_radiobutton(text = 'Ерміта', row=6, column=6, value='hermite', variable=self.polynomial_type)
         
    def init_function_weight(self):
        self.weight_average = tk.BooleanVar()
        
        self.init_radiobutton(
            text = 'Через максимум  і мінімум', row=2, column=11, columnspan=2, 
            value=False, variable=self.weight_average)
        
        self.init_radiobutton(
            text = 'Середнє арифметичне', row=3, column=11, columnspan=2,
            value=True, variable=self.weight_average)        
        
    # Labels with entries
    
    def init_samples_length(self):
        
        self.samples_length = tk.IntVar()
        self.init_label_with_entry(
            text='Розмір вибірки', column=0, row=2,
            variable=self.samples_length)
        
    def init_input_filename(self):
        self.input_filename = tk.StringVar(value='features.txt')
        self.init_label_with_entry(
            text='Файл зі значеннями x', column=0, row=2,
            variable=self.input_filename, entry_width=15)
        
    def init_label_filename(self):
        self.label_filename = tk.StringVar(value='labels.txt')
        self.init_label_with_entry(
            text='Файл зі значеннями y', column=0, row=3,
            variable=self.label_filename, entry_width=15) 
    
    def init_x_leng(self):
        self.x_leng_var = [tk.IntVar(value=def_value) for def_value in (3, 2, 2)]
        
        for ind, var in enumerate(self.x_leng_var):  
            self.init_label_with_entry(
                text='Розмірність x' + str(ind+1), column=3, row=ind+2,
                variable=var)
            
    def init_y_leng(self):
        self.y_leng = tk.IntVar(value=4)
        self.init_label_with_entry(
            text='Розмірність y', column=3, row=5,
            variable=self.y_leng)
    
    def init_polynomial_degrees(self):
        self.polynomial_degrees = [tk.IntVar(value=3) for _ in range(3)]
        
        for ind, var in enumerate(self.polynomial_degrees):  
            self.init_label_with_entry(
                text='Степінь x' + str(ind+1), column=8, row=ind+2,
                variable=var)
    
    def init_y_coord(self):
        self.y_coord = tk.IntVar(value=1)
        self.init_label_with_entry(
            text='Координата y', column=11, row=4,
            variable=self.y_coord)
    
    
    def set_output_text(self, output):
        
        self.scrolled_text.config(state=tk.NORMAL)
        self.scrolled_text.delete(1.0, tk.END)
        self.scrolled_text.insert(1.0, output)
        self.scrolled_text.config(state=tk.DISABLED)
    
    
    def update_graph(self):
        
        self.graph_image = ImageTk.PhotoImage(
            Image.open('graph.png').resize(self.canvas_size, Image.ANTIALIAS))
        
        if self.first_run:
            self.canvas_image = self.graph_canvas.create_image(
                0, 0, image=self.graph_image,  anchor='nw')
        else:
            self.graph_canvas.itemconfigure(self.canvas_image, image=self.graph_image)
    
    
    def add_output(self, inp='', new_line=True):
        self.output += str(inp)
        if new_line: self.output += '\n'
    
    
    def get_subscript(self, symbol):
        if symbol == 'i': return u'\u1d62'
        return chr(ord(u'\u2080') + symbol)
    
    
    def print_equation_3(self, coeff_matrix, lengths, degrees, coeff_name='λ', function_name='ψ', var_name='T'):
                
        ind = 0
        for eq_ind, (length, degree_range) in enumerate(zip(lengths, degrees)):
            self.add_output()
            self.add_output(
                'Матриця коефіціентів {0}{1}'.format(coeff_name, self.get_subscript(eq_ind + 1)))
            coeff_matrix_part = coeff_matrix[ind: ind + length * degree_range].reshape(length, degree_range)
            self.add_output(coeff_matrix_part)
            ind += length * degree_range
        
        ind = 0
        for eq_ind, (length, degree_range) in enumerate(zip(lengths, degrees)):
            
            #ind = 0
            
            for var_ind in range(length):
                self.add_output()
                
                self.add_output(
                    '{0}{1}{2}(x{1}{2}) = '.format(
                        function_name, 
                        self.get_subscript(eq_ind + 1), 
                        self.get_subscript(var_ind + 1)), 
                    new_line=False)
                                
                for degree in range(degree_range):
                    
                    if degree != 0:
                        if coeff_matrix[ind] >= 0:
                            self.add_output(' + ', new_line=False)
                        else:
                            self.add_output(' - ', new_line=False)
                        
                    self.add_output(
                    '{0:.5} {1}{2}(x{3}{4})'.format(
                        np.abs(coeff_matrix[ind]), var_name, self.get_subscript(degree),
                        self.get_subscript(eq_ind + 1), self.get_subscript(var_ind + 1)), new_line=False)
                    
                    ind += 1
    
    
    def print_equation_2(self, coeff_matrixes, target_ind=1, coeff_name='a', function_name='F', var_name='ψ'):
        
        for eq_ind, coeff_matrix in enumerate(coeff_matrixes):
            self.add_output()
            self.add_output(
                    'Вектор коефіціентів {0}{1}{2}'.format(
                        coeff_name, self.get_subscript(target_ind),
                        self.get_subscript(eq_ind + 1)))
            self.add_output(coeff_matrix)
        
        for eq_ind, coeff_matrix in enumerate(coeff_matrixes):
            
            self.add_output()
                
            self.add_output(
                '{0}{1}{2}(x{2}) = '.format(
                    function_name, self.get_subscript(target_ind),
                    self.get_subscript(eq_ind + 1)), 
                new_line=False)
                                
            for var_ind in range(coeff_matrix.shape[0]):
                    
                if var_ind != 0:
                    if coeff_matrix[var_ind] >= 0:
                        self.add_output(' + ', new_line=False)
                    else:
                        self.add_output(' - ', new_line=False)
                        
                self.add_output(
                '{0:.5} {1}{2}{3}(x{2}{3})'.format(
                    np.abs(coeff_matrix[var_ind]), var_name, self.get_subscript(eq_ind + 1),
                    self.get_subscript(var_ind + 1)), new_line=False)
                
                
    def print_equation_1(self, coeff_matrix, target_ind=1, coeff_name='c', function_name='Φ', var_name='F'):
                    
        self.add_output()
        self.add_output('Вектор коефіціентів {0}'.format(coeff_name))
        self.add_output(coeff_matrix)
        self.add_output()
                
        self.add_output(
            '{0}{1}(x) = '.format(
                function_name, self.get_subscript(target_ind)), 
            new_line=False)
                                
        for var_ind in range(coeff_matrix.shape[0]):
                    
            if var_ind != 0:
                if coeff_matrix[var_ind] >= 0:
                    self.add_output(' + ', new_line=False)
                else:
                    self.add_output(' - ', new_line=False)
                        
            self.add_output(
                '{0:.5} {1}{2}{3}(x{2})'.format(
                np.abs(coeff_matrix[var_ind]), var_name, self.get_subscript(var_ind + 1),
                self.get_subscript(target_ind)), new_line=False)
                        
    
    def output_diff(self, A, b, coeff, on_array=False):
        
        self.add_output()
        self.add_output()
        self.add_output("Нев'язка")

        if on_array: 
            diff = np.array([np.max(np.dot(A_inst, coeff_inst.T) - b) for A_inst, coeff_inst in zip(A, coeff)])
            self.add_output('{0}'.format(diff))
        else: 
            diff = np.max(np.dot(A, coeff.T) - b)
            self.add_output('{0:.5}'.format(diff))
            
        self.add_output()
    
    
    def run(self):
        
        self.output = ''
        np.set_printoptions(precision=5)
        
        self.polynomial_var = {
            'chebyshev_first': 'T',
            'chebyshev_second': 'U',
            'legendre': 'P',
            'hermite': 'H',
            'laguerre': 'L'
        }.get(self.polynomial_type.get())
        
        feature_lengths = ()
        
        if self.default_data.get(): 
            data = default_input()
            feature_lengths = (3, 2, 2)
        else: 
            data = read_input_from_file(self.input_filename.get(), self.label_filename.get())
            feature_lengths = [length.get() for length in self.x_leng_var]
        
        feature_ranges = get_ranges(feature_lengths)
        feature_amount = len(feature_lengths)
        
        polynomial_degree_values = [polynomial_degree.get() for polynomial_degree in self.polynomial_degrees]
                
        x, y = [normalize_data(item) for item in data]
                
        y_variable = y[:, self.y_coord.get() - 1]
        
        b = np.empty(y.shape[0], dtype=np.float32)
        
        if self.weight_average: b = y.mean(axis=1)
        else: b = (y.min(axis=1) + y.max(axis=1)) / 2
        
        A_full = create_equation_matrix_simult(
            x, polynomial_type=self.polynomial_type.get(), 
            polynomial_degrees=polynomial_degree_values,
            feature_lengths=(2, 2, 3))
                
        lambda_matrix_full = np.linalg.lstsq(A_full, b)[0]
                                        
        save_graph(b, np.dot(A_full, lambda_matrix_full.T))
        self.update_graph()
        
        self.add_output('Третій ієрархічний рівень')
        self.add_output('Формування функцій ψ')
        
        self.print_equation_3(
            coeff_matrix=lambda_matrix_full, lengths=feature_lengths, degrees=polynomial_degree_values, 
            coeff_name='λ', function_name='ψ', var_name=self.polynomial_var)
        
        self.output_diff(A=A_full, b=b, coeff=lambda_matrix_full)

        phi_values_full = []
        row_ind = 0
        
        for feature_ind, (feature_length, polynomial_degree) in enumerate(zip(feature_lengths, polynomial_degree_values)):
            phi_values = []
            
            for variable_ind in range(feature_length):
                A_part = A_full[:, row_ind: row_ind + polynomial_degree]
                lambda_part = lambda_matrix_full[row_ind: row_ind + polynomial_degree]
                row_ind = row_ind + polynomial_degree
                phi_values.append(np.dot(A_part, lambda_part))
                
            phi_values = np.array(phi_values).T
            phi_values_full.append(phi_values)
        
        self.add_output('Другий ієрархічний рівень')
        self.add_output('Формування функцій F')
        
        a_matrixes = [np.linalg.lstsq(phi_values, y_variable)[0] for phi_values in phi_values_full]
            
        self.print_equation_2(coeff_matrixes=a_matrixes, target_ind=self.y_coord.get())
        
        self.output_diff(A=phi_values_full, b=y_variable, coeff=a_matrixes, on_array=True)
        
        F_values = np.array([phi_values @ a_matrix.T for phi_values, a_matrix in zip(phi_values_full, a_matrixes)]).T

        self.add_output('Перший ієрархічний рівень')
        self.add_output('Формування функцій Φ')
        
        c_matrix = np.linalg.lstsq(F_values, y_variable)[0]
        
        self.print_equation_1(coeff_matrix=c_matrix, target_ind=self.y_coord.get())
        
        self.output_diff(A=F_values, b=y_variable, coeff=c_matrix)
        
        approx_values = F_values @ c_matrix.T
        
        lambda_matrix_y = np.linalg.lstsq(A_full, y_variable)[0]
                               
        save_graph(y_variable, np.dot(A_full, lambda_matrix_y.T)) 
        self.update_graph()
                
        self.set_output_text(self.output)
        
        if self.first_run: self.first_run = False