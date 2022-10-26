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
            line_parm = i.split()
            title.append(line_parm[0])

        title.insert(1, tab_count)
        all_titles.append(title)

    return all_titles


# Receive all_titles list and adds a qty of each tab level
def add_info_qty(all_titles):
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

    for title_data in all_titles:
        all_titles[all_titles.index(title_data)].insert(2, tab_qty[title_data[1]])
        all_titles[all_titles.index(title_data)].insert(
            3, (highest_tab * 10) - (title_data[1] * 5)
        )
    return all_titles


fl = get_filelines("file.txt")
fl = get_all_titles(fl)
fl = add_info_qty(fl)
# print(fl)
