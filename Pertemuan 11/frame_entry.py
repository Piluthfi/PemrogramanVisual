#CREATING GUI USING TKINTER
import tkinter as tk
#Jalankan code untuk tiap topik bergantian. Beri tanda # untuk topik yang 
#tidak dijalankan

root = tk.Tk()

#==================================================================
#-----------------Latihan-1: Membuat Widget Dasar------------------
#==================================================================
# WidgetDasarku = tk.Tk ()
# WidgetDasarku.mainloop ()

#==================================================================
#--------------------Latihan-2: Membuat Canvas---------------------
#==================================================================
# Kanvasku = tk.Canvas(root, height = 1080, width = 1920)
# Kanvasku.pack()
#
#==================================================================
#--------------------Latihan-3: Membuat Canvas---------------------
#==================================================================
Frameku = tk.Frame(root, bg = 'blue')
Frameku.place(relwidth = 0.8, relheight = 0.8)

# root.mainloop()

#==================================================================
#----------------Latihan-4a: Membuat Button Di Root----------------
#==================================================================
# Tombolku = tk.Button(root, text = "Tes Tombol", bg = 'gray', fg = 'red')
# Tombolku.pack()

#==================================================================
#----------------Latihan-4b: Membuat Button Di Frame---------------
#==================================================================
Tombolku = tk.Button(Frameku, text = "Tes Tombol", bg = 'gray', fg = 'red')
Tombolku.pack()

#==================================================================
#---------------------Latihan-5: Membuat Entry---------------------
#==================================================================
Entryku = tk.Entry(Frameku, bg = 'green')
Entryku.pack()

root.mainloop()
