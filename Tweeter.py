import httplib2, oauthlib, simplejson
import twitter, Sentence, mistype, random

def main(phrase):
    if phrase[0] == '@' and phrase[1] != '@':
    
        api = twitter.Api(consumer_key='5T8HEXRlLhxcnMU5RhC8UcX4y',
                  consumer_secret='QA5CIz4USVz0SuftfBXXyMwI6xHBnSrfxiDEAVrZFJi6qLUqa2',
                  access_token_key='2415264698-dg4OyNh4m9lxoSVjw6g9cqOroQi3lx22KvXm5n2',
                  access_token_secret='f1CH79PDiYANKNVCVcEBYeRKJTuef65nN3LqDlGyLtiid')
        n = random.randint(0, 5)
        tweet = phrase +' '+mistype.mash(Sentence.makeSentence('pattern.txt'), n)
        if len(tweet) > 140 :
            main(phrase)
        else:
            
            #print("Tweet the following sentence?")
            #print(tweet)
            #ans = raw_input("(Y/N): ")

            #if (ans == "Y" or ans == "y"):
                #print("Tweet sent!")
                #status = api.PostUpdate(tweet)
            #else:
                #print("Tweet not sent.")
            
            status = api.PostUpdate(tweet)
            return true
    else:
        return false
(main('@LAHacks'))