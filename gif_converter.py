import imageio, os, sys, getopt
from pathlib import Path

def makeGIF(source_full_path, target_format):
    reader = imageio.get_reader(source_full_path)
    output_file = os.path.splitext(source_full_path)[0] + target_format        
    # print("output filename: ", output_file)
    print(f"Convert {os.path.split(source_full_path)[1]} to {os.path.split(output_file)[1]}")
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(output_file, fps=fps)
    for frames in reader:
        writer.append_data(frames)
    writer.close()


def printHelpMessage():
    print("To make a GIF from a Video, run the following code in terminal")
    print("python -s source_input")
    print("or")
    print("python --source source_input")
    print("If python doesn't work, try python3 and make sure python is installed")
    print("Make sure the source video file is in this directory")
    print("Also, make sure package imageio and imageio-ffmpeg are installed with pip by running")
    print("pip install imageio imageio-ffmpeg")


if __name__ == '__main__':
    options, remainder = getopt.getopt(sys.argv[1:], 's:h', ['source=', 'help'])
    # print(options)
    source_input = ''
    current_directory_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    # print("curr path", current_directory_path)    
    help_mode = False

    for opt, arg in options:
        if opt in ('-s', '--source'):
            source_input = arg
        elif opt in ('-h', 'help'):
            printHelpMessage()
            help_mode = True

    if not help_mode:
        if source_input == '':
            print("Source file is not specified")
            printHelpMessage()
            raise FileNotFoundError

        if current_directory_path in source_input:
            source_full_path = source_input
        else:
            source_full_path = os.path.abspath(source_input)
            

        source_file = Path(source_full_path)
        if not source_file.exists():
            raise FileNotFoundError

        makeGIF(source_full_path, '.gif')
