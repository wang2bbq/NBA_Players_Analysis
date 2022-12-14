import requests
from bs4 import BeautifulSoup

def get_players_data(url):
    """
    Fetch NBA 2021-22 regular season advanced stats(players' avearge performance per game) from https://www.espn.com/nba/stats/player/_/season/2022/seasontype/2

    Args:
        url - string url indicating where to get the data

    Returns:
        output_file_name: the file containing NBA players performance data fetched from the webpage
    """
    params = {
        'region': 'us',
        'lang': 'en',
        'contentorigin': 'espn',
        'isqualified': 'true',
        'page': '1',
        'limit': '1000',
        'sort': 'offensive.avgPoints:desc',
        'season': '2022',
        'seasontype': '2',
    }
    output_file_name = 'data_players.csv' # define output data file name 
    page = requests.get(url,params=params)
    soup = BeautifulSoup(page.content, 'html.parser')
    column_names=[]
    header_rows = soup.select('thead.Table__header-group tr')
    data_rows = soup.select('tbody.Table__TBODY tr')
    with open('../data/'+output_file_name,'w') as outhand:
        for row in header_rows:
            for h in row:
                column_names.append(h.get_text().strip())
        header = ','.join([str(c) for c in column_names])
        outhand.write(header + '\n')
        i = 0
        while i<len(data_rows)/2:
            data1 = []
            data2 = []
            left_data = data_rows[i].find_all('td')
            right_data = data_rows[i+int(len(data_rows)/2)].find_all('td')
            for d in left_data:
                data1.append(d.get_text().strip())
            #row_data_left = ','.join([str(d) for d in data1])
            for d in right_data:
                data2.append(d.get_text().strip())
            #row_data_left = ','.join([str(d) for d in data1])
            data3 = data1+data2
            row_data = ','.join([str(d) for d in data3])
            outhand.write(row_data + '\n')
            i += 1
    return output_file_name
    


def get_curry_data(url):
    """
    Fetch Stephen Curry's per-game stats for 2021-22 and 2022-23 seasons from api https://rapidapi.com/api-sports/api/api-nba
     
    Args:
        url - string url indicating where to get the data

    Returns:
        output_file_name1: the file containing Stephen Curry's per-game stats for 2021-22 season fetched from the api
        output_file_name2: the file containing Stephen Curry's per-game stats for 2022-23 season fetched from the api
    """
    querystring1 = {"id":"124","season":"2021"}
    querystring2 = {"id":"124","season":"2022"}

    headers = {
        "X-RapidAPI-Key": "4f09c54029msh95c8f7c53c1d3acp136b17jsnb69f54013fed",
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    output_file_name1 = 'data_curry_2021.csv'
    output_file_name2 = 'data_curry_2022.csv'
    response1 = requests.request("GET", url, headers=headers, params=querystring1)
    response2 = requests.request("GET", url, headers=headers, params=querystring2)
    dic_2021 = response1.json()
    dic_2022 = response2.json()
    features = ['points','pos','min','fgm','fga','fgp','ftm','fta','ftp','tpm','tpa','tpp','offReb','defReb','totReb','assists','pFouls','steals','turnovers','blocks','plusMinus','comment']

    with open('../data/'+output_file_name1,'w') as outhand1:
        header1 = ','.join(features)
        outhand1.write(header1 + '\n')
        for i in range(len(dic_2021['response'])):
            single_game = []
            for f in features:
                single_game.append(dic_2021['response'][i][f])
            row_data = ','.join([str(v) for v in single_game])
            outhand1.write(row_data + '\n')
    
    with open('../data/'+output_file_name2,'w') as outhand2:
        header2 = ','.join(features)
        outhand2.write(header2 + '\n')
        for i in range(len(dic_2022['response'])):
            single_game = []
            for f in features:
                single_game.append(dic_2022['response'][i][f])
            row_data = ','.join([str(v) for v in single_game])
            outhand2.write(row_data + '\n')
    return output_file_name1, output_file_name2
