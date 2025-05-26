class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if len(flowerbed) == 1 and flowerbed[0] == 0:
                flowerbed[0] = 1
                n -= 1
            elif i == 0 and flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
            elif i == len(flowerbed) - 1 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                n -= 1
            else:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0