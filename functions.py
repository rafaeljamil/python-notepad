import tkinter as tk
from tkinter import filedialog
import window

def open_func(box):
	#print("Open func called")
	text = filedialog.askopenfilename(initialdir="/",title="Select a file",filetypes=(("Text files", "*.txt"),("All files","*.*")))
	with open(text, "r", encoding="utf-8") as f:
		box.delete("1.0", tk.END)
		box.insert("1.0", f.read())

def save_func(box):
	#print("Save func called")
	location = filedialog.asksaveasfilename(initialdir="/", initialfile="file", defaultextension=".txt", filetypes=(("Text files - *.txt", "*.txt"),("All files - *.*","*.*")))
	text = box.get('1.0', tk.END)
	with open(location, "w", encoding="utf-8") as f:
		f.write(text)
		f.close()

def font_edit(box):
	# Create a new font edit window
	font_edit = window.FontWindow()
	
	# Se the window up
	font_edit.setup(box)

	# Run the window loop and the event bindings
	font_edit.run_loop()

	