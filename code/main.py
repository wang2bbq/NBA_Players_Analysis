from get_data import get_players_data
from get_data import get_curry_data
from analyze_data import feature_correlation_analysis
from analyze_data import get_top_5
from analyze_data import find_best_k
from analyze_data import plot_k_means_5
from analyze_data import plot_pie_chart
from analyze_data import plot_line
from sklearn.preprocessing import StandardScaler
import pandas as pd

URL_PLAYERS = 'https://www.espn.com/nba/stats/player/_/season/2022/seasontype/2' # webpage
URL_CURRY = "https://api-nba-v1.p.rapidapi.com/players/statistics" # API

if __name__ == '__main__':
    file_players = get_players_data(URL_PLAYERS)
    file_curry_2021, file_curry_2022 = get_curry_data(URL_CURRY)
    # read the files as dataframes
    df_players = pd.read_csv('../data/'+file_players, sep=',', header=0)
    df_curry_2021 = pd.read_csv('../data/'+file_curry_2021, sep=',', header=0)
    df_curry_2022 = pd.read_csv('../data/'+file_curry_2022, sep=',', header=0)

# For the dataset of all players
    # Analysis 1
    heatmap_path = feature_correlation_analysis(df_players)
    print("The heatmap of correlation between statistics:", heatmap_path)

    # Analysis 2
    df_pts = get_top_5(df_players, 'PTS')
    df_reb = get_top_5(df_players, 'REB')
    df_ast = get_top_5(df_players, 'AST')
    df_stl = get_top_5(df_players, 'STL')
    df_blk = get_top_5(df_players, 'BLK')
    print("POINTS Leaders:")
    print(df_pts)
    print("REBOUNDS Leaders:")
    print(df_reb)
    print("ASSISTS Leaders:")
    print(df_ast)
    print("STEALS Leaders:")
    print(df_stl)
    print("BLOCKS Leaders:")
    print(df_blk)

    # Analysis 3 (find best k in k-means)
    # Feature Preprocessing
    to_drop = ['RK','Name','POS','GP']
    X = df_players.drop(to_drop, axis=1) # dropping useless feature
    # Standardized attributes
    scaler1 = StandardScaler()
    X_standard = scaler1.fit_transform(X)
    X_standard = pd.DataFrame(X_standard, columns=X.columns)
    best_k1, best_k2, clusters_best_k_path = find_best_k(df_players, X_standard)
    if best_k1 == best_k2:
        print("The best k is "+str(best_k1)+". The players are clustered into "+str(best_k1)+" clusters.")
    else:
        print("The players are clustered into "+str(best_k1)+" clusters(based on Silhouette).")
        print("The players are clustered into "+str(best_k2)+" clusters(based on CH index).")
    print("The clustering result for the best k:", clusters_best_k_path)

    # Analysis 4 (k=5 in k-means)
    clusters_5_path = plot_k_means_5(df_players,X_standard)
    print("The clustering result for k=5:", clusters_5_path)

# For the dataset of Stephen Curry
    # Analysis 5
    pie_path = plot_pie_chart(df_curry_2021)
    print("The pie chart for Stephen Curry's Points Scored in season 2021-22:", pie_path)

    # Analysis 6
    line_path_PTS, line_path_fgp = plot_line(df_curry_2021, df_curry_2022)
    print("The line chart of Stephen Curry's Points Scored in season 2021-22 and 2022-23:", line_path_PTS)
    print("The line chart of Stephen Curry's Field Goals Percentage in season 2021-22 and 2022-23:", line_path_fgp)
