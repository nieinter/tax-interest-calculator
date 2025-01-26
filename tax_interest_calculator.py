import ttkbootstrap as ttk
from datetime import timedelta, datetime, date
from ttkbootstrap import Style
from tkinter import messagebox


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="solar")import ttkbootstrap as ttk
from datetime import timedelta, datetime, date
from ttkbootstrap import Style
from tkinter import messagebox


# main class
class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="solar")
        # window parameters
        self.title("Kalkulator odsetek podatkowych")
        self.geometry("500x600")
        self.resizable(False, False)

        # data (dates and interest rates) - no API
        self.history = [[date(1000, 9, 1).strftime("%d-%m-%Y"), date(2006, 1, 31).strftime("%d-%m-%Y"), 12],
                        [date(2006, 2, 1).strftime("%d-%m-%Y"), date(2006, 2, 28).strftime("%d-%m-%Y"), 11.5],
                        [date(2006, 3, 1).strftime("%d-%m-%Y"), date(2007, 4, 25).strftime("%d-%m-%Y"), 11],
                        [date(2007, 4, 26).strftime("%d-%m-%Y"), date(2007, 6, 27).strftime("%d-%m-%Y"), 11.5],
                        [date(2007, 6, 28).strftime("%d-%m-%Y"), date(2007, 8, 29).strftime("%d-%m-%Y"), 12],
                        [date(2007, 8, 30).strftime("%d-%m-%Y"), date(2007, 11, 28).strftime("%d-%m-%Y"), 12.5],
                        [date(2007, 11, 29).strftime("%d-%m-%Y"), date(2008, 1, 30).strftime("%d-%m-%Y"), 13],
                        [date(2008, 1, 31).strftime("%d-%m-%Y"), date(2008, 2, 27).strftime("%d-%m-%Y"), 13.5],
                        [date(2008, 2, 28).strftime("%d-%m-%Y"), date(2008, 3, 26).strftime("%d-%m-%Y"), 14],
                        [date(2008, 3, 27).strftime("%d-%m-%Y"), date(2008, 6, 25).strftime("%d-%m-%Y"), 14.5],
                        [date(2008, 6, 26).strftime("%d-%m-%Y"), date(2008, 11, 26).strftime("%d-%m-%Y"), 15],
                        [date(2008, 11, 27).strftime("%d-%m-%Y"), date(2008, 12, 23).strftime("%d-%m-%Y"), 14.5],
                        [date(2008, 12, 24).strftime("%d-%m-%Y"), date(2009, 1, 27).strftime("%d-%m-%Y"), 13],
                        [date(2009, 1, 28).strftime("%d-%m-%Y"), date(2009, 2, 25).strftime("%d-%m-%Y"), 11.5],
                        [date(2009, 2, 26).strftime("%d-%m-%Y"), date(2009, 3, 25).strftime("%d-%m-%Y"), 11],
                        [date(2009, 3, 26).strftime("%d-%m-%Y"), date(2009, 6, 24).strftime("%d-%m-%Y"), 10.5],
                        [date(2009, 6, 25).strftime("%d-%m-%Y"), date(2010, 11, 8).strftime("%d-%m-%Y"), 10],
                        [date(2010, 11, 9).strftime("%d-%m-%Y"), date(2011, 1, 19).strftime("%d-%m-%Y"), 12],
                        [date(2011, 1, 20).strftime("%d-%m-%Y"), date(2011, 4, 5).strftime("%d-%m-%Y"), 12.5],
                        [date(2011, 4, 6).strftime("%d-%m-%Y"), date(2011, 5, 11).strftime("%d-%m-%Y"), 13],
                        [date(2011, 5, 12).strftime("%d-%m-%Y"), date(2011, 6, 8).strftime("%d-%m-%Y"), 13.5],
                        [date(2011, 6, 9).strftime("%d-%m-%Y"), date(2012, 5, 9).strftime("%d-%m-%Y"), 14],
                        [date(2012, 5, 10).strftime("%d-%m-%Y"), date(2012, 11, 7).strftime("%d-%m-%Y"), 14.5],
                        [date(2012, 11, 8).strftime("%d-%m-%Y"), date(2012, 12, 5).strftime("%d-%m-%Y"), 14],
                        [date(2012, 12, 6).strftime("%d-%m-%Y"), date(2013, 1, 9).strftime("%d-%m-%Y"), 13.5],
                        [date(2013, 1, 10).strftime("%d-%m-%Y"), date(2013, 2, 6).strftime("%d-%m-%Y"), 13],
                        [date(2013, 2, 7).strftime("%d-%m-%Y"), date(2013, 3, 6).strftime("%d-%m-%Y"), 12.5],
                        [date(2013, 3, 7).strftime("%d-%m-%Y"), date(2013, 5, 8).strftime("%d-%m-%Y"), 11.5],
                        [date(2013, 5, 9).strftime("%d-%m-%Y"), date(2013, 6, 5).strftime("%d-%m-%Y"), 11],
                        [date(2013, 6, 6).strftime("%d-%m-%Y"), date(2013, 7, 3).strftime("%d-%m-%Y"), 10.5],
                        [date(2013, 7, 4).strftime("%d-%m-%Y"), date(2014, 10, 8).strftime("%d-%m-%Y"), 10],
                        [date(2014, 10, 9).strftime("%d-%m-%Y"), date(2022, 2, 8).strftime("%d-%m-%Y"), 8],
                        [date(2022, 2, 9).strftime("%d-%m-%Y"), date(2022, 3, 8).strftime("%d-%m-%Y"), 8.5],
                        [date(2022, 3, 9).strftime("%d-%m-%Y"), date(2022, 4, 6).strftime("%d-%m-%Y"), 10],
                        [date(2022, 4, 7).strftime("%d-%m-%Y"), date(2022, 5, 5).strftime("%d-%m-%Y"), 12],
                        [date(2022, 5, 6).strftime("%d-%m-%Y"), date(2022, 6, 8).strftime("%d-%m-%Y"), 13.5],
                        [date(2022, 6, 9).strftime("%d-%m-%Y"), date(2022, 7, 7).strftime("%d-%m-%Y"), 15],
                        [date(2022, 7, 8).strftime("%d-%m-%Y"), date(2022, 9, 7).strftime("%d-%m-%Y"), 16],
                        [date(2022, 9, 8).strftime("%d-%m-%Y"), date(2023, 9, 6).strftime("%d-%m-%Y"), 16.5],
                        [date(2023, 9, 7).strftime("%d-%m-%Y"), date(2023, 10, 4).strftime("%d-%m-%Y"), 15],
                        [date(2023, 10, 5).strftime("%d-%m-%Y"), date(2100, 9, 7).strftime("%d-%m-%Y"), 14.5]
                        ]

        # style initialization
        style_b = Style()
        style_b.configure("Custom.TButton", font=(None, 20))

        style_c = Style()
        style_c.configure('Calendar.TCalendar', font=(None, 30))

        # widgets initialization
        self.entry_amount = ttk.Entry(self,
                                      font=(None, 25))
        self.calendar_from = ttk.DateEntry(self,
                                           style="Calendar")
        self.calendar_to = ttk.DateEntry(self)

        button_cal = ttk.Button(self,
                                text="Oblicz",
                                style="Custom.TButton",
                                command=self.date_pick
                                )

        self.label_total = ttk.Label(self,
                                     text="",
                                     font=(None, 18))

        # layout - grid configuration and widgets placement
        self.rowconfigure(1, weight=1, uniform="a")
        self.rowconfigure(2, weight=1, uniform="a")
        self.rowconfigure(3, weight=1, uniform="a")
        self.rowconfigure(4, weight=1, uniform="a")
        self.rowconfigure(5, weight=1, uniform="a")
        self.rowconfigure(6, weight=1, uniform="a")
        self.rowconfigure(7, weight=1, uniform="a")
        self.rowconfigure(8, weight=1, uniform="a")
        self.rowconfigure(9, weight=1, uniform="a")
        self.rowconfigure(10, weight=1, uniform="a")

        self.columnconfigure(0, weight=1, uniform="a")
        self.columnconfigure(1, weight=5, uniform="a")
        self.columnconfigure(2, weight=1, uniform="a")

        ttk.Label(self, text="Kwota:", font=(None, 20)).grid(row=2, column=1, sticky="ew")
        self.entry_amount.grid(row=3, column=1, sticky="we")

        ttk.Label(self, text="Termin płatności:", font=(None, 20)).grid(row=4, column=1, sticky="ew")
        self.calendar_from.grid(row=5, column=1)

        ttk.Label(self, text="Planowany termin zapłaty:", font=(None, 20)).grid(row=6, column=1, sticky="ew")
        self.calendar_to.grid(row=7, column=1)

        button_cal.grid(row=9, column=1)

        self.label_total.grid(row=10, column=0, columnspan=3)

    # calculate interest rates
    def date_pick(self):
        try:
            # getting values from entry and calendars
            kwota = float(self.entry_amount.get())
            fx = self.calendar_from.entry.get().replace(".", "-")
            ty = self.calendar_to.entry.get().replace(".", "-")

            fx = datetime.strptime(fx, "%d-%m-%Y")
            ty = datetime.strptime(ty, "%d-%m-%Y")

            if fx.weekday() == 5:
                fx = fx + timedelta(days=2)
            elif fx.weekday() == 6:
                fx = fx + timedelta(days=1)

            odsetki = 0

            if fx < ty:
                for i in range(0, len(self.history)):

                    f = datetime.strptime(self.history[i][0], "%d-%m-%Y")
                    t = datetime.strptime(self.history[i][1], "%d-%m-%Y")

                    # case checking
                    if ty > t > fx > f:
                        odsetki += (((t - fx).days + 1) * kwota * (self.history[i][-1] / 100)) / 365
                    if f > fx and t < ty:
                        odsetki += (((t - f).days + 1) * kwota * (self.history[i][-1] / 100)) / 365
                    if fx < f < ty < t:
                        odsetki += (((ty - f).days + 1) * kwota * (self.history[i][-1] / 100)) / 365
                    if f < fx < ty < t:
                        odsetki += ((ty - fx).days * kwota * (self.history[i][-1] / 100)) / 365

                    self.label_total.configure(text=f"Całkowita kwota do zapłaty: {round(odsetki + kwota)} zł")
            else:
                # date error communicate
                messagebox.showerror("BŁĄD", "Termin płatności powinien być mniejszy od daty wpłaty.")

        except ValueError:
            # value error communicate
            messagebox.showerror("BŁĄD", "Podano złe wartości w polach daty lub kwoty.")


if __name__ == "__main__":
    app = App()
    app.mainloop()

        self.title("Kalkulator odsetek podatkowych")
        self.geometry("500x600")
        self.resizable(False, False)

        # no api
        self.history = [[date(1000, 9, 1).strftime("%d-%m-%Y"), date(2006, 1, 31).strftime("%d-%m-%Y"), 12],
                        [date(2006, 2, 1).strftime("%d-%m-%Y"), date(2006, 2, 28).strftime("%d-%m-%Y"), 11.5],
                        [date(2006, 3, 1).strftime("%d-%m-%Y"), date(2007, 4, 25).strftime("%d-%m-%Y"), 11],
                        [date(2007, 4, 26).strftime("%d-%m-%Y"), date(2007, 6, 27).strftime("%d-%m-%Y"), 11.5],
                        [date(2007, 6, 28).strftime("%d-%m-%Y"), date(2007, 8, 29).strftime("%d-%m-%Y"), 12],
                        [date(2007, 8, 30).strftime("%d-%m-%Y"), date(2007, 11, 28).strftime("%d-%m-%Y"), 12.5],
                        [date(2007, 11, 29).strftime("%d-%m-%Y"), date(2008, 1, 30).strftime("%d-%m-%Y"), 13],
                        [date(2008, 1, 31).strftime("%d-%m-%Y"), date(2008, 2, 27).strftime("%d-%m-%Y"), 13.5],
                        [date(2008, 2, 28).strftime("%d-%m-%Y"), date(2008, 3, 26).strftime("%d-%m-%Y"), 14],
                        [date(2008, 3, 27).strftime("%d-%m-%Y"), date(2008, 6, 25).strftime("%d-%m-%Y"), 14.5],
                        [date(2008, 6, 26).strftime("%d-%m-%Y"), date(2008, 11, 26).strftime("%d-%m-%Y"), 15],
                        [date(2008, 11, 27).strftime("%d-%m-%Y"), date(2008, 12, 23).strftime("%d-%m-%Y"), 14.5],
                        [date(2008, 12, 24).strftime("%d-%m-%Y"), date(2009, 1, 27).strftime("%d-%m-%Y"), 13],
                        [date(2009, 1, 28).strftime("%d-%m-%Y"), date(2009, 2, 25).strftime("%d-%m-%Y"), 11.5],
                        [date(2009, 2, 26).strftime("%d-%m-%Y"), date(2009, 3, 25).strftime("%d-%m-%Y"), 11],
                        [date(2009, 3, 26).strftime("%d-%m-%Y"), date(2009, 6, 24).strftime("%d-%m-%Y"), 10.5],
                        [date(2009, 6, 25).strftime("%d-%m-%Y"), date(2010, 11, 8).strftime("%d-%m-%Y"), 10],
                        [date(2010, 11, 9).strftime("%d-%m-%Y"), date(2011, 1, 19).strftime("%d-%m-%Y"), 12],
                        [date(2011, 1, 20).strftime("%d-%m-%Y"), date(2011, 4, 5).strftime("%d-%m-%Y"), 12.5],
                        [date(2011, 4, 6).strftime("%d-%m-%Y"), date(2011, 5, 11).strftime("%d-%m-%Y"), 13],
                        [date(2011, 5, 12).strftime("%d-%m-%Y"), date(2011, 6, 8).strftime("%d-%m-%Y"), 13.5],
                        [date(2011, 6, 9).strftime("%d-%m-%Y"), date(2012, 5, 9).strftime("%d-%m-%Y"), 14],
                        [date(2012, 5, 10).strftime("%d-%m-%Y"), date(2012, 11, 7).strftime("%d-%m-%Y"), 14.5],
                        [date(2012, 11, 8).strftime("%d-%m-%Y"), date(2012, 12, 5).strftime("%d-%m-%Y"), 14],
                        [date(2012, 12, 6).strftime("%d-%m-%Y"), date(2013, 1, 9).strftime("%d-%m-%Y"), 13.5],
                        [date(2013, 1, 10).strftime("%d-%m-%Y"), date(2013, 2, 6).strftime("%d-%m-%Y"), 13],
                        [date(2013, 2, 7).strftime("%d-%m-%Y"), date(2013, 3, 6).strftime("%d-%m-%Y"), 12.5],
                        [date(2013, 3, 7).strftime("%d-%m-%Y"), date(2013, 5, 8).strftime("%d-%m-%Y"), 11.5],
                        [date(2013, 5, 9).strftime("%d-%m-%Y"), date(2013, 6, 5).strftime("%d-%m-%Y"), 11],
                        [date(2013, 6, 6).strftime("%d-%m-%Y"), date(2013, 7, 3).strftime("%d-%m-%Y"), 10.5],
                        [date(2013, 7, 4).strftime("%d-%m-%Y"), date(2014, 10, 8).strftime("%d-%m-%Y"), 10],
                        [date(2014, 10, 9).strftime("%d-%m-%Y"), date(2022, 2, 8).strftime("%d-%m-%Y"), 8],
                        [date(2022, 2, 9).strftime("%d-%m-%Y"), date(2022, 3, 8).strftime("%d-%m-%Y"), 8.5],
                        [date(2022, 3, 9).strftime("%d-%m-%Y"), date(2022, 4, 6).strftime("%d-%m-%Y"), 10],
                        [date(2022, 4, 7).strftime("%d-%m-%Y"), date(2022, 5, 5).strftime("%d-%m-%Y"), 12],
                        [date(2022, 5, 6).strftime("%d-%m-%Y"), date(2022, 6, 8).strftime("%d-%m-%Y"), 13.5],
                        [date(2022, 6, 9).strftime("%d-%m-%Y"), date(2022, 7, 7).strftime("%d-%m-%Y"), 15],
                        [date(2022, 7, 8).strftime("%d-%m-%Y"), date(2022, 9, 7).strftime("%d-%m-%Y"), 16],
                        [date(2022, 9, 8).strftime("%d-%m-%Y"), date(2023, 9, 6).strftime("%d-%m-%Y"), 16.5],
                        [date(2023, 9, 7).strftime("%d-%m-%Y"), date(2023, 10, 4).strftime("%d-%m-%Y"), 15],
                        [date(2023, 10, 5).strftime("%d-%m-%Y"), date(2100, 9, 7).strftime("%d-%m-%Y"), 14.5]
                        ]

        style_b = Style()
        style_b.configure("Custom.TButton", font=(None, 20))

        style_c = Style()
        style_c.configure('Calendar.TCalendar', font=(None, 30))

        self.entry_amount = ttk.Entry(self,
                                      font=(None, 25))
        self.calendar_from = ttk.DateEntry(self,
                                           style="Calendar")
        self.calendar_to = ttk.DateEntry(self)

        button_cal = ttk.Button(self,
                                text="Oblicz",
                                style="Custom.TButton",
                                command=self.date_pick
                                )

        self.label_total = ttk.Label(self,
                                     text="",
                                     font=(None, 18))

        self.rowconfigure(1, weight=1, uniform="a")
        self.rowconfigure(2, weight=1, uniform="a")
        self.rowconfigure(3, weight=1, uniform="a")
        self.rowconfigure(4, weight=1, uniform="a")
        self.rowconfigure(5, weight=1, uniform="a")
        self.rowconfigure(6, weight=1, uniform="a")
        self.rowconfigure(7, weight=1, uniform="a")
        self.rowconfigure(8, weight=1, uniform="a")
        self.rowconfigure(9, weight=1, uniform="a")
        self.rowconfigure(10, weight=1, uniform="a")

        self.columnconfigure(0, weight=1, uniform="a")
        self.columnconfigure(1, weight=5, uniform="a")
        self.columnconfigure(2, weight=1, uniform="a")

        ttk.Label(self, text="Kwota:", font=(None, 20)).grid(row=2, column=1, sticky="ew")
        self.entry_amount.grid(row=3, column=1, sticky="we")

        ttk.Label(self, text="Termin płatności:", font=(None, 20)).grid(row=4, column=1, sticky="ew")
        self.calendar_from.grid(row=5, column=1)

        ttk.Label(self, text="Planowany termin zapłaty:", font=(None, 20)).grid(row=6, column=1, sticky="ew")
        self.calendar_to.grid(row=7, column=1)

        button_cal.grid(row=9, column=1)

        self.label_total.grid(row=10, column=0, columnspan=3)

    def date_pick(self):
        try:
            kwota = float(self.entry_amount.get())
            fx = self.calendar_from.entry.get().replace(".", "-")
            ty = self.calendar_to.entry.get().replace(".", "-")

            fx = datetime.strptime(fx, "%d-%m-%Y")
            ty = datetime.strptime(ty, "%d-%m-%Y")

            if fx.weekday() == 5:
                fx = fx + timedelta(days=2)
            elif fx.weekday() == 6:
                fx = fx + timedelta(days=1)

            odsetki = 0

            if fx < ty:
                for i in range(0, len(self.history)):

                    f = datetime.strptime(self.history[i][0], "%d-%m-%Y")
                    t = datetime.strptime(self.history[i][1], "%d-%m-%Y")

                    if ty > t > fx > f:
                        odsetki += (((t - fx).days + 1) * kwota * (self.history[i][-1] / 100)) / 365
                    if f > fx and t < ty:
                        odsetki += (((t - f).days + 1) * kwota * (self.history[i][-1] / 100)) / 365
                    if fx < f < ty < t:
                        odsetki += (((ty - f).days + 1) * kwota * (self.history[i][-1] / 100)) / 365
                    if f < fx < ty < t:
                        odsetki += ((ty - fx).days * kwota * (self.history[i][-1] / 100)) / 365

                    self.label_total.configure(text=f"Całkowita kwota do zapłaty: {round(odsetki + kwota)} zł")
            else:
                messagebox.showerror("BŁĄD", "Termin płatności powinien być mniejszy od daty wpłaty.")

        except ValueError:
            messagebox.showerror("BŁĄD", "Podano złe wartości w polach daty lub kwoty.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
