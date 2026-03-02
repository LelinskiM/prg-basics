class SocialMediaProfile():
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    
    def display_posts(self):
        x=1
        print(f'{self.username}, your posts: ')
        for post in self.posts:
            print(f'{x},. {post}')
            x += 1

def main():
    prof1 = SocialMediaProfile("john_doe")
    prof1.add_post("Hello, world!")
    prof1.add_post("Had a great day at the park!")  
    prof1.add_post("What's up, Natalie? How are you?")

    prof1.display_posts()

if __name__ == "__main__":
    main()