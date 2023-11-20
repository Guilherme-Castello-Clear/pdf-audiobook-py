from PyPDF2 import PdfReader
import tkinter.filedialog
import tkinter.messagebox
from tkinter import Tk, Button, Entry, Label
from gtts import gTTS

TEXT = ""
FILE_NAME = ""


def read_file():
    pdf = tkinter.filedialog.askopenfilename(filetypes=[('PDF', '*.pdf')])
    opened_pdf = PdfReader(pdf)
    global TEXT
    global FILE_NAME

    for page in range(len(opened_pdf.pages) - 1):
        current_page = opened_pdf.pages[page]
        TEXT += current_page.extract_text()

        save_button = Button(window, text="Save", command=save_mp3)
        save_button.pack()


def save_mp3():
    global TEXT
    global FILE_NAME
    FILE_NAME = file_name_input.get()
    audio = gTTS(text=TEXT, lang="pt-BR", slow=False)
    audio.save(f"{FILE_NAME}.mp3")


window = Tk()

select_button = Button(window, text="Select file", highlightthickness=0, height=2, width=10, command=read_file)
select_button.pack()

name_label = Label(window, text="Como deseja salvar o arquivo?")
name_label.pack()

file_name_input = Entry(window)
file_name_input.pack()

window.mainloop()
