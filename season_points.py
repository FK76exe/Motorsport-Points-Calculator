import scraper as scrape
import points_file as points
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)

def calculate(system,series,year):

    #make points
    p_s = points.dictmaker(points.open_points(system))

    limit = scrape.season_length(series,year) #no_of_races
    racedata = pd.DataFrame(columns=["Fin","St","Driver","Laps_Led","Index"])

    for race in range(1,int(limit)+1):
        if race >= 10:
            for row in scrape.matrix_maker("https://www.racing-reference.info/race?s=1&series={}&id={}-{}".format(series,str(year),str(race))):
                row.append(str(year)+'-'+str(race))
                racedata.loc[len(racedata)] = row
        else:
            for row in scrape.matrix_maker("https://www.racing-reference.info/race?s=1&series={}&id={}-0{}".format(series,str(year),str(race))):
                row.append(str(year)+'-0'+str(race))
                #print(row)
                racedata.loc[len(racedata)] = row

    racedata['Laps_Led'] = pd.to_numeric(racedata.Laps_Led,errors='coerce')
    racedata['St'] = pd.to_numeric(racedata.St,errors='coerce')


    #racedata contains all race data; now create another database
    points_standings = pd.DataFrame(columns=["Name","Points","Points Races"])
    drivers = racedata.Driver.unique()
    for name in drivers:
        total = 0 #total = number of points
        fin,st,lap,most = p_s
        num_races = 0
        driver_data = racedata[racedata['Driver']==name]
        for x in driver_data.index:
            
            race = driver_data.loc[x]
            
            if (race['Fin'] != " " and race['Fin'].isdigit() and int(race['Fin']) <= len(fin)):
                total += fin[race['Fin']]
                num_races += 1

            if pd.isna(race['St']) == False:
                if int(race['St']) <= len(st):
                    total += int(race['St'])
                
            if (race['Laps_Led'] > 0):
                total += lap
                
            if race['Laps_Led'] == racedata[racedata['Index']==race['Index']]['Laps_Led'].max():
                total += most
            
        points_standings.loc[len(points_standings)+1] = [name,total,num_races]

    points_standings = points_standings.sort_values('Points',ascending=False).reset_index(drop=True)
    points_standings.index = points_standings.index +1
    return points_standings

def to_excel(table):
    name = input("Enter name for file (don't include extension): ")
    table.to_excel('excel/{}.xlsx'.format(name),sheet_name='Standings')

def from_excel(name):
    return pd.read_excel('excel/'+name+'.xlsx',index_col = 0)
