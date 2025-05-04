import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
root = tk.Tk()

root.title("PDF to MP3 Converter")
lbl1 = tk.Label(root, text="Archivo Pdf: ", font=("Arial", 10))
lbl1.place (x=10, y=10,width=100, height=30)
cb = ttk.Entry()
cb.place (x=110, y=10,width=300, height=30)
bt3 = tk.Button(root, text="Buscar", font=("Arial", 10), command=lambda: buscar_pdf())
bt3.place (x=420, y=10,width=100, height=30)
lbl2 = tk.Label(root, text="Archivo MP3: ", font=("Arial", 10))
lbl2.place (x=10, y=50,width=100, height=30)
cb2=ttk.Entry()
cb2.place (x=110, y=50,width=300, height=30)    
bt4=tk.Button(root, text="Destino", font=("Arial", 10), command=lambda: destino_mp3())  
bt4.place (x=420, y=50,width=100, height=30)    
bt=tk.Button(root, text="Convertir", font=("Arial", 10), command=lambda: print("Convertir PDF a MP3"))
bt.place (x=300, y=90,width=100, height=30)
bt2=tk.Button(root, text="Salir", font=("Arial", 10), command=root.quit)    
bt2.place (x=100, y=90,width=100, height=30)
root.geometry("600x200")    

def buscar_pdf():
    # Aquí puedes implementar la lógica para buscar el archivo PDF
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filename:
        cb.insert(0, filename)
    else:
        print("No se seleccionó ningún archivo PDF")
    
    
 
def destino_mp3():
    # Aquí puedes implementar la lógica para buscar el archivo MP3
    filename = filedialog.askdirectory(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if filename:
        cb2.insert(0, filename)
    else:
        print("No se seleccionó ningún directorio de destino")
        
def convert_mp3():
    # Aquí puedes implementar la lógica para convertir el PDF a MP3
    pdf_file = cb.get()
    mp3_file = cb2.get()
    if pdf_file and mp3_file:
        # Lógica de conversión aquí
        print(f"Convirtiendo {pdf_file} a {mp3_file}")
    else:
        messagebox.showerror("Error", "Por favor, selecciona un archivo PDF y un destino para el MP3.")  
    
          
root.mainloop()
root.update()
