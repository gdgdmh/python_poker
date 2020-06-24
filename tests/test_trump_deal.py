#!/usr/bin/env python
"""ディールテストクラス."""
from poker import trump_deal
from poker import trump_deck
from poker import trump_hand


def test_deal_001():
    """デッキからカードを配る(joker1 player1)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    deck.set_one_joker_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 53
    assert deck.size() == 0


def test_deal_002():
    """デッキからカードを配る(joker1 player2)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    deck.set_one_joker_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 27
    assert hand[1].size() == 26
    assert deck.size() == 0


def test_deal_003():
    """デッキからカードを配る(joker1 player3)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    deck.set_one_joker_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 18
    assert hand[1].size() == 18
    assert hand[2].size() == 17
    assert deck.size() == 0


def test_deal_004():
    """デッキからカードを配る(joker1 player4)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    deck.set_one_joker_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 14
    assert hand[1].size() == 13
    assert hand[2].size() == 13
    assert hand[3].size() == 13
    assert deck.size() == 0


def test_deal_005():
    """デッキからカードを配る(joker2 player1)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    deck.set_full_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 54
    assert deck.size() == 0


def test_deal_006():
    """デッキからカードを配る(joker2 player2)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    deck.set_full_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 27
    assert hand[1].size() == 27
    assert deck.size() == 0


def test_deal_007():
    """デッキからカードを配る(joker2 player3)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    deck.set_full_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 18
    assert hand[1].size() == 18
    assert hand[2].size() == 18
    assert deck.size() == 0


def test_deal_008():
    """デッキからカードを配る(joker2 player4)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    deck.set_full_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 14
    assert hand[1].size() == 14
    assert hand[2].size() == 13
    assert hand[3].size() == 13
    assert deck.size() == 0


def test_deal_009():
    """デッキからカードを配る(joker0 player1)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    deck.set_no_joker_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 52
    assert deck.size() == 0


def test_deal_010():
    """デッキからカードを配る(joker0 player2)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    deck.set_no_joker_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 26
    assert hand[1].size() == 26
    assert deck.size() == 0


def test_deal_011():
    """デッキからカードを配る(joker0 player3)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    deck.set_no_joker_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 18
    assert hand[1].size() == 17
    assert hand[2].size() == 17
    assert deck.size() == 0


def test_deal_012():
    """デッキからカードを配る(joker0 player4)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    hand.append(trump_hand.TrumpHand())
    deck.set_no_joker_deck()
    deal.deal(deck, hand)
    assert hand[0].size() == 13
    assert hand[1].size() == 13
    assert hand[2].size() == 13
    assert hand[3].size() == 13
    assert deck.size() == 0


def test_deal_013():
    """デッキからカードを配る(joker0 player52)."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    size = 52
    for _ in range(size):
        hand.append(trump_hand.TrumpHand())
    deck.set_no_joker_deck()
    deal.deal(deck, hand)
    for i in range(size):
        assert hand[i].size() == 1
    assert deck.size() == 0


def test_deal_014():
    """デッキからカードを配る(joker0 player53) カード以上に人数がいるパターン."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    size = 53
    for _ in range(size):
        hand.append(trump_hand.TrumpHand())
    deck.set_no_joker_deck()
    deal.deal(deck, hand)
    for i in range(size - 1):
        assert hand[i].size() == 1
    assert hand[52].size() == 0
    assert deck.size() == 0


def test_deal_015():
    """デッキからカードを配る(deck0) ValueErrorが発生."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    hand.append(trump_hand.TrumpHand())
    try:
        deal.deal(deck, hand)
    except ValueError:
        pass
    else:
        assert False


def test_deal_016():
    """デッキからカードを配る(hand0) ValueErrorが発生."""
    deal = trump_deal.TrumpDeal()
    deck = trump_deck.TrumpDeck()
    hand = []
    deck.set_no_joker_deck()
    try:
        deal.deal(deck, hand)
    except ValueError:
        pass
    else:
        assert False
