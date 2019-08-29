# boilerplate

from tkinter import *


class Application(Frame):
    """Create GUI for story program."""
    def __init__(self,master):
        """Initialize frame."""
        super(Application, self).__init__(master)
        self.grid()  # make gui visible
        self.create_widgets()  # add widgets to empty plate

    def create_widgets(self):
        """Create labels,text entry and radio buttons"""

        Label(self, text="Log In").grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self,text="Email").grid(row=2,column=0,columnspan=1,sticky=W)
        # email input
        self.email = Entry(self)
        self.email.grid(row= 5, column=0,columnspan=4,sticky=W)
        Label(self,text="Password").grid(row=6,column=0,columnspan=1,sticky=W)
        self.password = Entry(self)
        self.password.grid(row=7,column=0,columnspan=4,sticky=W)
    #     create a submit button

        self.submit = Button(self,text="Submit")
        self.submit.grid(row=9,column=1)



    def reveal(self):
        """Display the story after submission"""
        pass


def main():
    """Interact with the GUI class and have window."""
    root = Tk()
    root.title("Windows KeyLogger")
    root.geometry("300x200")

    app = Application(root)
    root.mainloop()
    return


if __name__ == '__main__':
    main()
