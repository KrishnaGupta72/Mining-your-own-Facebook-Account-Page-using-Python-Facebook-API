import json
import facebook #Use pip install facebook-sdk

def main():
    #User access  token: It is the access token required to access the page.
	token = "Your User Access Token"
    # GraphAPI object to access API methods.
	graph = facebook.GraphAPI(token)
	#we have extracted the desired fields in a variable profile.
    # Here, notice that 'me' in get_object() method indicates that we are doing it for our own account.
    #first_name: returns the first name of user.
    #location: The person's current location as entered by them on their profile. This field is not related to check-ins.
    #email: The person's primary email address listed on their profile. This field will not be returned if no valid email address is available.
    #link: A link to the person's timeline.'

	# fields = ['first_name', 'location{location}','email','link','user_friends']
	profile = graph.get_object('me',fields='id,name,address,website,email,first_name,gender,hometown,languages')
	#return desired fields
	print(json.dumps(profile, indent=4))
if __name__ == '__main__':
	main()

#o/p:
# {
#   "id": "2127115647378019",
#   "name": "Krishna Gupta",
#   "email": "krishna72gupta@gmail.com",
#   "first_name": "Krishna",
#   "hometown": {
#     "id": "112494682096316",
#     "name": "Bhagalpur"
#   },
#   "languages": [
#     {
#       "id": "106059522759137",
#       "name": "English language"
#     },
#     {
#       "id": "112969428713061",
#       "name": "Hindi"
#     }
#   ]
# }
