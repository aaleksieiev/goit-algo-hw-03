from turtle import *
import argparse
import argparse
  
def snowflake(lengthSide, levels): 
    if levels == 0: 
        forward(lengthSide) 
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1) 
    left(60) 
    snowflake(lengthSide, levels-1) 
    right(120) 
    snowflake(lengthSide, levels-1) 
    left(60) 
    snowflake(lengthSide, levels-1) 
  
# main function 
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Koch snowflake")
    parser.add_argument("-d", "--depth", required=False, default=1, help="depth")
    args = parser.parse_args()
    
    speed(0)                    
    length = 300.0   
             
    penup()                      
  
    backward(length/2.0) 
  
    # Pull the pen down – drawing when moving.         
    pendown()            
    for i in range(3):     
        snowflake(length, args.depth) 
        right(120) 

    done()