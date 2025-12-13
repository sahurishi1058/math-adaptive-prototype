MATH ADVENTURES: AI-POWERED ADAPTIVE LEARNING PROTOTYPE
=======================================================

Adaptive Learning Assignment Submission

A Python-based adaptive learning system that dynamically personalizes math 
puzzle difficulty based on user performance (accuracy and speed).

-------------------------------------------------------------------------
PROJECT OVERVIEW
-------------------------------------------------------------------------
The goal of this project is to demonstrate how algorithmic logic can keep 
learners in their optimal "challenge zone". The system tracks student 
performance in real-time and adjusts the difficulty of the next question 
using a rule-based engine.

CORE FEATURES:
* Adaptive Engine: Automatically promotes or demotes users based on performance.
* Smart Puzzle Generator: Creates age-appropriate math problems (ensures 
  non-negative results for subtraction and clean division).
* Performance Analytics: Utilizes Pandas to generate detailed session reports, 
  including accuracy per difficulty level.
* Modular Architecture: Clean separation of concerns (UI, Logic, Data, Generator).

-------------------------------------------------------------------------
REPOSITORY STRUCTURE
-------------------------------------------------------------------------
This project follows the recommended modular structure:

math-adaptive-prototype/
|
|-- requirements.txt      # Dependencies (pandas)
|-- README.md            # Project documentation
|-- src/
    |-- main.py           # Entry point (CLI Interface)
    |-- puzzle_generator.py # Generates math problems (Levels 1-3)
    |-- adaptive_engine.py  # Logic for adjusting difficulty
    |-- tracker.py        # Logs metrics and generates Pandas reports

-------------------------------------------------------------------------
INSTALLATION & USAGE
-------------------------------------------------------------------------

1. PREREQUISITES
   - Python 3.8 or higher
   - Pandas library

2. SETUP
   Clone the repository and install the required packages:
   
   $ git clone https://github.com/YOUR_USERNAME/math-adaptive-prototype.git
   $ cd math-adaptive-prototype
   $ pip install -r requirements.txt

3. RUN THE APPLICATION
   Navigate to the source folder and execute the main script:
   
   $ cd src
   $ python main.py

-------------------------------------------------------------------------
ADAPTIVE LOGIC EXPLAINED
-------------------------------------------------------------------------
The system uses a "Rule-Based Adaptive Engine" to determine the next 
difficulty level. This approach was chosen for its transparency and 
determinism.

LOGIC RULES:

1. TRIGGER: Incorrect Answer
   ACTION:  Decrease Difficulty
   REASON:  Immediate failure indicates the current level is too high; 
            lowering it rebuilds confidence.

2. TRIGGER: Correct Answer + Fast Time (< 5-7 seconds)
   ACTION:  Increase Difficulty
   REASON:  High accuracy combined with speed indicates mastery (automaticity); 
            the user needs a harder challenge.

3. TRIGGER: Correct Answer + Slow Time
   ACTION:  Maintain Level
   REASON:  The user understands the concept but lacks fluency. They need 
            more practice at the current level.

DIFFICULTY LEVELS:
* Level 1 (Easy): Basic Addition/Subtraction (numbers 1-10).
* Level 2 (Medium): Intermediate Add/Sub/Mult (numbers 1-50).
* Level 3 (Hard): Mixed Operations including Division (numbers 50-100).

-------------------------------------------------------------------------
ANALYTICS SAMPLE
-------------------------------------------------------------------------
At the end of a session, the system outputs a Pandas-powered summary:

****************************************
 Performance Analysis (Powered by Pandas)
****************************************
Total Questions: 10
Overall Accuracy: 90.00%
Average Time:     4.20 s

--- Detailed History by Level ---
       Accuracy  Avg_Time  Count
level                           
1         100.0       2.5      4
2         100.0       4.1      3
3          66.7       6.8      3

-------------------------------------------------------------------------
FUTURE IMPROVEMENTS
-------------------------------------------------------------------------
* GUI: Implement a Streamlit or Web interface for better visualization.
* Reinforcement Learning: Replace the rule-based engine with a Q-learning 
  model to optimize engagement over long-term usage.
* User Profiles: Save progress across multiple sessions using a database.