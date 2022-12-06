# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:06:56 2022

@author: emirh
"""

import pyautogui
import cv2
import numpy as np
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from recorder import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_teknobol_Recorder()
ui.setupUi(MainWindow)

MainWindow.show()

def StartRecord():
    rres = ui.cmb_Resolution.currentText()
    myResolution = rres.split(',')
    resolution = (int(myResolution[0]), int(myResolution[1]))
    print(resolution)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = ui.lne_FileName.text() + ui.cmb_FileType.currentText()
    print(filename)
    fps = float(ui.cmb_FPS.currentText())
    print(fps)
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    cv2.namedWindow("TeknoBol RECORD", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("TeknoBol RECORD", 480, 270)
      
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow('TeknoBol RECORD', frame)
        MainWindow.close()
        if cv2.waitKey(1) == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()
    
  
ui.startRecording.clicked.connect(StartRecord)
sys.exit(app.exec_())
