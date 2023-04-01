from tkinter import *  # To create a GUI for the application
import pyttsx3         # library to convert text to speech

window = Tk()            # create tkinter(GUI) window
window.title("text_to_speech_convertor")    # title of window
window.geometry("650x550+350+400")  # initial dimensions of the window

frame1 = Frame(window,bg = "lightpink",height = "150") # styling the frame
frame1.pack(fill = X)                                # place the widget in correct position
 
 
frame2 = Frame(window,bg = "lightgreen",height = "500")
frame2.pack(fill=X)

label = Label(frame1, text = "Text to Speech",font = "bold, 36",bg = "lightpink")  # styling the label which shows text
label.place(x = 180, y = 70)
 
def talk():    # function which helps to set speech properties and convert text to speech
    engine = pyttsx3.init() 
    engine.setProperty('rate',150) # setproperty method is used to set the properties like rate,voloume
    engine.setProperty('volume',1)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(enter_txt.get()) # say method is provided with the text as an argument to speak the given text
    engine.runAndWait()  # runandWait method is used to tell the engine that words spoken should not collide with any other task to be executed
    
enter_txt = Entry(frame2, width = 45,bd = 4, font = 14)  # entry is used to enter text
enter_txt.place(x = 130, y = 52)
enter_txt.insert(0, "") # insert method is used to add text to the widget.it takes two arguments (index,char) index to specify where txt has to be added and char ,the text to be added


button = Button(frame2, text = "SUBMIT",width = "15", pady = 10,font = "bold, 15",
             command = talk, bg='lightyellow')  # create button which holds talk function using command
 
button.place(x = 250,y = 130)


window.mainloop() # Start the GUI