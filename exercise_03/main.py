import numpy
import random
def main():
    print("hello world")
    stat = []
    for i in range(9):
        add = random.random()
        stat.append(add)
        
    print(stat)
    
    mean = numpy.mean(stat)
    median = numpy.median(stat)
    standard_deviation = numpy.std(stat)
    
    print(f"The mean is {mean}")
    print(f"The median is {median}")
    print(f"the standard deviation {standard_deviation}")
    
if __name__ == '__main__':
    main()