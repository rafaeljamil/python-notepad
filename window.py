import tkinter as tk
from tkinter import ttk
import menu

class Window:
	def setup(self):
		self.root = tk.Tk()
		self.root.minsize(600,400)
		self.root.title("Bloco de Notas...?")
		self.root.configure(background="gray")
		self.root.pack_propagate(0)
		#self.root.grid_columnconfigure(0, weight=1)
		#self.root.state("zoomed")

		# Frame
		# self.frame = tk.Frame(self.root, width=1, height=1)
		# self.frame.pack(expand=True, fill="both")
		# self.frame.pack_propagate(0)

		# Text Box
		self.box = tk.Text(self.root, font=("Arial", 12), padx=5, pady=5)
		self.box.pack_propagate(0)
		self.box.pack(expand=True, fill="both") #These options made the text box stretch to fill the parent

		# Scroll bar
		self.bar = tk.Scrollbar(self.box)
		self.bar.pack(side="right", fill="y")

		# Menu
		self.menu = menu.My_menu()
		self.menu.setup(self)

		# Config
		self.box.config(yscrollcommand=self.bar.set)
		self.bar.config(command=self.box.yview)

	def run_loop(self):
		self.root.mainloop()

class FontWindow:
	def setup(self, box):
		# Storing the box info
		self.box = box

		# Creating font options window
		self.root = tk.Tk()
		self.root.title("Fonte")
		#self.root.minsize(400,400)
		self.root.resizable(False, False)

		# getting font info from box
		self.font_info = self.box.cget("font")

		# Font info divided
		self.box_font_size = self.font_info[-2:]
		self.box_font_family = self.font_info[:-3]

		# A list to easily edit values
		self.font_list = [self.box_font_family, self.box_font_size]

		# Creating window frame
		self.left_window = tk.Frame(self.root)
		self.left_window.grid(column=0,row=0,padx=10,pady=10)

		self.right_window = tk.Frame(self.root)
		self.right_window.grid(column=1,row=0,padx=10,pady=10)

		# Creating a label to see the changes
		self.font_label = tk.Label(self.root, text="Exemplo:")
		self.my_label = tk.Text(self.root, width=20,height=1)
		self.my_label.insert(tk.END,self.font_info)
		self.my_label.config(state="disabled", font=("Arial", 10))

		# Font size combo box - Edit 'values' to add more sizes
		self.font_size_label = tk.Label(self.right_window, text="Tamanho")
		self.font_size = ttk.Combobox(self.right_window)
		self.font_size['values'] = [s for s in range(10,29,2)]
		self.font_size.current(self.font_size['values'].index(self.font_list[1])) # sets the current combobox value as the current font size of the box

		# Font family combo box - edit 'values' to add more families
		self.font_fam_label = tk.Label(self.left_window, text="Família")
		self.font_fam = ttk.Combobox(self.left_window)
		self.font_fam['values'] = ["Arial", "Calibri", "Comic Sans MS", "Tahoma", "Verdana", "Times New Roman"]
		self.font_fam.current(self.font_fam['values'].index(self.font_list[0])) # sets the current combobox value as the current font family of the box

		#Packing it all
		
		self.my_label.grid(column=1,row=3)
		self.font_label.grid(column=0,row=3)
		self.font_fam_label.grid()
		self.font_fam.grid()
		self.font_size_label.grid()
		self.font_size.grid()

		# Just a button to close window
		ok_btn = tk.Button(self.root, text="OK", command=self.root.destroy)
		ok_btn.grid(column=1,row=4)

	# Function to change the font size
	def get_font_size_selected(self, event):
		my_font = self.font_size.get()
		self.font_list[1] = my_font
		result = " ".join(self.font_list)
		#self.my_label.config(text=result)

		# writing to the widget, ugly version
		self.my_label.config(state="normal")
		self.my_label.delete("1.0",tk.END)
		self.my_label.config(font=(self.font_list[0],10))
		self.my_label.insert(tk.END, result)
		self.my_label.config(state="disabled")

		# Editing config from the actual main window
		print(" ".join(self.font_list))
		self.box.config(font=(self.font_list[0], self.font_list[1]))

    # Function to change font family
	def get_font_fam_selected(self, event):
		my_font = self.font_fam.get()
		self.font_list[0] = my_font
		result = " ".join(self.font_list)
		#self.my_label.config(text=result)

		# Writing to the widget, ugly version
		self.my_label.config(state="normal")
		self.my_label.delete("1.0",tk.END)
		self.my_label.config(font=(self.font_list[0],10))
		self.my_label.insert(tk.END, result)
		self.my_label.config(state="disabled")

		# Editing config from the actual main window
		print(" ".join(self.font_list))
		self.box.config(font=(self.font_list[0], self.font_list[1]))

	def run_loop(self):
		# Bind events and run main loop
		self.font_size.bind("<<ComboboxSelected>>", self.get_font_size_selected)
		self.font_fam.bind("<<ComboboxSelected>>", self.get_font_fam_selected)

		self.root.mainloop()