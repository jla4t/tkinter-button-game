from tkinter import *

CLICK_COUNT = 0


def get_text():
    global CLICK_COUNT
    input_str = txt_input.get()
    if input_str == "sorry":
        button.pack()
        text.config(text="Okay. You get one more chance.")
        CLICK_COUNT = 0
    else:
        text_label.config(text=input_str)


def button_click():
    global CLICK_COUNT
    CLICK_COUNT += 1
    text.config(text="Click Count: ")
    label.config(text=CLICK_COUNT)
    if CLICK_COUNT == 69 or CLICK_COUNT == 420:
        text.config(text="(nice) Click Count: ")
    elif CLICK_COUNT == 500:
        text.config(text="...Can you please stop clicking?")
    elif CLICK_COUNT == 600:
        text.config(text="Okay, you've won. You don't have to keep going.")
    elif CLICK_COUNT == 601:
        text.config(text="Stop.")
    elif CLICK_COUNT == 602:
        text.config(text="I mean it.")
    elif CLICK_COUNT == 603:
        text.config(text="Okay, i'm taking away your button until you apologize. I hope you're happy. ")
        button.pack_forget()


# window class
window = Tk()
window.title("Button Clicker")
window.minsize(width=500, height=300)

# label class
text = Label(text="Click Count: ")
text.pack()
label = Label(text=CLICK_COUNT)
label.pack()

# button class
button = Button(text="Click me.", command=button_click)
button.pack()

# entry class
txt_input = Entry()
input_button = Button(text="Submit", command=get_text)
txt_input.pack()
input_button.pack()
text_label = Label(text="your text here")
text_label.pack()



window.mainloop()
