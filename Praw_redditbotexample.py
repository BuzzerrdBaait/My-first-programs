import requests
from praw import *
from praw.models import MoreComments
from praw.models import *
import praw
import time
import openai
import json

openai.api_key = "sk-130850(EXAMPLE)1093875109387501"  #<---- API KEY GOES HERE (LOOK HERE)

#   AUTHENTICATE AND GET A TOKEN FROM REDDIT API   #

auth = requests.auth.HTTPBasicAuth('OWEXAM_PLESz71A', 'D_jk6L_yo6UEXAM-PLExVfcAQ') #<--- USER ACESS authentications

data = {'grant_type': 'password', #<----- stays the same
        'username': 'Redditusername', #<----insert username  (LOOK HERE)
        'password': 'Redditpasswordforuser'}    #<---- insert reddit password password   (LOOK HERE)

# Create a headers dictionary so reddit can briefly see what kind of app this is. We are a User-Agent"
headers = {'User-Agent': 'Redditusername/0.0.1'}    #<------ Insert USERNAME/0.01
# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']
# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
#while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

global comment_id
global comment_list
comment_id=[]
comment_list=[]



print(TOKEN)


def main():
    reddit = praw.Reddit(
        client_id="iDvUrEXAMPLESbJ7vNawA",
        client_secret="Yp0IEXAMPLESfSRig",
        password="WeEXAMPLES20",
        user_agent="LMGTFY (by u/BreakBitchesBacks)",
        username="BrEXAMPLESBacks",
       
    )

     #<-----DEFINE FUNCTIONS HERE

    def post_new_post(subreddit_input, title, content):
        subreddit_input= input("Enter a subreddit") 
        title=input("Title's Name?:")
        content=input("Content to post:")
        subreddit = reddit.subreddit(subreddit_input)
        subreddit.submit(title, selftext=content)
        print('Posted new post: ' + title)


    def check_all_posts(subreddit_input):
         #subreddit_input=input("Enter a subreddit to check the posts of....")
        subreddit = reddit.subreddit(subreddit_input)
        for submission in subreddit.stream.submissions():
            print('New post: ' + submission.title)
            print("newpost author: ", submission.author)
            #print("submission date:" + submission)
    
    # Now, let's create a function that can retrieve the top 10 posts from a specific subreddit: [WORKS]
    def top_posts(subreddit_input):
        posts = reddit.subreddit(subreddit_input).hot(limit=10)
        
        for post in posts:
            print(post.title)
            print(post.url)
            print(post.id)
            


    def cmd_line_for_comments():
        stop_iterating_cmds=["stop", "Stop", "STOP"]
        continue_cmds=["C","c", "continue"]
        commands=input("PRESS--> 'C' <--to Continue or type --->'stop'<--- to stop")
        command_1=["reply"]
        if commands in continue_cmds:
            (print("continue"))
        elif commands in stop_iterating_cmds:
            print("pressed stop")
            return(print(comment_list))
        elif commands in command_1:
            print("reply")
            text=input("Reply --->")
 

    def reply_to_comment(comment, reply):
        comment.reply(reply)
        print('Replied to comment: ' + comment.body)

    def check_users_subscribed_subreddits(user):
        for subreddit in reddit.user.subreddits(limit=None):
            print(str(subreddit))





    def get_posts_and_comments_for_post_in_subreddit(subreddit_input):
        stop_iterating = False
        subreddit_input=input("Enter a subreddit to iterate over comments...")
        global comment_id
        global comment_list
        while not stop_iterating:
             if stop_iterating == True:
                 return(comment_id, comment_list)
             posts = reddit.subreddit(subreddit_input).hot(limit=10)
             for post in posts:
                 print("\n \n POST TITLE:::", post.title)
                 print(" POST'S URL::", post.url, "\n \\REDDIT USERS//   \\COMMENTS//")
                 comment_list=[]
                 comment_id=[]
                 command_1=["reply"]
                 command_2=["subs", "check_users_subscribed_subreddits"]
                 for comment in post.comments:
                     comment_id.append(comment)
                     comment_list.append(comment.body)
                     print("REDDITOR,", comment.author, " says...", comment.body)
                     print("- - - - - - - - - - - - - - - - - - - -")
                     if isinstance(comment, MoreComments):
                         continue
                     stop_iterating_cmds=["stop", "Stop", "STOP"]
                     continue_cmds=["C","c", "continue"]
                     commands=input("PRESS--> 'C' <--to Continue or type --->'stop'<--- to stop")
                     
                     if commands in continue_cmds:
                         (print("continue"))
                     elif commands in stop_iterating_cmds:
                         print("pressed stop")
                         return(print(comment_list))
                     elif commands in command_1:
                         print("reply")
                         comment_list=[]
                         which_comment_input=input("Type in the comment number")
                         comment_list.append(which_comment_input)
                         reply=input("Reply --->")
                         reply_to_comment(comment, reply)
                     elif commands in command_2:
                         print("check users subs")
                         user=(comment.author)
                         check_users_subscribed_subreddits(user)


    def check_subreddit(subreddit_input):
        subreddit_input= input("ENTER A SUBREDDIT TO MONITOR....")
        in1=input("CHOSE A WORD OR PHRASE TO SEARCH MORTAL")
        in2=input("YES GOOD! NOW TYPE ANOTHER ONE AND PRESS ENTER!!")
        in3=input("GREAT! NOW TYPE IN YOUR LAST WORD OR PHRASE TO SEARCH....")

        comment_list=[]
        subreddit = reddit.subreddit(subreddit_input)
        for comment in subreddit.stream.comments():
            comment1=(comment.body)
            comment_list.append(comment1)
            word_input_list = [in1, in2, in3]
            normalized_title = comment.body.lower()
            for question_phrase in word_input_list:
                if question_phrase in normalized_title:
                    post = comment.submission
                    print("Comment author--(", comment.author, ")")
                    print("says..........''.", comment.body, ".''")
                    print("Original Post-->>", comment.id)


       



    content=("")
    title=("")
    subreddit_input=("")
    check_subreddit(subreddit_input)
    #get_posts_and_comments_for_post_in_subreddit(subreddit_input)
                         

    #praw.get_comment(comment_id) - Retrieves a comment by its ID.
    #praw.reply(comment_id, text) - Replies to a comment with the given text.
    #praw.edit(comment_id, text) - Edits a comment with the given text.
    #praw.delete(comment_id) - Deletes a comment by its ID.
    #praw.unsubscribe(comment_id) - Unsubscribes from a comment thread by its ID.
    #praw.upvote(comment_id) - Upvotes a comment by its ID.
    #praw.downvote(comment_id) - Downvotes a comment by its ID.


            
                

    #print("POST ID :" + post.id)
            
    #print("COMMENT ID: " , comment.id)
    #print("REDDITOR" , (comment.author))
    #print("SAID.....    " , (comment.body))
    #print("URL__>", post.url)
    #print("  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ ")
    #print(" ||_ |||_ |||_ |||_ |||_ |||_ |||  |||_ |||_ |||_ |||_ |||_ |||  |||_ ||\.")
    #print(" ||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||\_||")
    #print(" |/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_\|")


    #subreddit_input= input("ENTER A SUBREDDIT TO PERUSE:")
    #get_posts_and_comments_for_post_in_subreddit(subreddit_input)
            
    return


if __name__ == '__main__':
    main()
