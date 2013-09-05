from sys import argv


#places cards in decending order, A..2
#only used by card_array()
def order_hand(hand):
    aces=[]
    kings=[]
    queens=[]
    jacks=[]
    tens=[]
    numbers=[]
    for x in hand:
        if x[0]=='A':
            aces.append(x)
        elif x[0]=='K':
            kings.append(x)
        elif x[0]=='Q':
            queens.append(x)
        elif x[0]=='J':
            jacks.append(x)
        elif x[0]=='T':
            tens.append(x)
        else:
            numbers.append(x)
    numbers.sort()
    numbers.reverse()
    return aces+kings+queens+jacks+tens+numbers
    
# Card Array
# A-14
# K-13
# Q-12
# J-11
# T-10

def card_array(hand):
    hand=order_hand(hand)
    hand_mtrx=[]
    for card_str in hand:
        if card_str[0]=='A':
            hand_mtrx.append([14,card_str[1]])
        elif card_str[0]=='K':
            hand_mtrx.append([13,card_str[1]])
        elif card_str[0]=='Q':
            hand_mtrx.append([12,card_str[1]])
        elif card_str[0]=='J':
            hand_mtrx.append([11,card_str[1]])
        elif card_str[0]=='T':
            hand_mtrx.append([10,card_str[1]])
        else:
            hand_mtrx.append([int(card_str[0]),card_str[1]])
    return hand_mtrx    

# Frequency Array
# A-0
# K-1
# Q-2
# J-3
# T-4
# 9-5
# 8-6
# 7-7
# 6-8
# 5-9
# 4-10
# 3-11
# 2-12
# A-13* (In is_stright() only)
   
def freq_array(hand):
    array=[0]*13
    for card in hand:
        array[card[0]-2]+=1
    array.reverse()
    return array

def is_straight(hand):
    array=freq_array(hand)
    array.append(array[0])
    for i in range(10):
        if array[i:i+5]==[1]*5:
            return 14-i
    return False

def is_flush(hand):
    if hand[0][1]==hand[1][1]==hand[2][1]==hand[3][1]==hand[4][1]:
        return hand[0][0]
        
def is_fourkind(hand):
    array=freq_array(hand)
    if 4 in array:
        return 14-array.index(4)
    else:
        return False

def is_threekind(hand):
    array=freq_array(hand)
    if 3 in array:
        return 14-array.index(3)
    else:
        return False

def pairs(hand):
    array=freq_array(hand)
    pairs=[]
    for i in range(len(array)):
        if array[i]==2:
            pairs.append(14-i)
    #pairs.append(hand[0][0])
    return pairs

def is_pair(hand):
    vals=[]
    for card in hand:
        vals.append(card[0])
    if len(pairs(hand))==1:
        vals.remove(pairs(hand)[0])
        vals.remove(pairs(hand)[0])
        return pairs(hand)+[vals[0],vals[1],vals[2]]
    else:
        return False
        
def is_twopair(hand):
    vals=[]
    for card in hand:
        vals.append(card[0])
    if len(pairs(hand))==2:
        vals.remove(pairs(hand)[0])
        vals.remove(pairs(hand)[0])
        vals.remove(pairs(hand)[1])
        vals.remove(pairs(hand)[1])
        return pairs(hand)+[vals[0]]
    else:
        return False
    
def is_SF(hand):
    if is_straight(hand) and is_flush(hand):
        return hand[0][0]
    else:
        return False
    
def is_fullhouse(hand):
    array=freq_array(hand)
    if 2 in array and 3 in array:
        return [14-array.index(3),14-array.index(2)]

def high_cards(hand):
    vals=[]
    for card in hand:
        vals.append(card[0])
    return vals
        


#===============
    
script, filename= argv

outfile = open('poker_debug.txt','w')
file = open(filename,'r')
line = file.readline()
array = []
p1_wins=0
p2_wins=0
while line:
    cards = line.split()
    hand_p1 = card_array(cards[:5])
    hand_p2 = card_array(cards[5:])

    outfile.write(' '.join(cards)+' ')   
    
    if is_SF(hand_p1)>is_SF(hand_p2):
        p1_wins+=1
    elif is_SF(hand_p1)<is_SF(hand_p2):
        p2_wins+=1
    
    elif is_fourkind(hand_p1)>is_fourkind(hand_p2):
        p1_wins+=1
    elif is_fourkind(hand_p1)<is_fourkind(hand_p2):
        p2_wins+=1
    
    elif is_fullhouse(hand_p1)>is_fullhouse(hand_p2):
        p1_wins+=1
    elif is_fullhouse(hand_p1)<is_fullhouse(hand_p2):
        p2_wins+=1
    
    elif is_flush(hand_p1)>is_flush(hand_p2):
        p1_wins+=1
    elif is_flush(hand_p1)<is_flush(hand_p2):
        p2_wins+=1
    
    elif is_straight(hand_p1)>is_straight(hand_p2):
        p1_wins+=1
    elif is_straight(hand_p1)<is_straight(hand_p2):
        p2_wins+=1
    
    elif is_threekind(hand_p1)>is_threekind(hand_p2):
        p1_wins+=1
    elif is_threekind(hand_p1)<is_threekind(hand_p2):
        p2_wins+=1
    
    elif is_twopair(hand_p1)>is_twopair(hand_p2):
        p1_wins+=1
    elif is_twopair(hand_p1)<is_twopair(hand_p2):
        p2_wins+=1
    
    elif is_pair(hand_p1)>is_pair(hand_p2):
        p1_wins+=1
    elif is_pair(hand_p1)<is_pair(hand_p2):
        p2_wins+=1
    
    elif high_cards(hand_p1)>high_cards(hand_p2):
        p1_wins+=1
    elif high_cards(hand_p1)<high_cards(hand_p2):
        p2_wins+=1
    
    outfile.write('\n')
    
    line = file.readline()
    
    
print p1_wins,p2_wins