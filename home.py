import tkinter as tk

calc_result = ""
curr_result = ""
int_result = ""
calc_text = ""


class View(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def view(self):
        self.lift()


class Calculator(View):
    def __init__(self, *args, **kwargs):
        View.__init__(self, *args, **kwargs)

        buttonframe = tk.Frame(self)
        buttonframe.pack()

        input_expression = tk.Entry(buttonframe, textvariable=calc_text)
        input_expression.grid(row=0, column=0)

        button1 = tk.Button(buttonframe, text=1, height=2, width=3, command=self.click(1))
        button1.grid(row=1, column=0)

        button2 = tk.Button(buttonframe, text=2, height=2, width=3, command=self.click(2))
        button2.grid(row=1, column=1)

        button3 = tk.Button(buttonframe, text=3, height=2, width=3, command=self.click(3))
        button3.grid(row=1, column=2)

        button4 = tk.Button(buttonframe, text=4, height=2, width=3, command=self.click(4))
        button4.grid(row=2, column=0)

        button5 = tk.Button(buttonframe, text=5, height=2, width=3, command=self.click(5))
        button5.grid(row=2, column=1)

        button6 = tk.Button(buttonframe, text=6, height=2, width=3, command=self.click(6))
        button6.grid(row=2, column=2)

        button7 = tk.Button(buttonframe, text=7, height=2, width=3, command=self.click(7))
        button7.grid(row=3, column=0)

        button8 = tk.Button(buttonframe, text=8, height=2, width=3, command=self.click(8))
        button8.grid(row=3, column=1)

        button9 = tk.Button(buttonframe, text=9, height=2, width=3, command=self.click(9))
        button9.grid(row=3, column=2)

        button0 = tk.Button(buttonframe, text=0, height=2, width=3, command=self.click(0))
        button0.grid(row=4, column=0)

        plus = tk.Button(buttonframe, text='+', height=2, width=3, command=self.click('+'))
        plus.grid(row=1, column=3)

        minus = tk.Button(buttonframe, text='-', height=2, width=3, command=self.click('-'))
        minus.grid(row=2, column=3)

        multiply = tk.Button(buttonframe, text='*', height=2, width=3, command=self.click('*'))
        multiply.grid(row=3, column=3)

        divide = tk.Button(buttonframe, text='/', height=2, width=3, command=self.click('/'))
        divide.grid(row=4, column=3)

        equal = tk.Button(buttonframe, text='=', height=2, width=3, command=self.calculate())
        equal.grid(row=4, column=2)

        decimal = tk.Button(buttonframe, text='.', height=2, width=3, command=self.click('.'))
        decimal.grid(row=4, column=1)

        clear = tk.Button(buttonframe, text='clear', height=2, width=3, command=self.clear())
        clear.grid(row=4, column=4)

    def click(self, number):
        global calc_text
        calc_text = calc_text + str(number)

    def calculate(self):
        global calc_text
        try:
            result = str(eval(calc_text))
            calc_text = result
        except SyntaxError:
            calc_text = "Error"
        except ZeroDivisionError:
            calc_text = "Error"

    def clear(self):
        global calc_text
        calc_text = ""


class CurrencyConverter(View):
    def __init__(self, *args, **kwargs):
        View.__init__(self, *args, **kwargs)

        placeholder = tk.StringVar(self)
        options = ""

        buttonframe = tk.Frame(self)
        buttonframe.pack()

        label = tk.Label(buttonframe, text="Exchange your currencies here! See how far your money travels. There may be a few seconds of latency when converting.")
        label.grid(row=0, column=0)

        amount_label = tk.Label(buttonframe, text="Enter amount to convert below:")
        amount_label.grid(row=1, column=0)

        from_label = tk.Label(buttonframe, text="From:")
        from_label.grid(row=2, column=0)

        from_box = tk.OptionMenu(buttonframe, placeholder, options)
        from_box.grid(row=3, column=0)

        to_label = tk.Label(buttonframe, text="To:")
        to_label.grid(row=4, column=0)

        to_box = tk.OptionMenu(buttonframe, placeholder, options)
        to_box.grid(row=5, column=0)

        value_label = tk.Label(buttonframe, text="Converted Value:")
        value_label.grid(row=6, column=0)

        value_box = tk.Text(buttonframe)
        value_box.grid(row=7, column=0)

        clear_button = tk.Button(buttonframe, text="Clear Fields")
        clear_button.grid(row=7, column=1)


class InterestCalculator(View):
    def __init__(self, *args, **kwargs):
        View.__init__(self, *args, **kwargs)

        buttonframe = tk.Frame(self)
        buttonframe.pack()

        label = tk.Label(buttonframe, text="Calculate interest on an investment below! See how much you could on interest alone.")
        label.grid(row=0, column=0)

        amount_label = tk.Label(buttonframe, text="Enter invested amount below:")
        amount_label.grid(row=1, column=0)

        amount_entry = tk.Entry(buttonframe)
        amount_entry.grid(row=2, column=0)

        rate_label = tk.Label(buttonframe, text="Enter interest rate below:")
        rate_label.grid(row=3, column=0)

        rate_entry = tk.Entry(buttonframe)
        rate_entry.grid(row=4, column=0)

        times_compounded_label = tk.Label(buttonframe, text="Enter times compounded per year below:")
        times_compounded_label.grid(row=5, column=0)

        times_compounded_entry = tk.Entry(buttonframe)
        times_compounded_entry.grid(row=6, column=0)

        continuous_label = tk.Label(buttonframe, text="Continuously Compounded?")
        continuous_label.grid(row=5, column=1)

        continuous_checkbox = tk.Checkbutton(buttonframe, offvalue=0, onvalue=1)
        continuous_checkbox.grid(row=5, column=2)

        duration_label = tk.Label(buttonframe, text="Enter duration below in years:")
        duration_label.grid(row=7, column=0)

        duration_entry = tk.Entry(buttonframe)
        duration_entry.grid(row=8, column=0)

        total_box = tk.Text(buttonframe)
        total_box.grid(row=9, column=0)

        clear_button = tk.Button(buttonframe, text="Clear Fields")
        clear_button.grid(row=8, column=1)



class Home(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        calculator = Calculator(self)
        currency = CurrencyConverter(self)
        interest = InterestCalculator(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        calculator.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        currency.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        interest.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Standard Calculator", width=23, command=calculator.lift)
        b2 = tk.Button(buttonframe, text="Currency Converter", width=23, command=currency.lift)
        b3 = tk.Button(buttonframe, text="Interest Calculator", width=23, command=interest.lift)

        b1.grid(row=1, column=0)
        b2.grid(row=1, column=1)
        b3.grid(row=1, column=2)

        label = tk.Label(self, text="Welcome to the Expanded Calculator. Select an option from the labels at the top of your screen.",
                         font=('Arial', 10))
        label.pack(side="top", fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Expanded Calculator')
    main = Home(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("500x600")
    root.mainloop()

