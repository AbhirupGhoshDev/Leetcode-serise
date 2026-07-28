class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_map={}
        left = 0
        maxlen = 0

        for right in range(len(s)):
            char=s[right]

            if char in char_map and char_map[char]>=left :
                left = char_map[char]+1

            char_map[char]=right

            maxlen = max(maxlen, right - left + 1)
    
        return maxlen
        