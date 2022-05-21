import unittest

"""
https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.txt

======================================
Gilded Rose Requirements Specification
======================================
Hi and welcome to team Gilded Rose.
We are a small store with a prime location.
We also buy and sell only the finest goods.
Unfortunately, our goods are constantly degrading in quality as they approach their sell by date.
We have a system in place that updates our inventory for us.

Your task will be to add a new item to our system, "Conjured", so that we can begin selling a new category of items.

Each item has 3 attributes:
    - name: the name if the item.
    - sell_in: the number of days to sell item
    - quality: how valuable the item is. (This number should never be negative, and it should not increase above 50).

General items follow these rules when the system "updates" the items:
    - if sell_in > 0: quality decreases by 1. (Remember that the quality should never be negative).
    - if sell_in <= 0: quality decreases by 2.
    - sell_in decreases by 1 after the update.

"AgedBrie" follows the general rules, with one exception:
    - if sell_in <= 0: quality increases by 1. (Remember that the quality should never increase above 50).

"BackstagePass" follows the general rules, with these exceptions:
    - if sell_in > 10: quality increases by 1. (Remember that the quality should never increase above 50).
    - if sell_in <= 10: quality increases by 2.
    - if sell_in <= 5: quality increases by 3.
    - if sell_in <= 0: quality drops to 0.

"Sulfuras" does not follow the rules at all because:
    - sell_in never changes.
    - quality never changes.

"Conjured" is the new item that you will add. It follows the general rules, with this exception:
    - if sell_in > 0: quality decreases by 2. (Remember that the quality should never be negative).
    - if sell_in <= 0: quality decreases by 4.

You can change the GildedRose class update_quality() method.
You can also add any new code.
Do NOT alter the Item class or the Items property. (You can make the Items property static if you like).

"""


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras":
                continue

            item.sell_in -= 1

            if item.name == "AgedBrie":
                item.quality = (item.quality+1) if (item.quality < 50) else item.quality
                item.quality = (item.quality+1) if (item.quality < 50 and item.sell_in < 0) else item.quality

            elif item.name == "BackstagePasses":
                item.quality = (item.quality+1) if (item.quality < 50) else item.quality
                item.quality = (item.quality+1) if (item.quality < 50 and item.sell_in < 10) else item.quality
                item.quality = (item.quality+1) if (item.quality < 50 and item.sell_in < 5) else item.quality
                item.quality = 0 if (item.sell_in < 0) else item.quality

            else:
                item.quality = (item.quality-1) if (item.quality > 0) else item.quality
                item.quality = (item.quality-1) if (item.quality > 0 and item.sell_in < 0) else item.quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRoseTest(unittest.TestCase):

    def test_items(self):
        # if sell_in > 0: quality-=1 until 0
        # if sell_in <= 0: quality-=2 until 0
        # sell_in -= 1
        items = [Item("Item", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, -1)
        self.assertEquals(items[0].quality, 8)

        items = [Item("Item", -8, -10)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, -9)
        self.assertEquals(items[0].quality, -10)

        items = [Item("Item", 1, 1)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 0)
        self.assertEquals(items[0].quality, 0)

        items = [Item("Item", 10, 10)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 9)
        self.assertEquals(items[0].quality, 9)

        items = [Item("Item", 53, 53)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 52)
        self.assertEquals(items[0].quality, 52)

    def test_aged_brie(self):
        # if sell_in <= 0: quality+=2
        items = [Item("AgedBrie", -1, 10)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].name, "AgedBrie")
        self.assertEquals(items[0].sell_in, -2)
        self.assertEquals(items[0].quality, 12)

        items = [Item("AgedBrie", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, -1)
        self.assertEquals(items[0].quality, 12)

        items = [Item("AgedBrie", 1, 10)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 0)
        self.assertEquals(items[0].quality, 11)

        items = [Item("AgedBrie", -1, 49)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, -2)
        self.assertEquals(items[0].quality, 50)

        items = [Item("AgedBrie", 53, 53)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 52)
        self.assertEquals(items[0].quality, 53)

    def test_backstage(self):
        # if sell_in > 10: quality+=1
        # if sell_in <= 10: quality+=2
        # if sell_in <= 5: quality+=3
        # if sell_in <= 0: quality = 0
        items = [Item("BackstagePasses", 15, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].name, "BackstagePasses")
        self.assertEquals(items[0].sell_in, 14)
        self.assertEquals(items[0].quality, 21)

        items = [Item("BackstagePasses", 12, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 11)
        self.assertEquals(items[0].quality, 21)

        items = [Item("BackstagePasses", 11, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 10)
        self.assertEquals(items[0].quality, 21)

        items = [Item("BackstagePasses", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 9)
        self.assertEquals(items[0].quality, 22)

        items = [Item("BackstagePasses", 7, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 6)
        self.assertEquals(items[0].quality, 22)

        items = [Item("BackstagePasses", 6, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 5)
        self.assertEquals(items[0].quality, 22)

        items = [Item("BackstagePasses", 5, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 4)
        self.assertEquals(items[0].quality, 23)

        items = [Item("BackstagePasses", 1, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 0)
        self.assertEquals(items[0].quality, 23)

        items = [Item("BackstagePasses", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, -1)
        self.assertEquals(items[0].quality, 0)

    def test_sulfuras(self):
        # sell_in: never decreases
        # quality: never changes, should always be 80
        items = [Item("Sulfuras", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 10)
        self.assertEquals(items[0].quality, 20)
        items = [Item("Sulfuras", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, 0)
        self.assertEquals(items[0].quality, 20)
        items = [Item("Sulfuras", -5, 20)]
        GildedRose(items).update_quality()
        self.assertEquals(items[0].sell_in, -5)
        self.assertEquals(items[0].quality, 20)
    # def test_conjured(self):
    # if sell_in > 0: quality-=2
    # if sell_in <= 0: quality-=4
    # items = [Item("Conjured", 10, 20)]
    # GildedRose(items).update_quality()
    # self.assertEquals(items[0].name, "Conjured")
    # self.assertEquals(items[0].sell_in, 9)
    # self.assertEquals(items[0].quality, 18)
    #
    # items = [Item("Conjured", 0, 20)]
    # GildedRose(items).update_quality()
    # self.assertEquals(items[0].name, "Conjured")
    # self.assertEquals(items[0].sell_in, -1)
    # self.assertEquals(items[0].quality, 16)


if __name__ == '__main__':
    unittest.main()
