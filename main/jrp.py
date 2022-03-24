import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
import tkinter.font as TkFont
import main


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar()
        self.var_2 = tk.BooleanVar()

        self.setup_widgets()

    def setup_widgets(self):
        self.labels()
        self.checkbox_st()
        self.checkbox_fc()
        self.checkbox_both()
        self.entry()
        self.button()

    def labels(self):
        helv36 = TkFont.Font(family="Helvetica", size=25, weight="bold")
        self.label = tk.Label(self, text="JRailPasser", font=helv36, fg="#ef4054")
        self.label.place(x=160, y=20)

        self.label = tk.Label(self, text="Amount of passengers")
        self.label.place(x=25, y=95)

        self.label = tk.Label(self, text="Type of ticket")
        self.label.place(x=360, y=95)

    def checkbox_st(self):
        def check_states():
            if self.var_0.get() == True:
                self.var_1.set(False)
                self.var_2.set(False)

        self.checkbox_st = ttk.Checkbutton(
            self, text="Standard", variable=self.var_0, command=check_states
        )
        self.checkbox_st.place(x=360, y=125)

    def checkbox_fc(self):
        def check_states():
            if self.var_1.get() == True:
                self.var_0.set(False)
                self.var_2.set(False)

        self.checkbox_fc = ttk.Checkbutton(
            self, text="First Class", variable=self.var_1, command=check_states
        )
        self.checkbox_fc.place(x=360, y=165)

    def checkbox_both(self):
        def check_states():
            if self.var_2.get() == True:
                self.var_0.set(False)
                self.var_1.set(False)

        self.checkbox_bt = ttk.Checkbutton(
            self, text="Both", variable=self.var_2, command=check_states
        )
        self.checkbox_bt.place(x=360, y=205)

    def entry(self):
        self.entry = ttk.Entry(self, width=5)
        self.entry.place(x=70, y=125)
        # self.entry.bind("<Leave>", lambda x: print("text: ", self.entry.get()))

    def button(self):
        def check():
            try:
                convert_int = int(self.entry.get())
            except ValueError:
                self.entry.state(["invalid"])
            else:
                self.entry.state(["!invalid"])

                if self.var_0.get() == True:
                    typee_final = 1
                elif self.var_1.get() == True:
                    typee_final = 2
                elif self.var_2.get() == True:
                    typee_final = 3
                else:
                    return
                main.main(int(self.entry.get()), typee_final)

        self.button = ttk.Button(
            self, width=5, text="Ok", style="Accent.TButton", command=check
        )
        self.button.place(x=225, y=290)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("JRailPasser")
    root.geometry("500x400")
    root.resizable(False, False)
    ico = tk.PhotoImage(file="favicon.ico")
    root.tk.call("wm", "iconphoto", root._w, ico)
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    root.tk.call("ttk::style", "theme", "use") == "azure-dark"

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    app = App(root)
    app.pack(fill="both", expand=True)

    root.mainloop()