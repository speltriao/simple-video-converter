import os
import subprocess

import customtkinter as ctk
import operations as operations

from tkinter.filedialog import askopenfilename
from PIL import Image


class FFMpegApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.output_file_extension = "mp4"
        self.input_file = None
        self.remove_subtitles_checkbox = None
        self.status_label = None
        self.title("ffmpeg gui")
        self.geometry("600x300")
        self.create_widgets()

    def create_widgets(self):
        self.file_picker_button()
        self.output_format_textbox()
        self.output_format_combobox()
        self.subtitles_checkbox()
        self.convert_button()
        self.status_label_component()

        self.grid_columnconfigure(0, weight=1)

    def file_picker_button(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "file-picker.png")
        light_image = Image.open(image_path)
        dark_image = Image.open(image_path)
        image = ctk.CTkImage(light_image=light_image,
                             dark_image=dark_image,
                             size=(24, 24))

        file_picker_button = ctk.CTkButton(self, image=image, text="Choose video file",
                                           command=self.set_file_location)
        file_picker_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

    def output_format_textbox(self):
        output_format_textbox = ctk.CTkTextbox(self, height=4)
        output_format_textbox.insert("0.0", "Output format")  # insert at line 0 character 0
        output_format_textbox.grid(row=1, column=0, padx=20, pady=(20, 20), sticky="ew")

    def output_format_combobox(self):
        output_format_combobox = ctk.CTkComboBox(self, values=["mp4", "mkv"], command=self.update_output_format)
        output_format_combobox.grid(row=1, column=1)
        output_format_combobox.set(self.output_file_extension)
        self.output_file_extension = output_format_combobox.get()

    def subtitles_checkbox(self):
        self.remove_subtitles_checkbox = ctk.CTkCheckBox(self, text="Remove subtitles", onvalue=True, offvalue=False)
        self.remove_subtitles_checkbox.grid(row=0, column=1, padx=20, pady=(20, 20), sticky="w")

    def convert_button(self):
        convert_button = ctk.CTkButton(self, text="Convert", command=self.convert_button_callback)
        convert_button.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

    def status_label_component(self):
        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))

    def update_output_format(self, value):
        self.output_file_extension = value

    def set_file_location(self):
        self.input_file = askopenfilename()

    def convert_button_callback(self):
        try:
            output_file = operations.convert(self.input_file, self.output_file_extension, self.remove_subtitles_checkbox)
            self.status_label.configure(text=f"Conversion successful! \n{output_file}", fg_color="green")
        except subprocess.CalledProcessError as e:
            self.status_label.configure(text=operations.get_error_message(e), fg_color="red")
