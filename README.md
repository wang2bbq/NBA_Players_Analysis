# NBA Players Analysis
This is the final project to analyze the best players in NBA 2021-22 regular season, find the correlation between NBA statistics, cluster all the players to gain insights for player trading and player training, and assess FMVP Stephen Curry's scoring ability and competition state in season 2021-22 and 2022-23.

# Dependencies
- requests
- BeautifulSoup
- matplotlib.pyplot
- seaborn
- plotly.express
- plotly.graph_objects
- pandas
- KMeans
- silhouette_score
- calinski_harabasz_score
- PCA
- StandardScaler

# Installation
```
pip install -r requirements.txt
```

# Running the project
```
cd code
python main.py
```

# Data collection
- Collected NBA players’ average performance per game data in 2021-22 regular season from the webpage https://www.espn.com/nba/stats/player/_/season/2022/seasontype/2
- Collected FMVP Stephen Curry’s per game stats in season 2021-22 and 2022-23 from the “Players Statistics per player and season” API on https://rapidapi.com/api-sports/api/api-nba
- When web parsing, I used the CSS selector 'thead.Table__header-group tr' and 'tbody.Table__TBODY tr' to select rows of the header and data, and found ‘td’ to get specific data, and wrote it into a CSV file
- For API, I used query string including parameter “id” and “season”. The data is in JSON format and I transformed it into the python dictionary and wrote it into 2 CSV files using the keys such as ‘response'
- There are 581 instances and 22 features in the dataset of all players. In the dataset of Stephen Curry in season 2021-22, there are 92 instances and 22 features. In the dataset of Stephen Curry in season 2022-23, there are 28 instances and 22 features

# Methodology
- For dataset of all players:
    - Analyze the correlation between NBA statistics such as PTS, FGM, REB, AST, STL, BLK, etc. The result is displayed in a heat map
    - Find the TOP 5 players in every aspect using one statistic such as PTS, FGM, REB, AST, STL, BLK, etc. The result is printed
    - K-means clustering
      - Find the best k from {1,2,3,...,50} using Silhouette and CH index. The result is displayed in a scatter chart using plotly.express
      - Perform k-means clustering using k = 5 based on the 5 positions on the basketball court. The result is displayed in a scatter chart using plotly.express
- For dataset of Stephen Curry:
    - Analyze Stephen Curry's scoring ability(find the percentage of Stephen Curry's Points Scored in season 2021-22). The result is displayed in a pie chart
    - Analyze Stephen Curry's competition state(find Stephen Curry's Points Scored and Field Goals Percentage per game trend in season 2021-22 and 2022-23). The results are displayed in two line charts using plotly.graph_objects

# Visualization
- For dataset of all players:
  - From the heat map, we can see that PTS(Points Scored) is strongly correlated with AST(Assists). When a player's assists increase, it means that the team is coordinating better in offense, so it becomes easier for the player to score. And FTA(Free Throws Attempted) is strongly correlated with REB(Total Rebounds), which means that if a player is more active in fighting for rebounds, he is likely to get more free throws. Therefore, AST and REB are important for players.
  - From the TOP5 analysis, we can see that Luka Doncic is doing well in both Points Scored and Assists.
  - The best k selected by Silhouette and CH index is 2. From the scatter plot of the clustering result after using PCA, the two clusters represents two groups of players of different scoring ability levels. The dividing line is about PTS of 10
  - Based on the 5 positions on the basketball court, k is set to 5 in k-means to get 5 clusters. From the scatter plot of the clustering result after using PCA, the five clusters give five groups of players. We can see that Stephen Curry, Paul George and Kyrie Irving are from the same cluster, and Kevin Durant, Trae Young and James Harden are from the same cluster, which means they have similar performances
  - For team managers, they can trade players from the same cluster so that the team structure won’t change much and it may be good for a new player to integrate into the team
  - For coaches and trainers, they can learn from the training methods and playing patterns of the players from the same cluster. It's good for players to develop better
  - (By clicking a certain point with the mouse, the relevant clustering information can be displayed, and the players in the same cluster can be intuitively seen. And the larger the size of a point(player), the higher the player's PTS)
- For dataset of Stephen Curry:
  - From the pie chart showing Stephen Curry's Points Scored in season 2021-22, we can see that he often got points per game in the 20-30 range and sometimes he even scored more than 50 points in one game, which reflects that he did well in scoring last season
  - From the first 20+ games in the line charts, we can see that Stephen Curry’s Points Scored per game is steady and his Field Goals Percentage is better than last season when outliers are not considered. He keeps a good competitive state
    (By clicking a point with the mouse, we can intuitively see what his Points Scored and Field Goals Percentage are in which game)

# Future Work
- For a certain cluster of players, collect their statistical data of each game in recent seasons and find more specific similarities of these players. And provide more specific suggestions on the offensive/defensive strategy and training method of the players according to the domain knowledge
- Build a model(SVM/NN) to classify players. With PTS, FGM, REB and other statistics as the features, POS as the label, and data of previous seasons as the training set, for new players just entering NBA, his position is predicted according to his performance data, and insights are generated for player position adjustment

