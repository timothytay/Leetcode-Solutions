class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            
                if flowerbed[i] == 0 and flowerbed[i-1 if i-1 >= 0 else i] == 0 and flowerbed[i+1 if i+1 < len(flowerbed) else i] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0