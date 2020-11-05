import random
class RockPaperScissor:
    def __init__(self, rounds):
        self.rounds = rounds #Stores the rounds taken as an argument during instance creation
        self.comp_won = 0 #variable to store no. of times computer won
        self.user_won = 0 #variable to store number of times computer won
        self.order = {'rock':0,'scissors':1,'paper':2}
        self.choices ={'rock':0, 'paper':1, 'scissors':2}
        self.reverse_choices = {0: 'rock', 1: 'paper',  2: 'scissors'}
    
    #Method to take computer's input
    def computers_turn(self):    
        turn = random.randint(0,2)
        return (turn, self.reverse_choices[turn])
    
    #Method to take user's input
    def your_turn(self):
        print('')
        print('Enter your one choice from  rock  or  paper  or  scissors. Avoid spelling mistakes ')
        x = input() #Python inbuilt function to take user input
        #returning a tuple containing the choice
        return (self.choices[x], x)
    

    def compare_turns(self,user,comp): 
        #Calculate the difference of order between user and computer
        diff = self.order[user] - self.order[comp]
        return diff
    
    #Method to decide who is winning the current round
    #Returns 'user' or 'comp'
    def won_round(self):
        #Calling the methods as mentioned in question. 
        comp = self.computers_turn()
        user = self.your_turn()
        print('Computer\'s choice is: ', comp[1])
        print('User\'s choice is: ', user[1])
        diff = self.compare_turns(user[1],comp[1]) #We pass the string part from the tuple ie rock, paper or scissor.

        #order diff between user and computer is 2. Means user chose paper and computer got rock-
        #by checking order dictionary from above cell
        if(diff == 2):
            print('User Won!')
            return 'user'
        elif diff ==1:
            print('Computer Won!')
            return 'comp'
        elif diff == 0 :
            print('Its a draw')
            return 'draw'
        #diff == -1 means user chose rock and computer chose scissors
        elif diff == -1 :
            print('User Won!')
            return 'user'
        elif diff == -2:
            print('User Won!')
            return 'user'
    
    #Method to display score       
    def displayScore(self):
        print('')
        print('======Game Score======')
        print('Total number of rounds = ', self.rounds)
        print('Computer {} : {} User'.format(self.comp_won, self.user_won))
    
    #Method to compare scores and declare a winner    
    def declareWinner(self):
        print('')
        if self.user_won>self.comp_won:
            print('You Won!')
        elif self.comp_won>self.user_won:
            print('Computer Won!')
        else:
            print('Its a Draw!')
    
    #Method that conducts rounds and adds scores based on which player won    
    def run(self):
        for i in range(self.rounds):
            x=self.won_round()
            if x=='user':
                self.user_won += 1 #Increase the score
            elif x=='comp':
                self.comp_won += 1
            elif x == 'draw': # incase of a draw, we add 0.5 point to each
                self.user_won +=0.5
                self.comp_won +=0.5
        
        #display results at the end of all rounds
        self.displayScore()
        self.declareWinner()

if __name__ == '__main__':
    rps = RockPaperScissor(rounds = 3)
    rps.run()