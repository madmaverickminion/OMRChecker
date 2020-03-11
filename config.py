"""

Designed and Developed by-
Udayraj Deshmukh 
https://github.com/Udayraj123

"""

"""
Constants
"""
display_height = int(480)
display_width = int(640)
windowWidth = 1280
windowHeight = 720

# These flags need to be independant of template.json files.
saveMarked = 1
saveCropped = 1
showimglvl = 2
saveimglvl = 2
PRELIM_CHECKS = 0

explain = 0
# autorotate=1

BATCH_NO = 1000
NO_MARKER_ERR = 12
MULTI_BUBBLE_WARN = 15

# default paths
TEMPLATE_FILE = 'template.json'
EXTENSION_PATH = 'extensions'

# For preProcessing
GAMMA_LOW = 0.7
GAMMA_HIGH = 1.25

# For new ways of determining threshold
MIN_GAP, MIN_STD = 30, 25
MIN_JUMP = 25
# If only not confident, take help of globalTHR
CONFIDENT_JUMP = MIN_JUMP + 15
JUMP_DELTA = 30
# MIN_GAP : worst case gap of black and gray

# Templ alignment parameters
ALIGN_RANGE = range(-5, 6, 1)
# TODO ^THIS SHOULD BE IN LAYOUT FILE AS ITS RELATED TO DIMENSIONS
# ALIGN_RANGE  = [-6,-4,-2,-1,0,1,2,4,6]

# Presentation variables
uniform_height = int(1231 / 1.5)
uniform_width = int(1000 / 1.5)
# Original dims are about (3527, 2494)

# Any input images should be resized to this--
uniform_width_hd = int(uniform_width * 1.5)
uniform_height_hd = int(uniform_height * 1.5)

TEXT_SIZE = 0.95
CLR_BLACK = (50, 150, 150)
CLR_WHITE = (250, 250, 250)
CLR_GRAY = (130, 130, 130)
# CLR_DARK_GRAY = (190,190,190)
CLR_DARK_GRAY = (100, 100, 100)

# Filepaths
class Paths:
    def __init__(self, output):
        self.output = output
        self.saveMarkedDir = f'{output}/CheckedOMRs/'
        self.resultDir = f'{output}/Results/'
        self.manualDir = f'{output}/Manual/'
        self.errorsDir = f'{self.manualDir}ErrorFiles/'
        self.badRollsDir = f'{self.manualDir}BadRollNosFiles/'
        self.multiMarkedDir = f'{self.manualDir}MultiMarkedFiles/'

