from get_data import get_players_data
from get_data import get_curry_data
import pandas as pd
#import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
URL_PLAYERS = 'https://www.espn.com/nba/stats/player/_/season/2022/seasontype/2' # webpage
URL_CURRY = "https://api-nba-v1.p.rapidapi.com/players/statistics" # API

if __name__ == '__main__':
    file_players = get_players_data(URL_PLAYERS)
    file_curry_2021, file_curry_2022 = get_curry_data(URL_CURRY)
    # read the files as dataframes
    df_players = pd.read_csv('../data/'+file_players, sep=',', header=0)
    df_curry_2021 = pd.read_csv('../data/'+file_curry_2021, sep=',', header=0)
    df_curry_2022 = pd.read_csv('../data/'+file_curry_2022, sep=',', header=0)


    # 1st plot
    df_players = df_players.drop(['RK'], axis=1)
    corr_matrix = df_players.corr()
    fig1, ax1 = plt.subplots(figsize=(10,10))
    sns.heatmap(corr_matrix, ax=ax1, annot=True, fmt=".1f")
    plt.title("The pairwise correlation of features", fontdict={'fontsize': 8})
    plt.savefig('../heatmap')
    # 2nd plot
    fig2, ax2 = plt.subplots(figsize=(7,5))
    sns.histplot(data=df_players, x="PTS", hue="POS", element="poly", ax=ax2)
    plt.title("The distribution of points of players from different positions", fontdict={'fontsize': 8})
    plt.savefig('../histplot')
    # 3nd plot
    df_curry_2021 = df_curry_2021[df_curry_2021['min']!='0:00']
    new_column = []
    for i in range(len(df_curry_2021)):
        if df_curry_2021.iloc[i]['points']<20:
            new_column.append('<20')
        elif df_curry_2021.iloc[i]['points']>=20 and df_curry_2021.iloc[i]['points']<30:
            new_column.append('20-30')
        elif df_curry_2021.iloc[i]['points']>=30 and df_curry_2021.iloc[i]['points']<40:
            new_column.append('30-40')
        elif df_curry_2021.iloc[i]['points']>=40 and df_curry_2021.iloc[i]['points']<50:
            new_column.append('40-50')
        else:
            new_column.append('>=50')
    PTS_range_count = [new_column.count('<20'), new_column.count('20-30'), new_column.count('30-40'), 
                    new_column.count('40-50'), new_column.count('>=50')]
    labels = ['<20pts', '20-30pts', '30-40pts', '40-50pts', '>=50pts']
    explode = [0.02,0.27,0.02,0.02,0.02]
    colors = sns.color_palette("pastel")
    fig3, ax3 = plt.subplots(figsize=(6,6))
    plt.title("The percentage of Stephen Curry's points segment per game in 2021-22 season", fontdict={'fontsize': 8})
    ax3.pie(PTS_range_count, colors=colors, labels=labels,explode=explode, autopct='%.2f%%', shadow=True)
    plt.savefig('../pieplot')

