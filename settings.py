import ctypes
import os
import main

# Center the window
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Get window width and height
user32 = ctypes.windll.user32
WINDOWWIDTH = user32.GetSystemMetrics(0)
WINDOWHEIGHT = user32.GetSystemMetrics(1)

# Initialize pygame variables
main.pygame.init()
FPSCLOCK = main.pygame.time.Clock()
info = main.pygame.display.Info()
print("WINDOW WIDTH =", WINDOWWIDTH)
print("WINDOW HEIGHT =", WINDOWHEIGHT)
#WINDOWWIDTH = info.current_w
#WINDOWHEIGHT = info.current_h
DISPLAYSURF = main.pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), main.FULLSCREEN)
#DISPLAYSURF = main.pygame.display.set_mode((0, 0), main.RESIZABLE | main.FULLSCREEN)
BASICFONT = main.pygame.font.Font('freesansbold.ttf', 18)
BACKGROUNDSFONT = main.pygame.font.Font('freesansbold.ttf', 34)


def create_blank_dict():
    my_dict = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
        14: [],
        15: []
    }
    return my_dict


BOARD = create_blank_dict()

# CURRENTLY UNUSED
# BACKGROUNDIMAGE = pygame.image.load("background.jpg").convert()

# Function to display images
image_library = {}


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = main.pygame.image.load(canonicalized_path)
        image_library[path] = image
    return image

# Set variables
FPS = 60
BUFFER = 25
NUMLINES = 16
HALFWAY = WINDOWHEIGHT / NUMLINES / 2

#             R    G    B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
CYAN = (86, 255, 224)
PINK = (255, 160, 226)