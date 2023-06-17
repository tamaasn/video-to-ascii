import playsound

def play(file_path):
    if len(file_path)<1:
        return
    print(file_path)
    playsound.playsound(file_path)

