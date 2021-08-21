#!usr/bin/python
from tkinter import Tk, Label, Entry, Button, CENTER, FALSE, TRUE
from tkinter.font import Font
#Window
window = Tk()
window.title("Renaming")
window.geometry('960x540')
window.resizable(width = FALSE, height = FALSE)
#fonts
label_font = Font(family = 'Manjari thin', size = 32)
entry_font = Font(family = 'Manjari thin', size = 20)
window.grid_rowconfigure(1, weight = 0)
window.grid_columnconfigure(1, weight=1)
#entry and questions
def label_create(prompt, y):
    label_name = Label(window, text = prompt, font = label_font)
    label_name.grid(row = y, column = 1, pady = (20, 10))
def entry_create(y):
    entry_name = Entry(window, width = 20, borderwidth = 0, font = entry_font)
    entry_name.grid(row = y, column = 1, pady = (0, 15))
    return entry_name
entry1 = entry_create(2)
entry1.focus_set()
entry2 = entry_create(4)
entry3 = entry_create(6)
label_create('Enter your word:', 1)
label_create('What Would You Like Replaced?', 3)
label_create('Replaced With What? ', 5)
window.grid_rowconfigure(1, weight = 0)
window.grid_columnconfigure(1, weight=1)
#translate
def translatein(include):
    for x in old_name:
        if x in include:
            new_name = x.replace(x,replacement)
            new_string.append(new_name)
        else:
            new_string.append(x)
def translateout(exclude):
    for x in old_name:
        if not x in exclude:
            new_name = x.replace(x,replacement)
            new_string.append(new_name)
        else:
            new_string.append(x)
#first screen
def click():
    global old_name, new_name, replacement, new_string
    old_name = entry1.get().lower()
    replaced = entry2.get().lower()
    replacement = entry3.get().lower()
    new_string = []
    vowels = ['vowels', 'a, e, i, o, u', 'a, e, i, o, and u', 'aeiou', 'vowel']
    consonants = ['consonants', 'constants', 'consinants', 'consenants', 'consanents', 'consonents', 'consonant']
    everything = ['everything', 'everythin', 'yes', 'ye']
    numbers = ['numbers', 'numbres', 'nubmers']
    #vowels
    if replaced in vowels:
        include = ['a','e', 'i', 'o', 'u']
        translatein(include)
        new_name = "".join(new_string)
    #consonants
    elif replaced in consonants:
        exclude = [' ', 'a', 'e', 'i', 'o', 'u', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        translateout(exclude)
        new_name = "".join(new_string)
    #everything
    elif replaced in everything:
        exclude = ([' '])
        translateout(exclude)
        new_name = "".join(new_string)
    #numbers
    elif replaced in numbers:
        include = (['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
        translatein(include)
        new_name = "".join(new_string)
    else:
        new_name = old_name.replace(replaced,replacement)
    for widget in window.winfo_children():
        widget.destroy()
#second screen
def yes_or_no():
    global this_is, buttton1, button2
    this_is = Label(window, text = 'This is your new name:\n' + new_name + '\nWould you like to keep it?', font = label_font)
    this_is.grid(row = 1, column = 1, pady = (25, 35))
    buttton1 = Button(window, width = 15, height = 5, font = Font(family = 'Manjari thin', size = 15), text = 'Yes', command = click_yes, borderwidth = 2)
    buttton1.grid(row = 2, column = 1, padx = 25 , sticky = 'sw')
    button2 = Button(window, width = 15, height = 5, font = Font(family = 'Manjari thin', size = 15), text = 'No', command = click_no, borderwidth = 2)
    button2.grid(row = 2, column = 1, padx = 25, sticky = 'se')
    window.unbind('<Return>')
#continue
def enter(event):
    click()
    yes_or_no()
window.bind('<Return>', enter)
#yes click
def click_yes():
    for widget in window.winfo_children():
        widget.destroy()
    label5 = Label(window, text = 'Congratulations,\n' + new_name + '!\n \nPress Enter to Exit', font = label_font, anchor = CENTER)
    label5.grid(row = 1, column = 1, pady = (25, 0))
    window.bind('<Return>', exit)
#no click
def click_no():
    for widget in window.winfo_children():
        widget.destroy()
    label5 = Label(window, text = "Well that's too bad . . .\n\n\nPress Enter to Exit", font = label_font, anchor = CENTER)
    label6 = Label(window, text = 'you hurt my feelings', font = Font(family = 'Manjari thin', size = 10))
    label5.grid(row = 1, column = 1, pady = (25,0))
    label6.grid(row = 2, column = 1, sticky = 'se')
    window.bind('<Return>', exit)

window.mainloop()