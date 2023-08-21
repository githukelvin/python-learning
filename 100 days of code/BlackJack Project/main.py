############### Blackjack Project #####################
import os
import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer = []
want_to_play_game = True
pick_another_card = True


def pick_card(arr):
    print(logo)
    for i in range(2):
        player_card = random.choice(arr)
        computer_card = random.choice(arr)
        player.append(player_card)
        computer.append(computer_card)

    # print(player, "player")
    # print(computer, "computer")
    player_sum = sum(player)
    print(f" Your cards: {player}, current score: {player_sum}")
    print(f"Computer's first card:{computer[0]}")


def compare_cards(players_card, computers_card):
    global want_to_play_game
    global pick_another_card
    player_sum = sum(players_card)
    computers_sum = sum(computers_card)

    if player_sum == 21:
        pick_another_card = False
        print(f"you win.with blackjack{player_sum}")

    if computers_sum == 21:
        pick_another_card = False
        print(f"you lose .Opponent has blackjack{computers_sum}")

    if player_sum > 21:
        pick_another_card = False
        print(f"you lose .You went over{player_sum}")

    if computers_sum > 21:
        pick_another_card = False
        print(f"you win .opponent  went over{computers_sum}")

    if not want_to_play_game:
        pick_another_card = False
        players_card.clear()  # Clear player's card list
        computers_card.clear()


def compu(comps, plays):
    comp_sum = sum(comps)
    play_sum = sum(plays)
    if comp_sum >= 17:
        print(f"Your cards: {plays}, your final score: {play_sum}")
        print(f"Computer's final card:{comps} , final score: {comp_sum}")
        if play_sum < comp_sum < 21:
            print(f"you lose.opponent has the highest.{comp_sum}")
        if comp_sum < play_sum < 21:
            print("you win .You have the highest")
        if comp_sum == play_sum:
            print("Draw.You both have same cards")


def computer_is_17(comp_cards):
    comp = sum(comp_cards)
    # print(comp_cards)

    while comp < 17:
        pick_another_for_computer = random.choice(cards)
        comp_cards.append(pick_another_for_computer)
        comp += pick_another_for_computer


def pick_another_for_player(player):
    psum = sum(player)
    r_pick_player = random.choice(cards)
    csum = sum(computer)
    if r_pick_player == 11 and psum + r_pick_player > 21:
        r_pick_player = 1

    player.append(r_pick_player)
    psum += r_pick_player
    print(f"Your cards: {player}, current score: {psum}")
    print(f"Computer's first card: {computer[0]}")


def pick_cards():
    global pick_another_card
    while pick_another_card:
        pick = str(input("Type 'y' to get another card, type 'n' to pass: "))
        if pick == 'y':
            pick_another_for_player(player=player)
            compare_cards(players_card=player, computers_card=computer)
        else:
            computer_is_17(comp_cards=computer)
            compare_cards(players_card=player, computers_card=computer)
            compu(comps=computer, plays=player)
            # print(computer ,"after")
            pick_another_card = False


while want_to_play_game:
    select_quit = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n' :"))
    if select_quit == 'y':
        os.system('cls')
        pick_another_card = True
        pick_card(arr=cards)
        compare_cards(players_card=player, computers_card=computer)
        pick_cards()
        player.clear()
        computer.clear()

    else:
        want_to_play_game = False
