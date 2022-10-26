import turtle as tt

# Receive the previous radius and quantity of letters of the most long title and
# return a number with the radius that will contain all titles of that tab level
def _calc_radius(qty, prev_rad):
    return


def _calc_pos(tab, lentext):
    if tab == 0:
        return "center"
    else:
        return "left"


def _circle(text):
    pass


def write_titles(all_titles):
    canvas = tt.Screen()
    tt.TurtleScreen._RUNNING = True
    highest_tab = 0
    tab_qty = []

    for title_data in all_titles:

        # Takes the highest title's tab
        if highest_tab < title_data[1]:
            highest_tab = title_data[1]

    fontsize = highest_tab * 8 + 8  # GLOBAL???

    for tab in range(highest_tab + 1):
        qty = 0

        for title_data in all_titles:
            # Add tab's quantity in a list
            if tab == title_data[1]:
                qty = qty + 1

        tab_qty.insert(tab, qty)

    # Start to graphic
    for tab in range(len(tab_qty)):
        for title_data in all_titles:
            if title_data[1] == tab:
                tt.write(
                    title_data[0],
                    move=False,
                    align=_get_pos(tab, len(title_data[0])),
                    font=["Arial", fontsize - (tab * 8), "normal"],
                )

        # _circle(pos, size)

    canvas.exitonclick()
    tt.done()


all_titles = [
    ["title", 0, "comm1"],
    ["a", 1],
    ["a.1", 2],
    ["b", 1],
    ["b.1", 2],
    ["b.1.1", 3],
]

write_titles(all_titles)
