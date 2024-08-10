import tkinter as tk
import random
import string
import pyperclip

def gerarSenha():
    tamanho_senha = int(tamanho.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation;
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho_senha));
    saida.delete(0, tk.END);
    saida.insert(0, senha);

def copiar():
    senha_gerada = saida.get();
    pyperclip.copy(senha_gerada);

janela = tk.Tk();
janela.title("Gerador de Senha");
janela.geometry("500x250");
janela.config(bg='#016064')

tk.Label(janela, text="Gerador de Senha",bg='#016064',fg='white',font=("Tahoma Bold", 25)).pack(pady=5)
tk.Label(janela, text="Digite o Tamanho da Senha:",bg='#016064',fg='white',font=("Tahoma Bold", 15)).pack(pady=5)
tamanho = tk.Entry(janela);
tamanho.pack(pady=5);
tk.Button(janela, text="Gerar senha",bg="white",command=gerarSenha).pack(pady=5);
saida = tk.Entry(janela);
saida.pack(pady=5);
tk.Button(janela, text="Copiar Senha", bg="white",command=copiar).pack(pady=5);

janela.mainloop();