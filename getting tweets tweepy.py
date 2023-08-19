import tweepy

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "13VHNmMIkKZaTTsoAheLrS6Ol"
consumer_secret = "FE7cyqdDtppiCJzqfmKmKw2Xk9wYZ3XXb2IhdZKkqHHm6sideq"
access_key = "499851312-gTvpzYsphOwchp7hb7NH7nDoYWvktTJKCQx6xL0X"
access_secret = "6eW7aCOa1UFXmvu060YfeAHklhobfeRPXvZ5qzPOXlfvp"

# Function to extract tweets
def get_tweets(username):
		client =tweepy.Client("AAAAAAAAAAAAAAAAAAAAAFyBpQEAAAAAzCYhRX41nKWCrHyxpKQoZagtPrs%3Dll3oCJkHVYPmW2DwaO1sV66BAPTCS5I5vUP7SL6BjtpOf0koKZ")

		
		
		number_of_tweets=200
		tweets=client.search_all_tweets('infovkul', max_results=number_of_tweets)

		# Empty Array
		tmp=[]

		# create array of tweet information: username,
		# tweet id, date/time, text
		tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
		for j in tweets_for_csv:

			# Appending tweets to the empty array tmp
			tmp.append(j)

		# Printing the tweets
		print(tmp)


# Driver code
if __name__ == '__main__':

	# Here goes the twitter handle for the user
	# whose tweets are to be extracted.
	get_tweets("infovkul")
