from email.mime import application
from socialMedia import SocialMedia

class Instagram(SocialMedia):
    def __init__(self, name ):
        super().__init__(name)

        self.posts = []

    def publishNewPost(self , post):
        newPost = True
        if len(post) <= 2200:
            self.posts.append({"post": post}) 
        else:
            newPost = False
        return newPost

    def getPosts(self):
        return self.posts

Application = Instagram("instagram")

print(f"the name of application is {Application.getName()}")

i = 0
numbersOfPost = int(input("how many post you want to share?"))

while i < numbersOfPost:

    aPost = input("please enter your post: ")

    if Application.publishNewPost(aPost):
        print(f"your post is {Application.getPosts()}")
    else:
        print("Sorry!you don't have validation for posting")
    i+=1


