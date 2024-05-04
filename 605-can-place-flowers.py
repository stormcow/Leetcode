class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        new_flowers = 0

        for index, flower in enumerate(flowerbed):
            if (
                index > 0
                and index < len(flowerbed) - 2
                and flowerbed[index - 1] == 0
                and flowerbed[index + 1] == 0
                and flower == 0
            ):
                new_flowers += 1
                flowerbed[index] = 1
            elif index == 0 and flower == 0 and flowerbed[index + 1] == 0:
                new_flowers += 1
                flowerbed[index] = 1
            elif (
                index == (len(flowerbed) - 1)
                and flowerbed[index - 1] == 0
                and flower == 0
            ):
                new_flowers += 1
                flowerbed[index] = 1

        return True if new_flowers >= n else False
