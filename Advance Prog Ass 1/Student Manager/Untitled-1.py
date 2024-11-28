import tkinter as tk
from tkinter import ttk, messagebox

class Product:
    def __init__(self, code, name, marks):
        self.code = code
        self.name = name
        self.marks = marks  # List of integers
        self.total_score = sum(marks)
        self.percentage = (self.total_score / (len(marks) * 20)) * 100
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.percentage >= 70:
            return 'A'
        elif self.percentage >= 60:
            return 'B'
        elif self.percentage >= 50:
            return 'C'
        elif self.percentage >= 40:
            return 'D'
        else:
            return 'F'

    def display_record(self):
        return f"Student Name: {self.name}\nStudent Code: {self.code}\n" \
               f"Marks: {', '.join(map(str, self.marks))}\n" \
               f"Total Score: {self.total_score}\n" \
               f"Percentage: {self.percentage:.2f}%\nGrade: {self.grade}"

def load_products_from_file():
    products = []
    try:
        with open("names.txt", "r") as file:
            num_products = int(file.readline().strip())
            for _ in range(num_products):
                line = file.readline().strip().split(',')
                code = int(line[0])
                name = line[1].strip()
                marks = [int(mark) for mark in line[2:]]
                products.append(Product(code, name, marks))
    except FileNotFoundError:
        messagebox.showerror("Error", "The file 'names.txt' was not found. Please ensure it exists.")
    return products

class InventoryManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Manager")
        self.master.geometry("600x400")

        # Load products from the file
        self.products = load_products_from_file()

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.master, text="Inventory Manager", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="View All Students", command=self.view_all_students).grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="Show Top Performer", command=self.show_top_performer).grid(row=0, column=1, padx=10)
        ttk.Button(button_frame, text="Show Lowest Performer", command=self.show_lowest_performer).grid(row=0, column=2, padx=10)

        ttk.Button(self.master, text="View Student Details", command=self.view_student_details).pack(pady=10)
        
        self.result_text = tk.Text(self.master, height=15, width=70)
        self.result_text.pack(pady=10)

    def view_all_students(self):
        self.result_text.delete(1.0, tk.END)
        for product in self.products:
            self.result_text.insert(tk.END, product.display_record() + "\n\n")
        
        total_percentage = sum(product.percentage for product in self.products) / len(self.products)
        summary = f"Number of students: {len(self.products)}\n"
        summary += f"Average Percentage: {total_percentage:.2f}%"
        self.result_text.insert(tk.END, summary)

    def view_student_details(self):
        names = [product.name for product in self.products]
        student_window = tk.Toplevel(self.master)
        student_window.title("Select a Student")
        
        listbox = tk.Listbox(student_window)
        listbox.pack(padx=10, pady=10)
        
        for name in names:
            listbox.insert(tk.END, name)
        
        def on_select():
            selection = listbox.curselection()
            if selection:
                index = selection[0]
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, self.products[index].display_record())
                student_window.destroy()
        
        ttk.Button(student_window, text="Select", command=on_select).pack(pady=10)

    def show_top_performer(self):
        top_student = max(self.products, key=lambda x: x.total_score)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Top Performer:\n\n")
        self.result_text.insert(tk.END, top_student.display_record())

    def show_lowest_performer(self):
        lowest_student = min(self.products, key=lambda x: x.total_score)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Lowest Performer:\n\n")
        self.result_text.insert(tk.END, lowest_student.display_record())

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagerApp(root)
    root.mainloop()
