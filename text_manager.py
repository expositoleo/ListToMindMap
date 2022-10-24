# Get all file's lines in a str list, an element per line
def get_filelines(file_path) -> list[str]:
    try:
        with open(file_path, encoding="UTF-8") as f:
            return f.readlines()
    except:
        print("Opening File Error")


""" get_all_titles() return a list with a list per title that contains the next format: 
TitlesList = [title (str), comment (str), identation (int)]"""


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


fl = get_filelines("file.txt")
fl = get_all_titles(fl)
print(fl)
