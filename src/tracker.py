import pandas as pd
class Tracker:
    def __init__(self):
        self.history=[] # object created for each game session storage
    def log(self,level,usr_answer,correct_answer,time_taken): # function to log each attempt 
        entry={
            'level':level,
            'user_answer':usr_answer,
            'correct_answer':correct_answer,
            'is_correct':usr_answer==correct_answer,
            'time_taken':time_taken
        }
        self.history.append(entry)
    def get_history(self): # function to summarize the report of the attempt 
        if not self.history:
            print("No history available.")
            pass
        df=pd.DataFrame(self.history) # using pandas for a better understanding of the summary
        print("*"*40)
        print("Performance Analysis (Powered by Pandas)")
        print("*"*40)
        print("Total Questions Attempted:",len(df))
        accuracy=df['is_correct'].mean()*100
        avg_time=df['time_taken'].mean()
        print(f"Overall Accuracy: {accuracy:.2f}%")
        print(f"Average Time per Question: {avg_time:.2f} seconds")
        print("\nDetailed History:")
        lvl_stats=df.groupby('level').agg(Accuracy=('is_correct','mean'),Avg_Time=('time_taken','mean'),Count=('is_correct','count'))# grouping by level and using aggregate function for evaluating a level-wise summary.
        lvl_stats['Accuracy']*=100
        print(lvl_stats.round(1))
        print("*"*40)