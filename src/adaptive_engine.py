def game_engine(curr_level,is_correct,time_taken): # This function is used to decide the next level based on user performance
    if not is_correct:
        if curr_level>1:
            return curr_level - 1,"Decrease" # level decreases only if the current level is greter than 1
        
    if is_correct:
        if curr_level<3:
            if curr_level==1 and time_taken<5: # for level 1 the time threshold is 5 seconds for the user to answer if not then the user will not processd to next level
                return curr_level + 1,"Increase"
            elif curr_level==2 and time_taken<7: # Here the time threshold is 7 seconds  
                return curr_level + 1,"Increase"
            
    return curr_level,"Stay" # if the user doesn't meet the conditions the level remains the same