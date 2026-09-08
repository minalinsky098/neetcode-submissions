class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                index = stack[-1][1]
                stack.pop()
                difference = i - index
                output[index] = difference
            else: 
                stack.append((temperatures[i],i))

        return output
            


        
        