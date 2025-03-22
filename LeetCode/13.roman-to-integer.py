#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman numeral character map
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Edge case for empty string
        if not s:
            return 0
        
        # Step 1: Check for valid Roman characters
        for char in s:
            if char not in roman_map:
                return 0  # Invalid character
        
        total = 0
        
        # Step 2: Iterate through the Roman numeral string
        for i in range(len(s)):
            current_value = roman_map[s[i]]  # Get the value of the current character
            print(current_value)
            
            # If there's a next character, compare the current and next values
            if i + 1 < len(s):
                next_value = roman_map[s[i + 1]]  # Get the value of the next character
                if current_value < next_value:  # If current value is smaller, subtract
                    total -= current_value
                else:  # Otherwise, add it
                    total += current_value
            else:
                total += current_value  # Last character, simply add its value

        # Step 3: Validate Roman numeral structure based on repetition rules
        # Check for invalid repeated patterns (like "IIII", "VV", etc.)
        invalid_patterns = ["IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM"]
        for pattern in invalid_patterns:
            if pattern in s:
                return 0  # Invalid sequence

        return total
        
# @lc code=end
s = Solution()
print(s.romanToInt('IIII'))  # Invalid
print(s.romanToInt('IV'))  # 4
print(s.romanToInt('IX'))  # 9
print(s.romanToInt('MCMXCIV'))  # 1994
print(s.romanToInt('XX'))  # 20
