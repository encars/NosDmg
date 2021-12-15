import dataframe
import time
import threading
from tkinter import Tk, Label, Button, ttk, Scrollbar
from dataframe import *
from launcher import exitProgram
import settings


root = Tk()


def guiSetup(master):
    master = master
    master.title('Dmg Calculator')
    master.geometry('1000x500')

    treeframe = ttk.LabelFrame(master)
    treeframe.place(width=800, height=300)

    global tree
    tree = ttk.Treeview(treeframe)
    colNames = ['Name', 'Dmg', 'Max dmg', 'Hits', 'Crits', 'Crit chance', 'Miss', 'Dmg taken', 'Max dmg taken']
    tree['columns'] = colNames
    tree['show'] = 'headings'

    for column in colNames:
        tree.heading(column, text=column)
        tree.column(column, width=125, stretch=False)
    
    tree.place(relheight=1, relwidth=1)
    
    scrollVert = Scrollbar(treeframe, orient='vertical', command=tree.yview)
    scrollVert.pack(side='right', fill='y')

    scrollHoz = Scrollbar(treeframe, orient='horizontal', command=tree.xview)
    scrollHoz.pack(side='bottom', fill='x')
    tree.configure(xscrollcommand=scrollHoz.set, yscrollcommand=scrollVert.set)

    refresh = Button(master, text='Refresh', command=refreshData)
    refresh.place(x=810, y=7, height=100, width=180)

    clear = Button(master, text='Clear', command=clearData)
    clear.place(x=810, y=110, height=50, width=180)

    global bossModeButton
    bossModeButton = Button(master, text='Boss only: OFF', command=setBossMode)
    bossModeButton.place(x=810, y=175, height=50, width=180)

    global autoRefreshButton
    autoRefreshButton = Button(master, text='Auto refresh: OFF', command=setRefresh)
    autoRefreshButton.place(x=810, y=228, height=50, width=180)

    global fishingButton
    fishingButton = Button(master, text='Fishing Bot: OFF', command=setFishing)
    fishingButton.place(x=10, y=310, height=180, width=180)

    quitButton = Button(master, text='Exit', command=kill)
    quitButton.place(x=940, y=440, height=50, width=50)


def loadData():
    data = dataframe.playerList
    if not data:
        pass
    else:
        for player in data:
            tree.insert('', 'end', values=[player.name, player.damage, player.max_damage, player.hits, player.crits, player.calculateCrit(), player.miss, player.taken, player.max_taken])


def refreshData():
    tree.delete(*tree.get_children())
    loadData()
    sortList()


def clearData():
    tree.delete(*tree.get_children())
    clearList()


def setBossMode():
    settings.BOSSMODE = not settings.BOSSMODE
    if settings.BOSSMODE:
        bossModeButton.configure(text='Boss only: ON')
    else:
        bossModeButton.configure(text='Boss only: OFF')


def setRefresh():
    settings.REFRESH = not settings.REFRESH
    if settings.REFRESH:
        autoRefreshButton.configure(text='Auto refresh: ON')
        threading.Thread(target=autoRefresh).start()
    else:
        autoRefreshButton.configure(text='Auto refresh: OFF')


def setFishing():
    settings.FISHING = not settings.FISHING
    if settings.FISHING:
        fishingButton.configure(text='Fishing Bot: ON')
    else:
        fishingButton.configure(text='Fishing Bot: OFF')


def autoRefresh():
    while settings.REFRESH:
        refreshData()
        time.sleep(10)


def runGui():
    guiSetup(root)
    root.mainloop()


def kill():
    root.destroy()
    exitProgram()