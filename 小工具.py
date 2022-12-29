from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import *
from tkinter.ttk import *
from pynput.keyboard import Key, Controller
import webbrowser as web
import time
from random import *
import os as o
import pynput.mouse as mouse

number2 = ''
number1 = ''
newnumber1 = ''
xuanze = 0
language = 0
fileming = ''

label1_more = Label()
label2_more = Label()
label3_more = Label()
button_more = Button()
button1_more = Button()
button2_more = Button()
button3_more = Button()
button4_more = Button()
entry_more = Entry()
entry1_more = Entry()

label_more1 = Label()
label1_more1 = Label()
label2_more1 = Label()
button_more1 = Button()
button2_more1 = Button()
button3_more1 = Button()
button4_more1 = Button()
button5_more1 = Button()
button6_more1 = Button()
entry_more1 = Entry()
entry1_more1 = Entry()

label_more2 = Label()
button_more2_add0 = Button()
button_more2_add1 = Button()
button_more2_add2 = Button()
button_more2_add3 = Button()
button_more2_add4 = Button()
button_more2_add5 = Button()
button_more2_add6 = Button()
button_more2_add7 = Button()
button_more2_add8 = Button()
button_more2_add9 = Button()
button_more2_adddian = Button()
button_more2_add = Button()
button_more2_subtract = Button()
button_more2_multiply = Button()
button_more2_except = Button()
button_more2_means = Button()
button_more2_reset = Button()
button_more2_negative_number = Button()
button_more2_exit = Button()
button_more2_back = Button()
text_more2 = Text()

label_choose_language = Label()
radiobutton_choose_language_1 = Radiobutton()
radiobutton_choose_language_2 = Radiobutton()
button_choose_language = Button()

text1 = Text()
button_about_reset = Button()
text_save_file = Text()
button_save_file = Button()
button_1_save_file = Button()
entry_save_file = Entry()

button_about_reset_encoder = Button()
label_1_encoder = Label()
label_2_encoder = Label()
label_3_encoder = Label()
label_4_encoder = Label()
label_5_encoder = Label()
label_6_encoder = Label()
label_7_encoder = Label()
button_1_encoder = Button()
button_2_encoder = Button()
text_encoder = Text()
text_1_encoder = Text()
text_2_encoder = Text()
text_3_encoder = Text()
text_4_encoder = Text()
text_5_encoder = Text()
text_6_encoder = Text()
text_randint_1_encoder = Text()

Calculator_other_operations_window = Tk
Calculator_four_operations_windows = Tk
Calculator_point_and_click_window = Tk
language_window = Tk
colour_chooser_tk = Tk
about_tkinter = Tk
file_save_window = Tk
Parameter_generator_window = Tk
main_window = Tk
about_tkinter_randint = Tk

sitting = ''

fang_xiang_lian_dian = 'left'

fang_xiang_fan_ye = 'up'

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
        '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.',
        '?': '..--..', '=': '-...-', '\'': '.----.', '/': '-..-.',
        '!': '-.-.--', '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '(': '-.--.', ')': '-.--.-', '$': '...-..-', '&': '....',
        '@': '.--.-',
        'à': '.--.-', 'å': '.--.-', 'ä': '.-.-', 'æ': '.-.-',
        'ç': '-.-..', 'ĉ': '-.-..', 'ð': '..--.', 'é': '..-..',
        'è': '.-..-', 'ĝ': '--.-.', 'ĥ': '-.--.', 'ĵ': '.---.',
        'ñ': '--.--', 'ö': '---.', 'ø': '---.', 'ŝ': '...-.',
        'þ': '.--..', 'ü': '..--', 'ŭ': '..--'
        }


class Mosi(object):
    def __init__(self, code: dict):
        self.code = code

    def encode(self, string: str):
        pass

    def decode(self, string: int):
        pass


class Encode(Mosi):
    def __init__(self, code: dict):
        super().__init__(code)
        self.string = ''
        self.string_list = []
        self.mosi = []
        self.new_string = ''
        self.print_string = ''

    def encode(self, string: str):
        self.string = string.upper()
        for temp in self.string:
            self.string_list.append(temp)
        for temp1 in self.string_list:
            self.mosi.append(self.code[temp1])
        for temp2 in range(len(self.mosi)):
            self.new_string += self.mosi[temp2]
            self.new_string += '|'
        for temp3 in self.new_string:
            if temp3 == '.':
                self.print_string += 'A'
            elif temp3 == '-':
                self.print_string += 'B'
            elif temp3 == '|':
                self.print_string += 'C'
        self.print_string = int(self.print_string, 16)
        return self.print_string


class Decode(Mosi):
    def __init__(self, code: dict):
        super().__init__(code)
        self.int_string = 0
        self.new_string = ''
        self.mosi_list = []
        self.code_keys = []
        self.print_string = ''

    def decode(self, int_string: int):
        self.int_string = int_string
        self.int_string = hex(self.int_string)
        self.int_string = str(self.int_string).upper()
        for temp in self.int_string:
            if temp == 'A':
                self.new_string += '.'
            elif temp == 'B':
                self.new_string += '-'
            elif temp == 'C':
                self.new_string += '|'
        temp2 = ''
        for temp1 in self.new_string:
            if temp1 == '|':
                self.mosi_list.append(temp2)
                temp2 = ''
            else:
                temp2 += temp1
        for temp3 in range(len(self.mosi_list)):
            for temp4, temp5 in self.code.items():
                if self.mosi_list[temp3] == self.code[temp4]:
                    self.print_string += temp4
                    continue
        self.print_string = self.print_string.lower()
        if self.print_string == '':
            return '没有任何一个字符被解密'
        return self.print_string


class Calculator(object):
    def Calculator_other_operations(self):
        global label1_more
        global label2_more
        global label3_more
        global button_more
        global button1_more
        global button2_more
        global button3_more
        global button4_more
        global entry_more
        global entry1_more
        global Calculator_other_operations_window
        global language
        Calculator_other_operations_window = Tk()

        def ci():
            try:
                num = float(entry_more.get()) ** float(entry1_more.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)
            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def yu():
            try:
                num = float(entry_more.get()) % float(entry1_more.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)
            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def zheng():
            try:
                num = float(entry_more.get()) // float(entry1_more.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)
            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def tuichu():
            global language
            if language == 0:
                b = '是否退出？'
                a = askquestion("question", '%s' % b)
                if a == 'yes':
                    Calculator_other_operations_window.destroy()
                else:
                    pass
            elif language == 1:
                b = 'Do you want to quit?'
                a = askquestion("error", '%s' % b)
                if a == 'yes':
                    Calculator_other_operations_window.destroy()
                else:
                    pass

        if language == 0:
            Calculator_other_operations_window.geometry('500x500')
            Calculator_other_operations_window.title("计算器")
            Calculator_other_operations_window.iconbitmap(default="./calculator-icon_34473.ico")

            label1_more = Label(Calculator_other_operations_window, text='计算器附属窗口')
            label1_more.pack()

            label2_more = Label(Calculator_other_operations_window, text="数字一")
            label2_more.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

            label3_more = Label(Calculator_other_operations_window, text="数字二")
            label3_more.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.1)

            button_more = Button(Calculator_other_operations_window, text="次方", command=ci)
            button_more.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.1)

            button1_more = Button(Calculator_other_operations_window, text="取余", command=yu)
            button1_more.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.3)

            button2_more = Button(Calculator_other_operations_window, text="取整", command=zheng)
            button2_more.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.5)

            button3_more = Button(Calculator_other_operations_window, text="退出", command=tuichu)
            button3_more.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

            button4_more = Button(Calculator_other_operations_window, text="更多",
                                  command=self.Calculator_four_operations)
            button4_more.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

            entry_more = Entry(Calculator_other_operations_window)
            entry_more.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

            entry1_more = Entry(Calculator_other_operations_window)
            entry1_more.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)

        elif language == 1:
            Calculator_other_operations_window.geometry('500x500')
            Calculator_other_operations_window.title("calculator")
            Calculator_other_operations_window.iconbitmap(default="./calculator-icon_34473.ico")

            label1_more = Label(Calculator_other_operations_window,
                                text='Calculator attachment Calculator_point_and_click_window')
            label1_more.pack()

            label2_more = Label(Calculator_other_operations_window, text="number1")
            label2_more.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

            label3_more = Label(Calculator_other_operations_window, text="number2")
            label3_more.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.1)

            button_more = Button(Calculator_other_operations_window, text="to the power", command=ci)
            button_more.place(relheight=0.1, rely=0.8, relx=0.1)

            button1_more = Button(Calculator_other_operations_window, text="Take the balance", command=yu)
            button1_more.place(relheight=0.1, rely=0.8, relx=0.4)

            button2_more = Button(Calculator_other_operations_window, text="Rounding", command=zheng)
            button2_more.place(relheight=0.1, rely=0.8, relx=0.7)

            button3_more = Button(Calculator_other_operations_window, text="exit", command=tuichu)
            button3_more.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

            button4_more = Button(Calculator_other_operations_window, text="more",
                                  command=self.Calculator_four_operations)
            button4_more.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

            entry_more = Entry(Calculator_other_operations_window)
            entry_more.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

            entry1_more = Entry(Calculator_other_operations_window)
            entry1_more.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)

        Calculator_other_operations_window.mainloop()

    def Calculator_four_operations(self):
        global label_more1
        global label1_more1
        global label2_more1
        global button_more1
        global button2_more1
        global button3_more1
        global button4_more1
        global button5_more1
        global button6_more1
        global entry_more1
        global entry1_more1
        global Calculator_four_operations_windows
        global language
        Calculator_four_operations_windows = Tk()

        def jia():
            try:
                num = float(entry_more1.get()) + float(entry1_more1.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)
            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def jian():
            global language
            try:
                num = float(entry_more1.get()) - float(entry1_more1.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)
            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def cheng():
            try:
                num = float(entry_more1.get()) * float(entry1_more1.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)

            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def chu():
            global language
            while 1:
                try:
                    num = float(entry_more1.get()) / float(entry1_more1.get())
                    if float(entry1_more1.get()) == 0:
                        if language == 0:
                            a = "输入的数字不能为零"
                            showerror("error", '%s' % a)
                            entry1_more1.delete(0, END)
                            break
                        elif language == 1:
                            a = "The number entered cannot be zero"
                            showerror("error", '%s' % a)
                            entry1_more1.delete(0, END)
                            break
                except:
                    if language == 0:
                        a = "输入的数字格式不正确,请重新输入"
                        showerror("error", '%s' % a)
                        entry_more1.delete(0, END)
                        entry1_more1.delete(0, END)
                        break
                    elif language == 1:
                        a = "The number entered is not in the correct format, please reenter it"
                        showerror("error", '%s' % a)
                        entry_more1.delete(0, END)
                        entry1_more1.delete(0, END)
                        break
                else:
                    if language == 0:
                        showinfo("得数是", '%f' % num)
                        entry_more1.delete(0, END)
                        entry1_more1.delete(0, END)
                        break
                    elif language == 1:
                        showinfo("The number is", '%f' % num)
                        entry_more1.delete(0, END)
                        entry1_more1.delete(0, END)
                        break

        def tuichu():
            global language
            if language == 0:
                b = '是否退出？'
                a = askquestion("question", '%s' % b)
                if a == 'yes':
                    Calculator_four_operations_windows.destroy()
                else:
                    pass
            elif language == 1:
                b = 'Do you want to quit?'
                a = askquestion("error", '%s' % b)
                if a == 'yes':
                    Calculator_four_operations_windows.destroy()
                else:
                    pass

        if language == 0:
            Calculator_four_operations_windows.geometry('500x500')
            Calculator_four_operations_windows.title("计算器")
            Calculator_four_operations_windows.iconbitmap(default="./calculator-icon_34473.ico")

            label_more1 = Label(Calculator_four_operations_windows, text="数字一")
            label_more1.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

            label1_more1 = Label(Calculator_four_operations_windows, text="数字二")
            label1_more1.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.1)

            label2_more1 = Label(Calculator_four_operations_windows, text="计算器")
            label2_more1.pack()

            button_more1 = Button(Calculator_four_operations_windows, text="+", command=jia)
            button_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.1)

            button2_more1 = Button(Calculator_four_operations_windows, text="-", command=jian)
            button2_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.3)

            button3_more1 = Button(Calculator_four_operations_windows, text="×", command=cheng)
            button3_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.5)

            button4_more1 = Button(Calculator_four_operations_windows, text='÷', command=chu)
            button4_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.7)

            button5_more1 = Button(Calculator_four_operations_windows, text="更多",
                                   command=self.Calculator_other_operations)
            button5_more1.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

            button6_more1 = Button(Calculator_four_operations_windows, text="退出", command=tuichu)
            button6_more1.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

            entry_more1 = Entry(Calculator_four_operations_windows)
            entry_more1.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

            entry1_more1 = Entry(Calculator_four_operations_windows)
            entry1_more1.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)
        elif language == 1:
            Calculator_four_operations_windows.geometry('500x500')
            Calculator_four_operations_windows.title("calculator")
            Calculator_four_operations_windows.iconbitmap(default="./calculator-icon_34473.ico")

            label_more1 = Label(Calculator_four_operations_windows, text="number1")
            label_more1.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

            label1_more1 = Label(Calculator_four_operations_windows, text="number2")
            label1_more1.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.1)

            label2_more1 = Label(Calculator_four_operations_windows, text="calculator")
            label2_more1.pack()

            button_more1 = Button(Calculator_four_operations_windows, text="+", command=jia)
            button_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.1)

            button2_more1 = Button(Calculator_four_operations_windows, text="-", command=jian)
            button2_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.3)

            button3_more1 = Button(Calculator_four_operations_windows, text="×", command=cheng)
            button3_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.5)

            button4_more1 = Button(Calculator_four_operations_windows, text='÷', command=chu)
            button4_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.7)

            button5_more1 = Button(Calculator_four_operations_windows, text="more",
                                   command=self.Calculator_other_operations)
            button5_more1.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

            button6_more1 = Button(Calculator_four_operations_windows, text="exit", command=tuichu)
            button6_more1.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

            entry_more1 = Entry(Calculator_four_operations_windows)
            entry_more1.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

            entry1_more1 = Entry(Calculator_four_operations_windows)
            entry1_more1.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)

        Calculator_four_operations_windows.mainloop()

    def Calculator_point_and_click(self):
        global label_more2
        global button_more2_add0
        global button_more2_add1
        global button_more2_add2
        global button_more2_add3
        global button_more2_add4
        global button_more2_add5
        global button_more2_add6
        global button_more2_add7
        global button_more2_add8
        global button_more2_add9
        global button_more2_adddian
        global button_more2_add
        global button_more2_subtract
        global button_more2_multiply
        global button_more2_except
        global button_more2_means
        global button_more2_reset
        global button_more2_negative_number
        global button_more2_exit
        global button_more2_back
        global text_more2
        global Calculator_point_and_click_window
        global language
        Calculator_point_and_click_window = Tk()

        # ----------------------------------------------------------------------------------------------------------------------------

        class Add(object):

            def add0(self):
                global number1
                a1 = '0'
                text_more2.insert(END, a1)
                number1 += a1

            def add1(self):
                global number1
                a1 = '1'
                text_more2.insert(END, a1)
                number1 += a1

            def add2(self):
                global number1
                a1 = '2'
                text_more2.insert(END, a1)
                number1 += a1

            def add3(self):
                global number1
                a1 = '3'
                text_more2.insert(END, a1)
                number1 += a1

            def add4(self):
                global number1
                a1 = '4'
                text_more2.insert(END, a1)
                number1 += a1

            def add5(self):
                global number1
                a1 = '5'
                text_more2.insert(END, a1)
                number1 += a1

            def add6(self):
                global number1
                a1 = '6'
                text_more2.insert(END, a1)
                number1 += a1

            def add7(self):
                global number1
                a1 = '7'
                text_more2.insert(END, a1)
                number1 += a1

            def add8(self):
                global number1
                a1 = '8'
                text_more2.insert(END, a1)
                number1 += a1

            def add9(self):
                global number1
                a1 = '9'
                text_more2.insert(END, a1)
                number1 += a1

            def adddian(self):
                global number1
                a1 = '.'
                text_more2.insert(END, a1)
                number1 += a1

        # ----------------------------------------------------------------------------------------------------------------------------

        class Yunsuanfuhao(object):

            def add(self):
                global number1
                global newnumber1
                newnumber1 = number1
                string = '+'
                text_more2.insert(END, string)
                number1 += string

            def jian(self):
                global number1
                global newnumber1
                newnumber1 = number1
                string = '-'
                text_more2.insert(END, string)
                number1 += string

            def cheng(self):
                global number1
                global newnumber1
                newnumber1 = number1
                string = '*'
                string1 = '×'
                text_more2.insert(END, string1)
                number1 += string

            def chu(self):
                global number1
                global newnumber1
                newnumber1 = number1
                string = '/'
                string1 = '÷'
                text_more2.insert(END, string1)
                number1 += string

        # ----------------------------------------------------------------------------------------------------------------------------

        def dengyu():
            global number2
            global number1
            global xuanze
            global language
            try:
                global number2
                global number1
                global newnumber1
                number2 = eval(number1)
                string = '='
                text_more2.insert(END, string)
                text_more2.insert(END, number2)
            except (ValueError, ZeroDivisionError, SyntaxError) as e:
                if language == 0:
                    a1 = '请输入（点击）正确的数'
                    showerror(e, '%s' % a1)
                    number2 = ''
                    number1 = ''
                    xuanze = 0
                    text_more2.delete(1.0, END)
                elif language == 1:
                    a1 = 'Please enter (click) the correct number'
                    showerror(e, '%s' % a1)
                    number2 = ''
                    number1 = ''
                    xuanze = 0
                    text_more2.delete(1.0, END)

        def ac():
            global number2
            global number1
            global xuanze
            number2 = ''
            number1 = ''
            xuanze = 0
            text_more2.delete(1.0, END)

        def zhengfushu():
            global number1
            global number2
            text_more2.insert(END, '-')
            number1 += '-'

        def back():
            global language
            try:
                global number1
                global number2
                global xuanze
                number1 = int(number1) // 10
                text_more2.delete(1.0, END)
                text_more2.insert(END, str(number1))
            except ValueError as e:
                if language == 0:
                    a1 = '请输入（点击）正确的数'
                    showerror(str(e), '%s' % a1)
                    number2 = ''
                    number1 = ''
                    xuanze = 0
                    text_more2.delete(1.0, END)
                elif language == 1:
                    a1 = 'Please enter (click) the correct number'
                    showerror(str(e), '%s' % a1)
                    number2 = ''
                    number1 = ''
                    xuanze = 0
                    text_more2.delete(1.0, END)

        def tuichu():
            global language
            if language == 0:
                b2 = '是否退出？'
                a1 = askquestion('questions', '%s' % b2)
                if a1 == 'yes':
                    Calculator_point_and_click_window.destroy()
                else:
                    pass
            elif language == 1:
                b2 = 'Do you want to quit?'
                a1 = askquestion('questions', '%s' % b2)
                if a1 == 'yes':
                    Calculator_point_and_click_window.destroy()
                else:
                    pass

        # ----------------------------------------------------------------------------------------------------------------------------

        addnumber = Add()
        addyunsuanfuhao = Yunsuanfuhao()

        if language == 0:
            Calculator_point_and_click_window.geometry('500x500')
            Calculator_point_and_click_window.title('计算器')
            Calculator_point_and_click_window.iconbitmap(default="./calculator-icon_34473.ico")

            label_more2 = Label(Calculator_point_and_click_window, text='计算器')
            label_more2.pack()

            button_more2_add0 = Button(Calculator_point_and_click_window, text='0', command=addnumber.add0)
            button_more2_add0.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.3)

            button_more2_add1 = Button(Calculator_point_and_click_window, text='1', command=addnumber.add1)
            button_more2_add1.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.1)

            button_more2_add2 = Button(Calculator_point_and_click_window, text='2', command=addnumber.add2)
            button_more2_add2.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.3)

            button_more2_add3 = Button(Calculator_point_and_click_window, text='3', command=addnumber.add3)
            button_more2_add3.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.5)

            button_more2_add4 = Button(Calculator_point_and_click_window, text='4', command=addnumber.add4)
            button_more2_add4.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.1)

            button_more2_add5 = Button(Calculator_point_and_click_window, text='5', command=addnumber.add5)
            button_more2_add5.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.3)

            button_more2_add6 = Button(Calculator_point_and_click_window, text='6', command=addnumber.add6)
            button_more2_add6.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.5)

            button_more2_add7 = Button(Calculator_point_and_click_window, text='7', command=addnumber.add7)
            button_more2_add7.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.1)

            button_more2_add8 = Button(Calculator_point_and_click_window, text='8', command=addnumber.add8)
            button_more2_add8.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.3)

            button_more2_add9 = Button(Calculator_point_and_click_window, text='9', command=addnumber.add9)
            button_more2_add9.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.5)

            button_more2_adddian = Button(Calculator_point_and_click_window, text='.', command=addnumber.adddian)
            button_more2_adddian.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.1)

            button_more2_add = Button(Calculator_point_and_click_window, text='+', command=addyunsuanfuhao.add)
            button_more2_add.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.8)

            button_more2_subtract = Button(Calculator_point_and_click_window, text='-', command=addyunsuanfuhao.jian)
            button_more2_subtract.place(relheight=0.1, relwidth=0.2, rely=0.5, relx=0.8)

            button_more2_multiply = Button(Calculator_point_and_click_window, text='×', command=addyunsuanfuhao.cheng)
            button_more2_multiply.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.8)

            button_more2_except = Button(Calculator_point_and_click_window, text='÷', command=addyunsuanfuhao.chu)
            button_more2_except.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.8)

            button_more2_means = Button(Calculator_point_and_click_window, text='=', command=dengyu)
            button_more2_means.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.8)

            button_more2_reset = Button(Calculator_point_and_click_window, text='AC', command=ac)
            button_more2_reset.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.8)

            button_more2_negative_number = Button(Calculator_point_and_click_window, text='-/+（负）', command=zhengfushu)
            button_more2_negative_number.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.6)

            button_more2_exit = Button(Calculator_point_and_click_window, text='退出', command=tuichu)
            button_more2_exit.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.2)

            button_more2_back = Button(Calculator_point_and_click_window, text='<--', command=back)
            button_more2_back.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.4)

            text_more2 = Text(Calculator_point_and_click_window)
            text_more2.place(rely=0.05, relheight=0.3, relwidth=1)
        elif language == 1:
            Calculator_point_and_click_window.geometry('500x500')
            Calculator_point_and_click_window.title('calculator')
            Calculator_point_and_click_window.iconbitmap(default="./calculator-icon_34473.ico")

            label_more2 = Label(Calculator_point_and_click_window, text='calculator')
            label_more2.pack()

            button_more2_add0 = Button(Calculator_point_and_click_window, text='0', command=addnumber.add0)
            button_more2_add0.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.3)

            button_more2_add1 = Button(Calculator_point_and_click_window, text='1', command=addnumber.add1)
            button_more2_add1.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.1)

            button_more2_add2 = Button(Calculator_point_and_click_window, text='2', command=addnumber.add2)
            button_more2_add2.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.3)

            button_more2_add3 = Button(Calculator_point_and_click_window, text='3', command=addnumber.add3)
            button_more2_add3.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.5)

            button_more2_add4 = Button(Calculator_point_and_click_window, text='4', command=addnumber.add4)
            button_more2_add4.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.1)

            button_more2_add5 = Button(Calculator_point_and_click_window, text='5', command=addnumber.add5)
            button_more2_add5.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.3)

            button_more2_add6 = Button(Calculator_point_and_click_window, text='6', command=addnumber.add6)
            button_more2_add6.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.5)

            button_more2_add7 = Button(Calculator_point_and_click_window, text='7', command=addnumber.add7)
            button_more2_add7.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.1)

            button_more2_add8 = Button(Calculator_point_and_click_window, text='8', command=addnumber.add8)
            button_more2_add8.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.3)

            button_more2_add9 = Button(Calculator_point_and_click_window, text='9', command=addnumber.add9)
            button_more2_add9.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.5)

            button_more2_adddian = Button(Calculator_point_and_click_window, text='.', command=addnumber.adddian)
            button_more2_adddian.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.1)

            button_more2_add = Button(Calculator_point_and_click_window, text='+', command=addyunsuanfuhao.add)
            button_more2_add.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.8)

            button_more2_subtract = Button(Calculator_point_and_click_window, text='-', command=addyunsuanfuhao.jian)
            button_more2_subtract.place(relheight=0.1, relwidth=0.2, rely=0.5, relx=0.8)

            button_more2_multiply = Button(Calculator_point_and_click_window, text='×', command=addyunsuanfuhao.cheng)
            button_more2_multiply.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.8)

            button_more2_except = Button(Calculator_point_and_click_window, text='÷', command=addyunsuanfuhao.chu)
            button_more2_except.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.8)

            button_more2_means = Button(Calculator_point_and_click_window, text='=', command=dengyu)
            button_more2_means.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.8)

            button_more2_reset = Button(Calculator_point_and_click_window, text='AC', command=ac)
            button_more2_reset.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.8)

            button_more2_back = Button(Calculator_point_and_click_window, text='<--', command=back)
            button_more2_back.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.4)

            text_more2 = Text(Calculator_point_and_click_window)
            text_more2.place(rely=0.05, relheight=0.3, relwidth=1)

            button_more2_negative_number = Button(Calculator_point_and_click_window, text='-/+（negative）',
                                                  command=zhengfushu)
            button_more2_negative_number.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.6)

            button_more2_exit = Button(Calculator_point_and_click_window, text='exit', command=tuichu)
            button_more2_exit.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.2)

        Calculator_point_and_click_window.mainloop()


def Calculator_main_interface():
    global language
    question = askquestion('question?', '%s' % 'Do you speak English?')
    if question == 'yes':
        language = 1
    else:
        language = 0

    def about():
        global about_tkinter
        global text1
        global button_about_reset
        about_tkinter = Tk()

        about_tkinter.geometry('500x500')
        about_tkinter.title('关于界面(about interface)')
        about_tkinter.iconbitmap(default="./calculator-icon_34473.ico")

        text1 = Text(about_tkinter)
        text1.place(relheight=0.9, relwidth=1, rely=0)

        def reset():
            if language == 0:
                a11 = '制作：@QQ小井井\n如需搬运请加QQ：771732203（注明来意）\n或更改此为（第一行）：\n制作：@QQ小井井，已注明，已获得许可\ngithub:\nhttps://github.com' \
                      '/jingcygz/jingcygz\n（此网站为readme.md） '
                text1.delete(1.0, END)
                text1.insert(END, a11)
            elif language == 1:
                a22 = 'Production: @QQ Xiaojingjing\nWell If you need to move, please add QQ:771732203 (indicate the intention)\nOr change this to (first line):\nProduction: @QQ Xiaojing, indicated, licensed \ngithub:https://github.com/jingcygz/jingcygz\n(this site is readme.md) '
                text1.delete(1.0, END)
                text1.insert(END, a22)

        if language == 0:
            a1 = '制作：@QQ小井井\n如需搬运请加QQ：771732203（注明来意）\n或更改此为（第一行）：\n制作：@QQ小井井，已注明，已获得许可\ngithub:\nhttps://github.com' \
                 '/jingcygz/jingcygz\n（此网站为readme.md） '
            text1.insert(END, a1)

            button_about_reset = Button(about_tkinter, text='重置', command=reset)
            button_about_reset.place(rely=0.9)
        elif language == 1:
            a2 = 'Production: @QQ Xiaojingjing\nWell If you need to move, please add QQ:771732203 (indicate the intention)\nOr change this to (first line):\nProduction: @QQ Xiaojing, indicated, licensed \ngithub:https://github.com/jingcygz/jingcygz\n(this site is readme.md) '
            text1.insert(END, a2)

            button_about_reset = Button(about_tkinter, text='reset', command=reset)
            button_about_reset.place(rely=0.9)

    def colour_chooser():
        global colour_chooser_tk
        global label_more2
        global button_more2_add0
        global button_more2_add1
        global button_more2_add2
        global button_more2_add3
        global button_more2_add4
        global button_more2_add5
        global button_more2_add6
        global button_more2_add7
        global button_more2_add8
        global button_more2_add9
        global button_more2_adddian
        global button_more2_add
        global button_more2_subtract
        global button_more2_multiply
        global button_more2_except
        global button_more2_means
        global button_more2_reset
        global button_more2_negative_number
        global button_more2_exit
        global button_more2_back
        global text_more2

        global label_more1
        global label1_more1
        global label2_more1
        global button_more1
        global button2_more1
        global button3_more1
        global button4_more1
        global button5_more1
        global button6_more1
        global entry_more1
        global entry1_more1

        global label1_more
        global label2_more
        global label3_more
        global button_more
        global button1_more
        global button2_more
        global button3_more
        global button4_more
        global entry_more
        global entry1_more

        global language_window
        global label_choose_language
        global radiobutton_choose_language_1
        global radiobutton_choose_language_2
        global button_choose_language

        global about_tkinter
        global text1
        global button_about_reset

        global Calculator_other_operations_window
        global Calculator_point_and_click_window
        global Calculator_four_operations_windows
        global language

        def changeColor():
            while 1:
                try:
                    if language == 0:
                        color = askcolor()
                        color1 = askcolor()
                        fg, bg = str(color[1]), str(color1[1])
                        style = Style()
                        style.configure('test.TButton', background=bg, foreground=fg)
                        if fg == bg:
                            a4 = '你确定要选择一样的颜色吗？'
                            choose4 = askquestion('question', '%s' % a4)
                            if choose4 == 'yes':
                                a = '用于计算器（点击式）？'
                                choose = askquestion('question', '%s' % a)
                                if choose == 'yes':
                                    label_more2.configure(foreground=fg, background=bg)
                                    button_more2_add0.configure(style='test.TButton')
                                    button_more2_add1.configure(style='test.TButton')
                                    button_more2_add2.configure(style='test.TButton')
                                    button_more2_add3.configure(style='test.TButton')
                                    button_more2_add4.configure(style='test.TButton')
                                    button_more2_add5.configure(style='test.TButton')
                                    button_more2_add6.configure(style='test.TButton')
                                    button_more2_add7.configure(style='test.TButton')
                                    button_more2_add8.configure(style='test.TButton')
                                    button_more2_add9.configure(style='test.TButton')
                                    button_more2_adddian.configure(style='test.TButton')
                                    button_more2_add.configure(style='test.TButton')
                                    button_more2_subtract.configure(style='test.TButton')
                                    button_more2_multiply.configure(style='test.TButton')
                                    button_more2_except.configure(style='test.TButton')
                                    button_more2_means.configure(style='test.TButton')
                                    button_more2_reset.configure(style='test.TButton')
                                    button_more2_negative_number.configure(style='test.TButton')
                                    button_more2_exit.configure(style='test.TButton')
                                    button_more2_back.configure(style='test.TButton')
                                    text_more2.configure(foreground=fg, background=bg)
                                    Calculator_point_and_click_window.configure(background=bg)
                                    break
                                else:
                                    a1 = '用于计算器（输入式）？'
                                    choose1 = askquestion('question', '%s' % a1)
                                    if choose1 == 'yes':
                                        label_more1.configure(foreground=fg, background=bg)
                                        label1_more1.configure(foreground=fg, background=bg)
                                        label2_more1.configure(foreground=fg, background=bg)
                                        button_more1.configure(style='test.TButton')
                                        button2_more1.configure(style='test.TButton')
                                        button3_more1.configure(style='test.TButton')
                                        button4_more1.configure(style='test.TButton')
                                        button5_more1.configure(style='test.TButton')
                                        button6_more1.configure(style='test.TButton')
                                        entry_more1.configure(foreground=fg, background=bg)
                                        entry1_more1.configure(foreground=fg, background=bg)
                                        Calculator_four_operations_windows.configure(background=bg)

                                        label1_more.configure(foreground=fg, background=bg)
                                        label2_more.configure(foreground=fg, background=bg)
                                        label3_more.configure(foreground=fg, background=bg)
                                        button_more.configure(style='test.TButton')
                                        button1_more.configure(style='test.TButton')
                                        button2_more.configure(style='test.TButton')
                                        button3_more.configure(style='test.TButton')
                                        button4_more.configure(style='test.TButton')
                                        entry_more.configure(foreground=fg, background=bg)
                                        entry1_more.configure(foreground=fg, background=bg)
                                        Calculator_other_operations_window.configure(background=bg)
                                        break
                                    else:
                                        a2 = '用于语言选择界面？'
                                        choose2 = askquestion('question', '%s' % a2)
                                        if choose2 == 'yes':
                                            language_window.configure(background=bg)
                                            label_choose_language.configure(foreground=fg, background=bg)
                                            radiobutton_choose_language_1.configure(style='test.TButton')
                                            radiobutton_choose_language_2.configure(style='test.TButton')
                                            button_choose_language.configure(style='test.TButton')
                                            break
                                        else:
                                            a3 = '用于关于界面？'
                                            choose3 = askquestion('question', '%s' % a3)
                                            if choose3 == 'yes':
                                                about_tkinter.configure(background=bg)
                                                text1.configure(foreground=fg, background=bg)
                                                button_about_reset.configure(style='test.TButton')
                                                break
                                            else:
                                                label_choose_colour.configure(foreground=fg, background=bg)
                                                color_choose_button.configure(style='test.TButton')
                                                colour_chooser_tk.configure(background=bg)
                                                break
                            else:
                                break
                        elif fg != bg:
                            a = '用于计算器（点击式）？'
                            choose = askquestion('question', '%s' % a)
                            if choose == 'yes':
                                label_more2.configure(foreground=fg, background=bg)
                                button_more2_add0.configure(style='test.TButton')
                                button_more2_add1.configure(style='test.TButton')
                                button_more2_add2.configure(style='test.TButton')
                                button_more2_add3.configure(style='test.TButton')
                                button_more2_add4.configure(style='test.TButton')
                                button_more2_add5.configure(style='test.TButton')
                                button_more2_add6.configure(style='test.TButton')
                                button_more2_add7.configure(style='test.TButton')
                                button_more2_add8.configure(style='test.TButton')
                                button_more2_add9.configure(style='test.TButton')
                                button_more2_adddian.configure(style='test.TButton')
                                button_more2_add.configure(style='test.TButton')
                                button_more2_subtract.configure(style='test.TButton')
                                button_more2_multiply.configure(style='test.TButton')
                                button_more2_except.configure(style='test.TButton')
                                button_more2_means.configure(style='test.TButton')
                                button_more2_reset.configure(style='test.TButton')
                                button_more2_negative_number.configure(style='test.TButton')
                                button_more2_exit.configure(style='test.TButton')
                                button_more2_back.configure(style='test.TButton')
                                text_more2.configure(foreground=fg, background=bg)
                                Calculator_point_and_click_window.configure(background=bg)
                                break
                            else:
                                a1 = '用于计算器（输入式）？'
                                choose1 = askquestion('question', '%s' % a1)
                                if choose1 == 'yes':
                                    label_more1.configure(foreground=fg, background=bg)
                                    label1_more1.configure(foreground=fg, background=bg)
                                    label2_more1.configure(foreground=fg, background=bg)
                                    button_more1.configure(style='test.TButton')
                                    button2_more1.configure(style='test.TButton')
                                    button3_more1.configure(style='test.TButton')
                                    button4_more1.configure(style='test.TButton')
                                    button5_more1.configure(style='test.TButton')
                                    button6_more1.configure(style='test.TButton')
                                    entry_more1.configure(foreground=fg, background=bg)
                                    entry1_more1.configure(foreground=fg, background=bg)
                                    Calculator_four_operations_windows.configure(background=bg)

                                    label1_more.configure(foreground=fg, background=bg)
                                    label2_more.configure(foreground=fg, background=bg)
                                    label3_more.configure(foreground=fg, background=bg)
                                    button_more.configure(style='test.TButton')
                                    button1_more.configure(style='test.TButton')
                                    button2_more.configure(style='test.TButton')
                                    button3_more.configure(style='test.TButton')
                                    button4_more.configure(style='test.TButton')
                                    entry_more.configure(foreground=fg, background=bg)
                                    entry1_more.configure(foreground=fg, background=bg)
                                    Calculator_other_operations_window.configure(background=bg)
                                    break
                                else:
                                    a2 = '用于语言选择界面？'
                                    choose2 = askquestion('question', '%s' % a2)
                                    if choose2 == 'yes':
                                        language_window.configure(background=bg)
                                        label_choose_language.configure(foreground=fg, background=bg)
                                        radiobutton_choose_language_1.configure(style='test.TButton')
                                        radiobutton_choose_language_2.configure(style='test.TButton')
                                        button_choose_language.configure(style='test.TButton')
                                        break
                                    else:
                                        a3 = '用于关于界面？'
                                        choose3 = askquestion('question', '%s' % a3)
                                        if choose3 == 'yes':
                                            about_tkinter.configure(background=bg)
                                            text1.configure(foreground=fg, background=bg)
                                            button_about_reset.configure(style='test.TButton')
                                            break
                                        else:
                                            label_choose_colour.configure(foreground=fg, background=bg)
                                            color_choose_button.configure(style='test.TButton')
                                            colour_chooser_tk.configure(background=bg)
                                            break
                    elif language == 1:
                        color = askcolor()
                        color1 = askcolor()
                        fg, bg = str(color[1]), str(color1[1])
                        style = Style()
                        style.configure('test.TButton', background=bg, foreground=fg)
                        if fg == bg:
                            a4 = 'Are you sure you want to choose the same color?？'
                            choose4 = askquestion('question', '%s' % a4)
                            if choose4 == 'yes':
                                a = 'For calculator (point-and-click)？'
                                choose = askquestion('question', '%s' % a)
                                if choose == 'yes':
                                    label_more2.configure(foreground=fg, background=bg)
                                    button_more2_add0.configure(style='test.TButton')
                                    button_more2_add1.configure(style='test.TButton')
                                    button_more2_add2.configure(style='test.TButton')
                                    button_more2_add3.configure(style='test.TButton')
                                    button_more2_add4.configure(style='test.TButton')
                                    button_more2_add5.configure(style='test.TButton')
                                    button_more2_add6.configure(style='test.TButton')
                                    button_more2_add7.configure(style='test.TButton')
                                    button_more2_add8.configure(style='test.TButton')
                                    button_more2_add9.configure(style='test.TButton')
                                    button_more2_adddian.configure(style='test.TButton')
                                    button_more2_add.configure(style='test.TButton')
                                    button_more2_subtract.configure(style='test.TButton')
                                    button_more2_multiply.configure(style='test.TButton')
                                    button_more2_except.configure(style='test.TButton')
                                    button_more2_means.configure(style='test.TButton')
                                    button_more2_reset.configure(style='test.TButton')
                                    button_more2_negative_number.configure(style='test.TButton')
                                    button_more2_exit.configure(style='test.TButton')
                                    button_more2_back.configure(style='test.TButton')
                                    text_more2.configure(foreground=fg, background=bg)
                                    Calculator_point_and_click_window.configure(background=bg)
                                    break
                                else:
                                    a1 = 'For calculator (input type)？'
                                    choose1 = askquestion('question', '%s' % a1)
                                    if choose1 == 'yes':
                                        label_more1.configure(foreground=fg, background=bg)
                                        label1_more1.configure(foreground=fg, background=bg)
                                        label2_more1.configure(foreground=fg, background=bg)
                                        button_more1.configure(style='test.TButton')
                                        button2_more1.configure(style='test.TButton')
                                        button3_more1.configure(style='test.TButton')
                                        button4_more1.configure(style='test.TButton')
                                        button5_more1.configure(style='test.TButton')
                                        button6_more1.configure(style='test.TButton')
                                        entry_more1.configure(foreground=fg, background=bg)
                                        entry1_more1.configure(foreground=fg, background=bg)
                                        Calculator_four_operations_windows.configure(background=bg)

                                        label1_more.configure(foreground=fg, background=bg)
                                        label2_more.configure(foreground=fg, background=bg)
                                        label3_more.configure(foreground=fg, background=bg)
                                        button_more.configure(style='test.TButton')
                                        button1_more.configure(style='test.TButton')
                                        button2_more.configure(style='test.TButton')
                                        button3_more.configure(style='test.TButton')
                                        button4_more.configure(style='test.TButton')
                                        entry_more.configure(foreground=fg, background=bg)
                                        entry1_more.configure(foreground=fg, background=bg)
                                        Calculator_other_operations_window.configure(background=bg)
                                        break
                                    else:
                                        a2 = 'Used for the language selection interface？'
                                        choose2 = askquestion('question', '%s' % a2)
                                        if choose2 == 'yes':
                                            language_window.configure(background=bg)
                                            label_choose_language.configure(foreground=fg, background=bg)
                                            radiobutton_choose_language_1.configure(style='test.TButton')
                                            radiobutton_choose_language_2.configure(style='test.TButton')
                                            button_choose_language.configure(style='test.TButton')
                                            break
                                        else:
                                            a3 = 'Used for the About interface？'
                                            choose3 = askquestion('question', '%s' % a3)
                                            if choose3 == 'yes':
                                                about_tkinter.configure(background=bg)
                                                text1.configure(foreground=fg, background=bg)
                                                button_about_reset.configure(style='test.TButton')
                                                break
                                            else:
                                                label_choose_colour.configure(foreground=fg, background=bg)
                                                color_choose_button.configure(style='test.TButton')
                                                colour_chooser_tk.configure(background=bg)
                                                break
                            else:
                                break
                        elif fg != bg:
                            a = 'For calculator (point-and-click)？'
                            choose = askquestion('question', '%s' % a)
                            if choose == 'yes':
                                label_more2.configure(foreground=fg, background=bg)
                                button_more2_add0.configure(style='test.TButton')
                                button_more2_add1.configure(style='test.TButton')
                                button_more2_add2.configure(style='test.TButton')
                                button_more2_add3.configure(style='test.TButton')
                                button_more2_add4.configure(style='test.TButton')
                                button_more2_add5.configure(style='test.TButton')
                                button_more2_add6.configure(style='test.TButton')
                                button_more2_add7.configure(style='test.TButton')
                                button_more2_add8.configure(style='test.TButton')
                                button_more2_add9.configure(style='test.TButton')
                                button_more2_adddian.configure(style='test.TButton')
                                button_more2_add.configure(style='test.TButton')
                                button_more2_subtract.configure(style='test.TButton')
                                button_more2_multiply.configure(style='test.TButton')
                                button_more2_except.configure(style='test.TButton')
                                button_more2_means.configure(style='test.TButton')
                                button_more2_reset.configure(style='test.TButton')
                                button_more2_negative_number.configure(style='test.TButton')
                                button_more2_exit.configure(style='test.TButton')
                                button_more2_back.configure(style='test.TButton')
                                text_more2.configure(foreground=fg, background=bg)
                                Calculator_point_and_click_window.configure(background=bg)
                                break
                            else:
                                a1 = 'For calculator (input type)？'
                                choose1 = askquestion('question', '%s' % a1)
                                if choose1 == 'yes':
                                    label_more1.configure(foreground=fg, background=bg)
                                    label1_more1.configure(foreground=fg, background=bg)
                                    label2_more1.configure(foreground=fg, background=bg)
                                    button_more1.configure(style='test.TButton')
                                    button2_more1.configure(style='test.TButton')
                                    button3_more1.configure(style='test.TButton')
                                    button4_more1.configure(style='test.TButton')
                                    button5_more1.configure(style='test.TButton')
                                    button6_more1.configure(style='test.TButton')
                                    entry_more1.configure(foreground=fg, background=bg)
                                    entry1_more1.configure(foreground=fg, background=bg)
                                    Calculator_four_operations_windows.configure(background=bg)

                                    label1_more.configure(foreground=fg, background=bg)
                                    label2_more.configure(foreground=fg, background=bg)
                                    label3_more.configure(foreground=fg, background=bg)
                                    button_more.configure(style='test.TButton')
                                    button1_more.configure(style='test.TButton')
                                    button2_more.configure(style='test.TButton')
                                    button3_more.configure(style='test.TButton')
                                    button4_more.configure(style='test.TButton')
                                    entry_more.configure(foreground=fg, background=bg)
                                    entry1_more.configure(foreground=fg, background=bg)
                                    Calculator_other_operations_window.configure(background=bg)
                                    break
                                else:
                                    a2 = 'Used for the language selection interface？'
                                    choose2 = askquestion('question', '%s' % a2)
                                    if choose2 == 'yes':
                                        language_window.configure(background=bg)
                                        label_choose_language.configure(foreground=fg, background=bg)
                                        radiobutton_choose_language_1.configure(style='test.TButton')
                                        radiobutton_choose_language_2.configure(style='test.TButton')
                                        button_choose_language.configure(style='test.TButton')
                                    else:
                                        a3 = 'Used for the About interface？'
                                        choose3 = askquestion('question', '%s' % a3)
                                        if choose3 == 'yes':
                                            about_tkinter.configure(background=bg)
                                            text1.configure(foreground=fg, background=bg)
                                            button_about_reset.configure(style='test.TButton')
                                            break
                                        else:
                                            label_choose_colour.configure(foreground=fg, background=bg)
                                            color_choose_button.configure(style='test.TButton')
                                            colour_chooser_tk.configure(background=bg)
                                            break
                except TclError as e:
                    if language == 0:
                        b = '请选择/打开窗口！'
                        showerror(e, '%s' % b)
                        break
                    elif language == 1:
                        b = 'Please select/open Calculator_point_and_click_window!'
                        showerror(e, '%s' % b)
                        break

        colour_chooser_tk = Tk()
        colour_chooser_tk.geometry('240x240')
        colour_chooser_tk.title('计算器颜色选择界面(Calculator color selection interface)')
        colour_chooser_tk.iconbitmap(default="./calculator-icon_34473.ico")

        if language == 0:
            label_choose_colour = Label(colour_chooser_tk, text='颜色选择界面')
            label_choose_colour.pack()

            color_choose_button = Button(colour_chooser_tk,
                                         text='选择颜色（请保持打开）\n由于是ttk不能变换一些东西的颜色，敬请谅解',
                                         command=changeColor)
            color_choose_button.pack()
        elif language == 1:
            label_choose_colour = Label(colour_chooser_tk, text='Color selection interface')
            label_choose_colour.pack()

            color_choose_button = Button(colour_chooser_tk, text='Choose a color (please keep the windows open)',
                                         command=changeColor)
            color_choose_button.pack()

    c = Calculator()
    calculator_window = Tk()
    calculator_window.geometry("500x500")
    calculator_window.title('计算器显示界面(The calculator displays the interface)')
    calculator_window.iconbitmap(default="./calculator-icon_34473.ico")

    label1 = Label(calculator_window, text='计算器选择界面(Calculator selection interface)')
    label1.pack()

    button1 = Button(calculator_window, text='计算器（输入式）(Calculator (input))', command=c.Calculator_four_operations)
    button1.place(rely=0.2, relx=0.25, relheight=0.1)

    button2 = Button(calculator_window, text='计算器（点击式）(Calculator (point-and-click))',
                     command=c.Calculator_point_and_click)
    button2.place(rely=0.3, relx=0.25, relheight=0.1)

    button3 = Button(calculator_window, text='颜色切换(Color switching)', command=colour_chooser)
    button3.place(rely=0.4, relx=0.25, relheight=0.1)

    button_about = Button(calculator_window, text='关于(about)', command=about)
    button_about.place(rely=0.5, relx=0.25, relheight=0.1)

    calculator_window.mainloop()


def file_save():
    global file_save_window
    global text1
    global button_about_reset
    global text_save_file
    global button_save_file
    global button_1_save_file
    global entry_save_file

    file_save_window = Tk()
    file_save_window.geometry('500x500')
    file_save_window.title('写文件')
    file_save_window.iconbitmap(default='file_type_word_icon_130070.ico')

    def file():
        global fileming
        textget = text_save_file.get(1.0, END)
        fileming += '.txt'
        try:
            with open(file=fileming, encoding='utf-8', mode='a') as f:
                f.write(textget)
                f.close()
            b = '存储成功！'
            showinfo('成功', '%s' % b)
        except Exception as e:
            a = '出错!'
            showerror(str(e), '%s' % a)

    def file_ming():
        global fileming
        fileming = entry_save_file.get()
        c = '存储成功！'
        showinfo('成功', '%s' % c)

    def remove_file():
        global fileming
        fileming = entry_save_file.get()
        fileming += '.txt'
        o.remove(fileming)
        c = '删除成功！'
        showinfo('成功', '%s' % c)

    text_save_file = Text(file_save_window)
    text_save_file.place(relheight=0.8, relwidth=1, rely=0)

    button_save_file = Button(file_save_window, text='保存', command=file)
    button_save_file.place(rely=0.9, relheight=0.1, relwidth=1)

    button_1_save_file = Button(file_save_window, text='保存路径', command=file_ming)
    button_1_save_file.place(rely=0.8, relx=0.6, relheight=0.1, relwidth=0.2)

    button_1_save_file = Button(file_save_window, text='删除文件', command=remove_file)
    button_1_save_file.place(rely=0.8, relx=0.8, relheight=0.1, relwidth=0.2)

    entry_save_file = Entry(file_save_window)
    entry_save_file.place(rely=0.8, relx=0, relwidth=0.6, relheight=0.1)

    file_save_window.mainloop()


def Parameter_generator():
    global button_about_reset_encoder
    global label_1_encoder
    global label_2_encoder
    global label_3_encoder
    global label_4_encoder
    global label_5_encoder
    global label_6_encoder
    global label_7_encoder
    global button_1_encoder
    global button_2_encoder
    global text_encoder
    global text_1_encoder
    global text_2_encoder
    global text_3_encoder
    global text_4_encoder
    global text_5_encoder
    global text_6_encoder
    global text_randint_1_encoder
    global Parameter_generator_window

    Parameter_generator_window = Tk()
    Parameter_generator_window.geometry('500x500')
    Parameter_generator_window.title('生成编码器(Build the encoder)')

    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

    def xuanze():
        temp1 = str(8)
        temp2 = str(6)
        temp3 = str(randint(0, 9))
        temp4 = str(randint(0, 9))
        temp5 = str(randint(0, 9))
        temp6 = str(randint(0, 9))
        temp7 = str(randint(0, 9))
        temp8 = str(randint(0, 9))
        temp9 = str(randint(0, 9))
        temp10 = str(randint(0, 9))
        temp11 = str(randint(0, 9))
        temp12 = str(randint(0, 9))
        temp13 = str(randint(0, 9))
        temp14 = str(randint(0, 9))
        temp15 = str(randint(0, 9))
        tempadd = temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11 + temp12 + temp13 + temp14 + temp15
        text_encoder.delete(1.0, END)
        text_encoder.insert(END, tempadd)

        temp1 = str(8)
        temp2 = str(6)
        temp3 = str(randint(0, 9))
        temp4 = str(randint(0, 9))
        temp5 = str(randint(0, 9))
        temp6 = str(randint(0, 9))
        temp7 = str(randint(0, 9))
        temp8 = str(randint(0, 9))
        temp9 = str(randint(0, 9))
        temp10 = str(randint(0, 9))
        temp11 = str(randint(0, 9))
        temp12 = str(randint(0, 9))
        temp13 = str(randint(0, 9))
        temp14 = str(randint(0, 9))
        temp15 = str(randint(0, 9))
        tempadd = temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11 + temp12 + temp13 + temp14 + temp15
        text_1_encoder.delete(1.0, END)
        text_1_encoder.insert(END, tempadd)

        temp1 = 'A'
        temp2 = str(randint(0, 9))
        temp3 = str(randint(0, 9))
        temp4 = str(randint(0, 9))
        temp5 = str(randint(0, 9))
        temp6 = str(randint(0, 9))
        temp7 = str(randint(0, 9))
        temp8 = str(randint(0, 9))
        temp9 = str(randint(0, 9))
        temp10 = str(randint(0, 9))
        temp11 = str(randint(0, 9))
        temp12 = str(randint(0, 9))
        temp13 = str(randint(0, 9))
        temp14 = str(randint(0, 9))
        temp15 = str(randint(0, 9))
        tempadd = temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11 + temp12 + temp13 + temp14 + temp15
        text_2_encoder.delete(1.0, END)
        text_2_encoder.insert(END, tempadd)

        choose = randint(1, 2)
        if choose == 2:
            choosezimu = randint(0, 25)
            temp1 = abc[choosezimu]
        else:
            temp1 = str(randint(0, 9))

        choose1 = randint(1, 2)
        if choose1 == 2:
            choosezimu = randint(0, 25)
            temp2 = abc[choosezimu]
        else:
            temp2 = str(randint(0, 9))

        choose2 = randint(1, 2)
        if choose2 == 2:
            choosezimu = randint(0, 25)
            temp3 = abc[choosezimu]
        else:
            temp3 = str(randint(0, 9))

        choose3 = randint(1, 2)
        if choose3 == 2:
            choosezimu = randint(0, 25)
            temp4 = abc[choosezimu]
        else:
            temp4 = str(randint(0, 9))

        choose4 = randint(1, 2)
        if choose4 == 2:
            choosezimu = randint(0, 25)
            temp5 = abc[choosezimu]
        else:
            temp5 = str(randint(0, 9))

        choose5 = randint(1, 2)
        if choose5 == 2:
            choosezimu = randint(0, 25)
            temp6 = abc[choosezimu]
        else:
            temp6 = str(randint(0, 9))

        choose6 = randint(1, 2)
        if choose6 == 2:
            choosezimu = randint(0, 25)
            temp7 = abc[choosezimu]
        else:
            temp7 = str(randint(0, 9))

        choose7 = randint(1, 2)
        if choose7 == 2:
            choosezimu = randint(0, 25)
            temp8 = abc[choosezimu]
        else:
            temp8 = str(randint(0, 9))

        choose8 = randint(1, 2)
        if choose8 == 2:
            choosezimu = randint(0, 25)
            temp9 = abc[choosezimu]
        else:
            temp9 = str(randint(0, 9))

        choose9 = randint(1, 2)
        if choose9 == 2:
            choosezimu = randint(0, 25)
            temp10 = abc[choosezimu]
        else:
            temp10 = str(randint(0, 9))

        choose10 = randint(1, 2)
        if choose10 == 2:
            choosezimu = randint(0, 25)
            temp11 = abc[choosezimu]
        else:
            temp11 = str(randint(0, 9))

        choose11 = randint(1, 2)
        if choose11 == 2:
            choosezimu = randint(0, 25)
            temp12 = abc[choosezimu]
        else:
            temp12 = str(randint(0, 9))

        choose12 = randint(1, 2)
        if choose12 == 2:
            choosezimu = randint(0, 25)
            temp13 = abc[choosezimu]
        else:
            temp13 = str(randint(0, 9))

        choose13 = randint(1, 2)
        if choose13 == 2:
            choosezimu = randint(0, 25)
            temp14 = abc[choosezimu]
        else:
            temp14 = str(randint(0, 9))

        choose14 = randint(1, 2)
        if choose14 == 2:
            choosezimu = randint(0, 25)
            temp15 = abc[choosezimu]
        else:
            temp15 = str(randint(0, 9))

        tempadd = temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11 + temp12 + temp13 + temp14 + temp15
        text_3_encoder.delete(1.0, END)
        text_3_encoder.insert(END, tempadd)

        choose = randint(1, 2)
        if choose == 2:
            choosezimu = randint(0, 25)
            temp1 = abc[choosezimu]
        else:
            temp1 = str(randint(0, 9))

        choose1 = randint(1, 2)
        if choose1 == 2:
            choosezimu = randint(0, 25)
            temp2 = abc[choosezimu]
        else:
            temp2 = str(randint(0, 9))

        choose2 = randint(1, 2)
        if choose2 == 2:
            choosezimu = randint(0, 25)
            temp3 = abc[choosezimu]
        else:
            temp3 = str(randint(0, 9))

        choose3 = randint(1, 2)
        if choose3 == 2:
            choosezimu = randint(0, 25)
            temp4 = abc[choosezimu]
        else:
            temp4 = str(randint(0, 9))

        choose4 = randint(1, 2)
        if choose4 == 2:
            choosezimu = randint(0, 25)
            temp5 = abc[choosezimu]
        else:
            temp5 = str(randint(0, 9))

        choose5 = randint(1, 2)
        if choose5 == 2:
            choosezimu = randint(0, 25)
            temp6 = abc[choosezimu]
        else:
            temp6 = str(randint(0, 9))

        choose6 = randint(1, 2)
        if choose6 == 2:
            choosezimu = randint(0, 25)
            temp7 = abc[choosezimu]
        else:
            temp7 = str(randint(0, 9))

        choose7 = randint(1, 2)
        if choose7 == 2:
            choosezimu = randint(0, 25)
            temp8 = abc[choosezimu]
        else:
            temp8 = str(randint(0, 9))

        choose8 = randint(1, 2)
        if choose8 == 2:
            choosezimu = randint(0, 25)
            temp9 = abc[choosezimu]
        else:
            temp9 = str(randint(0, 9))

        choose9 = randint(1, 2)
        if choose9 == 2:
            choosezimu = randint(0, 25)
            temp10 = abc[choosezimu]
        else:
            temp10 = str(randint(0, 9))

        choose10 = randint(1, 2)
        if choose10 == 2:
            choosezimu = randint(0, 25)
            temp11 = abc[choosezimu]
        else:
            temp11 = str(randint(0, 9))

        choose11 = randint(1, 2)
        if choose11 == 2:
            choosezimu = randint(0, 25)
            temp12 = abc[choosezimu]
        else:
            temp12 = str(randint(0, 9))

        choose12 = randint(1, 2)
        if choose12 == 2:
            choosezimu = randint(0, 25)
            temp13 = abc[choosezimu]
        else:
            temp13 = str(randint(0, 9))

        choose13 = randint(1, 2)
        if choose13 == 2:
            choosezimu = randint(0, 25)
            temp14 = abc[choosezimu]
        else:
            temp14 = str(randint(0, 9))

        choose14 = randint(1, 2)
        if choose14 == 2:
            choosezimu = randint(0, 25)
            temp15 = abc[choosezimu]
        else:
            temp15 = str(randint(0, 9))

        tempadd = temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11 + temp12 + temp13 + temp14 + temp15
        text_4_encoder.delete(1.0, END)
        text_4_encoder.insert(END, tempadd)

        choose = randint(1, 2)
        if choose == 2:
            choosezimu = randint(0, 25)
            temp1 = abc[choosezimu]
        else:
            temp1 = str(randint(0, 9))

        choose1 = randint(1, 2)
        if choose1 == 2:
            choosezimu = randint(0, 25)
            temp2 = abc[choosezimu]
        else:
            temp2 = str(randint(0, 9))

        temp3 = ':'

        choose3 = randint(1, 2)
        if choose3 == 2:
            choosezimu = randint(0, 25)
            temp4 = abc[choosezimu]
        else:
            temp4 = str(randint(0, 9))

        choose4 = randint(1, 2)
        if choose4 == 2:
            choosezimu = randint(0, 25)
            temp5 = abc[choosezimu]
        else:
            temp5 = str(randint(0, 9))

        temp6 = ':'

        choose6 = randint(1, 2)
        if choose6 == 2:
            choosezimu = randint(0, 25)
            temp7 = abc[choosezimu]
        else:
            temp7 = str(randint(0, 9))

        choose7 = randint(1, 2)
        if choose7 == 2:
            choosezimu = randint(0, 25)
            temp8 = abc[choosezimu]
        else:
            temp8 = str(randint(0, 9))

        temp9 = ':'

        choose9 = randint(1, 2)
        if choose9 == 2:
            choosezimu = randint(0, 25)
            temp10 = abc[choosezimu]
        else:
            temp10 = str(randint(0, 9))

        choose10 = randint(1, 2)
        if choose10 == 2:
            choosezimu = randint(0, 25)
            temp11 = abc[choosezimu]
        else:
            temp11 = str(randint(0, 9))

        temp12 = ':'

        choose12 = randint(1, 2)
        if choose12 == 2:
            choosezimu = randint(0, 25)
            temp13 = abc[choosezimu]
        else:
            temp13 = str(randint(0, 9))

        choose13 = randint(1, 2)
        if choose13 == 2:
            choosezimu = randint(0, 25)
            temp14 = abc[choosezimu]
        else:
            temp14 = str(randint(0, 9))

        temp15 = ':'

        choose15 = randint(1, 2)
        if choose15 == 2:
            choosezimu = randint(0, 25)
            temp16 = abc[choosezimu]
        else:
            temp16 = str(randint(0, 9))

        choose16 = randint(1, 2)
        if choose16 == 2:
            choosezimu = randint(0, 25)
            temp17 = abc[choosezimu]
        else:
            temp17 = str(randint(0, 9))

        tempadd = temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11 + temp12 + temp13 + temp14 + temp15 + temp16 + temp17
        text_5_encoder.delete(1.0, END)
        text_5_encoder.insert(END, tempadd)

        choose = randint(1, 2)
        if choose == 2:
            choosezimu = randint(0, 25)
            temp1 = abc[choosezimu]
        else:
            temp1 = str(randint(0, 9))

        choose1 = randint(1, 2)
        if choose1 == 2:
            choosezimu = randint(0, 25)
            temp2 = abc[choosezimu]
        else:
            temp2 = str(randint(0, 9))

        temp3 = ':'

        choose3 = randint(1, 2)
        if choose3 == 2:
            choosezimu = randint(0, 25)
            temp4 = abc[choosezimu]
        else:
            temp4 = str(randint(0, 9))

        choose4 = randint(1, 2)
        if choose4 == 2:
            choosezimu = randint(0, 25)
            temp5 = abc[choosezimu]
        else:
            temp5 = str(randint(0, 9))

        temp6 = ':'

        choose6 = randint(1, 2)
        if choose6 == 2:
            choosezimu = randint(0, 25)
            temp7 = abc[choosezimu]
        else:
            temp7 = str(randint(0, 9))

        choose7 = randint(1, 2)
        if choose7 == 2:
            choosezimu = randint(0, 25)
            temp8 = abc[choosezimu]
        else:
            temp8 = str(randint(0, 9))

        temp9 = ':'

        choose9 = randint(1, 2)
        if choose9 == 2:
            choosezimu = randint(0, 25)
            temp10 = abc[choosezimu]
        else:
            temp10 = str(randint(0, 9))

        choose10 = randint(1, 2)
        if choose10 == 2:
            choosezimu = randint(0, 25)
            temp11 = abc[choosezimu]
        else:
            temp11 = str(randint(0, 9))

        temp12 = ':'

        choose12 = randint(1, 2)
        if choose12 == 2:
            choosezimu = randint(0, 25)
            temp13 = abc[choosezimu]
        else:
            temp13 = str(randint(0, 9))

        choose13 = randint(1, 2)
        if choose13 == 2:
            choosezimu = randint(0, 25)
            temp14 = abc[choosezimu]
        else:
            temp14 = str(randint(0, 9))

        temp15 = ':'

        choose15 = randint(1, 2)
        if choose15 == 2:
            choosezimu = randint(0, 25)
            temp16 = abc[choosezimu]
        else:
            temp16 = str(randint(0, 9))

        choose16 = randint(1, 2)
        if choose16 == 2:
            choosezimu = randint(0, 25)
            temp17 = abc[choosezimu]
        else:
            temp17 = str(randint(0, 9))

        tempadd = temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10 + temp11 + temp12 + temp13 + temp14 + temp15 + temp16 + temp17
        text_6_encoder.delete(1.0, END)
        text_6_encoder.insert(END, tempadd)

    def about():
        global about_tkinter_randint
        about_tkinter_randint = Tk()
        about_tkinter_randint.geometry('500x500')
        about_tkinter_randint.title('关于(about)')

        text_randint_1 = Text(about_tkinter_randint)
        text_randint_1.place(relheight=0.9, relwidth=1, rely=0)

        def reset():
            global button_about_reset_encoder
            a11 = '制作：@QQ小井井 和 @QQ阿旭\n如需搬运请加QQ：771732203（注明来意）\n或更改此为（第一行）：\n制作：@QQ小井井和@QQ阿旭，已注明，已获得许可\ngithub:\nhttps://github.com' \
                  '/jingcygz/jingcygz\n（此网站为readme.md）\nProduction: @QQ Xiaojing and @QQ Axu\n if you need to move, please add QQ:771732203 (indicate the intention)\n ' \
                  'or change this to (first line):\n Production: @QQ Xiaojing and @QQ Axu, already noted, permission has been obtained\n github:\nhttps://github.com/jingcygz/jingcygz (this site is readme.md) '
            text_randint_1.delete(1.0, END)
            text_randint_1.insert(END, a11)

        a1 = '制作：@QQ小井井 和 @QQ阿旭\n如需搬运请加QQ：771732203（注明来意）\n或更改此为（第一行）：\n制作：@QQ小井井和@QQ阿旭，已注明，已获得许可\ngithub:\nhttps://github.com' \
             '/jingcygz/jingcygz\n（此网站为readme.md）\nProduction: @QQ Xiaojing and @QQ Axu\n if you need to move, please add QQ:771732203 (indicate the intention)\n ' \
             'or change this to (first line):\n Production: @QQ Xiaojing and @QQ Axu, already noted, permission has been obtained\n github:\nhttps://github.com/jingcygz/jingcygz (this site is readme.md) '
        text_randint_1.insert(END, a1)

        button_about_reset_encoder = Button(about_tkinter_randint, text='重置', command=reset)
        button_about_reset_encoder.place(rely=0.9)

    label_1_encoder = Label(Parameter_generator_window, text='IMEI1')
    label_1_encoder.place(relx=0.1, rely=0.1)

    label_2_encoder = Label(Parameter_generator_window, text='IMEI2')
    label_2_encoder.place(relx=0.1, rely=0.2)

    label_3_encoder = Label(Parameter_generator_window, text='MEID')
    label_3_encoder.place(relx=0.1, rely=0.3)

    label_4_encoder = Label(Parameter_generator_window, text='SN')
    label_4_encoder.place(relx=0.1, rely=0.4)

    label_5_encoder = Label(Parameter_generator_window, text='PCBSN')
    label_5_encoder.place(relx=0.1, rely=0.5)

    label_6_encoder = Label(Parameter_generator_window, text='WIFI')
    label_6_encoder.place(relx=0.1, rely=0.6)

    label_7_encoder = Label(Parameter_generator_window, text='BLUETOOTH')
    label_7_encoder.place(relx=0.1, rely=0.7)

    button_1_encoder = Button(Parameter_generator_window, text='一键生成参数\n(One click \nparameter \ngeneration)',
                              command=xuanze)
    button_1_encoder.place(relx=0.8, rely=0, relheight=1, relwidth=0.2)

    button_2_encoder = Button(Parameter_generator_window, text='关于(about)', command=about)
    button_2_encoder.place(relx=0.1, rely=0.9, relwidth=0.2)

    text_encoder = Text(Parameter_generator_window)
    text_encoder.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.05)

    text_1_encoder = Text(Parameter_generator_window)
    text_1_encoder.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.05)

    text_2_encoder = Text(Parameter_generator_window)
    text_2_encoder.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.05)

    text_3_encoder = Text(Parameter_generator_window)
    text_3_encoder.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.05)

    text_4_encoder = Text(Parameter_generator_window)
    text_4_encoder.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.05)

    text_5_encoder = Text(Parameter_generator_window)
    text_5_encoder.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.05)

    text_6_encoder = Text(Parameter_generator_window)
    text_6_encoder.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.05)

    Parameter_generator_window.mainloop()


def shua():
    abc_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '~',
                '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '[', '}', ']', '\\',
                '|', ';', ':', '\'', '"', '<', ',', '>', '.', '?', '/', '！', '？', '（', '）', '……', '￥', '——', '【', '】',
                '、', '：', '；', '‘', '“', '，', '《', '》', '。', '·']

    screen_brushing_machine_window = Tk()
    screen_brushing_machine_window.geometry("600x400")
    screen_brushing_machine_window.title("刷屏鸡~~~")

    def 设置():
        global sitting
        question = askquestion('设置', '%s' % '是否在刷屏字符后加上刷屏机声明？')
        if question == 'yes':
            sitting = True
        else:
            sitting = False

    def 刷屏():
        try:
            global sitting
            entry_get = entry.get()
            entry_get_1 = entry_1.get()
            entry_get_2 = entry_2.get()
            if sitting == '':
                sitting = True
            if entry_get == '':
                entry_get = 1
            else:
                entry_get = int(entry_get)
            if entry_get_2 == '':
                entry_get_2 = 0
            else:
                entry_get_2 = float(entry_get_2)

            def ok():
                question = askretrycancel('确定？', '%s' % '最后一遍，是否刷屏（可能造成卡顿）')
                if question:
                    if sitting:
                        j = 5
                        showinfo('准备', '%s' % '开始计时5秒钟')
                        for i in range(5):  # 倒计时
                            print('倒计时:' + str(j))
                            j = j - 1
                            time.sleep(1)

                        for i in range(entry_get):  # 次数
                            shuru.type(entry_1.get() + '（刷屏机刷的）')
                            shuru.press(Key.enter)
                            shuru.press(Key.enter)
                            time.sleep(entry_get_2)
                    else:
                        j = 5
                        showinfo('准备', '%s' % '开始计时5秒钟')
                        for i in range(5):  # 倒计时
                            print('倒计时:' + str(j))
                            j = j - 1
                            time.sleep(1)

                        for i in range(entry_get):  # 次数
                            shuru.type(entry_get_1)
                            shuru.press(Key.enter)
                            shuru.press(Key.enter)
                            time.sleep(entry_get_2)

            if entry_get <= 1000:
                if entry_get >= 50:
                    question = askquestion('确定？', '%s' % '确定要刷大于50遍吗？')
                    if question == 'yes':
                        if len(entry_get_1) >= 15:
                            question = askquestion('确定？', '%s' % '确定要字数刷大于15个字吗？')
                            if question == 'yes':
                                ok()
                                if entry_get_2 <= 1:
                                    question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
                                    if question == 'yes':
                                        ok()
                                else:
                                    ok()
                        elif entry_get_2 <= 1:
                            question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
                            if question == 'yes':
                                ok()
                        else:
                            ok()

                elif len(entry_get_1) >= 15:
                    question = askquestion('确定？', '%s' % '确定要字数刷大于15个字吗？')
                    if question == 'yes':
                        ok()
                        if entry_get_2 <= 1:
                            question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
                            if question == 'yes':
                                ok()
                        else:
                            ok()
                elif entry_get_2 <= 1:
                    question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
                    if question == 'yes':
                        ok()
                else:
                    ok()
            else:
                showerror('错误', '%s' % '请勿刷大于1000遍')
                entry.delete(0, END)
                entry_1.delete(0, END)
                entry_2.delete(0, END)
        except Exception as x:
            showerror('错误', '%s' % x)
            entry.delete(0, END)
            entry_1.delete(0, END)
            entry_2.delete(0, END)

    def shua_sui_ji():
        try:
            entry_get = entry.get()
            entry_get_2 = entry_2.get()
            if entry_get == '':
                entry_get = 1
            else:
                entry_get = int(entry_get)
            if entry_get_2 == '':
                entry_get_2 = 0
            else:
                entry_get_2 = float(entry_get_2)

            def ok():
                question = askretrycancel('确定？', '%s' % '最后一遍，是否刷屏（可能造成卡顿）')
                if question:
                    if sitting:
                        j = 5
                        showinfo('准备', '%s' % '开始计时5秒钟')
                        for i in range(5):  # 倒计时
                            print('倒计时:' + str(j))
                            j = j - 1
                            time.sleep(1)

                        for i in range(entry_get):  # 次数
                            for a in range(randint(0, 15)):
                                temp = abc_list[randint(0, 112)]
                                shuru.type(temp)
                            shuru.type('（刷屏机刷的）')
                            shuru.press(Key.enter)
                            shuru.press(Key.enter)
                            time.sleep(entry_get_2)
                    else:
                        j = 5
                        showinfo('准备', '%s' % '开始计时5秒钟')
                        for i in range(5):  # 倒计时
                            print('倒计时:' + str(j))
                            j = j - 1
                            time.sleep(1)

                        for i in range(entry_get):  # 次数
                            for a in range(randint(0, 15)):
                                temp = abc_list[randint(0, 112)]
                                shuru.type(temp)
                            shuru.press(Key.enter)
                            shuru.press(Key.enter)
                            time.sleep(entry_get_2)

            if entry_get <= 1000:
                if entry_get >= 50:
                    question = askquestion('确定？', '%s' % '确定要刷大于50遍吗？')
                    if question == 'yes':
                        if entry_get_2 <= 1:
                            question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
                            if question == 'yes':
                                ok()
                        else:
                            ok()
                    elif entry_get_2 <= 1:
                        question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
                        if question == 'yes':
                            ok()
                    else:
                        ok()
                elif entry_get_2 <= 1:
                    question = askquestion('确定？', '%s' % '确定要刷间隔小于1秒吗？')
                    if question == 'yes':
                        ok()
                else:
                    ok()
            else:
                showerror('错误', '%s' % '请勿刷大于1000遍')
                entry.delete(0, END)
                entry_1.delete(0, END)
                entry_2.delete(0, END)
        except Exception as x:
            showerror('错误', '%s' % x)
            entry.delete(0, END)
            entry_1.delete(0, END)
            entry_2.delete(0, END)

    shuru = Controller()

    label = Label(screen_brushing_machine_window, text="制作：小井井")
    label.pack()

    label_1 = Label(screen_brushing_machine_window, text="次数")
    label_1.place(relx=0.3, rely=0.3)

    label = Label(screen_brushing_machine_window, text="内容")
    label.place(relx=0.3, rely=0.4)

    label_2 = Label(screen_brushing_machine_window, text="间隔")
    label_2.place(relx=0.3, rely=0.5)

    entry = Entry(screen_brushing_machine_window)
    entry.place(relx=0.5, rely=0.3)

    entry_1 = Entry(screen_brushing_machine_window)
    entry_1.place(relx=0.5, rely=0.4)

    entry_2 = Entry(screen_brushing_machine_window)
    entry_2.place(relx=0.5, rely=0.5)

    button = Button(screen_brushing_machine_window, text="开始刷屏", command=刷屏)
    button.place(relx=0.5, rely=0.6)

    button = Button(screen_brushing_machine_window, text="随机刷屏", command=shua_sui_ji)
    button.place(relx=0.5, rely=0.7)

    button_1 = Button(screen_brushing_machine_window, text="设置", command=设置)
    button_1.place(relx=0.5, rely=0.8)

    button_1 = Button(screen_brushing_machine_window, text="小破站", command=lambda: web.open('https://github.com/jingcygz/Screen-brushing-machine'))
    button_1.place(relx=0.5, rely=0.9)

    screen_brushing_machine_window.mainloop()


def connectator():
    global fang_xiang_lian_dian
    m = mouse.Controller()
    connectator_window = Tk()
    connectator_window.title('连点鸡~~~')
    connectator_window.geometry('600x400')

    def dianji():
        global fang_xiang_lian_dian
        try:
            entry_get = entry.get()
            entry_get_1 = entry_1.get()
            entry_get_2 = entry_2.get()
            if entry_get == '':
                entry_get = 1
            else:
                entry_get = int(entry_get)
            if entry_get_1 == '':
                entry_get_1 = 0
            else:
                entry_get_1 = float(entry_get_1)
            if entry_get_2 == '':
                entry_get_2 = 1
            else:
                entry_get_2 = int(entry_get_2)

            def ok():
                question = askretrycancel('确定？', '%s' % '最后一遍，是否点击（可能造成卡顿）')
                if question:
                    j = 5
                    showinfo('准备', '%s' % '开始计时5秒钟')
                    for a in range(5):  # 倒计时
                        print('倒计时:' + str(j))
                        j = j - 1
                        time.sleep(1)
                    if fang_xiang_lian_dian == 'left':
                        for b in range(entry_get):
                            m.click(mouse.Button.left, entry_get_2)
                            time.sleep(entry_get_1)
                    elif fang_xiang_lian_dian == 'right':
                        for c in range(entry_get):
                            m.click(mouse.Button.right, entry_get_2)
                            time.sleep(entry_get_1)
                    elif fang_xiang_lian_dian == 'middle':
                        for d in range(entry_get):
                            m.position = (randint(-1, 3000), randint(-1, 2000))
                            m.click(mouse.Button.right, entry_get_2)
                            time.sleep(entry_get_1)

            if entry_get <= 1000:
                if entry_get_2 <= 30:
                    if entry_get >= 50:
                        question = askquestion('确定？', '%s' % '确定要点击大于50遍吗？')
                        if question == 'yes':
                            if entry_get_1 <= 1:
                                question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                                if question == 'yes':
                                    if entry_get_2 >= 10:
                                        question = askquestion('确定？', '%s' % '确定要每次点击大于10次吗？')
                                        if question == 'yes': ok()
                                    else:
                                        ok()
                            else:
                                ok()
                    elif entry_get_1 <= 1:
                        question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                        if question == 'yes':
                            if entry_get_2 >= 10:
                                question = askquestion('确定？', '%s' % '确定要每次点击大于10次吗？')
                                if question == 'yes':
                                    ok()
                                else:
                                    ok()
                            else:
                                ok()
                    elif entry_get_1 <= 1:
                        question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                        if question == 'yes':
                            ok()
                    else:
                        ok()
                else:
                    showerror('错误', '%s' % '请勿每次点击大于30次或者请勿刷大于1000遍')
                    entry.delete(0, END)
                    entry_1.delete(0, END)
                    entry_2.delete(0, END)
            else:
                showerror('错误', '%s' % '请勿刷大于1000遍或者每次点击大于30次')
                entry.delete(0, END)
                entry_1.delete(0, END)
                entry_2.delete(0, END)
        except Exception as x:
            showerror('错误', '%s' % x)
            entry.delete(0, END)
            entry_1.delete(0, END)

    def suiji():
        global fang_xiang_lian_dian
        try:
            entry_get = entry.get()
            entry_get_1 = entry_1.get()
            entry_get_2 = entry_2.get()
            if entry_get == '':
                entry_get = 1
            else:
                entry_get = int(entry_get)
            if entry_get_1 == '':
                entry_get_1 = 0
            else:
                entry_get_1 = float(entry_get_1)
            if entry_get_2 == '':
                entry_get_2 = 1
            else:
                entry_get_2 = int(entry_get_2)

            def ok():
                question = askretrycancel('确定？', '%s' % '最后一遍，是否点击（可能造成卡顿）')
                if question:
                    j = 5
                    showinfo('准备', '%s' % '开始计时5秒钟')
                    for a in range(5):  # 倒计时
                        print('倒计时:' + str(j))
                        j = j - 1
                        time.sleep(1)
                    if fang_xiang_lian_dian == 'left':
                        for b in range(entry_get):
                            m.position = (randint(-1, 3000), randint(-1, 2000))
                            m.click(mouse.Button.left, entry_get_2)
                            time.sleep(entry_get_1)
                    elif fang_xiang_lian_dian == 'right':
                        for c in range(entry_get):
                            m.position = (randint(-1, 3000), randint(-1, 2000))
                            m.click(mouse.Button.right, entry_get_2)
                            time.sleep(entry_get_1)
                    elif fang_xiang_lian_dian == 'middle':
                        for d in range(entry_get):
                            m.position = (randint(-1, 3000), randint(-1, 2000))
                            m.click(mouse.Button.right, entry_get_2)
                            time.sleep(entry_get_1)

            if entry_get <= 1000:
                if entry_get_2 <= 30:
                    if entry_get >= 50:
                        question = askquestion('确定？', '%s' % '确定要点击大于50遍吗？')
                        if question == 'yes':
                            if entry_get_1 <= 1:
                                question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                                if question == 'yes':
                                    if entry_get_2 >= 10:
                                        question = askquestion('确定？', '%s' % '确定要每次点击大于10次吗？')
                                        if question == 'yes': ok()
                                    else:
                                        ok()
                            else:
                                ok()
                    elif entry_get_1 <= 1:
                        question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                        if question == 'yes':
                            if entry_get_2 >= 10:
                                question = askquestion('确定？', '%s' % '确定要每次点击大于10次吗？')
                                if question == 'yes':
                                    ok()
                                else:
                                    ok()
                            else:
                                ok()
                    elif entry_get_1 <= 1:
                        question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                        if question == 'yes':
                            ok()
                    else:
                        ok()
                else:
                    showerror('错误', '%s' % '请勿每次点击大于30次或者请勿刷大于1000遍')
                    entry.delete(0, END)
                    entry_1.delete(0, END)
                    entry_2.delete(0, END)
            else:
                showerror('错误', '%s' % '请勿刷大于1000遍或者每次点击大于30次')
                entry.delete(0, END)
                entry_1.delete(0, END)
                entry_2.delete(0, END)
        except Exception as x:
            showerror('错误', '%s' % x)
            entry.delete(0, END)
            entry_1.delete(0, END)

    def left():
        global fang_xiang_lian_dian
        fang_xiang_lian_dian = 'left'
        showinfo('成功', '%s' % '设置成功，键为{}'.format(fang_xiang_lian_dian))

    def right():
        global fang_xiang_lian_dian
        fang_xiang_lian_dian = 'right'
        showinfo('成功', '%s' % '设置成功，键为{}'.format(fang_xiang_lian_dian))

    def middle():
        global fang_xiang_lian_dian
        fang_xiang_lian_dian = 'middle'
        showinfo('成功', '%s' % '设置成功，键为{}'.format(fang_xiang_lian_dian))

    label = Label(connectator_window, text="制作：小井井")
    label.pack()

    label_1 = Label(connectator_window, text="点击次数")
    label_1.place(relx=0.3, rely=0.3)

    label_2 = Label(connectator_window, text="间隔")
    label_2.place(relx=0.3, rely=0.4)

    label_3 = Label(connectator_window, text="每次点击点击次数")
    label_3.place(relx=0.3, rely=0.5)

    entry = Entry(connectator_window)
    entry.place(relx=0.5, rely=0.3)

    entry_1 = Entry(connectator_window)
    entry_1.place(relx=0.5, rely=0.4)

    entry_2 = Entry(connectator_window)
    entry_2.place(relx=0.5, rely=0.5)

    button = Button(connectator_window, text="左键", command=left)
    button.place(relx=0.3, rely=0.6)

    button_1 = Button(connectator_window, text="中键", command=middle)
    button_1.place(relx=0.5, rely=0.6)

    button_1 = Button(connectator_window, text="右键", command=right)
    button_1.place(relx=0.7, rely=0.6)

    button_2 = Button(connectator_window, text="开始", command=dianji)
    button_2.place(relx=0.5, rely=0.7)

    button_3 = Button(connectator_window, text="随机地点连点", command=suiji)
    button_3.place(relx=0.5, rely=0.8)

    button_3 = Button(connectator_window, text="小破站", command=lambda: web.open('https://github.com/jingcygz/Connectator'))
    button_3.place(relx=0.5, rely=0.9)

    connectator_window.mainloop()


def automatic_page_turner():
    global fang_xiang_fan_ye
    m = mouse.Controller()
    automatic_page_turner_window = Tk()
    automatic_page_turner_window.title('自动翻页器')
    automatic_page_turner_window.geometry('600x400')

    def fanye():
        global fang_xiang_fan_ye
        try:
            entry_get = entry.get()
            if entry_get == '':
                entry_get = 10
            else:
                entry_get = float(entry_get)
            if entry_get == 0:
                entry_get = 10
            if fang_xiang_fan_ye == 'up' and entry_get < 0:
                entry_get = abs(entry_get)
            if fang_xiang_fan_ye == 'down' and entry_get > 0:
                entry_get = abs(entry_get)

            def ok():
                question = askretrycancel('确定？', '%s' % '最后一遍，是否翻页（可能造成卡顿）')
                if question:
                    j = 5
                    showinfo('准备', '%s' % '开始计时5秒钟')
                    for a in range(5):  # 倒计时
                        print('倒计时:' + str(j))
                        j = j - 1
                        time.sleep(1)
                    m.scroll(0, entry_get)

            if entry_get <= 1000:
                if entry_get >= 50:
                    question = askquestion('确定？', '%s' % '确定要翻页大于50次吗？')
                    if question == 'yes':
                        ok()
                else:
                    ok()
            else:
                showerror('错误', '%s' % '请勿翻大于1000遍')
                entry.delete(0, END)
        except Exception as x:
            showerror('错误', '%s' % x)
            entry.delete(0, END)

    def suijifanye():
        try:
            def ok():
                question = askretrycancel('确定？', '%s' % '最后一遍，是否翻页（可能造成卡顿）')
                if question:
                    j = 5
                    showinfo('准备', '%s' % '开始计时5秒钟')
                    for a in range(5):  # 倒计时
                        print('倒计时:' + str(j))
                        j = j - 1
                        time.sleep(1)
                    m.scroll(0, randint(-1000, 1000))

            ok()
        except Exception as x:
            showerror('错误', '%s' % x)
            entry.delete(0, END)

    def up():
        global fang_xiang_fan_ye
        fang_xiang_fan_ye = 'up'
        showinfo('成功', '%s' % '设置成功，键为{}'.format(fang_xiang_lian_dian))

    def down():
        global fang_xiang_fan_ye
        fang_xiang_fan_ye = 'down'
        showinfo('成功', '%s' % '设置成功，键为{}'.format(fang_xiang_lian_dian))

    label = Label(automatic_page_turner_window, text="制作：小井井")
    label.pack()

    label_1 = Label(automatic_page_turner_window, text="翻页")
    label_1.place(relx=0.3, rely=0.3)

    entry = Entry(automatic_page_turner_window)
    entry.place(relx=0.5, rely=0.3)

    button = Button(automatic_page_turner_window, text="开始", command=fanye)
    button.place(relx=0.5, rely=0.6)

    button_1 = Button(automatic_page_turner_window, text="随机地翻", command=suijifanye)
    button_1.place(relx=0.5, rely=0.7)

    button_2 = Button(automatic_page_turner_window, text="小破站",
                      command=lambda: web.open('https://github.com/jingcygz/Automatic_page_turner'))
    button_2.place(relx=0.5, rely=0.8)

    button_3 = Button(automatic_page_turner_window, text="上", command=up)
    button_3.place(relx=0.4, rely=0.5)

    button_4 = Button(automatic_page_turner_window, text="下", command=down)
    button_4.place(relx=0.6, rely=0.5)

    automatic_page_turner_window.mainloop()


def morse_cipher_encryption():
    morse_cipher_encryption_window = Tk()
    morse_cipher_encryption_window.title('摩斯密码加密')
    morse_cipher_encryption_window.geometry('600x400')

    class Window(object):
        def keyControl(self, event):
            if 12 == event.state and (event.keysym in ["c", "a"]):
                return
            else:
                return "break"

        def jiami(self):
            text_get = text.get(1.0, END)
            text_get = text_get.strip('\n')
            e = Encode(code=CODE)
            encode = e.encode(text_get)
            text1.delete(1.0, END)
            text1.insert(END, str(encode))

        def jiemi(self):
            text_get = text1.get(1.0, END)
            d = Decode(code=CODE)
            decode = d.decode(int(text_get))
            text.delete(1.0, END)
            text.insert(END, str(decode))

        def qingchu(self):
            text.delete(1.0, END)
            text1.delete(1.0, END)

    w = Window()

    label = Label(morse_cipher_encryption_window, text='明文:')
    label.place(relx=0, rely=0, relheight=0.1, relwidth=0.1)

    label1 = Label(morse_cipher_encryption_window, text='密文：')
    label1.place(relx=0, rely=0.5, relheight=0.1, relwidth=0.1)

    button = Button(morse_cipher_encryption_window, text='加密↓', command=w.jiami)
    button.place(rely=0.5, relx=0.2, relheight=0.1, relwidth=0.1)

    button1 = Button(morse_cipher_encryption_window, text='清空↺', command=w.qingchu)
    button1.place(rely=0.5, relx=0.4, relheight=0.1, relwidth=0.1)

    button2 = Button(morse_cipher_encryption_window, text='解密↑', command=w.jiemi)
    button2.place(rely=0.5, relx=0.6, relheight=0.1, relwidth=0.1)

    button3 = Button(morse_cipher_encryption_window, text='解密↑', command=w.jiemi)
    button3.place(rely=0.5, relx=0.6, relheight=0.1, relwidth=0.1)

    text = Text(morse_cipher_encryption_window)
    text.place(relx=0, rely=0.1, relwidth=1, relheight=0.4)

    text1 = Text(morse_cipher_encryption_window)
    text1.place(relx=0, rely=0.6, relheight=0.4, relwidth=1)

    morse_cipher_encryption_window.mainloop()


def Default_window():
    global main_window
    main_window = Tk()
    main_window.geometry('500x500')
    main_window.title('小工具(gadget)')

    label_default = Label(main_window, text='实用小工具(Utility gadgets)')
    label_default.pack()

    label_default_1 = Label(main_window,
                            text='qq@小井井，QQ：77173203，邮箱：771732203@qq.com\n(qq@ Xiaojingjing, QQ: 77173203, Email: 771732203@qq.com)')
    label_default_1.place(rely=0.8, relheight=0.2, relx=0.1)

    button_default = Button(main_window, text='计算器(calculator)', command=Calculator_main_interface)
    button_default.pack()

    button_default_1 = Button(main_window, text='写文件(write file)', command=file_save)
    button_default_1.pack()

    button_default_2 = Button(main_window, text='生成参数(Build parameters)', command=Parameter_generator)
    button_default_2.pack()

    button_default_3 = Button(main_window, text='刷屏机(Screen brushing machine)', command=shua)
    button_default_3.pack()

    button_default_4 = Button(main_window, text='连点器(connectator)', command=connectator)
    button_default_4.pack()

    button_default_5 = Button(main_window, text='自动翻页器(automatic page turner)', command=automatic_page_turner)
    button_default_5.pack()

    button_default_6 = Button(main_window, text='摩斯密码加密(morse cipher encryption)', command=morse_cipher_encryption)
    button_default_6.pack()

    main_window.mainloop()


if __name__ == '__main__':
    Default_window()
