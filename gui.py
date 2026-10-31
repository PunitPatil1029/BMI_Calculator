
import tkinter as tk
from tkinter import messagebox, ttk
import database


# Create database table
database.create_table()


def calculate_bmi():
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return

        if weight <= 0 or height <= 0:
            messagebox.showerror(
                "Error",
                "Weight and height must be greater than zero."
            )
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Save record in database
        database.save_record(name, weight, height, bmi, category)

        result_label.config(
            text=f"{name}, your BMI is {bmi:.2f}\nCategory: {category}"
        )

        messagebox.showinfo(
            "Success",
            "Your BMI record has been saved successfully!"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers for weight and height."
        )


def reset_fields():
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="Your BMI result will appear here")


def view_history():
    records = database.get_records()

    if not records:
        messagebox.showinfo("BMI History", "No BMI records found.")
        return

    # Create history window
    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("950x400")
    history_window.configure(bg="#EAF2F8")

    tk.Label(
        history_window,
        text="BMI HISTORY",
        font=("Arial", 20, "bold"),
        bg="#EAF2F8",
        fg="#154360"
    ).pack(pady=15)

    # Table frame
    table_frame = tk.Frame(history_window)
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)

    columns = (
        "ID", "Name", "Weight", "Height",
        "BMI", "Category", "Date & Time"
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=120, anchor="center")

    tree.column("ID", width=50)
    tree.column("Name", width=100)
    tree.column("Date & Time", width=170)

    # Add vertical scrollbar
    scrollbar_y = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    # Add horizontal scrollbar
    scrollbar_x = ttk.Scrollbar(
        table_frame,
        orient="horizontal",
        command=tree.xview
    )

    tree.configure(
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )

    tree.grid(row=0, column=0, sticky="nsew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    scrollbar_x.grid(row=1, column=0, sticky="ew")

    table_frame.rowconfigure(0, weight=1)
    table_frame.columnconfigure(0, weight=1)

    # Insert database records into table
    for record in records:
        tree.insert(
            "",
            tk.END,
            values=(
                record[0],
                record[1],
                record[2],
                record[3],
                f"{record[4]:.2f}",
                record[5],
                record[6]
            )
        )


# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("450x600")
root.resizable(False, False)
root.configure(bg="#EAF2F8")

# Heading
title_label = tk.Label(
    root,
    text="BMI CALCULATOR",
    font=("Arial", 22, "bold"),
    bg="#EAF2F8",
    fg="#154360"
)
title_label.pack(pady=20)

# Name
tk.Label(
    root,
    text="Enter Your Name",
    font=("Arial", 12),
    bg="#EAF2F8"
).pack()

name_entry = tk.Entry(root, font=("Arial", 12), width=25)
name_entry.pack(pady=5)

# Weight
tk.Label(
    root,
    text="Weight (kg)",
    font=("Arial", 12),
    bg="#EAF2F8"
).pack()

weight_entry = tk.Entry(root, font=("Arial", 12), width=25)
weight_entry.pack(pady=5)

# Height
tk.Label(
    root,
    text="Height (meters)",
    font=("Arial", 12),
    bg="#EAF2F8"
).pack()

height_entry = tk.Entry(root, font=("Arial", 12), width=25)
height_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12, "bold"),
    bg="#2874A6",
    fg="white",
    width=18,
    command=calculate_bmi
)
calculate_button.pack(pady=10)

# Reset button
reset_button = tk.Button(
    root,
    text="Reset",
    font=("Arial", 12, "bold"),
    bg="#CB4335",
    fg="white",
    width=18,
    command=reset_fields
)
reset_button.pack(pady=5)

# View History button
history_button = tk.Button(
    root,
    text="View BMI History",
    font=("Arial", 12, "bold"),
    bg="#239B56",
    fg="white",
    width=18,
    command=view_history
)
history_button.pack(pady=10)

# Result
result_label = tk.Label(
    root,
    text="Your BMI result will appear here",
    font=("Arial", 13, "bold"),
    bg="#EAF2F8",
    fg="#154360"
)
result_label.pack(pady=15)

root.mainloop()
