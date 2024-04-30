import subprocess


def get_error_message(error: subprocess.CalledProcessError):
    output = error.stderr.decode('utf8').split('\n')
    last_line = output[-2]  # Get the last line: contains the detailed error message
    return last_line


def get_input_folder(input_file: str) -> str:
    current_location = input_file.rsplit("/", 1)
    return current_location[0]


def remove_subtitles_flag(remove_subtitles_checkbox) -> str:
    if remove_subtitles_checkbox.get() == 1:
        return "-sn"
    else:
        return ""


def convert(input_file, output_file_extension, remove_subtitles_checkbox):
    output_file = f"{get_input_folder(input_file)}/output.{output_file_extension}"

    command = (f"ffmpeg -y -i \"{input_file}\" "
               f"-codec copy {remove_subtitles_flag(remove_subtitles_checkbox)} "
               f"\"{output_file}\"")
    subprocess.run(command, shell=True, check=True, capture_output=True)
    return output_file
