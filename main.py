import scraper as scrape
import points_file as pf
import pandas as pd
import season_points as sp

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)


print('''Welcome! There are a few commands that work:
        Note: They are not case-sensitive
        Make Points: Allows to create a points system
        Make Standings: Generates points standings
        Export: exports standings to an excel sheet
        Import: imports standings from an excel sheet
        Print: View Standings
        Note: You will need bs4 and pandas installed for this to work
        Another Note: if mistake happens, program will tell you or return
        an empty dataframe''')


n = ''
points = ''
series = ''
year = 0
table = pd.DataFrame()
while n.upper() != "Q":
    n = input("Enter command: ")

    if n.upper() == "MAKE POINTS":
        pf.create_points()
        
    elif n.upper() == "MAKE STANDINGS":
        print('''options:
                Cup (W)
                Xfinity (B)
                Trucks (C)
                ARCA West (AW)
                K&N West (P)
                ARCA East (AE)
                K&N East (E)
                ARCA (A)
                Modifieds (N)
                F1 (F)
                Weathertech (TU)
                Pinty's (T)
                Formula E (FE)
                V8 Supercars (V8)''')
        series = input("Choose a key: ")
        
        try:
            year = int(input('select year: '))
        except ValueError:
            print("must be an integer")
        
        points = input("enter system name: ")

        try:
            table = sp.calculate(points,series.upper(),year)
            print(table)
        except FileNotFoundError:
            print("points not found")
        
    elif n.upper() == "EXPORT":
        sp.to_excel(table)
        
    elif n.upper() == "IMPORT":
        name = input("Enter File Name: ")
        
        try:
            sp.from_excel(name)
        except FileNotFoundError:
            print("File does not exist")

    elif n.upper() == "PRINT":
        print(table)
                
                
                
        
