from genericpath import getsize
from PIL import ImageFont

# With the file path, get all file's lines in a str list, an element per line
def get_filelines(file_path) -> list[str]:
    try:
        with open(file_path, encoding="UTF-8") as f:
            return f.readlines()
    except:
        print("Opening File Error")


# get_all_titles() receives all filelines and return a list with a list per title that contains the next format:
# TitlesList = [title (str), comment (str), identation (int)]
def get_all_titles(filelines) -> list[list]:
    all_titles = []

    for line in filelines:
        title = []
        tab_count = 0

        # Count title's tabs
        line_parm = line.split("\t")
        for i in line_parm:
            if i == "":
                tab_count = tab_count + 1
            else:
                break

        # Look if comment exists and add all elements to all_titles list
        line_parm = line.split("#")
        for i in line_parm:
            title.append(i.strip())

        title.insert(1, tab_count)
        all_titles.append(title)

    return all_titles


# Receive all_titles list and make a list with the qty of each tab level [tab0 qty, tab1 qty, tab2 qty, ...]
def get_tab_qty(all_titles) -> list:
    highest_tab = 0
    tab_qty = []

    for title_data in all_titles:

        # Takes the highest title's tab
        if highest_tab < title_data[1]:
            highest_tab = title_data[1]

    for tab in range(highest_tab + 1):
        qty = 0

        for title_data in all_titles:
            # Add tab's quantity in a list
            if tab == title_data[1]:
                qty = qty + 1

        tab_qty.append(qty)
    return tab_qty


# Receive the title and font_size and add line break if there are more than one word and it's a long phrase, then return only the title with line breaks
def _fix_title_len(title, font_size) -> str and int:
    font = ImageFont.truetype("times.ttf", font_size)
    size = font.getbbox(title)

    if size[0] / size[1] > 5 and title.find(" ") == -1:
        print("nicee")
        spacepos = [m.start() for m in re.finditer(" ", title)]
        spacepos = min(spacepos, key=lambda x: abs(x - abs(len(title))))
        title = title[:spacepos] + "\n" + title[spacepos + 1 :]
        # size = font.getbbox(title)
        # size = (size[2], size[3])
    print(title)
    return title


# Receive a title and return his length and width in pixel size
def _width_and_height(title, font_size) -> tuple:
    font = ImageFont.truetype("times.ttf", font_size)
    size = font.getbbox(title)
    size = (size[2], size[3])
    return size


# Insert title info in all_titles list, the info in each list is the next one: [title, tab, tab_qty, font_size, title_len_and_width, comment]
def insert_data(all_titles, tab_qty) -> list[list]:

    for title_data in all_titles:
        all_titles[all_titles.index(title_data)].insert(2, tab_qty[title_data[1]])
        all_titles[all_titles.index(title_data)].insert(
            3, (len(tab_qty) * 10) - (title_data[1] * 5)
        )
        all_titles[all_titles.index(title_data)][0] = _fix_title_len(
            all_titles[all_titles.index(title_data)][0],
            all_titles[all_titles.index(title_data)][3],
        )
        all_titles[all_titles.index(title_data)].insert(
            4, _width_and_height(title_data[0], title_data[3])
        )

    return all_titles


fl = get_filelines("file.txt")
at = get_all_titles(fl)
tq = get_tab_qty(at)
at = insert_data(at, tq)
print(at)
