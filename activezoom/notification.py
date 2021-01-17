import sys
import time

import tkinter as tk
from tkinter import ttk
from tkinterhtml import HtmlFrame

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QMovie, QIcon
from PyQt5 import QtCore

from activezoom import exercises
from activezoom.toggledframe import ToggledFrame
from activezoom.settings import SettingsWindow
import re
from urllib.request import Request, urlopen

popup = tk.Tk()
LARGE_FONT= ("Verdana", 12, "bold")
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
PAD_Y=15

app = QApplication(sys.argv)
window = QWidget()

exercise_controlelr = exercises.Exercises()

from PyQt5.QtGui import QPixmap, QIcon

def parse_header(msg):
    header_regex = r'<h3>(\n.*)+</p>\n?(?=<p>)'
    return re.search(header_regex, msg).group()

def parse_instructions(msg):
    instructions_regex = r'<ol.*>(\n.*)+<\/ol>'
    return re.search(instructions_regex, msg).group()

def display_popup(msg): 
    global window
   
    def close_msg():
        popup.destroy()

    window.setWindowIcon(QIcon('icon.png'))
    rand_exercise = exercise_controlelr.recommend_exercise()

    window.setWindowTitle('Your Exercise Recommendation Is:')
    window.setGeometry(100, 100, 600, 600)
    window.move(60, 15)

    main_layout = QVBoxLayout()
    exercise_header = parse_header(rand_exercise)
    header_label = QLabel(exercise_header)
    header_label.move(60, 15)
    main_layout.addWidget(header_label)

    img_urls = [x.group() for x in re.finditer(r'<img id=".*" src=".*/>', rand_exercise, re.M)]
    img_urls = [re.search(r'src="(.+?)"', url).group(1) for url in img_urls] 

    movies_data = []
    data_buffers = []
    movies = []
    movie_labels = []
    gif_layout = QHBoxLayout()
    gif_layout.addStretch(1)
    for i in range(len(img_urls)):
        print(img_urls[i])

        req = Request(img_urls[i], headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req).read()

        movies_data.append(QtCore.QByteArray(data))
        data_buffers.append(QtCore.QBuffer(movies_data[i]))
        data_buffers[i].open(QtCore.QIODevice.ReadOnly)
        movies.append(QMovie())
        movies[i].setDevice(data_buffers[i])
        movies[i].setFormat(QtCore.QByteArray(b'gif'))
        movie_labels.append(QLabel())
        movie_labels[i].setMovie(movies[i])
        gif_layout.addWidget(movie_labels[i])
        movies[i].start()
  
    gif_layout.addStretch(1)
    main_layout.addLayout(gif_layout)

    exercise_instructions = parse_instructions(rand_exercise)
    instructions_label = QLabel(exercise_instructions)
    instructions_label.move(60, 15)
    main_layout.addWidget(instructions_label)

    window.setLayout(main_layout)
    window.show()
    app.exec_()


    #settings = SettingsWindow(popup)

    #popup.lift()
    #popup.attributes('-topmost', True)
    #popup.attributes('-topmost', False)
    #popup.mainloop()

display_popup("Test!")
