import json


# opening json response file
with open('response.json', encoding="utf-8") as f:
  data = json.load(f)

#for state in data['data']:
#  print(state['id'])


#print(len(data['data']))




teng=0 # counter for counting total engagement

urlsrc = "https://twitter.com/narendramodi/status/"



#declaring dictionary for again converting it into a json file
jdict = {
    
}



#looping through reponses
for item in data['data']:
  rcount = item['public_metrics']['retweet_count']   # getting retweet count
  lcount = item['public_metrics']['like_count']      # getting likes count
  idd = item['id']                                   # getting id to form tweet url
  #print("\ntweet id",idd)
  url = urlsrc +idd                                  # forming tweet url
  engagement = rcount+lcount                         # getting engagement count
  teng +=engagement                                  # for total engagement count
  print("\nTweet Url:",url)
  #print("\nRetweet Count:",rcount)
  #print("\nLikes Count:",lcount)
  print("Engagement count:",engagement)
  dictkey = "Tweet-Url: "+url
  dictval = "Engagment count is:",engagement
  jdict[dictkey]=[]
  jdict[dictkey].append(dictval)
  


totalt=len(data['data'])                 # for getting total number of tweets
print("\nTotal Tweets Fetched:",totalt)  # printing totat tweets
print("\nTotal Engagement Count:",teng)  # printing total engagment number



t="Total tweets fetched: "    # to add total tweet count in the new json file
jdict[t]=[]
jdict[t].append(totalt)

e="Total Engagement: "       # to add total engagement count in the new json file
jdict[e]=[]
jdict[e].append(teng)


#for again converting it into a json file
with open('jsonreturn.json', 'w', encoding="utf-8") as f:
  json.dump(jdict, f, indent=4)