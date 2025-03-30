import customtkinter as tk
from fish import start

tk.set_appearance_mode('dark')
tk.set_default_color_theme('blue')

app = tk.CTk()
app.title('Fisha')
app.geometry('600x400')

button_send = tk.CTkButton(
    master = app,
    text = '↑',
    corner_radius = 10,
    command = start(),
    text_color = 'white',
    font = ('Arial', 14),
    fg_color = '#455baf',
    hover_color = '#2d3b71'
)
button_send.pack(pady=20)



app.mainloop()
