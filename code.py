#Joe Melia EET-107
from adafruit_circuitplayground import cp

notes_dict = {"A4":440, "B4":494, "C5":523, "D5":587, "E5":659,
              "F5":698, "G5":784, "A5":880, "B5":988, "C6":1047}
colors = {"black":(0, 0, 0), "red":(255, 0 ,0), "green":(0, 255, 0),
          "blue":(0, 0, 255), "yellow":(255, 255, 0), "purple":(255, 0, 255),
          "cyan":(0, 255, 255), "white":(255, 255, 255)}
def fill_pixels(color):
    cp.pixels.fill(color)
    
def main():
    while True:
        if cp.touch_A1:
            cp.start_tone(notes_dict["A4"])
            fill_pixels(colors["red"])
        elif cp.touch_A3:
            cp.start_tone(notes_dict["B4"])
            fill_pixels(colors["yellow"])
        elif cp.touch_A4:
            cp.start_tone(notes_dict["E5"])
            fill_pixels(colors["green"])
        elif cp.touch_A6:
            cp.start_tone(notes_dict["F5"])
            fill_pixels(colors["blue"])
        else:
            cp.stop_tone()
            fill_pixels(colors["black"])
main()
