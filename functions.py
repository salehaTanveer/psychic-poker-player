from itertools import permutations

from deck import rank_array, suit_array, royal_flush
import collections


# # # # # # # # # # # # utility functions # # # # # # # # # # # #

# check is given cards are in sequence not suits
def is_sequential_cards(card_ranks):
    return sorted(card_ranks) == list(range(min(card_ranks), max(card_ranks) + 1))


# separates the hand and deck cards from the input list
def split_list(card_list):
    half = len(card_list) // 2
    return card_list[:half], card_list[half:]


def compare_cards(card1, card2):
    print(card1, card2)


def convert_to_uppercase(card_list):
    return [card.upper() for card in card_list]


def check_duplicates(card_list):
    return not (len(card_list) == len(set(card_list)))  # false = no duplicate


# check if rank is within given array
def check_rank(rank):
    if rank in rank_array:
        return True
    else:
        return False


# ranks to numerical values and returns the priority. works only fo ranks.
def create_card_precedence(rs):
    try:
        key = rank_array.index(rs)
        return key
    except:
        return None


# check if suit is within given array
def check_suits(suit):
    if suit in suit_array:
        return True
    else:
        return False


def is_suit_same(card_list):
    return len(set(card_list)) == 1


def is_rank_same(card_list):
    print("card list: ", card_list)
    common = card_list[0]
    count = 0
    for card in card_list:
        if common == card:
            count += 1
    return count


# validate rank and sequence
def is_valid_card(card_list):
    if len(card_list) != 10:
        print("Cards less than 10. enter 10 cards")
        return
    if check_duplicates(card_list):  # check duplicate
        print("duplicated card value")
        return
    for card in card_list:
        if check_rank(card[:1]) is False:  # check rank
            return False
        if check_suits(card[1:]) is False:  # check suit
            return False
    return True


# # # # # # # # # # # # Best hand checking functions # # # # # # # # # # # #

def is_royal_flush(card_list):
    card_ranks = []
    card_suits = []
    for card in card_list:
        for rs in card:
            value = create_card_precedence(rs)
            if value is not None:
                card_ranks.append(value)
            else:
                card_suits.append(rs)
    if is_suit_same(card_suits) and sorted(card_ranks) == royal_flush:
        return True
    return False


def is_straight_flush(card_list):
    card_ranks = []
    card_suits = []
    for card in card_list:
        for rs in card:
            value = create_card_precedence(rs)
            if value is not None:
                card_ranks.append(value)
            else:
                card_suits.append(rs)
    if is_suit_same(card_suits) and is_sequential_cards(card_ranks):
        return True
    return False


def is_four_of_a_kind(card_list):
    card_ranks = []
    for card in card_list:
        for rs in card:
            value = create_card_precedence(rs)
            if value is not None:
                card_ranks.append(value)
    if sorted(collections.Counter(card_ranks).values()) == [1, 4]:
        return True
    return False


def is_full_house(card_list):
    card_ranks = []
    for card in card_list:
        for rs in card:
            value = create_card_precedence(rs)
            if value is not None:
                card_ranks.append(value)
    if sorted(collections.Counter(card_ranks).values()) == [2,
                                                            3]:  # shows the repeated values and their numbers in dictionary format. see only values.
        return True
    return False


def is_flush(card_list):
    card_suits = []
    for card in card_list:
        for rs in card:
            value = create_card_precedence(rs)
            if value is None:
                card_suits.append(rs)
    if is_suit_same(card_suits):
        return True
    return False


def is_straight(card_list):
    card_ranks = []
    for card in card_list:
        for rs in card:
            value = create_card_precedence(rs)
            if value is not None:
                card_ranks.append(value)  # use the array index value in card ranks for comparisons not the rs value.
    if is_sequential_cards(card_ranks) or sorted(card_ranks) == royal_flush:
        return True
    return False


def remove_repeated(list_possible, card_list):
    res = list(set(tuple(sorted(sub)) for sub in list_possible))
    list_not_possible = []
    for i in res:
        H, D = split_list(card_list)
        index = []
        count_hand = -1
        count_deck = -1
        for j in i:
            if j in H:
                count_hand += 1
            if j in D:
                count_deck += 1
                index.append(D.index(j))
        if index and count_hand > count_deck:
            diff = count_hand - max(index)
            if diff < 2:
                list_not_possible.append(i)
            elif diff >= count_hand:
                list_not_possible.append(i)
        elif index and count_deck > count_hand:
            if max(index) <= count_hand:
                list_not_possible.append(i)
    for i in list_not_possible:
        if i in res:
            res.remove(i)
    return res


# # # # # # # # # # # # Functions Call # # # # # # # # # # # #
def compare_lists(card_list):
    perm = permutations(card_list, 5)
    list_possible = []
    for i in perm:
        if get_best_hand(i) is not False:
            list_possible.append(sorted(i))
    res = remove_repeated(list_possible, card_list)
    if res is None:
        return False
    final_hand = []
    for i in res:
        if get_best_hand(i) != 9:
            final_hand.append(get_best_hand(i))
    return min(final_hand)


def get_best_hand(card_list):
    if is_royal_flush(card_list):
        return 0
    elif is_straight_flush(card_list):
        return 1
    elif is_four_of_a_kind(card_list):
        return 2
    elif is_full_house(card_list):
        return 3
    elif is_flush(card_list):
        return 4
    elif is_straight(card_list):
        return 5
    else:
        return 9


def print_best_hand(numb):
    if numb == 0:
        print("Best Hand: Royal flush")
    elif numb == 1:
        print("Best Hand: Straight flush")
    elif numb == 2:
        print("Best Hand: Four of a kind")
    elif numb == 3:
        print("Best Hand: Full house")
    elif numb == 4:
        print("Best Hand: Flush")
    elif numb == 5:
        print("Best Hand: Straight")
    elif numb == 6:
        print("Best Hand: Straight flush")
    elif numb == 7:
        print("Best Hand: Straight flush")
    else:
        print("none")


# get list
list_cards = []
list_cards = input("Enter a cards separated by space ").split()
# hand, deck = split_list(list_cards)
list_cards = convert_to_uppercase(list_cards)

if is_valid_card(list_cards) is False:
    print("Invalid card entry")
else:
    #  check hand combinations
    hand, deck = split_list(list_cards)

    combo_hand = get_best_hand(hand)
    combo_deck = get_best_hand(deck)
    combo_both = compare_lists(list_cards)
    print("combo hand: ", combo_hand, " combo deck", combo_deck, " combo ", combo_both)

    print("Hand: ", hand, " Deck: ", deck)
    if combo_both <= combo_deck and combo_both <= combo_hand:
        print_best_hand(combo_both)
    elif combo_hand <= combo_deck and combo_hand <= combo_both:
        print_best_hand(combo_hand)
    elif combo_deck <= combo_both and combo_deck <= combo_hand:
        print_best_hand(combo_deck)
