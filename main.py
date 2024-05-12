import json
followersRaw=open('followers_1.json')
followingRaw=open('following.json')
followers=json.load(followersRaw)
following=json.load(followingRaw)
listFollower=[]
listFollowing=[]

for follower in followers:
    listFollower.append(follower['string_list_data'][0]['value'])

for followed in following['relationships_following']:
    listFollowing.append(followed['string_list_data'][0]['value'])

for following in listFollowing:
    if following in listFollower:
        continue
    else:
        print(following)