# Cube Number Test... Print out all cubed numbers up to the total value 1000, so if the cubed number is over 1000 break the loop. 

# Create an empty list to hold all values
one_thousand = []
# Create a range of range values up to 1000 and store in the empty list          
one_thousand = range(1, 1001) 

# Create a loop that will loop over each number up to 1000 
for num in one_thousand:   
    cubed = num ** 3       
    
    if cubed > 1000:
        break      
    print(cubed) 

                           