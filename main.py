import sys
import save_frame
import write_ascii
import run_ascii
import sound
import threading

command = sys.argv[1]

if (command == "make"):

    #Save video frames to a directory
    if (sys.argv[2] == "frames"):
        filename = input("mp4 file :")
        directory = input("Directory for saving frame files : ")
        path = directory + "/"
        save_frame.save(path , filename)

    #Save ascii file to a directory
    elif (sys.argv[2] == "ascii"):
        frame_directory = input("Frame files directory : ")
        save_directory = input("Save directory :")
        path = frame_directory+"/"
        write_ascii.write(frame_directory , save_directory)

#Run video
if (command == "run"):
    ascii_directory = input("ASCII files directory : ")
    sound_file = input("music file (if you dont want to add music just press enter)")
    thread = threading.Thread(target=sound.play, args=(sound_file,))
    thread.start()
    run_ascii.run(ascii_directory)




