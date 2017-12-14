#Imports
import csv
import tkinter as tk

#import custom modules
from header import *
from census1850 import *
from census1860 import *
from census1870 import *
from census1880 import *
from census1900 import *
from census1910 import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.create_widgets()


    def create_widgets(self):

        #dictionary of countries
        self.dict = {'United States': ['1850', '1860', '1870'],
                    'England': ['1', '2', '3'],
                    'Sweden':['1','2','3']}
        
        #label for country selector
        countryLabel = tk.Label(self, text="Select a country:")
        #render on left side of screen
        countryLabel.grid(row = 0)
        

        #label for year selector
        countryLabel = tk.Label(self, text="Select a census year:")
        #render on left side of screen
        countryLabel.grid(row = 1)

        
        #country selector
        self.countrySelect = tk.StringVar(self)
        #year selector
        self.yearSelect = tk.StringVar(self)
        #checkbox 1
        self.optionImmigration = tk.IntVar(self)
        #checkbox 2
        self.optionOccupation = tk.IntVar(self)


        #update year select based on country select
        self.countrySelect.trace('w', self.update_options)
        


        #render the country options menu
        self.countryOptions = tk.OptionMenu(self, self.countrySelect, *self.dict.keys())
        self.yearOptions = tk.OptionMenu(self, self.yearSelect, '')


        #set United States as the default value
        self.countrySelect.set("United States")

        #render on right side of widget
        self.countryOptions.grid(row = 0, column = 1)
        self.yearOptions.grid(row=1,column=1)

        # #renders a separation line between widgets
        # separator = tk.Frame(height=2, bd=1, relief= tk.SUNKEN)
        # separator.pack(fill= tk.X, padx=5, pady=5)

        #checkbutton widgets

        #Immigration
        self.CheckboxImmigration = tk.Checkbutton(self, text="Immigration Year", variable=self.optionImmigration)
        self.CheckboxImmigration.grid(row=2)
        
        #Occupation
        self.CheckboxOccupation = tk.Checkbutton(self, text="Occupation", variable=self.optionOccupation)
        self.CheckboxOccupation.grid(row=2,column=1)


        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                             command=root.destroy)
        self.quit.grid(row =5, column =2)



    #update options list of years
    def update_options(self, *args):
        countries = self.dict[self.countrySelect.get()]
        self.yearSelect.set(countries[0])

        menu = self.yearOptions['menu']
        menu.delete(0, 'end')

        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: self.yearSelect.set(nation))

        if self.countrySelect.get()=='United States':
            #dictionary of options
            self.dict2 ={'1850':['option 1','option 2', 'option 3'],'1860':['2 option','3 option', '4 option']}
            return self.dict2

    


root = tk.Tk()
root.minsize(200, 200)
app = Application(master=root)
app.mainloop()

def main (g, y):

    g = str(g +'.ged')
    printHeader(g)
    if y == '1850':
        writeName1850(file_path , g)
    elif y == '1860':
        writeName1860(file_path , g)
    elif y == '1870':
        writeName1870(file_path , g)
    elif y == '1880':
        writeName1880(file_path , g)
    elif y == '1900':
        writeName1900(file_path , g)
    elif y == '1910':
        writeName1910(file_path, g)

    else:
        pass
       
       
try:   
    main(fieldValuesgedname, fieldValuesyear)
except:
    pass
