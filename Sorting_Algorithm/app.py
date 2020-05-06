# private imports
from .algorithm_tester import Algorithm_Tester
from .wiki_formatter import Wiki_Formatter

## python imports
# used to display graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
# used for graph legends
import matplotlib.patches as mpatches
# Tkinter GUI
import tkinter as tk

# constants
LARGE_FONT = ("Times", 30, "bold")
SMALL_FONT = ("Times", 20)
BUTTON_FONT = ("Helvetica", 15)
LIST_FONT = ("Helvetica", 15)

# currently supported sorting algorithms:
IMPLEMENTED_SORTS = [("Python sorted()", "sorted_sort"),
                    ("List.sort()", "list_sort"),
                    ("Insertion Sort", "insertion_sort"),
                    ("Selection Sort", "selection_sort"),
                    ("Bubble Sort", "bubble_sort"),
                    ("Merge Sort", "merge_sort"),
                    ("Heap Sort", "heap_sort"),
                    ("Quick Sort", "quick_sort")]

## This should probably get its own styling file
class Menu_Button(tk.Button):

    def __init__(self, *args, **kwargs):

        tk.Button.__init__(self, *args, **kwargs)

        self["font"] = BUTTON_FONT
        self["padx"] = 10
        self["pady"] = 5
        

class Sorting_Algorithm_App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, "icon/icon.ico")
        tk.Tk.title(self, "Sorting Algorithm Explorer")

        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # dictionary to map classes of frames ("pages") to
        # their created objects
        self.frames = {}

        # initialize all of the frames

        # it's important that the wiki and graph pages come first
        # because other frames refer to them
        for name, func_name in IMPLEMENTED_SORTS:

            graph_frame = GraphPage(container, self, name, func_name)
            wiki_frame = WikiPage(container, self, name, func_name)

            self.frames[f"{name}_graph"] = graph_frame
            self.frames[f"{name}_wiki"] = wiki_frame

            graph_frame.grid(row=0, column=0, sticky="nesw")
            wiki_frame.grid(row=0, column=0, sticky="nesw")

        for F in (TestPage, StartPage, SelectPage, HelpPage, CompPage, WikiHub):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nesw")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        # parent is master (tk.Frame/tk.Tk object), controller is the
        # Sorting_Algorithm_App object which has access to show_frame

        tk.Frame.__init__(self, parent)
        
        lbl_title = tk.Label(self, text="Sorting Algorithm Explorer", font=LARGE_FONT)
        lbl_title.pack(padx=10, pady=10)

        btn_start = Menu_Button(self, text="Explore the Graphs",
                              command=lambda: controller.show_frame(SelectPage))
        btn_start.pack(pady=5)

        btn_test = Menu_Button(self, text="Test Drive An Algorithm",
                              command=lambda: controller.show_frame(TestPage))
        btn_test.pack(pady=5)

        btn_lesson = Menu_Button(self, text="Sorting Wiki",
                                 command=lambda: controller.show_frame(WikiHub))
        btn_lesson.pack(pady=5)

        btn_help = Menu_Button(self, text="Help",
                              command=lambda: controller.show_frame(HelpPage))
        btn_help.pack(pady=5)

class SelectPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        lbl_title = tk.Label(self, text="See Time Complexity Graphs", font=LARGE_FONT)
        lbl_title.pack(padx=10, pady=10)

        sorts = [i[0] for i in IMPLEMENTED_SORTS]

        # StringVar to update which option is chose in menu
        choice = tk.StringVar(self)
        choice.set(sorts[0])

        opm_opt = tk.OptionMenu(self, choice, *sorts)
        opm_opt.config(font=LIST_FONT, width=13)
        opm_opt.pack(pady=5)
        
        btn_run = Menu_Button(master=self, text="See Graph",
                            command=lambda:
                              controller.show_frame(f"{choice.get()}_graph"))
        btn_run.pack(pady=5)

        btn_comp = Menu_Button(master=self, text="Compare All",
                               command=lambda: controller.show_frame(CompPage))
        btn_comp.pack(pady=5)
        

        btn_back = Menu_Button(master=self, text="Back",
                             command=lambda: controller.show_frame(StartPage))
        btn_back.pack(pady=5)
        

class HelpPage(tk.Frame):

    INSTRUCTIONS = """Welcome to Dawson Ren's algorithm tester!\nThis program\
 is designed to be an interactive tool to \nexplore how sorting algorithms work
 and how different algorithms differ. \nSee README.txt for more information.
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl_title = tk.Label(self, text="Help Page", font=LARGE_FONT)
        lbl_title.pack(padx=10, pady=10)

        lbl_main = tk.Label(self, text=HelpPage.INSTRUCTIONS, font=SMALL_FONT)
        lbl_main.pack()

        btn_back = Menu_Button(self, text="Back",
                             command=lambda: controller.show_frame(StartPage))
        btn_back.pack()

class GraphPage(tk.Frame):

    def __init__(self, parent, controller, name, func_name):
        # mode designates whether max_values or comp_values are accessed
        tk.Frame.__init__(self, parent)

        ## Test the sorting algorithm (get their values)
        test = Algorithm_Tester(name, func_name)
        x, y = test.get_values()

        ## Create a figure
        f = Figure(figsize=(5, 5), dpi=100)
        # add_subplot(x by y, chart # z) => x = 1, y = 1, z = 1
        a = f.add_subplot(111)
        a.set_title(f"Time Complexity of {name}")
        a.set_xlabel("Length of List")
        a.set_ylabel("Seconds to Sort")
        a.plot(x, y)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack()
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        btn_back = Menu_Button(self, text="Back",
                             command=lambda: controller.show_frame(SelectPage))
        btn_back.pack()

class TestPage(tk.Frame):
    # chooses a specific algorithm and tests it

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        # configure overall grid pattern
        self.rowconfigure([i for i in range(6)], weight=1)

        self.columnconfigure(0, minsize=100)
        lbl_title = tk.Label(self, text="Algorithm Tester", font=LARGE_FONT)
        lbl_title.grid(row=0, column=0, sticky="ew")

        sorts = [i[0] for i in IMPLEMENTED_SORTS]

        # StringVar to update which option is chose in menu
        choice = tk.StringVar(self)
        choice.set(sorts[0])

        # OptionMenu
        self.columnconfigure(0)
        opm_opt = tk.OptionMenu(self, choice, *sorts)
        opm_opt.config(font=LIST_FONT, width=13)
        opm_opt.grid(row=1, column=0)

        # frame for entry
        self.columnconfigure(0, minsize=150)
        frm_ent = tk.Frame(self)
        frm_ent.grid(row=2, column=0, sticky="ew")

        # StringVar for length of list, how many times, and resulting test time.
        length = tk.StringVar()
        times = tk.StringVar()
        testtime = tk.StringVar()

        # Displays "Test the algorithm _ times, and repeat _ times."
        lbl_test = tk.Label(frm_ent, text="Sort list a list of length", font=SMALL_FONT)
        lbl_test.pack(side=tk.LEFT, padx=5, pady=5)
        ent_len = tk.Entry(frm_ent, text="2000", textvariable=length, font=SMALL_FONT)
        # default is list len 2000
        ent_len.insert(tk.END, "2000")
        ent_len.pack(side=tk.LEFT, padx=5, pady=5)
        lbl_len = tk.Label(frm_ent, text=", ", font=SMALL_FONT)
        lbl_len.pack(side=tk.LEFT, padx=5, pady=5)
        ent_times = tk.Entry(frm_ent, text="10", textvariable=times, font=SMALL_FONT)
        # default is 10 times
        ent_times.insert(tk.END, "10")
        ent_times.pack(side=tk.LEFT, padx=5, pady=5)
        lbl_times = tk.Label(frm_ent, text=" times.", font=SMALL_FONT)
        lbl_times.pack(side=tk.LEFT, padx=5, pady=5)

        # frame for result
        self.columnconfigure(0, minsize=150)
        frm_result = tk.Frame(self)
        frm_result.grid(row=3, column=0, sticky="ew")
        
        lbl_result = tk.Label(frm_result, text="The test took ", font=SMALL_FONT)
        lbl_result.pack(side=tk.LEFT, padx=5, pady=5)
        lbl_tm = tk.Label(frm_result, text=" ", textvariable=testtime, font=SMALL_FONT)
        lbl_tm.pack(side=tk.LEFT, padx=5, pady=5)
        lbl_sec = tk.Label(frm_result, text=" seconds.", font=SMALL_FONT)
        lbl_sec.pack(side=tk.LEFT, padx=5, pady=5)

        def run_test(event):
            # find the func_name associated with choice.get(), or the name
            name = choice.get()
            func_name = [tup[1] for tup in IMPLEMENTED_SORTS if name == tup[0]][0]

            try:
                l = int(length.get())
                t = int(times.get())
                
            except ValueError:
                testtime.set("N/A")
                return

            timing = Algorithm_Tester(name, func_name).run(num=l, repeat=t)
            testtime.set(f"{timing:.4f}")
            
        # run and back button frame
        self.columnconfigure(0, minsize=50)
        frm_btn = tk.Frame(self)
        frm_btn.grid(row=4, column=0)
        
        btn_run = Menu_Button(frm_btn, text="Run")
        btn_run.bind("<Button-1>", run_test)
        btn_run.pack(side=tk.LEFT)

        btn_back = Menu_Button(frm_btn, text="Back",
                               command=lambda: controller.show_frame(StartPage))
        btn_back.pack(side=tk.LEFT)

class CompPage(tk.Frame):
    # compares all of the sorts in one page

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.set_title(f"Comparing Sorting Algorithms")
        a.set_xlabel("Length of List")
        a.set_ylabel("Seconds to Sort")

        # list of possible colors
        colors = ["black", "gray", "lightcoral", "maroon", "darkorange", "gold",
                  "chartreuse", "darkgreen", "turquoise", "aqua", "steelblue",
                  "royalblue", "darkorchid", "deeppink"]

        # legend data
        patches = []

        # iterate through sorting algorithms, collecting their comp_values
        for i, tup in enumerate(IMPLEMENTED_SORTS):
            # unpack the tuple
            name, func_name = tup
            
            # use mode not 0 to get comp_values
            test = Algorithm_Tester(name, func_name)
            x, y = test.get_values(mode = 1)
            line = a.plot(x, y, c=colors[i])

            # insert the line on the legend
            legend_entry = mpatches.Patch(color=colors[i], label=f"{name}")
            patches.append(legend_entry)
        
        # create legend
        a.legend(handles=patches)

        # draw the graph
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # display the toolbar
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        btn_back = Menu_Button(self, text="Back",
                             command=lambda: controller.show_frame(SelectPage))
        btn_back.pack()

class WikiHub(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        lbl_title = tk.Label(self, text="Sorting Wiki", font=LARGE_FONT)
        lbl_title.pack(pady=5)

        # frame to hold buttons that redirect to LessonPage
        frm_hub = tk.Frame(self)
        frm_hub.pack()

        # configure grid layout
        frm_hub.columnconfigure([i for i in range(3)], weight=1, minsize=15)
        frm_hub.rowconfigure([i for i in range(4)], weight=1, minsize=5)

        btn_list = []

        # first instantiate and grid all of the buttons

        for i, name in enumerate([i[0] for i in IMPLEMENTED_SORTS]):
            row = i // 4
            column = i % 4

            btn_wiki = Menu_Button(frm_hub, text=name)

            btn_list.append(btn_wiki)

            btn_wiki.grid(row=row, column=column, sticky="nesw",
                             padx=3, pady=3)

        # odd bug -- doesn't work with for loop, so I had to hard-code it
        btn_list[0]["command"] = lambda: controller.show_frame("Python sorted()_wiki")
        btn_list[1]["command"] = lambda: controller.show_frame("List.sort()_wiki")
        btn_list[2]["command"] = lambda: controller.show_frame("Insertion Sort_wiki")
        btn_list[3]["command"] = lambda: controller.show_frame("Selection Sort_wiki")
        btn_list[4]["command"] = lambda: controller.show_frame("Bubble Sort_wiki")
        btn_list[5]["command"] = lambda: controller.show_frame("Merge Sort_wiki")
        btn_list[6]["command"] = lambda: controller.show_frame("Heap Sort_wiki")
        btn_list[7]["command"] = lambda: controller.show_frame("Quick Sort_wiki")

        btn_back = Menu_Button(self, text="Back",
                             command=lambda: controller.show_frame(StartPage))
        btn_back.pack()

class WikiPage(tk.Frame):

    def __init__(self, parent, controller, name, func_name):
        
        tk.Frame.__init__(self, parent)

        content = Wiki_Formatter(name, func_name, self)
        content.pack(fill=tk.BOTH, expand=True)

        btn_back = Menu_Button(self, text="Back",
                             command=lambda: controller.show_frame(WikiHub))
        btn_back.pack()

def main():
    run = Sorting_Algorithm_App()
    run.mainloop()

