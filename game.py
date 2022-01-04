import random

#建立魔物class
class Monster:
    def __init__(self,name,hp,atk,shield):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.shield = shield

#建立戰鬥系統class
class Fight:
    def __init__(self):        
        self.game = Monster()
    #攻擊敵人 優先判斷有無護盾
    def attack_enemy(player,enemy):
        if enemy.shield == 0:
            enemy.hp -= player.atk
            if enemy.hp < 0:
                enemy.hp = 0
        elif enemy.shield > player.atk:
            enemy.shield -= player.atk
        elif player.shield <= player.atk:
            overdamage = enemy.shield - player.atk
            enemy.shield = 0
            enemy.hp += overdamage
    #攻擊玩家 優先判斷有無護盾   
    def attack_player(player,enemy):
        if player.shield == 0:
            player.hp -= enemy.atk
            if player.hp < 0:
                player.hp = 0
        elif player.shield > enemy.atk:
            player.shield -= enemy.atk
        elif player.shield <= enemy.atk:
            overdamage = player.shield - enemy.atk
            player.shield = 0
            player.hp += overdamage   

#建立魔物objects
#玩家魔物
playerMonster1 = Monster("哥布林",50,15,0)
playerMonster2 = Monster("火精靈",80,15,35)
playerMonster3 = Monster("惡狼犬",50,20,15)
#敵方魔物
enemyMonster = Monster("敵方",220,30,0)

#雙方狀態
playerStatus = [playerMonster1,playerMonster2,playerMonster3]
enemyStatus = enemyMonster

#戰鬥開始
print("戰鬥開始!")
#外while loop: 抽出隨機一個魔物 判斷死亡沒
while playerStatus:
    #抽出隨機魔物戰鬥，從playerList移除抽出的魔物
    currentMonster = random.choice(playerStatus)
    print(currentMonster.name + "上場")
    playerStatus.remove(currentMonster)
    #內while loop: 跑當前魔物跟敵方的戰鬥
    while currentMonster.hp > 0:
        Fight.attack_enemy(currentMonster,enemyStatus)
        print("對敵方進行攻擊，敵方所剩血量" + str(enemyStatus.hp) + "，護盾" + str(enemyStatus.shield))
        if enemyStatus.hp == 0:
            break
        Fight.attack_player(currentMonster,enemyStatus)
        print("敵方襲擊猛烈，" + currentMonster.name + "所剩血量" + str(currentMonster.hp) + "，護盾" + str(currentMonster.shield))
        if currentMonster.hp == 0:
            print(currentMonster.name + "戰死")
    #判斷玩家勝利或失敗
    if enemyStatus.hp <= 0:
        print("戰鬥勝利!")
        break
    elif playerStatus == []:
        print("戰鬥失敗!")
        break