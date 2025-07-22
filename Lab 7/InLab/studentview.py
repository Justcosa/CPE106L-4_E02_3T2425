"""
File: studentview.py
The view for editing and analyzing student scores.
"""

from breezypythongui import EasyFrame
import matplotlib.pyplot as plt

class StudentView(EasyFrame):

    def __init__(self, model):
        """Creates and lays out window components
        to view and manipulate the model's data."""
        EasyFrame.__init__(self)
        self.setSize(500, 200)
        self.model = model
        self.addLabel("Mean", row = 0, column = 0)            
        self.addLabel("Median", row = 1, column = 0)            
        self.addLabel("Mode", row = 2, column = 0)            
        self.addLabel("Standard deviation", row = 3, 
                                            column = 0)
        self.meanFld = self.addFloatField(value = 0.0, 
                                          row = 0,
                                          column = 1,
                                          precision = 2)            
        self.medianFld = self.addFloatField(value = 0.0, 
                                            row = 1,
                                            column = 1,
                                            precision = 2)            
        self.modeFld = self.addFloatField(value = 0.0, 
                                          row = 2,
                                          column = 1,
                                          precision = 1)            
        self.stdFld = self.addFloatField(value = 0.0, 
                                         row = 3,
                                         column = 1,
                                         precision = 4)                        
        self.addLabel("Data", row = 0, column = 2,
                      sticky = "NEW")
        self.scoreArea = self.addTextArea(text = "", 
                                          row = 1,
                                          column = 2,
                                          width = 12,
                                          rowspan = 3)
        # Create a panel for the buttons to center them
        # in 4 columns
        bp = self.addPanel(row = 4, column = 0,
                           columnspan = 3,
                           background = "black")
        bp.addButton(text = "Edit score", 
                     row = 0, column = 0,
                     command = self.editScore)
        bp.addButton(text = "Add score", 
                     row = 0, column = 1,
                     command = self.addScore)
        bp.addButton(text = "Delete score", 
                     row = 0, column = 2,
                     command = self.deleteScore)
        bp.addButton(text = "Randomize scores", 
                     row = 0, column = 3,
                     command = self.randomizeScores)
        bp.addButton(text = "Plot scores", 
                     row = 0, column = 4,
                     command = self.plotScores)
        # Place the model's contents in the view
        self.refreshData()

    def refreshData(self):
        """Updates the view with the contents of the model."""
        self.setTitle(self.model.getName() + "'s Scores")
        self.meanFld.setNumber(self.model.getMean())
        self.medianFld.setNumber(self.model.getMedian())
        self.modeFld.setNumber(self.model.getMode())
        self.stdFld.setNumber(self.model.getStd())
        self.scoreArea.setText(str(self.model))

    # Event-handling methods

    def editScore(self):
        """Obtains a new score and its position from the user
        and updates the model and the view."""
        position = self.prompterBox(title="Edit score",
                                    promptString="Position of the score to edit:")
        score = self.prompterBox(title="Edit score",
                                 promptString="New score value:")
        try:
            self.model.setScore(int(position), float(score))
        except Exception as e:
            self.messageBox(title="Error", message=str(e))
        self.refreshData()

    def addScore(self):
        """Obtains a new score from the user,
        adds it to the model, and updates the view."""
        score = self.prompterBox(title="Add score",
                                 promptString="Score to add:")
        try:
            self.model.addScore(float(score))
        except Exception as e:
            self.messageBox(title="Error", message=str(e))
        self.refreshData()
    
    def deleteScore(self):
        """Obtains the position of a score from the user,
        deletes the score at that position from the model,
        and updates the view."""
        position = self.prompterBox(title="Delete score",
                                    promptString="Position of the score:")
        try:
            self.model.deleteScore(int(position))
        except Exception as e:
            self.messageBox(title="Error", message=str(e))
        self.refreshData()
    
    def randomizeScores(self):
        """Obtains the number of scores, lowest score,
        and highest score from the user, randomizes the model's scores,
        and updates the view."""
        size = self.prompterBox(title="Randomize scores",
                                promptString="Number of scores:")
        lower = self.prompterBox(title="Randomize scores",
                                 promptString="Lowest score:")
        upper = self.prompterBox(title="Randomize scores",
                                 promptString="Highest score:")
        try:
            self.model.randomizeScores(int(size), int(lower), int(upper))
        except Exception as e:
            self.messageBox(title="Error", message=str(e))
        self.refreshData()
    
    def plotScores(self):
        """Plots the student's test scores."""
        scores = self.model.scores
        positions = list(range(1, len(scores) + 1))
        plt.figure("Test Scores")
        plt.plot(positions, scores, marker='o', linestyle='-')
        plt.title(f"{self.model.getName()}'s Test Scores")
        plt.xlabel("Position")
        plt.ylabel("Score")
        plt.grid(True)
        plt.show()

