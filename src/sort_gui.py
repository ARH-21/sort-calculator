import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import time
import os
from sort_algos import bubble_sort, insertion_sort, selection_sort

class SortGUI:
    # Constructor
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Sorting Calculator")
        self.numbers = []
        self.filename = ""
        self.trial = 1
        
        
        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side="left", padx=10, pady=10)
        
        self.center_frame = tk.Frame(root)
        self.center_frame.pack(side="left", padx=20, pady=10)
        
        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side="left", padx=10, pady=10)
        
        # Choose Algorithm Buttons
        tk.Button(self.left_frame, text="Bubble Sort",
                  command=lambda: self.run_sort("Bubble Sort", bubble_sort)).pack(fill="x", pady=2)
        tk.Button(self.left_frame, text="Insertion Sort",
                  command=lambda: self.run_sort("Insertion Sort", insertion_sort)).pack(fill="x", pady=2)
        tk.Button(self.left_frame, text="Selection Sort",
                  command=lambda: self.run_sort("Selection Sort", selection_sort)).pack(fill="x", pady=2)
        # TO-DO (The other 3 sorts):
        # tk.Button(self.left_frame, text="Merge Sort",
        #           command=lambda: self.run_sort("Merge Sort", merge_sort)).pack(fill="x", pady=2)
        # tk.Button(self.left_frame, text="Quick Sort",
        #           command=lambda: self.run_sort("Quick Sort", quick_sort)).pack(fill="x", pady=2)
        # tk.Button(self.left_frame, text="Heap Sort",
        #           command=lambda: self.run_sort("Heap Sort", heap_sort)).pack(fill="x", pady=2)
        

        # File Info on GUI
        self.num_label = tk.Label(self.center_frame, text="Total Amount of Ints: 0")
        self.num_label.pack()
        
        self.file_label = tk.Label(self.center_frame, text="Current File: None")
        self.file_label.pack()
        
        # File Data Buttons
        tk.Button(self.center_frame, text="Load Data", command=self.load_data).pack(pady=5)
        tk.Button(self.center_frame, text="Clear Data", command=self.clear_data).pack(pady=5)
        
        # Display Results
        self.tree = ttk.Treeview(self.right_frame,
                                 columns=("Trial", "File", "Alg", "ms", "Swaps", "Comps"),
                                 show="headings")
        for col in ("Trial", "File", "Alg", "ms", "Swaps", "Comps"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        # Scrollbar if trials exceed the window size
        scrollbar = ttk.Scrollbar(self.right_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left")
        scrollbar.pack(side="right", fill="y")
    
    def load_data(self):
        file_path = filedialog.askopenfilename(
            title="Select text file", 
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not file_path:
            return
        
        try:
            self.filename = os.path.basename(file_path)
            
            with open(file_path, "r") as f:
                content = f.read().strip()
                if not content:
                    messagebox.showerror("Error: File has no data")
                    return
                
                self.numbers = list(map(int, content.split()))
            
            self.num_label.config(text=f"Number of Ints: {len(self.numbers)}")
            self.file_label.config(text=f"Current File: {self.filename}")
            
        except ValueError:
            messagebox.showerror("Error", "File contains non-integer values")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file: {str(e)}")
    
    def clear_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.trial = 0
    
    def run_sort(self, alg_name, algorithm):
        if not self.numbers:
            messagebox.showwarning("Error", "No file loaded")
            return
        
        try:
            arr = self.numbers.copy()
            start = time.time()

            # _ (ignore value, only because of the GUI I'm not returning the sorted array)
            _, swaps, comps = algorithm(arr)

            end = time.time()
            
            runtime_ms = round((end - start) * 1000, 3)
            
            self.tree.insert("", "end",
                           values=(self.trial, self.filename, alg_name,
                                   runtime_ms, swaps, comps))
            self.trial += 1
            
        except Exception as e:
            messagebox.showerror("Error", f"Error running {alg_name}: {str(e)}")
