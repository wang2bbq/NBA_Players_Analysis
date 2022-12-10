from get_data import get_players_data
from get_data import get_curry_data
from analyze_data import feature_correlation_analysis
from analyze_data import get_top_5
from analyze_data import find_best_k
from analyze_data import plot_k_means_5
from analyze_data import plot_pie_chart
from analyze_data import plot_line
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
import plotly.graph_objects as go
import pandas as pd
import numpy as np
#import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import plotly.express as px
URL_PLAYERS = 'https://www.espn.com/nba/stats/player/_/season/2022/seasontype/2' # webpage
URL_CURRY = "https://api-nba-v1.p.rapidapi.com/players/statistics" # API

if __name__ == '__main__':
    file_players = get_players_data(URL_PLAYERS)
    file_curry_2021, file_curry_2022 = get_curry_data(URL_CURRY)
    # read the files as dataframes
    df_players = pd.read_csv('../data/'+file_players, sep=',', header=0)
    df_curry_2021 = pd.read_csv('../data/'+file_curry_2021, sep=',', header=0)
    df_curry_2022 = pd.read_csv('../data/'+file_curry_2022, sep=',', header=0)

    # Analysis 1
    heatmap_path = feature_correlation_analysis(df_players)
    # Analysis 2
    df_pts = get_top_5(df_players, 'PTS')
    df_reb = get_top_5(df_players, 'REB')
    df_ast = get_top_5(df_players, 'AST')
    # Analysis 3(find best k)
    # Feature Preprocessing
    to_drop = ['RK','Name','POS','GP']
    X = df_players.drop(to_drop, axis=1) # dropping useless feature
    # Standardized attributes
    scaler1 = StandardScaler()
    X_standard = scaler1.fit_transform(X)
    X_standard = pd.DataFrame(X_standard, columns=X.columns)
    best_k1, best_k2, model_1, model_2 = find_best_k(X_standard)
    # Analysis 4(k=5)
    clusters_5_path = plot_k_means_5(df_players,X_standard)
    # Analysis 5
    pie_path = plot_pie_chart(df_curry_2021)
    # Analysis 6
    line_path = plot_line(df_curry_2021, df_curry_2022)
