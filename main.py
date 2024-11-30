import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from data_generator import DatasetGenerator
from typing import List, Tuple

class DatasetApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Advanced Dataset Generator")
        self.root.geometry("600x400")

        # Define available data types
        self.data_types: List[str] = [
            "Name", "Age", "Datetime", "Phone", "Email", "Address", "City", 
            "Country", "Zip Code", "Company", "Job Title", "Salary",
            "Integer", "Float", "Boolean", "Date", "Text", 
            "Random String", "URL", "IPAddress", "Credit Card", 
            "SSN", "Latitude", "Longitude"
        ]

        # Number of rows
        ttk.Label(root, text="Number of Rows:").grid(row=0, column=0, padx=10, pady=10)
        self.rows_var: tk.IntVar = tk.IntVar(value=100)
        ttk.Entry(root, textvariable=self.rows_var).grid(row=0, column=1, padx=10, pady=10)

        # File format
        ttk.Label(root, text="File Format:").grid(row=1, column=0, padx=10, pady=10)
        self.format_var: tk.StringVar = tk.StringVar(value="CSV")
        ttk.Combobox(root, textvariable=self.format_var, values=["CSV", "JSON", "TXT"], state="readonly").grid(row=1, column=1, padx=10, pady=10)

        # File save path
        ttk.Label(root, text="Save File As:").grid(row=2, column=0, padx=10, pady=10)
        self.file_path_var: tk.StringVar = tk.StringVar()
        ttk.Entry(root, textvariable=self.file_path_var, width=30).grid(row=2, column=1, padx=10, pady=10)
        ttk.Button(root, text="Browse", command=self.browse_file).grid(row=2, column=2, padx=10, pady=10)

        # Columns Configuration
        self.columns_frame = ttk.LabelFrame(root, text="Columns Configuration")
        self.columns_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=20, sticky="ew")

        self.columns: List[Tuple[tk.StringVar, tk.StringVar]] = []
        ttk.Button(self.columns_frame, text="Add Column", command=self.add_column).grid(row=0, column=0, padx=10, pady=5)

        # Generate button
        ttk.Button(root, text="Generate Dataset", command=self.generate_dataset).grid(row=4, column=1, pady=20)

    def browse_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(defaultextension=f".{self.format_var.get().lower()}",
                                                     filetypes=[("CSV Files", "*.csv"), ("JSON Files", "*.json"), ("TXT Files", "*.txt")])
        self.file_path_var.set(file_path)

    def add_column(self) -> None:
        # Create a new frame for the column
        column_frame: ttk.Frame = ttk.Frame(self.columns_frame)
        column_frame.grid(row=len(self.columns) + 1, column=0, sticky="w", pady=5, padx=10)  # Dynamic row placement
    
        # Column name input
        ttk.Label(column_frame, text="Column Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        column_name_var: tk.StringVar = tk.StringVar()
        ttk.Entry(column_frame, textvariable=column_name_var, width=20).grid(row=0, column=1, padx=5, pady=5, sticky="w")
    
        # Data type selection
        ttk.Label(column_frame, text="Data Type:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        column_type_var: tk.StringVar = tk.StringVar(value="Name")
        ttk.Combobox(column_frame, textvariable=column_type_var, values=self.data_types, state="readonly").grid(row=0, column=3, padx=5, pady=5, sticky="w")
    
        # Add a "Remove" button for the column
        remove_button: ttk.Button = ttk.Button(column_frame, text="Remove", 
                                               command=lambda: self.remove_column(column_frame, column_name_var, column_type_var))
        remove_button.grid(row=0, column=4, padx=5, pady=5, sticky="w")
    
        # Save column settings in self.columns
        self.columns.append((column_name_var, column_type_var))

    def remove_column(self, frame: ttk.Frame, column_name_var: tk.StringVar, column_type_var: tk.StringVar) -> None:
        # Remove the frame from the GUI
        frame.destroy()
    
        # Remove the column configuration from the internal list
        self.columns = [col for col in self.columns if col[0] != column_name_var and col[1] != column_type_var]
    
        # Re-arrange remaining column frames if needed (optional)

    def generate_dataset(self) -> None:
        rows: int = self.rows_var.get()
        file_format: str = self.format_var.get()
        file_path: str = self.file_path_var.get()

        if not file_path:
            messagebox.showerror("Error", "Please specify a file path to save the dataset.")
            return

        if not self.columns:
            messagebox.showerror("Error", "Please configure at least one column.")
            return

        columns_config: List[Tuple[str, str]] = [(col[0].get(), col[1].get()) for col in self.columns]

        generator = DatasetGenerator()
        try:
            generator.generate(rows, columns_config, file_format, file_path)
            messagebox.showinfo("Success", f"Dataset successfully generated and saved at {file_path}!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root: tk.Tk = tk.Tk()
    app = DatasetApp(root)
    root.mainloop()
