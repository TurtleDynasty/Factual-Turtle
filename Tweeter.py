import httplib2
import oauthlib
import simplejson
import twitter
import Sentence

api = twitter.Api(consumer_key='5T8HEXRlLhxcnMU5RhC8UcX4y',
                  consumer_secret='QA5CIz4USVz0SuftfBXXyMwI6xHBnSrfxiDEAVrZFJi6qLUqa2',
                  access_token_key='2415264698-dg4OyNh4m9lxoSVjw6g9cqOroQi3lx22KvXm5n2',
                  access_token_secret='f1CH79PDiYANKNVCVcEBYeRKJTuef65nN3LqDlGyLtiid')

tweet = Sentence.makeSentence('pattern.txt')

print("Tweet the following sentence?")
print(tweet)
ans = raw_input("(Y/N): ")

if (ans == "Y" or ans == "y"):
    print("Tweet sent!")
    status = api.PostUpdate(tweet)
else:
    print("Tweet not sent.")
