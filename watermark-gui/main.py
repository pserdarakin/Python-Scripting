import tkinter
from tkinter import filedialog, Button
from PIL import Image, ImageTk


global resized_image_main
global resized_image_watermark
global final_image

window = tkinter.Tk()
window.title("Add Watermark")
window.minsize(width=700, height=400)


def upload_watermark():
    filename = filedialog.askopenfilename()
    if filename:
        load_and_display(filename, 'watermark')


def upload_image():
    filename = filedialog.askopenfilename()
    if filename:
        load_and_display(filename, 'main')


def load_and_display(img_path, img_type):
    image = Image.open(img_path)
    global resized_image_main, resized_image_watermark
    if img_type == 'watermark':
        resized_image_watermark = image.resize((50, 50))
        photo = ImageTk.PhotoImage(resized_image_watermark)
        if hasattr(upload_watermark, "image_label"):
            load_and_display.image_label.config(image=photo)
        else:
            load_and_display.image_label = tkinter.Label(window, image=photo)
            load_and_display.image_label.image = photo
            load_and_display.image_label.grid(row=1, column=2)
    elif img_type == 'main':
        resized_image_main = image.resize((350, 350))
        photo = ImageTk.PhotoImage(resized_image_main)
        if hasattr(upload_image, "image_label"):
            load_and_display.image_label.config(image=photo)
        else:
            load_and_display.image_label = tkinter.Label(window, image=photo)
            load_and_display.image_label.image = photo
            load_and_display.image_label.grid(row=4, column=2)


def add_watermark():
    global resized_image_main, resized_image_watermark, final_image
    if resized_image_main and resized_image_watermark:
        main_image_rgba = resized_image_main.convert("RGBA")
        watermark_rgba = resized_image_watermark.convert("RGBA")
        position = (main_image_rgba.width - watermark_rgba.width, main_image_rgba.height - watermark_rgba.height)
        combined = Image.new("RGBA", main_image_rgba.size)
        combined.paste(main_image_rgba, (0, 0))
        combined.paste(watermark_rgba, position, mask=watermark_rgba)
        final_image = combined.convert("RGB")
        display_final_image(final_image)
    else:
        print("Both main image and watermark need to be uploaded first.")


def display_final_image(final_image):
    global window
    photo = ImageTk.PhotoImage(final_image)
    if hasattr(display_final_image, "final_image_label"):
        display_final_image.final_image_label.config(image=photo)
    else:
        display_final_image.final_image_label = tkinter.Label(window, image=photo)
        display_final_image.final_image_label.image = photo
        display_final_image.final_image_label.grid(row=6, column=2)


def save_image():
    global final_image
    if final_image:
        filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
        if filepath:
            final_image.save(filepath)
            print(f"Image saved to {filepath}")
    else:
        print("No image to save.")


label_watermark = tkinter.Label(text="Choose watermark image:")
label_watermark.grid(row=1, column=0)
choose_watermark = Button(window, text="Upload", command=upload_watermark)
choose_watermark.grid(row=1, column=1)

label_image = tkinter.Label(text="Choose image:")
label_image.grid(row=4, column=0)
choose_image = Button(window, text="Upload", command=upload_image)
choose_image.grid(row=4, column=1)

apply_watermark_button = Button(window, text="Apply Watermark", command=add_watermark)
apply_watermark_button.grid(row=5, column=1)

save_image_button = Button(window, text="Save Image", command=save_image)
save_image_button.grid(row=7, column=1)

window.mainloop()
