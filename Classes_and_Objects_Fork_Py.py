# Initial Template for Python 3


def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        ##input object1
        name1 = input()
        hp1 = int(input())
        boost1 = int(input())
        ##input object2
        name2 = input()
        hp2 = int(input())
        boost2 = int(input())
        ##creating objects 1 and 2
        chara1 = Character(name1, hp1)
        chara1.boost(boost1)

        chara2 = Character(name2, hp2)
        chara2.boost(boost2)
        ##fuse and show the result
        show(fusion(chara1, chara2))
        testcases -= 1


if __name__ == '__main__':
    main()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''


# User function Template for python3
class Character:
    def __init__(self, name, hp):
        self.name = name  ##Assigning name to the current object's name variable
        self.hp = hp  ##Assigning hp to the current object's hp variable

    def boost(self, amount):
        self.hp = self.hp * amount  ## boosting current object's hp

    def getName(self):
        ##complete this. Return name of the current object
        return self.name

    def getHp(self):
        ##complete this. return hp of the current object
        return self.hp


def fusion(a, b):
    ##This function takes two Character objects as parameter
    ## Create a new object that has name equal to first-half of a's name + last-half of b's name
    ## Also new object's hp is the sum of a's hp + b's hp
    ##return the newly created object
    a_name = a.getName();
    b_name = b.getName();
    tot_name = a_name[0:(len(a_name) // 2)] + b_name[len(b_name) // 2:]
    tot_hp = a.getHp() + b.getHp()
    chara_ = Character(tot_name, tot_hp)
    return chara_


def show(a):  ##Already completed
    print(a.getName(), a.getHp())  ##printing the newobject's name and hp

