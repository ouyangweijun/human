# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
flowers = ('♦', '♣', '♥', '♠')
values = ('2', '3', '4', '5',
    '6', '7', '8', '9',
    '10', 'J', 'Q', 'K', 'A')
class Card(object):
    def __init__(self, flower, value):
        self.flower = flower
        self.value = value

    def __gt__(self, other):
        if not isinstance(other, Card):
            raise TypeError('+运算要求目标是Card')
        if values.index(self.value) > values.index(other.value):
            return True
        elif values.index(self.value) == values.index(other.value) and \
            flowers.index(self.flower) > flowers.index(other.flower):
            return True
        else:
            return False
    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError('+运算要求目标是Card')
        if values.index(self.value) == values.index(other.value) and \
            flowers.index(self.flower) == flowers.index(other.flower):
            return True
        else:
            return False
    def __ge__(self, other):
        if not isinstance(other, Card):
            raise TypeError('+运算要求目标是Card')
        return self > other or self == other
    def __repr__(self):
        return '%s-%s' % (self.flower, self.value)

if __name__ == "__main__":
    cd1 = Card(flower="♠", value="A")
    cd2 = Card(flower="♠", value="K")
    cd3 = Card(flower="♥", value="K")
    cd4 = Card(flower="♥", value="J")
    cd5 = Card(flower="♥", value="K")
    print(cd1 > cd2)  # True
    print(cd1 < cd2)  # False
    print(cd2 < cd3)  # False
    print(cd2 > cd3)  # True
    print(cd3 == cd5) # True
    print(cd3 < cd5)  # False
    print(cd3 > cd5)  # False
    print(cd3 >= cd5) # True
    print(cd3 <= cd5) # True

        