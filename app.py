from tkinter import *
import sofie

root = Tk()

root.title("S.O.F.I.E")
root.geometry("210x310")
root.configure(bg = "midnight blue")

speakText = Label(root, text="S.O.F.I.E", bg = "midnight blue", fg= "white", font= ("Serif", 15))

listenButton = Button(root, text = "Listen", font=("Serif", 10), command=sofie.listen, bg="white", fg="black",padx=210)
listenButton.pack(side=BOTTOM)

whatYouSaid = Label(root)

speakText.pack()

root.mainloop()


#mic_btn= PhotoImage(file='Graphics/Logo.png')
#mic_img_label= Label(image=mic_btn)
#listean_button= Button(root, image=mic_btn,command= sofie.listen)
#listean_button.place(x = 90, y = 250)

#listenButton = Button(root, text = "listen", command=sofie.listen)
#speechBox = Entry(root)
#speechBox.place(x = 45, y = 260)
#speakText.pack()
#listenButton.place(x = 85, y = 260)
