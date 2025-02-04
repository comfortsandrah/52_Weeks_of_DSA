def equalStacks(h1, h2, h3):
    # Write your code here
    def get_cummulative_sums(stack):
        cummulative_sums = []
        total = 0
        for height in reversed(stack):
            total += height
            cummulative_sums.append(total)
        return set(cummulative_sums)
        
    s1 = get_cummulative_sums(h1)
    s2 = get_cummulative_sums(h2)
    s3 = get_cummulative_sums(h3)
    return max(s1 & s2 & s3) if s1 & s2 & s3 else 0
