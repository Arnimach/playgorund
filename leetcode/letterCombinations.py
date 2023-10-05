class Solution:

    def letterCombinations(self, digits: str) -> list:
        """
        A function to convert a string containing digits from 2-9 inclusive to all possible
        combinations that the number could represent (just like on telephone buttons).
        """
        # list to determine the combinations in the current iteration of every digit
        multi_str = [""]
        # A list add the results after completion of iterations for each digit in digits
        cur = []
        # return empty list if digits is an empty string
        if digits == '':
            return cur

        # A =dictionary for codes associated with each digit
        hash_nums = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # for each digit in digits, find codes
        for i in digits[-1::-1]:
            code = hash_nums[i]
            # iterate over code in reverse
            # making combinations from right to left
            for item in code:
                # make combinations by adding letters
                for strg in multi_str:
                    # adding results to cur list
                    cur.append(item + strg)
            # copy combinations generated
            # for the current digit
            # so that new combinations will
            # be formed with the next digit
            multi_str = cur
            # reassign cur to be an empty list
            # to add results for next iteration
            cur = []

        return multi_str
