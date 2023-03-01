import tkinter as tk


class App(tk.Tk):
    def __init__(self, history_of_play_labyrinth):
        super().__init__()

        self.title('Лабиринт')
        width = 500
        height = 500

        self.geometry("%dx%d" % (width, height))
        self.minsize(500, 500)

        w = width
        h = height
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        self.geometry('+%d+%d' % (x, y))

        self.history_labyrinth = history_of_play_labyrinth

        self.labyrinth_frame = tk.LabelFrame(self, text="Лабиринт")
        self.labyrinth_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.74)

        self.counter = 0
        self.labyrinth = tk.Label(self.labyrinth_frame, text=self.history_labyrinth[self.counter][1],
                                font='Helvetica 10 bold', width=21)
        self.labyrinth.grid(row=0, column=0, columnspan=1, sticky='w', padx=10, pady=10)

        self.control_panel = tk.LabelFrame(self, text="Панель управления")
        self.control_panel.place(relx=0.01, rely=0.75, relwidth=0.49, relheight=0.24)

        self.panel_info = tk.LabelFrame(self, text="Информация")
        self.panel_info.place(relx=0.51, rely=0.75, relwidth=0.48, relheight=0.24)

        self.position_and_direction = tk.Label(self.panel_info, text=self.history_labyrinth[self.counter][0],
                                  font='Helvetica 10 bold', width=21)
        self.position_and_direction.grid(row=0, column=0, columnspan=1, sticky='w', padx=10, pady=10)

        def prev_step():
            self.counter = self.counter - 1
            self.refresh_labyrinth_output(self.counter)
        self.btn_prev = tk.Button(self.control_panel, text="Предыдущий шаг", command=prev_step, state="disabled")
        self.btn_prev.grid(row=0, column=0, columnspan=1, sticky='n', padx=7, pady=8)

        def next_step():
            self.counter += 1
            self.refresh_labyrinth_output(self.counter)
        self.btn_next = tk.Button(self.control_panel, text="Следующий шаг", command=next_step)
        self.btn_next.grid(row=0, column=1, columnspan=1, sticky='n', padx=5, pady=8)

    def refresh_labyrinth_output(self, number_frame):
        if number_frame == len(self.history_labyrinth)-1:
            self.btn_next.config(state="disabled")
        elif number_frame == 0:
            self.btn_prev.config(state="disabled")
        else:
            self.btn_next.config(state="active")
            self.btn_prev.config(state="active")

        self.labyrinth.config(text=self.history_labyrinth[number_frame][1])
        self.position_and_direction.config(text=self.history_labyrinth[self.counter][0])





