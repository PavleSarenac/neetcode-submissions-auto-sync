class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largestPile = max(piles)
        minimumEatingSpeed = 1
        maximumEatingSpeed = largestPile
        while minimumEatingSpeed <= maximumEatingSpeed:
            middleEatingSpeed = (minimumEatingSpeed + maximumEatingSpeed) // 2
            
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / middleEatingSpeed)

            if totalHours > h:
                minimumEatingSpeed = middleEatingSpeed + 1
            elif totalHours <= h:
                maximumEatingSpeed = middleEatingSpeed - 1

        return minimumEatingSpeed