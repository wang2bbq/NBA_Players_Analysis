import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.decomposition import PCA
import plotly.express as px
import plotly.graph_objects as go
# Analysis 1
def feature_correlation_analysis(x):
    """
    Find the correlation between features(statistics such as PTS, FGM, REB, AST, STL, BLK...)

    Args:
        x - data(n_samples, m_features)

    Returns:
        file_heatmap: the path for heatmap
    """
    X_1 = x.drop(['RK','Name','POS','GP'], axis=1)
    corr_matrix = X_1.corr()
    fig1, ax1 = plt.subplots(figsize=(12,12))
    sns.heatmap(corr_matrix, ax=ax1, annot=True, fmt=".1f")
    plt.title("The pairwise correlation of features", fontdict={'fontsize': 11})
    plt.savefig('../result/heatmap.pdf')
    file_heatmap = '../result/heatmap.pdf'
    return file_heatmap

# Analysis 2
def get_top_5(x, statistic):
    """
    Get the TOP 5 players using one statistic such as PTS, FGM, REB, AST, STL, BLK...

    Args:
        x - data(n_samples, m_features)
        statistic - PTS, FGM, REB, AST, STL, BLK...

    Returns:
        df_output: a dataframe of TOP 5 players'name and performance
    """
    dic_output = {}
    df_sort = x.sort_values(by=statistic, ascending=False)
    df_sort.index = range(len(df_sort))
    name = list(df_sort.loc[0:4, 'Name'])
    performance = list(df_sort.loc[0:4,statistic])
    dic_output['Player'] = name
    dic_output[statistic] = performance
    df_output = pd.DataFrame(dic_output)
    return df_output

# Analysis 3 (clustering)
def find_best_k(x):
    """
    Find the best k from {1,2,3,...,50} in k-means using Silhouette and CH index

    Args:
        x - data(n_samples, m_features)

    Returns:
        best_k1: the k selected by Silhouette
        best_k2: the k selected by CH index
        model_1: best model selected by Silhouette
        model_2: best model selected by CH index
    """
    dic_models = {}
    dic_silhouette = {}
    dic_ch = {}
    for k in range(1,51): # choose best k from {1,2,3,...,50}
        if k == 1:
            pass
        else:
            kmeans = KMeans(n_clusters=k, init='random', n_init=20).fit(x) # run the k-means algorithm n_init times
            dic_models[k] = kmeans
            dic_silhouette[k] = silhouette_score(x, labels=kmeans.labels_)
            dic_ch[k] = calinski_harabasz_score(x, labels=kmeans.labels_)
    sorted_silhouette = sorted(dic_silhouette.items(), key=lambda x:x[1], reverse=True)
    sorted_ch = sorted(dic_ch.items(), key=lambda x:x[1], reverse=True)
    best_k1 = sorted_silhouette[0][0]
    best_k2 = sorted_ch[0][0]
    model_1 = dic_models[best_k1]
    model_2 = dic_models[best_k2]
    return best_k1, best_k2, model_1, model_2

# Analysis 4 (clustering)
# use k-means to get 5 clusters(5 positions on the basketball court)
def plot_k_means_5(df,x):
    """
    Perform k-means when k = 5

    Args:
        df - raw data
        x - Standardized data

    Returns:
        file_5_clusters: the path for clustering results
    """
    kmeans_5 = KMeans(n_clusters=5, init='random', n_init=20).fit(x)
    labels_5 = kmeans_5.labels_
    #Transform the data
    pca = PCA(2)
    X_standard_pca = pca.fit_transform(x)
    dic_results_pca = {}
    dic_results_pca['Name'] = df['Name']
    dic_results_pca['PTS'] = df['PTS']
    dic_results_pca['POS'] = df['POS']
    dic_results_pca['Cluster'] = labels_5
    dic_results_pca['pca1'] = X_standard_pca[:,0]
    dic_results_pca['pca2'] = X_standard_pca[:,1]
    df_results_pca = pd.DataFrame(dic_results_pca)

    fig2 = px.scatter(df_results_pca, x="pca1", y="pca2",
               size="PTS", color="Cluster", hover_name="Name",size_max=15)
    fig2.write_html("../result/players_5_clusters.html")
    file_5_clusters = '../result/players_5_clusters.html'
    return file_5_clusters

# Analysis 5
def plot_pie_chart(df):
    """
    Plot pie chart of the percentage of Stephen Curry's points segment per game in 2021-22 season

    Args:
        df - raw data for season 2021-22

    Returns:
        file_pie: the path for pie chart
    """
    df_curry_2021_play = df[df['min'] != '0:00']
    df_curry_2021_play['game'] = list(range(1,len(df_curry_2021_play)+1))
    new_column = []
    for i in range(len(df_curry_2021_play)):
        if df_curry_2021_play.iloc[i]['points']<20:
            new_column.append('<20')
        elif df_curry_2021_play.iloc[i]['points']>=20 and df_curry_2021_play.iloc[i]['points']<30:
            new_column.append('20-30')
        elif df_curry_2021_play.iloc[i]['points']>=30 and df_curry_2021_play.iloc[i]['points']<40:
            new_column.append('30-40')
        elif df_curry_2021_play.iloc[i]['points']>=40 and df_curry_2021_play.iloc[i]['points']<50:
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
    plt.savefig('../result/pie.pdf')
    file_pie = '../result/pie.pdf'
    return file_pie

# Analysis 6
def plot_line(df1, df2):
    """
    Plot line chart of Stephen Curry's Points Scored per game in 2021-22 season and 2022-23 season

    Args:
        df1 - raw data for season 2021-22
        df2 - raw data for season 2022-23

    Returns:
        file_pie: the path for pie chart
    """
    df_curry_2021_play = df1[df1['min'] != '0:00']
    df_curry_2021_play['game'] = list(range(1,len(df_curry_2021_play)+1))
    df_curry_2022_play = df2[df2['min'] != '0:00']
    df_curry_2022_play['game'] = list(range(1,len(df_curry_2022_play)+1))
    # Create traces
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=df_curry_2021_play['game'], y=df_curry_2021_play['points'],
                        mode='lines',
                        name='points(2021)'))
    fig4.add_trace(go.Scatter(x=df_curry_2022_play['game'], y=df_curry_2022_play['points'],
                        mode='lines+markers',
                        name='points(2022)'))
    fig4.write_html("../result/PTS_line.html")
    file_line = '../result/PTS_line.html'
    return file_line
