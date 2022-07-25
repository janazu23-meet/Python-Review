def create_youtube_video(title, desc):
	youtube = {"Title":title, "Desc":desc, "Likes":0, "Dislikes":0, "Username":{} }
	return youtube

youtube = create_youtube_video("Video 1", "Funny Video")

def like(dict1):
	if "Likes" in dict1.keys():
		youtube["Likes"] +=1
	return youtube

like(youtube)

def dislike(dict2):
	if "Likes" in dict2.keys():
		youtube["Dislikes"] +=1
	return youtube

dislike(youtube)

def add_comment(youtubevideo, username, comment_text):
	comments = {"Username": comment_text}



