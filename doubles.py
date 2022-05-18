# axe scores style app to record a league worth of scoring
#a branch of the original program meant for doubles play

# use pygmae for gui
import pandas as pd
import pygame, sys
from button import Button
pygame.init()

display_size = (1280, 720)
SCREEN = pygame.display.set_mode(display_size)
BLACK = (0,0,0)
BG = pygame.transform.scale(pygame.image.load("Assets/woodgrain.jpg"), display_size)
WOOD2 = pygame.transform.scale(pygame.image.load("Assets/wood2.jpg"), display_size)
orange_button = pygame.transform.scale(pygame.image.load("Assets/button.png"), (400, 100))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def get_inpt(question):  #gets user input, built for names, modded for any input
    name = ""
    pygame.display.flip()
    done = True
    while done:
        SCREEN.blit(WOOD2, (0, 0))
        NAME_TEXT = get_font(25).render(question, True, BLACK)
        NAME_RECT = NAME_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(NAME_TEXT, NAME_RECT)
        TYPED_TEXT = get_font(40).render(name, True, BLACK)
        TYPED_RECT = TYPED_TEXT.get_rect(center=(640, 400))
        SCREEN.blit(TYPED_TEXT, TYPED_RECT)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    name+=str(chr(event.key))
                if event.key == pygame.K_b:
                    name+=chr(event.key)
                if event.key == pygame.K_c:
                    name+=chr(event.key)
                if event.key == pygame.K_d:
                    name+=chr(event.key)
                if event.key == pygame.K_e:
                    name+=str(chr(event.key))
                if event.key == pygame.K_f:
                        name += str(chr(event.key))
                if event.key == pygame.K_g:
                    name+=str(chr(event.key))
                if event.key == pygame.K_h:
                    name+=str(chr(event.key))
                if event.key == pygame.K_i:
                    name+=str(chr(event.key))
                if event.key == pygame.K_j:
                    name+=str(chr(event.key))
                if event.key == pygame.K_k:
                    name+=str(chr(event.key))
                if event.key == pygame.K_l:
                    name+=str(chr(event.key))
                if event.key == pygame.K_m:
                    name+=str(chr(event.key))
                if event.key == pygame.K_n:
                    name+=str(chr(event.key))
                if event.key == pygame.K_o:
                    name+=str(chr(event.key))
                if event.key == pygame.K_p:
                    name+=str(chr(event.key))
                if event.key == pygame.K_q:
                    name+=str(chr(event.key))
                if event.key == pygame.K_r:
                    name += str(chr(event.key))
                if event.key == pygame.K_s:
                    name+=str(chr(event.key))
                if event.key == pygame.K_t:
                    name+=str(chr(event.key))
                if event.key == pygame.K_u:
                    name+=str(chr(event.key))
                if event.key == pygame.K_v:
                    name+=str(chr(event.key))
                if event.key == pygame.K_w:
                    name+=str(chr(event.key))
                if event.key == pygame.K_x:
                    name+=str(chr(event.key))
                if event.key == pygame.K_y:
                    name+=str(chr(event.key))
                if event.key == pygame.K_z:
                    name+=str(chr(event.key))
                if event.key == pygame.K_SPACE:
                    name+=str(chr(event.key))
                if event.key == pygame.K_BACKSPACE:
                    name= name[:-1]
                if event.key == pygame.K_RETURN:
                    done=False
        pygame.display.update()

    return name.upper()


match_columns =['thrower', 'opponent', 'ccalled', 'chit', 'score', 'won']#, '1', '2', '3',
                                    # '4', '5', '6', '7', '8', '9', '10',
                                     #'11', '12', '13', '14', '15']
#matches_played = pd.DataFrame(columns=match_columns)
stats_columns = ['thrower', 'mplayed', 'wins', 'tscore', 'avg']
stats = pd.DataFrame(columns = stats_columns)


def play_match():   #scorekeep a match
    global matches_played
    pygame.display.set_caption('Play Match')
    thrower1 = get_inpt('Enter the name of Thrower 1')
    thrower2 = get_inpt('Enter the name of Thrower 2')
    t1_tcount = 0 #increment through 0-15 throws for thrower 1
    t2_tcount = 0
    t1_score = 0
    t2_score = 0
    #t1_round1, t2_round1, t1_round2, t2_round2, t1_round3, t2_round3, t1_bigaxe, t2_bigaxe = 0

    player1_results = pd.DataFrame({'thrower': [thrower1],
                                    'opponent': [thrower2],
                                    'ccalled': [0],
                                    'chit': [0],
                                    'score': [0],
                                    'won': [False],
                                    1: [0], 2: [0], 3: [0], 4: [0], 5: [0],
                                    6: [0], 7: [0], 8: [0], 9: [0], 10: [0],
                                    11: [0], 12: [0], 13: [0], 14: [0], 15: [0]})
    player2_results = pd.DataFrame({'thrower': [thrower2],
                                    'opponent': [thrower1],
                                    'ccalled': [0],
                                    'chit': [0],
                                    'score': [0],
                                    'won': [False],
                                    1: [0], 2: [0], 3: [0], 4: [0], 5: [0],
                                    6: [0], 7: [0], 8: [0], 9: [0], 10: [0],
                                    11: [0], 12: [0], 13: [0], 14: [0], 15: [0]})

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(WOOD2, (0, 0))

        t1_round1 = (player1_results.loc[0,1] + player1_results.loc[0,2] + player1_results.loc[0,3]+
                     player1_results.loc[0,4]+ player1_results.loc[0,5])
        t1_round2 = (player1_results.loc[0, 6] + player1_results.loc[0, 7] + player1_results.loc[0, 8] +
                     player1_results.loc[0, 9] + player1_results.loc[0, 10])
        t1_round3 = (player1_results.loc[0, 11] + player1_results.loc[0, 12] + player1_results.loc[0, 13] +
                     player1_results.loc[0, 14] + player1_results.loc[0, 15])

        t2_round1 = (player2_results.loc[0,1] + player2_results.loc[0,2] + player2_results.loc[0,3]+
                     player2_results.loc[0,4]+ player2_results.loc[0,5])
        t2_round2 = (player2_results.loc[0, 6] + player2_results.loc[0, 7] + player2_results.loc[0, 8] +
                     player2_results.loc[0, 9] + player2_results.loc[0, 10])
        t2_round3 = (player2_results.loc[0, 11] + player2_results.loc[0, 12] + player2_results.loc[0, 13] +
                     player2_results.loc[0, 14] + player2_results.loc[0, 15])

        PLAY_TEXT = get_font(30).render(thrower1 + '   VS.  ' + thrower2, True, "black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        PLAY_SCORE1 = get_font(30).render('Round 1:  ' + str(t1_round1) + ' | ' + str(t2_round1), True, "black")
        PLAY_SCORE1_RECT = PLAY_SCORE1.get_rect(center=(640, 200))
        PLAY_SCORE2 = get_font(30).render('Round 2:  ' + str(t1_round2) + ' | ' + str(t2_round2), True, "black")
        PLAY_SCORE2_RECT = PLAY_SCORE2.get_rect(center=(640, 300))
        PLAY_SCORE3 = get_font(30).render('Round 3:  ' + str(t1_round3) + ' | ' + str(t2_round3), True, "black")
        PLAY_SCORE3_RECT = PLAY_SCORE3.get_rect(center=(640, 400))
        PLAY_THROWS = get_font(30).render('Throw: '+ str(t1_tcount+1)+ ' | '+ str(t2_tcount+1), True, "black")
        PLAY_THROWS_RECT = PLAY_THROWS.get_rect(center=(600, 550))

        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(PLAY_SCORE1, PLAY_SCORE1_RECT)
        SCREEN.blit(PLAY_SCORE2, PLAY_SCORE2_RECT)
        SCREEN.blit(PLAY_SCORE3, PLAY_SCORE3_RECT)
        SCREEN.blit(PLAY_THROWS, PLAY_THROWS_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 650),
                           text_input="EXIT MATCH", font=get_font(20), base_color="black", hovering_color="Green")

        THROWER1_7 = Button(image=None, pos=(300,150),
                             text_input='7', font=get_font(50), base_color='dark green', hovering_color="green")
        THROWER1_5 = Button(image=None, pos=(300,250),
                             text_input='5', font=get_font(50), base_color='black', hovering_color="green")
        THROWER1_3 = Button(image=None, pos=(300,350),
                             text_input='3', font=get_font(50), base_color='red', hovering_color="green")
        THROWER1_1 = Button(image=None, pos=(300,450),
                             text_input='1', font=get_font(50), base_color='blue', hovering_color="green")
        THROWER1_0 = Button(image=None, pos=(300,550),
                             text_input='0', font=get_font(50), base_color='grey', hovering_color="green")
        THROWER2_7 = Button(image=None, pos=(980,150),
                             text_input='7', font=get_font(50), base_color='dark green', hovering_color="green")
        THROWER2_5 = Button(image=None, pos=(980,250),
                             text_input='5', font=get_font(50), base_color='black', hovering_color="green")
        THROWER2_3 = Button(image=None, pos=(980,350),
                             text_input='3', font=get_font(50), base_color='red', hovering_color="green")
        THROWER2_1 = Button(image=None, pos=(980,450),
                             text_input='1', font=get_font(50), base_color='blue', hovering_color="green")
        THROWER2_0 = Button(image=None, pos=(980,550),
                             text_input='0', font=get_font(50), base_color='grey', hovering_color="green")

        for button in [PLAY_BACK, THROWER1_7, THROWER1_5, THROWER1_3, THROWER1_1, THROWER1_0,
                       THROWER2_7, THROWER2_5, THROWER2_3, THROWER2_1, THROWER2_0]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    player2_results.loc[0, 'score'] += t2_score
                    player1_results.loc[0, 'score'] += t1_score
                    t1_roundswon, t2_roundswon = 0,0
                    if t1_round1 > t2_round1:
                        t1_roundswon +=1
                    elif t2_round1 > t1_round1:
                        t2_roundswon += 1
                    if t1_round2 > t2_round2:
                        t1_roundswon +=1
                    elif t2_round2 > t1_round2:
                        t2_roundswon += 1
                    if t1_round3 > t2_round3:
                        t1_roundswon +=1
                    elif t2_round3 > t1_round3:
                        t2_roundswon += 1

                    if t1_roundswon > t2_roundswon:
                        print(f'{thrower1} WINS!!')
                        player1_results.loc[0,'won'] = True
                    elif t2_roundswon > t1_roundswon:
                        print(f'{thrower2} WINS!')
                        player2_results.loc[0, 'won'] = True
                    else:
                        print('It is a tie and I haven\'t coded ties yet')

                    matches_played = pd.concat([matches_played, player1_results], ignore_index=True, axis=0)
                    matches_played = pd.concat([matches_played, player2_results], ignore_index=True, axis=0)
                    main_menu()

                if THROWER2_0.checkForInput(PLAY_MOUSE_POS) and t2_tcount<15:
                    t2_tcount += 1
                    t2_score += 0
                    player2_results.loc[0,t2_tcount] = 0
                    print('Thrower 2 scored a 0')
                if THROWER2_1.checkForInput(PLAY_MOUSE_POS) and t2_tcount<15:
                    t2_tcount += 1
                    t2_score += 1
                    player2_results.loc[0,t2_tcount] = 1
                    print('Thrower 2 scored a 1')
                if THROWER2_3.checkForInput(PLAY_MOUSE_POS) and t2_tcount<15:
                    t2_tcount += 1
                    t2_score += 3
                    player2_results.loc[0,t2_tcount] = 3
                    print('Thrower 2 scored a 3')
                if THROWER2_5.checkForInput(PLAY_MOUSE_POS) and t2_tcount<15:
                    t2_tcount += 1
                    t2_score += 5
                    player2_results.loc[0,t2_tcount] = 5
                    print('Thrower 2 scored a 5')
                if THROWER2_7.checkForInput(PLAY_MOUSE_POS) and t2_tcount<15:
                    t2_tcount += 1
                    player2_results.loc[0, 'chit'] += 1
                    if t2_tcount == 5 or t2_tcount == 10 or t2_tcount==15:
                        t2_score += 7
                        player2_results.loc[0,t2_tcount] = 7
                        print('Thrower 2 scored a 7')
                    else:
                        t2_score += 0
                        player2_results.loc[0,t2_tcount] = 0
                        print('Thrower 2 scored 0')

                if THROWER1_0.checkForInput(PLAY_MOUSE_POS) and t1_tcount<15:
                    t1_tcount += 1
                    t1_score += 0
                    player1_results.loc[0,t1_tcount] = 0
                    print('Thrower 1 scored a 0')
                if THROWER1_1.checkForInput(PLAY_MOUSE_POS) and t1_tcount<15:
                    t1_tcount += 1
                    t1_score += 1
                    player1_results.loc[0,t1_tcount] = 1
                    print('Thrower 1 scored a 1')
                if THROWER1_3.checkForInput(PLAY_MOUSE_POS) and t1_tcount<15:
                    t1_tcount += 1
                    t1_score += 3
                    player1_results.loc[0,t1_tcount] = 3
                    print('Thrower 1 scored a 3')
                if THROWER1_5.checkForInput(PLAY_MOUSE_POS) and t1_tcount<15:
                    t1_tcount += 1
                    t1_score += 5
                    player1_results.loc[0,t1_tcount] = 5
                    print('Thrower 1 scored a 5')
                if THROWER1_7.checkForInput(PLAY_MOUSE_POS) and t1_tcount<15:
                    t1_tcount += 1
                    player1_results.loc[0, 'chit'] += 1
                    if t1_tcount == 5 or t1_tcount == 10 or t1_tcount==15:
                        t1_score += 7
                        player1_results.loc[0,t1_tcount] = 7
                        print('Thrower 1 scored a 7')
                    else:
                        t1_score += 0
                        player1_results.loc[0,t1_tcount] = 0
                        print('Thrower 1 scored 0')
#todo make the if statements checking for input a function
#todo make a function that checks the score every five throws and shows round winner



        pygame.display.update()
#just have a counter for each person's clutch call for the match and save that at the end of the df?
#TODO how to deal with big axe going an unknown number of rounds?

def show_stats():      #displays current league stats
    pygame.display.set_caption('League stats')

    while True:
        STATS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(WOOD2, (0, 0))

        STATS_TEXT = get_font(20).render("Thrower     Wins    Average", True, "black")
        STATS_RECT = STATS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(STATS_TEXT, STATS_RECT)

        stats = pd.DataFrame(columns = ['avg', 'wins', 'games_played'])
        stats.avg = matches_played.groupby('thrower').score.mean().round(1)
        stats['wins'] = matches_played.groupby('thrower').won.sum()
        stats['games_played'] = matches_played.groupby('thrower').thrower.count()
        stats.sort_values(by= ['wins', 'avg'], inplace = True, ascending= False)

        yposition = 200 #where to place lines of stats on screen
        for thrower in stats.index:
            avg_TEXT = get_font(15).render(str(stats.loc[thrower,'avg']), True, "black")
            avg_RECT = avg_TEXT.get_rect(center=(860, yposition))
            SCREEN.blit(avg_TEXT, avg_RECT)
            wins_TEXT = get_font(15).render(str(stats.loc[thrower,'wins']), True, "black")
            wins_RECT = wins_TEXT.get_rect(center=(640, yposition))
            SCREEN.blit(wins_TEXT, wins_RECT)
            thrower_TEXT = get_font(15).render(str(thrower), True, "black")
            thrower_RECT = thrower_TEXT.get_rect(center=(400, yposition))
            SCREEN.blit(thrower_TEXT, thrower_RECT)
            yposition += 30

        STATS_BACK = Button(image=None, pos=(640, 600),
                           text_input="BACK", font=get_font(75), base_color="black", hovering_color="Green")

        STATS_BACK.changeColor(STATS_MOUSE_POS)
        STATS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STATS_BACK.checkForInput(STATS_MOUSE_POS):
                    main_menu()


        pygame.display.update()
#TODO show stats just displays a big chart of the stats dataframe

def save_stats():       #saves stats and matches to csv
    pygame.display.set_caption('Saving League')
    matches_played.to_csv(f'{league_name}.csv', header= True, encoding='utf-8', index= False)
    stats.to_csv(f'{league_name}_stats.csv', header= True, encoding ='utf-8', index= False)
    while True:
        SAVE_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(WOOD2, (0, 0))

        SAVE_TEXT = get_font(45).render("This is the Save screen.", True, "black")
        SAVE_RECT = SAVE_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(SAVE_TEXT, SAVE_RECT)

        SAVE_BACK = Button(image=orange_button, pos=(640, 460),
                           text_input="BACK", font=get_font(35), base_color="black", hovering_color="Green")

        SAVE_BACK.changeColor(SAVE_MOUSE_POS)
        SAVE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SAVE_BACK.checkForInput(SAVE_MOUSE_POS):
                    main_menu()


        pygame.display.update()
#TODO save league calculates all stats from the dataframe of games played and overwrites the original stats dataframe
#TODO save also saves both data frames as csv files to reimport or edit if needed.

def main_menu():    #main menu screen
    pygame.display.set_caption("Menu")
    while True:
        SCREEN.blit(BG, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render('MAIN MENU', True, '#b68f40')
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=orange_button, pos=(640,250),
                             text_input='PLAY MATCH', font=get_font(15), base_color='#d7fcd4', hovering_color="green")
        STATS_BUTTON = Button(image=orange_button, pos=(640,400),
                             text_input='DISPLAY STATS', font=get_font(15), base_color='#d7fcd4', hovering_color="green")
        SAVE_BUTTON = Button(image=orange_button, pos=(640,550),
                             text_input='SAVE MATCHES/LEAGUE', font=get_font(15), base_color='#d7fcd4', hovering_color="green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, STATS_BUTTON, SAVE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_match()
                if STATS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    show_stats()
                if SAVE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    save_stats()

        pygame.display.update()

def league_select():
    global matches_played
    global league_name
    pygame.display.set_caption('Throw Counter V1')

    while True:
         LEAGUE_MOUSE_POS = pygame.mouse.get_pos()
         pygame.display.set_caption('Throw Counter V1')
         SCREEN.blit(BG, (0,0))

         LEAGUE_TEXT = get_font(25).render("Run an existing league OR start a new league?", True, "#b68f40")
         LEAGUE_RECT = LEAGUE_TEXT.get_rect(center=(640, 260))
         SCREEN.blit(LEAGUE_TEXT, LEAGUE_RECT)

         LEAGUE_NEW = Button(image=orange_button, pos=(640, 400),
                       text_input="NEW LEAGUE", font=get_font(15), base_color="black", hovering_color="Green")

         LEAGUE_NEW.changeColor(LEAGUE_MOUSE_POS)
         LEAGUE_NEW.update(SCREEN)

         LEAGUE_EXIST = Button(image=orange_button, pos=(640, 550),
                       text_input="EXISTING LEAGUE", font=get_font(15), base_color="black", hovering_color="Green")

         LEAGUE_EXIST.changeColor(LEAGUE_MOUSE_POS)
         LEAGUE_EXIST.update(SCREEN)

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEAGUE_NEW.checkForInput(LEAGUE_MOUSE_POS):  #selected button to create league
                    league_name = get_inpt('Enter the name of the new league: ')
                    # TODO create 2 dataframes, one of stats housing scores and win losses, the second will hold each match on a line
                    match_columns = ['thrower', 'opponent', 'matchid', 'ccalled', 'chit', 'score', 'won', 'bccalled', 'bchit', 'B1', 'B2', 'B3', 'B4', 'B5']
                    matches_played = pd.DataFrame(columns=match_columns)
                    stats_columns = ['thrower', 'mplayed', 'wins', 'tscore', 'avg', '']
                    stats = pd.DataFrame(columns = stats_columns)
                    # matchid column would be a number saved or pulled from csv save file to correlate two matches in the dataframe, may be redundant?
                    # they should be saved as two rows, one above the other...?
                    # add clutch hit function that can check throws 5,10,15 for 7's, should it save r7 and l7 in the df?
                    # could do that and then have if digit add, if r7||l7 add 7?

                    main_menu()
                if LEAGUE_EXIST.checkForInput(LEAGUE_MOUSE_POS):    #open existing league from csv
                    league_name = get_inpt('Enter the name of the existing league: ')
                    matches_played = pd.read_csv(f'{league_name}.csv')
                    stats = pd.read_csv(f'{league_name}_stats.csv')
                        #todo make each league a seperate instanse of a league class
                    main_menu()

         pygame.display.update()


league_select()
main_menu()







