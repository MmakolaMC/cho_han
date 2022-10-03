class ChoHan:
    
    def __init__(self):
        
        print('Guess if the total sum of the dice roll will be even(CHO) or odd(HAN).\n')
        
    def roll_dice(self):
        
        import random
        
        dice_sum = random.randint(1, 7) + random.randint(1, 7)
        
        return dice_sum
    
    def play(self):
        
        while True:
            answer = self.roll_dice()

            money = input('How much money do you have?\n')
            print(f'You have {money}. How much do you bet? or (QUIT)\n')
            user_input = input('CHO(even) or HAN(odd)? or QUIT?\n')


            if user_input.lower() == 'quit':
                break

            elif answer % 2 == 0 and user_input.lower() == 'cho':
                print(f'Congratulations, You have won. The sum is {answer}!\n')

            elif answer % 2 != 0 and user_input.lower() == 'han':
                print(f'Congratulations, You have won. The sum is {answer}\n')

            else:
                print(f'Sorry, you have lost. The sum is {answer}\n')


if __name__ == '__main__':

    game = ChoHan()

    game.play()