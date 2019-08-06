import imageio, os, sys, getopt
from pathlib import Path

def makeGIF(input_filename, target_format):
    output_filename = os.path.splitext(input_filename)[0] + target_format
    source_full_path = os.path.abspath(input_filename)
    
    reader = imageio.get_reader(source_full_path)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(output_filename, fps=fps)
    for frames in reader:
        writer.append_data(frames)
    writer.close()


def printHelpMessage():
    print("To make a GIF from a Video, run the following code in terminal")
    print("python -s source_filename")
    print("or")
    print("python --source source_filename")
    print("If python doesn't work, try python3 and make sure python is installed")
    print("Make sure the source video file is in this directory")
    print("Also, make sure package imageio and imageio-ffmpeg are installed with pip by running")
    print("pip install imageio imageio-ffmpeg")


if __name__ == '__main__':
    options, remainder = getopt.getopt(sys.argv[1:], 's:h', ['source=', 'help'])
    # print(options)
    source_filename = ''
    pathname = os.path.dirname(sys.argv[0])        
    help_mode = False

    for opt, arg in options:
        if opt in ('-s', '--source'):
            source_filename = arg
        elif opt in ('-h', 'help'):
            printHelpMessage()
            help_mode = True

    if not help_mode:
        if source_filename == '':
            print("Source file is not specified")
            printHelpMessage()
            raise FileNotFoundError

        source_full_path = os.path.abspath(source_filename)
        source_file = Path(source_full_path)
        if not source_file.exists():
            raise FileNotFoundError

        makeGIF(source_filename, '.gif')
