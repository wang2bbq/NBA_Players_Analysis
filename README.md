# Final_Project_510_huiqi_wang
This is the final project to analyze the best players in NBA 2021-22 regular season, cluster all the players to gain insights for player training and trading, and assess FMVP Stephen Curry's ability and competition status in 2021-22 and 2022-23.

# Dependencies
pandas
requests
BeautifulSoup
seaborn
matplotlib.pyplot
plotly.express
plotly.graph_objects
...
# Installattion

```
pip freeze > requirements.txt
```

# Running the project

```
python main.py
```

# Methodology
- For dataset of all players:
- Exploratory data analysis:
    - Analyze the correlation between features(statistics such as PTS, FGM, REB, AST, STL, BLK...) and plot heatmap
    - Find the TOP 5 players using one statistic such as PTS, FGM, REB, AST, STL, BLK...
- K-means clustering
    - Find the best k from {1,2,3,...,50} for players using Silhouette and CH index
    - Perform k-means using k = 5 to get 5 clusters(5 positions on the basketball court) and plot scatter chart of clustering results using plotly.express (By clicking a certain point with the mouse, the relevant clustering information can be displayed, and the players in the same cluster can be intuitively seen.)

- For dataset of Stephen Curry:
- Exploratory data analysis:
    - Analyze Stephen Curry's scoring ability(find the percentage of Stephen Curry's points scored segment per game in 2021-22 season) and plot pie chart
    - Find Stephen Curry's Points Scored per game trend in 2021-22 season and 2022-23 season and plot line chart using plotly.graph_objects (By clicking a point with the mouse, we can visually see how many points Curry scored in which game.)

# Visualization
- From the heat map, we can see that PTS(Points Scored) is strongly correlated with AST(Assists) and FTA(Free Throws Attempted) is strongly correlated with REB(Total Rebounds). So, AST and REB are important for players to score.
- The best k selected by the metrics is 2. The two clusters represents two groups of players of different ability levels.
- From the scatter chart results of k-means(k=5), the five clusters give five groups of players. We can see that Stephen Curry, Paul George and Kyrie Irving are from same cluster, and Kevin Durant, Trae Young and James Harden are from the same cluster, which means they have similar performances. 
For team managers, they can trade players from the same cluster so that the team structure won’t change much and it may be good for a new player to integrate into the team.
For coaches and trainers, they can learn from the training methods and playing patterns of the players from the same cluster. It's good for players to develop better.

- From the pie chart showing Stephen Curry's points segment in all games in season 2021-22, we can see that he often got points per game in the 20-30 range.
- From the first 20+ games of the line chart, we can see that Stephen Curry’s points scored per game has been a little more steady in 2022-23 season than 2021-22 season.

# Future Work


