import tkinter as tk


LARGE_FONT= ("Verdana", 12)
class PillTracker(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

#here we have the hom epage with two buttons to take you where you need to go#     
class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Hi Welcome to Pill Tracker, did you take your pill yet today?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Yes I would like to enter an updated pill date.",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="When was my last pill?",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

#page one is where you go if you want to input the date#
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Please enter the date here.", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        txtfld=tk.Entry(self, text="This is Entry Widget", bd=5)
        txtfld.place(x=80, y=150)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Home))
        button1.pack()

      

#at page two you go here to remeber the last date you took a pill#
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Your last Pill was taken on", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Home))
        button1.pack()

        button2 = tk.Button(self, text="Ok, I will take my pill now and enter the date.",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = PillTracker()
app.mainloop()

#in all, i bit off more than i could chew wiht this project. i cant get it to take the#
#input that i want and i have no idea how to make it remeber #
#once it has been closed#