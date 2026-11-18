# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   We are taking in a list and a target value, and need to find 2 values in the list
    #   with the first being less than the second that add to the target number.
    
    #   What can be done is to create a for loop that reads every index in the list and
    #   inside that create another for loop that also reads every index and in the second
    #   loop check if the value the first for loop is reading is less than the value the 
    #   second for loop is reading and if this is true, then check to see that sum of the 
    #   values that each for loop is reading equals to the target.

    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                if nums[i] + nums[j] == target:
                    return [i, j]


def max_profit(prices):
    # Outline:
    #   taking the lowest index that exists and setting it to a minimum price variable 
    #   and comparing it to every other index and seeing which index gives the largest 
    #   difference and then it returns that difference.
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    min_price = prices[0]
    m_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > m_profit:
            m_profit = profit

    return m_profit


def max_subarray(nums):
    # Outline:
    #   Read through an entire list and continuously checking the sum of the list to see
    #   what streak of numbers will lead to the highest sum and then returns said sum.
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        if current_sum + num > num:
            current_sum = current_sum + num
        else:
            current_sum = num

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == "__main__":
    main()
