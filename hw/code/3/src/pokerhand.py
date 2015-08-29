"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from card import *
from prettytable import PrettyTable


class PokerHand(Hand):


    def sort_rank(self):
        # sort according to rank
        for i in range(0,len(self.cards)):
            for j in range(i+1,len(self.cards)):
                if self.cards[i].rank>self.cards[j].rank:
                    card_temp=self.cards[i]
                    self.cards[i]=self.cards[j]
                    self.cards[j]=card_temp



    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """similar with suit_hist(), but for rank instead

        stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        if len(self.cards)<2: return False
        else:
            self.rank_hist()
            for val in self.ranks.values():
                if val>=2:
                    return True
            return False

    def has_twopair(self):
        if len(self.cards)<4: return False
        self.rank_hist()
        count=0;
        for val in self.ranks.values():
            if val>=2:
                count+=1
        if count>=2: return True
        else: return False

    def has_threeofakind(self):
        if len(self.cards)<3: return False
        self.rank_hist()
        count=0;
        for val in self.ranks.values():
            if val>=3:
                count+=1
        if count>=1: return True
        else: return False

    def has_straight(self):
        if len(self.cards)<5: return False
        new=PokerHand()
        for card in self.cards:
            new.cards.append(card)
        new.sort_rank()
        for card in new.cards:
            if card.rank==1:
                new.add_card(Card(0,14))
        count=1
        card_temp=new.cards[0]
        for card in new.cards[1:]:
            if card.rank==card_temp.rank+1:
                count+=1
                if count>=5: return True
            elif card.rank==card_temp.rank:
                count=count
            else:
                count=1
            card_temp=card
        return False

    def has_fullhouse(self):
        if len(self.cards)<5: return False
        self.rank_hist()
        count1=0;
        count2=0;
        for val in self.ranks.values():
            if val>=3:
                count1+=1
            elif val>=2:
                count2+=1
        if (count1>=1 and count2>=1) or (count1>=2): return True
        else: return False

    def has_fourofakind(self):
        if len(self.cards)<4: return False
        self.rank_hist()
        count=0;
        for val in self.ranks.values():
            if val>=4:
                count+=1
        if count>=1: return True
        else: return False

    def has_straightflush(self):
        if len(self.cards)<5: return False
        newhandlst=[PokerHand(),PokerHand(),PokerHand(),PokerHand()]
        for card in self.cards:
            newhandlst[card.suit].add_card(card)
        for newhand in newhandlst:
            if newhand.has_straight(): return True
        return False

    def classify(self):
        if self.has_straightflush(): self.label='straight flush'
        elif self.has_fourofakind(): self.label='four of a kind'
        elif self.has_fullhouse(): self.label='full house'
        elif self.has_flush(): self.label='flush'
        elif self.has_straight(): self.label='straight'
        elif self.has_threeofakind(): self.label='three of a kind'
        elif self.has_twopair(): self.label='two pair'
        elif self.has_pair(): self.label='pair'
        else: self.label='nothing'



def estimate(times,handcardnum):
    #times=how many times we try, handcardnum= how many cards in a hand

    labelcount=[0,0,0,0,0,0,0,0]
    for i in range(0,times):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, handcardnum)
        hand.classify()
        if hand.label=='straight flush': labelcount[0]+=1
        elif hand.label=='four of a kind': labelcount[1]+=1
        elif hand.label=='full house': labelcount[2]+=1
        elif hand.label=='flush': labelcount[3]+=1
        elif hand.label=='straight': labelcount[4]+=1
        elif hand.label=='three of a kind': labelcount[5]+=1
        elif hand.label=='two pair': labelcount[6]+=1
        elif hand.label=='pair': labelcount[7]+=1
        del deck
        del hand
    for i in range(0,8):
        labelcount[i]=float(labelcount[i])/times
    return labelcount


if __name__ == '__main__':


    rang=7

    t=PrettyTable(['hand card number','number of tries','straight flush','four of a kind','full house','flush',
                   'straight','three of a kind','two pair','pair'])
    handcardnum=5
    for i in range(1,rang):
        labelcount=[]
        times=10**i
        labelcount=estimate(times,handcardnum)
        row=[handcardnum,times]+labelcount
        t.add_row(row)

    handcardnum=7
    for i in range(1,rang):
        labelcount=[]
        times=10**i
        labelcount=estimate(times,handcardnum)
        row=[handcardnum,times]+labelcount
        t.add_row(row)

    print t




