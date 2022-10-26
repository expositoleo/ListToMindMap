# Receive the previous radius and quantity of letters of the most long title and
# return a number with the radius that will contain all titles of that tab level
def _calc_radius(all_titles, highest_tab):
    for titles in all_titles:
        if titles[1] == highest_tab:

    return

s
def _calc_pos(tab, lentext):
    if tab == 0:
        return "center"
    else:
        return "left"


testlist = [
    ["Title", 0, 1, 30, "Title"],
    ["1.0", 1, 3, 25, "firstv"],
    ["1.1", 2, 4, 20, "unouno"],
    ["1.2", 2, 4, 20],
    ["1.2.1", 3, 2, 15],
    ["1.3", 2, 4, 20],
    ["1.3.1", 3, 2, 15],
    ["2.0", 1, 3, 25],
    ["3.0", 1, 3, 25],
    ["3.1", 2, 4, 20],
]
_calc_radius(testlist, 4)