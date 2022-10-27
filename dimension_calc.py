# Receive all_titles list and tab_qty and calculate the radious of the space that will use each identation level


def _calc_radius(all_titles, tab_qty):
    for titles in all_titles:
        if titles[1] == highest_tab:

            return


def _calc_pos(tab, lentext):
    if tab == 0:
        return "center"
    else:
        return "left"


testlist = [
    ["Title", 0, 1, 40, (75, 36), "Title"],
    ["1.0", 1, 3, 35, (45, 32), "firstv"],
    ["1.1", 2, 4, 30, (38, 27), "unouno"],
    ["1.2", 2, 4, 30, (38, 27)],
    ["1.2.1", 3, 2, 25, (51, 23)],
    ["1.3", 2, 4, 30, (38, 27)],
    ["1.3.1", 3, 2, 25, (51, 23)],
    ["2.0", 1, 3, 35, (45, 32)],
    ["3.0", 1, 3, 35, (45, 32)],
    ["3.1", 2, 4, 30, (38, 27)],
]

# _calc_radius(testlist, 4)
import re
from PIL import ImageFont

title = "this is a heavy long title "
font_size = 35

font = ImageFont.truetype("times.ttf", font_size)
size = font.getbbox(title)
size = [size[2], size[3]]

if size[0] / size[1] >= 5 and title.find(" ") != -1:
    print(size[0] / size[1])
    spacepos = [m.start() for m in re.finditer(" ", title)]
    spacepos = min(spacepos, key=lambda x: abs(x - abs(len(title) / count)))
    title = title[:spacepos] + "\n" + title[spacepos + 1 :]
    size = font.getbbox(title)
    size = (size[2], size[3])


print(size)
print(title)
