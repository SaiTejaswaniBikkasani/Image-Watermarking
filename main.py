from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont

window = Tk()
window.title("PhotoImage")
window.minsize(height=500, width=1000)
# window.config(bg="#D5C8F0", highlightthickness=0)

title = Label(text="Image WaterMarking", bg="black", fg="#FF7FBD")
title.config(width=20, height=2, font=("Courier", 16, "bold"))
title.place(x=320, y=10)

FONTS = {"Arial": "arial.ttf", "Verdana": r"C:\Users\Sai Tejaswani\Downloads\Verdana-Font\Verdana.ttf",
         "Sixtyfour": r"C:\Users\Sai Tejaswani\Downloads\Sixtyfour\Sixtyfour-Regular-VariableFont_BLED,SCAN.ttf",
         "Impact": r"C:\Users\Sai Tejaswani\Downloads\impact\impact.ttf", "Trebuchet MS": r"C:\Users\Sai Tejaswani\Downloads\trebuchet-ms-2-cufonfonts\trebuc.ttf",
         "Comicz": r"C:\Users\Sai Tejaswani\Downloads\comic-sans-ms\comicz.ttf", "Comici": r"C:\Users\Sai Tejaswani\Downloads\comic-sans-ms\comici.ttf",
         "ComicSansMS3": r"C:\Users\Sai Tejaswani\Downloads\comic-sans-ms\ComicSansMS3.ttf"}


# -------------------------- TO UPLOAD IMAGE --------------------------------
def image_upload():
    global img_label, img
    file_types = [('Jpg Files', '*.jpg')]
    file_name = filedialog.askopenfilename(filetypes=file_types)
    image = Image.open(file_name)
    resize_image = image.resize((400, 400))
    img = ImageTk.PhotoImage(resize_image)
    img_label = Label(image=img)
    img_label.image = img  # Keep a reference to prevent garbage collection
    img_label.image_path = file_name  # Store image path for future reference
    img_label.config(width=400, height=400)
    img_label.place(x=110, y=70)


# ----------------------------- TO ADD WATERMARK --------------------------------------
def watermark_added():
    global img_label, image
    text = text_type.get()
    font_name = font1.get()
    font_size = int(size.get())
    font_color = color.get()
    position = place.get()

    image = Image.open(img_label.image_path)
    image = image.resize((400, 400))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONTS[font_name], font_size)

    # Calculate text size and position
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
    img_width, img_height = image.size
    if "top" in position:
        y = 10
    elif "bottom" in position:
        y = img_height - text_height - 10
    else:
        y = (img_height - text_height) // 2

    if "left" in position:
        x = 10
    elif "right" in position:
        x = img_width - text_width - 10
    else:
        x = (img_width - text_width) // 2

    draw.text((x, y), text, fill=font_color, font=font)
    img_with_text = ImageTk.PhotoImage(image)
    img_label.configure(image=img_with_text)
    img_label.config(width=400, height=400)

    img_label.image = img_with_text


# -------------------------- TO SAVE IMAGE ------------------------------------
def save_image():
    image.save(r"C:\Users\Sai Tejaswani\Documents\web development projects\watermarked.jpg")


button1 = Button(text="Upload File", command=image_upload)
button1.config(width=35)
button1.place(x=650, y=330)

label1 = Label(text="Text:", fg="black", font=("Times New Roman", 13, "italic"))
label1.place(x=600, y=100)

text_type = Entry(width=40)
text_type.place(x=720, y=105)

label2 = Label(text="Font:", fg="black", font=("Times New Roman", 13, "italic"))
label2.place(x=600, y=140)

fonts_list = ["Arial", "Verdana", "Sixtyfour", "Impact", "Trebuchet MS", "Comicz", "Comici", "ComicSansMS3"]
font1 = StringVar(window)
font1.set("Times New Roman")
fontOptions = OptionMenu(window, font1, *fonts_list)
menu_width = len(max(fonts_list))
fontOptions.config(width=34)
fontOptions.place(x=720, y=140)

label3 = Label(text="Color:", fg="black", font=("Times New Roman", 13, "italic"))
label3.place(x=600, y=185)

colors_list = ["black", "white", "olive", "punch", "juniper", "wine", "blue", "yellow", "red", "green", "pink",
               "purple", "sky blue", "shadow", "purple"]
color = StringVar(window)
color.set("black")
colorMenu = OptionMenu(window, color, *colors_list)
colorMenu.config(width=34)
colorMenu.place(x=720, y=181)

label4 = Label(text="Size:", fg="black", font=("Times New Roman", 13, "italic"))
label4.place(x=600, y=225)

size = Spinbox(from_=1, to=20, width=39)
size.place(x=720, y=230)

label5 = Label(text="Text Position:", fg="black", font=("Times New Roman", 13, "italic"))
label5.place(x=600, y=260)

text_places = ["top left", "top right", "top center", "bottom left", "bottom center", "bottom right", "center"]
place = StringVar(window)
place.set("center")
text_place = OptionMenu(window, place, *text_places)
text_place.config(width=34)
text_place.place(x=720, y=260)

add_watermark = Button(text="Add WaterMark", command=watermark_added)
add_watermark.place(x=650, y=370)

save_image = Button(text="Save Image", command=save_image)
save_image.config(width=15)
save_image.place(x=790, y=370)

window.mainloop()
