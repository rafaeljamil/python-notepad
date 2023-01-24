from tkinter import Menu
import functions as f
from functools import partial

class My_menu:
	def setup(self, window):
		self.window_root = window.root
		self.window_box = window.box
		# Creating main menu
		self.menu = Menu(self.window_root)
		self.window_root.config(menu=self.menu)

		# Creating sub-menu
		self.file = Menu(self.window_root)
		self.menu.add_cascade(label="Arquivo", menu=self.file)
		self.edit = Menu(self.menu)
		self.menu.add_cascade(label="Editar", menu=self.edit)
		self.format = Menu(self.menu)
		self.menu.add_cascade(label="Formatar", menu=self.format)

		# Menu : File commands
		# Partial é uma opção melhor do que função anônima (lambda) pra organizar os menus em dicionários assim
		my_menu = {
			"Abrir":partial(f.open_func, self.window_box), 
			"Salvar":partial(f.save_func, self.window_box), 
			"Sair":self.window_root.destroy}

		for a,b in my_menu.items():
			self.file.add_command(label=a, command=b)

		# Menu : Edit commands


		# Menu : Format commands
		self.format.add_command(label="Fonte...", command=partial(f.font_edit, self.window_box))