import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox 
from the_math import Converter

def test_N_to_Q():

    final_answers = []
    this_converter = Converter()

    for index in range(1,10000):
        this_converter.set_natural_number(index)
        this_converter.convert_N_to_Q()
        the_answer=this_converter.get_answer()
        final_answers.append({'num':the_answer['final_num'],'den':the_answer['final_den'], 'answer':the_answer['final_N']})

    this_file=open('testing_ouput.txt','w')
    for one_value in final_answers:
        this_file.write('{},{},{}\n'.format(one_value['num'],one_value['den'],one_value['answer']))

    this_file.close()

    messagebox.showinfo(title='Status', message='Done')
    
def test_Q_to_N():

    values_used = []

    final_answers = []
    this_converter=Converter()

    for denominator in range(1,10):
        for numerator in range(1,20):
            if not (numerator/denominator) in values_used:
                this_converter.set_rational_number(numerator,denominator)
                this_converter.convert_Q_to_N()
                the_answer = this_converter.get_answer()
                final_answers.append({'num':numerator,'den':denominator, 'answer':the_answer['final_N']})
                values_used.append(numerator/denominator)

    this_file=open('testing_ouput.txt','w')
    for one_value in final_answers:
        this_file.write('{},{},{}\n'.format(one_value['num'],one_value['den'],one_value['answer']))

    this_file.close()

    messagebox.showinfo(title='Status', message='Done')
def switch():
    global The_Frame_Q_to_N
    global The_Frame_N_to_Q
    global which_frame

    if which_frame == 'Q_to_N':
        The_Frame_N_to_Q.tkraise()
        which_frame = 'N_to_Q'
    else:
        The_Frame_Q_to_N.tkraise()
        which_frame = 'Q_to_N'

def convert_Q_to_I():
    global The_Frame_Q_to_N

    numerator = The_Frame_Q_to_N.nametowidget('numerator').get()
    denomenator = The_Frame_Q_to_N.nametowidget('denomenator').get()

    if not all([x.isdigit() for x in numerator]):
        messagebox.showwarning(title='Numerator Error', message='Numerator must be a natural number')
        return
    
    if not all([x.isdigit() for x in denomenator]):
        messagebox.showwarning(title='Denomenator Error', message='Denomenator must be a natural number')
        return
    
    if all([x=='0' for x in denomenator]):
        messagebox.showwarning(title='Denomenator Error', message='Denomenator must be greater than zero')
        return
        
    this_converter = Converter()
    this_converter.set_rational_number(int(numerator),int(denomenator))
    this_converter.convert_Q_to_N()
    the_answer = this_converter.get_answer()

    the_answer_label = The_Frame_Q_to_N.nametowidget('corr_natural')
    the_answer_label['text']=the_answer['final_N']

    The_Frame_Q_to_N.update()

def convert_I_to_Q():
    global The_Frame_N_to_Q

    natural_number = The_Frame_N_to_Q.nametowidget('natural_number').get()
    if not all([x.isdigit() for x in natural_number]):
        messagebox.showwarning(title='Natural number Error', message='Natural number must be a natural number')
        return

    this_converter = Converter()
    this_converter.set_natural_number(int(natural_number))
    this_converter.convert_N_to_Q()
    the_answer = this_converter.get_answer()
    the_answer_label = The_Frame_N_to_Q.nametowidget('corr_rational')
    the_answer_label['text']='{}/{}'.format(the_answer['final_num'],the_answer['final_den'])

    The_Frame_Q_to_N.update()    

The_Gui = tk.Tk()
this_font=tkfont.Font(family='Helvitica', size=16)   

The_Gui.title('Q to N Mapping')
this_row=0
The_Gui.grid_rowconfigure(this_row, weight=1)
The_Gui.grid_columnconfigure(0, weight=1)

this_row += 1
The_Frame_Q_to_N = tk.Frame(The_Gui, highlightbackground='black', highlightthickness=2 )
The_Frame_Q_to_N.grid(row=this_row, column=1, sticky='news', padx=100, pady=100)

The_Frame_N_to_Q = tk.Frame(The_Gui, highlightbackground='black', highlightthickness=2 )
The_Frame_N_to_Q.grid(row=1, column=1, sticky='news', padx=100, pady=100)

which_frame = 'Q_to_N'
The_Frame_Q_to_N.tkraise()

this_row += 1
tk.Button(The_Gui, text='Switch Direction', font=this_font,command=switch).grid(row=this_row, column=1, sticky='news')

this_row += 1
tk.Button(The_Gui, text='Test', font=this_font,command=test_N_to_Q).grid(row=this_row, column=1, sticky='news')

The_Gui.grid_rowconfigure(this_row, weight=1)
The_Gui.grid_columnconfigure(2, weight=1)


this_row=0
The_Frame_Q_to_N.grid_rowconfigure(this_row, weight=1)
The_Frame_Q_to_N.grid_columnconfigure(0, weight=1)

this_row += 1
tk.Label(The_Frame_Q_to_N, text=' Find a rational number\'s corresponding natural number', font=this_font,).grid(row=this_row, column=2, columnspan = 3)

this_row += 1
tk.Label(The_Frame_Q_to_N, text='Numerator :', font=this_font,).grid(row=this_row, column=1)
tk.Entry(The_Frame_Q_to_N, name='numerator', font=this_font,).grid(row=this_row, column=2)

this_row += 1
tk.Label(The_Frame_Q_to_N, text='Denomenator :', font=this_font,).grid(row=this_row, column=1)
tk.Entry(The_Frame_Q_to_N, name='denomenator', font=this_font,).grid(row=this_row, column=2)

this_row += 1
tk.Label(The_Frame_Q_to_N, text='Corresponding Natural Number :', font=this_font,).grid(row=this_row, column=1)
tk.Label(The_Frame_Q_to_N, name='corr_natural', font=this_font,).grid(row=this_row, column=2)

this_row += 1
tk.Button(The_Frame_Q_to_N, text='Convert', font=this_font, command=convert_Q_to_I).grid(row=this_row, column=2, columnspan = 3)

The_Frame_Q_to_N.grid_rowconfigure(this_row, weight=1)
The_Frame_Q_to_N.grid_columnconfigure(4, weight=1)




this_row=0
The_Frame_N_to_Q.grid_rowconfigure(this_row, weight=1)
The_Frame_N_to_Q.grid_columnconfigure(0, weight=1)

this_row += 1
tk.Label(The_Frame_N_to_Q, text=' Find a natural number\'s corresponding rational number', font=this_font,).grid(row=this_row, column=2, columnspan = 3)

this_row += 1
tk.Label(The_Frame_N_to_Q, text='Natural Number :', font=this_font,).grid(row=this_row, column=1)
tk.Entry(The_Frame_N_to_Q, name='natural_number', font=this_font,).grid(row=this_row, column=2)

this_row += 1
tk.Label(The_Frame_N_to_Q, text='Corresponding Rational Number :', font=this_font,).grid(row=this_row, column=1)
tk.Label(The_Frame_N_to_Q, name='corr_rational', font=this_font,).grid(row=this_row, column=2)

this_row += 1
tk.Button(The_Frame_N_to_Q, text='Convert', font=this_font, command=convert_I_to_Q).grid(row=this_row, column=2, columnspan = 3)

The_Frame_N_to_Q.grid_rowconfigure(this_row, weight=1)
The_Frame_N_to_Q.grid_columnconfigure(4, weight=1)

The_Gui.mainloop()