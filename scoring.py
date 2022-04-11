import pandas as pd

thrower1 = 'Liam'
thrower2 = 'Tom'

match_columns = ['thrower', 'opponent', 'ccalled', 'chit', 'score', 'won', '1', '2', '3',
                                     '4', '5', '6', '7', '8', '9', '10',
                                     '11', '12', '13', '14', '15']
matches_played = pd.DataFrame(columns=match_columns)
stats_columns = ['thrower', 'mplayed', 'wins', 'tscore', 'avg', '']
stats = pd.DataFrame(columns = stats_columns)

player2_results = pd.DataFrame({'thrower': [thrower1],
                                'opponent': [thrower2],
                                'ccalled': [3],
                                'chit': [2],
                                'score': [60],
                                'won': [True],
                                1:[10], 2:[0], 3:[0], 4:[0], 5:[0],
                                6:[0], 7:[0], 8:[0], 9:[0], 10:[0],
                                11:[0], 12:[0], 13:[0], 14:[0], 15:[0]})



matches_played = pd.concat([matches_played,player2_results], ignore_index= True, axis= 0)

print(matches_played.head())
matches_played.to_csv('scoringtest.csv' , header= True, encoding='utf-8', index= False)