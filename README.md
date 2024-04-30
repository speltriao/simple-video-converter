# FFMpeg GUI

## Description
FFMpeg GUI is a simple graphical user interface (GUI) application built using Tkinter in Python. It provides an easy way to convert video files using FFMpeg with options to select input files, choose output formats, and remove subtitles.

![](https://github.com/speltriao/simple-video-converter/blob/main/example.gif)


## Features
- **File Picker Button:** Allows users to choose the video file they want to convert.
- **Output Format Selection:** Users can select the desired output format from the provided options (MP4 or MKV).
- **Subtitles Removal:** Option to remove subtitles from the output video.
- **Convert Button:** Initiates the conversion process.
- **Status Label:** Displays the conversion status, whether successful or if any errors occur.

## Installation from source
1. Clone the repository: `git clone <repository_url>`
2. Install dependencies: `pip install -r requirements.txt`

## Windows binary
1. Download the .exe from the ["releases"](https://github.com/speltriao/simple-video-converter/releases/tag/release)

## Usage
1. Run the application: `python ffmpeg_app.py`
2. Click on the "Choose video file" button and select the input video.
3. Choose the desired output format and select the "Remove subtitles" checkbox if needed.
4. Click on the "Convert" button to start the conversion process.
5. Once the conversion is complete, the status label will display the outcome.

## Dependencies
- `customtkinter`: A custom Tkinter library for enhanced GUI components.-
- `FFMpeg`: For the conversion to work properly.
