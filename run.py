import sys
import ui
import menu

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.start()
    else:
        app = ui.MainWindow()
        app.mainloop()
