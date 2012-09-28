import os
import sys
import time
import reddit
import types
import random
list = ["str1","str2","str3"]
r = reddit.Reddit(user_agent='TrantBot')
r.login(usrname, pword)
user = r.get_redditor('nothix')
for post in user.get_submitted():
    for k in range(1):
        i = random.randint(1, len(list))
    strComment = list[i - 1]
    print "10 Minute wait time starts now : " + strComment
    time.sleep(610)
    try:
        post.downvote()
        post.add_comment(strComment)
        print "Commented: %s" %post.__unicode__()
    except:
        exception('Cannot Comment or Vote!')