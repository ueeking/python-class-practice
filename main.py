import random
import time


class GameCharacter():
    def __init__(self):
        self.Hp = 500
        self.Damage = 80
        self.Mana = 150

    def Attack(self, Damage, targetInfo):
        print(targetInfo.Name, " 공격!", Damage, "데미지!")
        if targetInfo.Hp - Damage <= 0:
            print(targetInfo.Name, "사망\n")
            targetInfo.DChangeHp(0)
        if targetInfo.Hp - Damage > 0:
            targetInfo.ChangeHp(Damage)
            print(targetInfo.Name, "HP : ", targetInfo.Hp, "\n")

    def Skill(self, Damage, Mana, targetInfo):
        if self.Mana >= Mana:
            print(targetInfo.Name, " 에게 스킬 사용!", Damage, "데미지!")
            self.Mana -= Mana
            print("남은 마나 :", self.Mana)

            if targetInfo.Hp - Damage <= 0:
                print(targetInfo.Name, "사망\n")
                targetInfo.DChangeHp(0)
            if targetInfo.Hp - Damage > 0:
                targetInfo.ChangeHp(Damage)
                print(targetInfo.Name, "HP : ", targetInfo.Hp, "\n")

        if self.Mana < Mana:
            print("마나 부족, 필요한 마나 :", Mana, "보유 마나 :", self.Mana, "\n")


class 마법사(GameCharacter):
    def __init__(self):
        self.Hp = 500
        self.Damage = 80
        self.Mana = 150
        self.SkillManaCost = 20
        self.Name = "마법사"
    def SetName(self,name):
        self.Name = name
    def Attack(self, targetInfo):
        super().Attack((self.Damage * 0.7), targetInfo)

    def Skill(self, targetInfo):
        super().Skill((self.Damage * 1.6), self.SkillManaCost, targetInfo)

    def ChangeHp(self, dmg):
        self.Hp -= dmg

    def DChangeHp(self, dmg):
        self.Hp = dmg


class 전사(GameCharacter):
    def __init__(self):
        self.Hp = 500
        self.Damage = 80
        self.Mana = 150
        self.SkillManaCost = 30
        self.Name = "전사"
    def SetName(self,name):
        self.Name = name
    def Attack(self, targetInfo):
        super().Attack((self.Damage), targetInfo)

    def Skill(self, targetInfo):
        super().Skill((self.Damage * 1.5), self.SkillManaCost, targetInfo)

    def ChangeHp(self, dmg):
        self.Hp -= dmg

    def DChangeHp(self, dmg):
        self.Hp = dmg


class Game():
    attack = 0
    randomnumber = 0
    randomnumber2 = 0
    def __init__(self):
        self.list = ["NULL",전사(), 전사(), 마법사(),마법사()]

    def Start(self):
        warriorteam = [self.list[1],self.list[2]]
        mageteam = [self.list[3],self.list[4]]

        warrior = self.list[1]
        mage = self.list[3]

        self.list[1].SetName("전사1")
        self.list[2].SetName("전사2")
        self.list[3].SetName("마법사1")
        self.list[4].SetName("마법사2")

        while True:
            time.sleep(1)
            if mage.Hp <= 0 or warrior.Hp <= 0 or warrior2.Hp <= 0 or mage2.Hp <= 0:
                if mage.Hp <= 0:
                    print("게임 종료", warrior.Name, "승리\n")
                if warrior.Hp <= 0:
                    print("게임 종료", mage.Name, "승리\n")
                break
            # print(mage.Hp,warrior.Hp)
            attack = random.randrange(1, 3)
            randomnumber = random.randrange(1, 3)
            warriorrandom = random.randrange(1, 3)
            magerandom = random.randrange(3, 5)
            AttackWarrior = self.list[warriorrandom]
            AttackMage = self.list[magerandom]
            if attack == 1:  # 1 = 마법사 공격 차례 , #2 = 전사 공격 차례
                if randomnumber == 1:  # 1 = 공격, #2 = 마법
                    mage.Attack(AttackWarrior)
                if randomnumber == 2:
                    mage.Skill(AttackWarrior)
            if attack == 2:  # 1 = 마법사 공격 차례 , #2 = 전사 공격 차례
                if randomnumber == 1:  # 1 = 공격, #2 = 마법
                    warrior.Attack(AttackMage)
                if randomnumber == 2:
                    warrior.Skill(AttackMage)

game = Game()
GameStart = game.Start()



