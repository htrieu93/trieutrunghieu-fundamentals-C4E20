map_size = {
    'x' : 6,
    'y' : 6
}

player = {
    'x' : 1,
    'y' : 1
}

boxes = [
    {'x' : 0, 'y' : 2},
    {'x' : 1, 'y' : 2},
    {'x' : 2, 'y' : 2},
    {'x' : 3, 'y' : 2}
]

obs = [
    {'x' : 1, 'y' : 3},
    {'x' : 4, 'y' : 5}
]

dest = [
    {'x' : 0, 'y' : 3},
    {'x' : 1, 'y' : 4},
    {'x' : 0, 'y' : 5},
    {'x' : 3, 'y' : 5}
]

player_copy = {}
box_copy = {}
box_index = -1

finish = False
box_move = False

while finish != True:
    for y in range(map_size['y']):
        for x in range(map_size['x']):
            box_loc = False
            obs_loc = False
            dest_loc = False
            player_loc = False

            if x == player['x'] and y == player['y']:
                player_loc = True
            for b in boxes:
                if x == b['x'] and y == b['y']:
                    box_loc = True
                    break
            for o in obs:
                if x == o['x'] and y == o['y']:
                    obs_loc = True
                    break
            for d in dest:
                if x == d['x'] and y == d['y']:
                    dest_loc = True
                    break

            if player_loc:
                print('P', end = ' ')
            elif box_loc:
                print('B', end = ' ')
            elif obs_loc:
                print('O', end = ' ')
            elif dest_loc:
                print('D', end = ' ')
            else:
                print('-', end = ' ')
        print()

    #Check win
    count = 0
    for b in boxes:
        if b not in dest:
            finish = False
            break
        else:
            count += 1
    if count == 4:
        print('CONGRATULATIONS, YOU WIN!!!')
        break
    
    #Player move
    move = input('What is your next move? W/S/A/D Or (Undo - Z): ').upper()
    dx = 0
    dy = 0

    if move == 'W':
        dy = -1
    elif move == 'S':
        dy = 1
    elif move == 'A':
        dx = -1
    elif move == 'D':
        dx = 1
    elif move == 'Z':
        player = player_copy
        if box_move:
            boxes[box_index] = box_copy
            box_move = False
        print('Undo Action!!')
        continue
    
    # Check if player is moving within map, then check if player is running into obstacles (if true then exit the loop and not 
    # move player), else change player's location. Player's prior location was copied for Undo.
    if 0 <= player['x'] + dx <= map_size['x']-1 and 0 <= player['y'] + dy <= map_size['y'] - 1:
        for o in obs:
            if player['x'] + dx == o['x'] and player['y'] + dy == o['y']:
                print("Oops! Obstalce :'(")
                break
        else:
            player_copy = player.copy()
            player['x'] += dx
            player['y'] += dy
    
    # Check if any box (from list of boxes) is being moved into obstacles (if true then exit the loop), else check if player is 
    # trying to move a box(player's location is at box's location), then check if box is being moved within map. If all of the 
    # above is true, then check if the moving box new location also has a box. If true then cancel the movement (can't move a box
    # on top of another), else change the moving box's location. Box's prior location (and box index/number) was copied for Undo.
    for b in boxes:
        for o in obs:
            if b['x'] + dx == o['x'] and b['y'] + dy == o['y']:
                break
        else:
            if player['x'] == b['x'] and player['y']  == b['y']:
                if 0 <= b['x'] + dx <= map_size['x'] - 1 and 0 <= b['y'] + dy <= map_size['y'] - 1:
                    for b_ in boxes:
                        if b['x'] + dx == b_['x'] and b['y'] + dy == b_['y']:
                            break    
                    else:
                        box_move = True
                        box_copy = b.copy()
                        box_index = boxes.index(b)
                        b['x'] += dx
                        b['y'] += dy
                    
            

    

