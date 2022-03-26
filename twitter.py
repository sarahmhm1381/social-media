from socialMedia import SocialMedia

class Twitter(SocialMedia):
    def __init__(self, name):
        super().__init__(name)
        self.tweets = []


    def getTweet(self):
        return self.tweets
    
    def createNewTweet(self,tweet):
        newTweet = True
        if len(tweet) <= 280:
            self.tweets.append({"tweet": tweet}) 
        else:
            newTweet = False
        return newTweet


Application = Twitter("twitter")

print(f"the name of application is {Application.getName()}")

i = 0
numbersOfTweet = int(input("how many Tweet you want to share?"))

while i < numbersOfTweet:

    aTweet = input("please enter your Tweet: ")

    if Application.createNewTweet(aTweet):
        print(f"your Tweet is {Application.getTweet()}")
    else:
        print("Sorry!you don't have validation for tweeting")
    i+=1
