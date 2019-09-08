game_running = True

while game_running == True:
    new_round = True
    player = {'name': 'hero', 'attack': 10, 'heal': 25, 'health': 100}
    monster = {'name': 'demon', 'attack': 12, 'health': 100}

    print('___' * 7)
    print('Enter Player Name')
    player['name'] = input()

    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(player['health']) + ' health')

    while new_round == True:

        player_won = False
        monster_won = False
        
        
        print('---' * 7)
        print("A MONSTER HAS CROSSED YOUR PATH")
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')

        player_choice = input()


        if player_choice == '1':
            print('You Attack')
            player['health'] = player['health'] - monster['attack']
            monster['health'] = monster['health'] - player['attack']

        if monster['health'] <=0:
            player_won = True
            
                
        else:
              player['health'] = player['health'] - monster['attack']
              if player['health'] <= 0:
                  monster_won = True

        print(monster['health'])
        print(player['health'])
    
               
              
        if player_choice == '2':
            print('you heal')
            player['health'] = player['health'] + player['heal']

            print(monster['health'])
            print(player['health'])

        elif player_choice == '3':
            new_round = False
            game_running = False

            if player_won == True or monster_won == True:
             new_round = False

          
            
