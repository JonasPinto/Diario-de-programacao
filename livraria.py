import tkinter as tk
from tkinter import messagebox
import json

def limp_tela():
    ent1.delete(0,tk.END)
    ent2.delete(0,tk.END)
    ent3.delete(0,tk.END)
    ent4.delete(0,tk.END)
    ent5.delete(0,tk.END)
    ent6.delete(0,tk.END)
    ent7.delete(0,tk.END)
    ent8.delete(0,tk.END)

def salvar_livro():
    livro = {
        'ISBN': ent1.get(),
        'Titulo': ent2.get(),
        'Autor': ent3.get(),
        'Editora': ent4.get(),
        'Paginas': ent5.get(),
        'Ano': ent6.get(),
        'Genero': ent7.get(),
        'Edicao': ent8.get()
    }
    limp_tela()
    
    with open('livros.json', 'w') as f:
        json.dump(livro, f, indent=4)
    messagebox.showinfo('Sucesso', 'Livro salvo com sucesso!')

def ent_f(linha, coluna):
    x = tk.Entry(main_window, font=['Calibri', 18], width= 30, bg='#2f4f4a', fg='#c9f3f3', justify='center')
    x.grid(row= linha, column= coluna, padx= 5, pady= 5)
    return x

def lab_f(titulo, linha, coluna):
    x = tk.Label(main_window, text= titulo, width= 30, bg= '#2f4f4f', fg= 'white', font=['Calibri', 18])
    x.grid(row= linha, column= coluna, padx= 5, pady= 5)
    return x

main_window = tk.Tk()
main_window.title('LIVRARIA')               
main_window.geometry('400x500')          
main_window.configure(bg="#2f4f4a")    

lab1 = lab_f('ISBN', 0, 0)
ent1 = ent_f(0, 1)
lab2 = lab_f('Título', 0, 2)
ent2 = ent_f(0, 3)
lab3 = lab_f('Autor', 1, 0)
ent3 = ent_f(1, 1)
lab4 = lab_f('Editora', 1, 2)
ent4 = ent_f(1, 3)
lab5 = lab_f('Páginas', 2, 0)
ent5 = ent_f(2, 1)
lab6 = lab_f('Ano', 2, 2)
ent6 = ent_f(2, 3)
lab7 = lab_f('Gênero', 3, 0)
ent7 = ent_f(3, 1)
lab8 = lab_f('Edição', 3, 2)
ent8 = ent_f(3, 3)

button_localizar = tk.Button(main_window, text='Localizar', bg= '#2f4f4a', fg= 'white', font=['Calibri', 18], width=20)
button_localizar.grid(row=7, column=0, padx= 5, pady= 5)

button_salvar = tk.Button(main_window, text='Salvar', bg= '#2f4f4a', fg= 'white', font=['Calibri', 18], width=20, command=salvar_livro)
button_salvar.grid(row=7, column=1, padx= 5, pady= 5)

button_excluir = tk.Button(main_window, text='Excluir', bg= '#2f4f4a', fg= 'white', font=['Calibri', 18], width=20)
button_excluir.grid(row=7, column=2, padx= 5, pady= 5)

main_window.mainloop()
