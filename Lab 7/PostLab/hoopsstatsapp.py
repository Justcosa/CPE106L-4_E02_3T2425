"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(frame):
    """
    Cleans the basketball stats data frame.
    Steps (example):
    - Remove rows with missing values
    - Convert column names to lowercase
    - Remove duplicate rows
    - Reset index
    """
    frame = frame.dropna()
    frame.columns = [col.lower() for col in frame.columns]
    frame = frame.drop_duplicates()
    frame = frame.reset_index(drop=True)
    return frame

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    frame = cleanStats(frame)
    HoopStatsView(frame)

if __name__ == "__main__":
    main()
