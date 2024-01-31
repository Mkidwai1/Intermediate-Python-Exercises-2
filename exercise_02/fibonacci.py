import time
import random
def main():
    
    def fibonnaci_sequence():
        startTime = time.time()
        n = random.randint(15,35)
        fibonnaci_sequence = [0,1]
        for i in range(2,n):
            nextNum = fibonnaci_sequence[i-1] + fibonnaci_sequence[i-2]
            fibonnaci_sequence.append(nextNum)
        print(f"fib({n})= {fibonnaci_sequence[n-1]}")
        endTime = time.time()
        executionTime = endTime - startTime
        print(f"fib({n})= {executionTime} seconds")
            
    #print(fibonnaci_sequence())
    fibonnaci_sequence()
    
if __name__ == "__main__":
    main()
    