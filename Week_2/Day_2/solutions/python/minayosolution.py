def equalStacks(h1, h2, h3):
   
    total_height1 = sum(h1)
    total_height2 = sum(h2)
    total_height3 = sum(h3)
    
    
    stacks = [total_height1, total_height2, total_height3]
    heights = [h1, h2, h3]
    indices = [0, 0, 0] 
    
    while True:
        
        max_height = max(stacks)
        
       
        if stacks[0] == stacks[1] == stacks[2]:
            return stacks[0]
        
       
        for i in range(3):
            if stacks[i] == max_height:
                if indices[i] < len(heights[i]):
                  
                    stacks[i] -= heights[i][indices[i]]
                    indices[i] += 1
                else:
                   
                    return 0
