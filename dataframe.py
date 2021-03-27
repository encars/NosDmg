player_list = []


class Player():

    def __init__(self, player_id, name, damage, max_damage, hits, crits, miss):
        self.player_id = player_id
        self.name = name
        self.damage = damage
        self.max_damage = max_damage
        self.hits = hits
        self.crits = crits
        self.miss = miss
    
    def __repr__(self):
        return f'{self.name} | Damage: {self.damage} | Max Damage: {self.max_damage} | Hits: {self.hits} | Crits: {self.crits} | Miss: {self.miss}'

    def __str__(self):
        return f'{self.name} | Damage: {self.damage} | Max Damage: {self.max_damage} | Hits: {self.hits} | Crits: {self.crits} | Miss: {self.miss}'


def create_new_player(player_name, player_id):
    if not any(x.player_id == player_id for x in player_list):
        p = Player(player_id, player_name, 0, 0, 0, 0, 0)
        player_list.append(p)
    else:
        print('Player already in list')


def process_entry(data):
    if data.startswith('0 in 1'):
        player_data = data.split(' ')
        create_new_player(player_data[3], int(player_data[5]))

    if data.startswith('rdlst'):
        print(data)

    if data.startswith('0 su 1'):
        dmg_data = data.split(" ")
        process_damage(int(dmg_data[3]), int(dmg_data[14]), int(dmg_data[15]))
    
    if data.startswith('0 c_info'):
        print(data)
        own_data = data.split(' ')
        create_new_player(own_data[2], int(own_data[7]))


def process_damage(p_id, dmg, hitmode):
    for player in player_list:
        if player.player_id == p_id:
            player.damage += dmg
            if dmg > player.max_damage:
                player.max_damage = dmg
                
            if not hitmode == 1:
                player.hits += 1
                if hitmode == 3:
                    player.crits += 1
            else:
                player.miss += 1


def print_list():
    for player in player_list:
        print(player)


# p = Player(501, 'test', 500, 1000, 5, 2, 1)
# print(str(p))
# p.damage += 500
# print(str(p))