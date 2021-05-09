from fishing import start_fish
import settings


bossIDs = [388, 414, 282, 284, 285, 289, 286, 1028, 1046, 1044, 1058, 2504, 2514, 2574, 2305, 2034, 2049, 2326, 2619, 2639, 3027, 3028, 3029, 3124, 563, 629, 624, 577, 2317]
playerList = []
bossUIDs = []


class Player():

    def __init__(self, player_id, name, damage, max_damage, hits, crits, miss, dmg_taken, max_dmg_taken):
        self.player_id = player_id
        self.name = name
        self.damage = damage
        self.max_damage = max_damage
        self.hits = hits
        self.crits = crits
        self.miss = miss
        self.taken = dmg_taken
        self.max_taken = max_dmg_taken
    
    def __repr__(self):
        return f'{self.name} | Damage: {self.damage} | Max Damage: {self.max_damage} | Hits: {self.hits} | Crits: {self.crits} | Crit Chance: {self.calculateCrit()} | Miss: {self.miss} | Damage taken: {self.taken} | Max Damage taken: {self.max_taken}'

    def __str__(self):
        return f'{self.name} | Damage: {self.damage} | Max Damage: {self.max_damage} | Hits: {self.hits} | Crits: {self.crits} | Crit Chance: {self.calculateCrit()} | Miss: {self.miss} | Damage taken: {self.taken} | Max Damage taken: {self.max_taken}'
    
    def calculateCrit(self):
        if self.crits == 0 or self.hits == 0:
            return('0%')

        critChance = int(round(self.crits / self.hits, 2) * 100)
        return f'{str(critChance)}%'


def processData(data):
    if data.startswith('0 in 1'):
        player_data = data.split(' ')
        createNewPlayer(False, player_data[3], int(player_data[5]))
    
    if data.startswith('0 in 3'):
        boss_data = data.split(' ')
        if int(boss_data[3]) in bossIDs:
            bossUIDs.append(int(boss_data[4]))

    if data.startswith('0 su 1'):
        dmg_data = data.split(' ')
        if settings.BOSSMODE:
            if int(dmg_data[5]) in bossUIDs:
                processDamage(int(dmg_data[3]), int(dmg_data[14]), int(dmg_data[15]))
        else:
            processDamage(int(dmg_data[3]), int(dmg_data[14]), int(dmg_data[15]))
    
    if data.startswith('0 su 3'):
        receive_data = data.split(' ')
        processTaken(int(receive_data[5]), int(receive_data[14]))
    
    if data.startswith('0 c_info'):
        own_data = data.split(' ')
        createNewPlayer(True, own_data[2], int(own_data[7]))

    if data.startswith('0 guri 6'):
        fishing_data = data.split(' ')
        start_fish(fishing_data)



def createNewPlayer(is_user, player_name, player_id):
    if not any(x.player_id == player_id for x in playerList):
        if is_user:
            settings.USER_ID = player_id
        p = Player(player_id, player_name, 0, 0, 0, 0, 0, 0, 0)
        playerList.append(p)


def processDamage(p_id, dmg, hitmode):
    for player in playerList:
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
            player.calculateCrit()


def processTaken(p_id, dmg):
    for player in playerList:
        if player.player_id == p_id:
            player.taken += dmg
            if dmg > player.max_taken:
                player.max_taken = dmg


def sortList():
    playerList.sort(key=lambda x: x.damage, reverse=True)


def clearList():
    global playerList
    playerList = []