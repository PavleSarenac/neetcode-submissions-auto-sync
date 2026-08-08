class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int numIndex = 1, uniqueNumIndex = 1;
        while (numIndex < nums.size()) {
            if (nums[numIndex] != nums[numIndex - 1]) {
                nums[uniqueNumIndex] = nums[numIndex];
                uniqueNumIndex++;
            }
            numIndex++;
        }
        return uniqueNumIndex;
    }
};