import tkinter as tk

def draw_point(event):
    canvas_points.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill='black')

def draw_line(event):
    global prev_x, prev_y
    canvas_lines.create_line(prev_x, prev_y, event.x, event.y, fill='red')
    prev_x, prev_y = event.x, event.y

root = tk.Tk()
root.title("Aplikasi untuk Menggambar Titik dan Garis")

paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

frame_points = tk.Frame(paned_window, width=200, height=400, bg='white')
frame_lines = tk.Frame(paned_window, width=200, height=400, bg='white')

canvas_points = tk.Canvas(frame_points, bg='white')
canvas_points.pack(fill=tk.BOTH, expand=True)
canvas_points.bind('<Button-1>', draw_point)

canvas_lines = tk.Canvas(frame_lines, bg='white')
canvas_lines.pack(fill=tk.BOTH, expand=True)
canvas_lines.bind('<B1-Motion>', draw_line)

paned_window.add(frame_points)
paned_window.add(frame_lines)

prev_x, prev_y = 0, 0

root.mainloop()
