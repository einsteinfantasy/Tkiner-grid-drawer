import tkinter as tk

class GridDrawer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Grid Drawer")
        self.geometry("1280x720")

        self.row_var = tk.StringVar()
        self.column_var = tk.StringVar()
        self.rows = None
        self.columns = None

        self.create_widgets()

    def create_widgets(self):
        control_frame = tk.Frame(self)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(control_frame, text="Rows:").pack(side=tk.LEFT, padx=(10, 2))
        row_entry = tk.Entry(control_frame, textvariable=self.row_var)
        row_entry.pack(side=tk.LEFT, padx=(0, 10))
        row_entry.bind("<Return>", lambda e: self.update_grid())

        tk.Label(control_frame, text="Columns:").pack(side=tk.LEFT, padx=(10, 2))
        column_entry = tk.Entry(control_frame, textvariable=self.column_var)
        column_entry.pack(side=tk.LEFT, padx=(0, 10))
        column_entry.bind("<Return>", lambda e: self.update_grid())

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Motion>", self.show_tooltip)

        self.tooltip = tk.Label(self.canvas, text="", bg="lightyellow", bd=1, relief="solid", font=("Arial", 10))

    def update_grid(self):
        try:
            self.rows = int(self.row_var.get())
            self.columns = int(self.column_var.get())
            self.draw_grid(self.rows, self.columns)
        except ValueError:
            self.rows = self.columns = None  # Reset if the input is not a valid integer

    def draw_grid(self, rows, columns):
        self.canvas.delete("all")  # Clear the canvas

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Ensure width and height are updated
        self.canvas.update_idletasks()

        self.row_height = height / rows
        self.column_width = width / columns

        # Draw horizontal lines
        for i in range(1, rows):
            y = i * self.row_height
            self.canvas.create_line(0, y, width, y, fill="gray")

        # Draw vertical lines
        for j in range(1, columns):
            x = j * self.column_width
            self.canvas.create_line(x, 0, x, height, fill="gray")

    def show_tooltip(self, event):
        # Check if rows and columns are defined and greater than 0
        if self.rows and self.columns:
            row = int(event.y // self.row_height)
            column = int(event.x // self.column_width)
            tooltip_text = f"Row={row + 1}, Column={column + 1}"
            self.tooltip.config(text=tooltip_text)
            self.tooltip.place(x=event.x + 20, y=event.y + 20)
        else:
            self.tooltip.place_forget()  # Hide the tooltip if rows or columns are not defined

if __name__ == "__main__":
    app = GridDrawer()
    app.mainloop()