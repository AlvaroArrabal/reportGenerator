import pandas as pd
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from modules import getQueryData

def create_graph(cell, nameKPI):

    df = getQueryData.get4G(cell[0])
    data = df.loc[:,["Date",nameKPI]]
    data["Date"] = pd.to_datetime(data["Date"])

    fig, ax = plt.subplots(1,1,figsize=(13,8))

    ax.plot(data["Date"], data[nameKPI])
    fig.autofmt_xdate()

    xfmt = mdates.DateFormatter('%m/%d-%H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    ax.grid()
    ax.set_title(cell[0])
    ax.set_ylabel(nameKPI)
    ax.set_xlabel("Date")

    graphname = ".\\graphs\\" + cell[0] + "-" + nameKPI + ".png"

    fig.savefig(graphname)