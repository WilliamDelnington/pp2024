import curses
from curses.textpad import Textbox, rectangle

def cursesInput(stdscr, ncols, nlines, uly, ulx):
    win = curses.newwin(nlines, ncols, uly, ulx)
    box = Textbox(win)
    rectangle(stdscr, uly-1, ulx-1, uly+nlines, ulx+ncols)
    stdscr.addstr(uly+nlines+1, 0, "Press Ctrl + G to confirm the input progress.")

    stdscr.refresh()

    box.edit()
    val = box.gather()
    return val