import tkinter as tk
from tkinter import messagebox
from disk import Disk

class DiskManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Disk Manager")
        
        # Création des champs de saisie et labels
        self.total_label = tk.Label(root, text="Total capacity (Gb)")
        self.total_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.total_entry = tk.Entry(root)
        self.total_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.used_label = tk.Label(root, text="Used capacity (Gb)")
        self.used_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        self.used_entry = tk.Entry(root)
        self.used_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Bouton de calcul
        self.calc_button = tk.Button(root, text="Percent usage", command=self.calculate_usage)
        self.calc_button.grid(row=2, column=1, sticky="e", padx=5, pady=5)
    
    def calculate_usage(self):
        try:
            total = float(self.total_entry.get())
            used = float(self.used_entry.get())
            
            disk = Disk(total, used)
            percentage = disk.used_perc * 100
            
            messagebox.showinfo("Usage", f"Disk usage: {percentage:.1f}%")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Total capacity cannot be zero")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiskManagerUI(root)
    root.mainloop()