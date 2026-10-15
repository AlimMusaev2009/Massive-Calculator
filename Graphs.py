import tkinter as tk

y = 0
x = 0
vertex = 0

def getorigin(eventorigin):
    global vertex
    global x, y
    x = eventorigin.x
    y = eventorigin.y
    ver = tk.Canvas.create_oval(can, x - 10, y - 10, x + 10, y + 10, fill='white', outline='black')
    vertex += 1
    print(vertex)
    return ver








root = tk.Tk()
can = tk.Canvas(root, bg='white', height=1000, width=1000)
can.pack(side=tk.RIGHT)

root.bind("<Button 1>", getorigin)
root.geometry("500x500")
root.mainloop()
