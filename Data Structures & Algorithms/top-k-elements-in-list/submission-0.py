class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberToFrequencyMap = dict()
        for number in nums:
            if number not in numberToFrequencyMap:
                numberToFrequencyMap[number] = 1
            else:
                numberToFrequencyMap[number] += 1

        frequencyToNumbersMap = dict()
        for number, frequency in numberToFrequencyMap.items():
            if frequency not in frequencyToNumbersMap:
                frequencyToNumbersMap[frequency] = [number]
            else:
                frequencyToNumbersMap[frequency].append(number)

        print(frequencyToNumbersMap)

        topKFrequentElements = []
        for frequency in range(len(nums), 0, -1):
            if frequency not in frequencyToNumbersMap:
                continue
            for number in frequencyToNumbersMap[frequency]:
                topKFrequentElements.append(number)
                if len(topKFrequentElements) == k:
                    return topKFrequentElements