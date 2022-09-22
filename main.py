from tkinter import *
from subprocess import run



# GET AUDIO
def get_audio():
    import platform
    os = str(platform.uname()[0])
    if "linux" in os.lower():
        run(["yt-dlp", "-x" ,"--audio-format" ,"mp3" ,"-o" ,f"~/Downloads/{new_file_input.get()}.%(ext)s" ,song_endpoint_input.get()])
        print("[+] Process Complete")
    elif "win" in os.lower():
        run(["yt-dlp", "-x" ,"--audio-format" ,"mp3" ,"-o" ,f"$HOME\Downloads\{new_file_input.get()}.%(ext)s" ,song_endpoint_input.get()])
        print("[+] Process Complete")


screen = Tk()
screen.title("Music Downloader")
screen.config(padx=50, pady=50)

# LABELS
song_endpoint_label = Label(screen, text="Youtube Url: ")
song_endpoint_label.grid(column=0, row=1)
new_file_label = Label(screen, text="File Name: ")
new_file_label.grid(column=0, row=2)

# ENTRIES
song_endpoint_input = Entry(screen)
song_endpoint_input.grid(column=1, row=1, pady=5)
new_file_input = Entry(screen)
new_file_input.grid(column=1, row=2, pady=5)

# BUTTONS
download_button = Button(screen, text="Download", command=get_audio)
download_button.grid(column=0, row=3, columnspan=2, pady=5)

screen.mainloop()