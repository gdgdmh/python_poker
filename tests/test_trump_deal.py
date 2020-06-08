#!/usr/bin/env python
"""ディールテストクラス."""
from poker import trump_deal
from poker import trump_deck
from poker import trump_hand


def test_deal_001():
    """デッキからカードを配る."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    deck.set_one_joker_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 53
    assert deck.size() == 0


def test_deal_002():
    """デッキからカードを配る."""
    # deal = trump_deal.TrumpDeal()
    # deck = trump_deck.TrumpDeck()
    # old_maid_players = []
    # old_maid_players.append(old_maid_player.OldMaidPlayer())
    # old_maid_players.append(old_maid_player.OldMaidPlayer())
    # old_maid_players.append(old_maid_player.OldMaidPlayer())
    # deck.set_one_joker_deck()
    # deal.deal(deck, old_maid_players)
    # assert old_maid_players[0].get_hand_size() == 18
    # assert old_maid_players[1].get_hand_size() == 18
    # assert old_maid_players[2].get_hand_size() == 17
    # assert deck.size() == 0


def test_deal_003():
    """デッキからカードを配る."""
    # deal = trump_deal.TrumpDeal()
    # deck = trump_deck.TrumpDeck()
    # old_maid_players = []
    # old_maid_players.append(old_maid_player.OldMaidPlayer())
    # old_maid_players.append(old_maid_player.OldMaidPlayer())
    # old_maid_players.append(old_maid_player.OldMaidPlayer())
    # old_maid_players.append(old_maid_player.OldMaidPlayer())
    # deck.set_one_joker_deck()
    # deal.deal(deck, old_maid_players)
    # assert old_maid_players[0].get_hand_size() == 14
    # assert old_maid_players[1].get_hand_size() == 13
    # assert old_maid_players[2].get_hand_size() == 13
    # assert old_maid_players[3].get_hand_size() == 13
    # assert deck.size() == 0
