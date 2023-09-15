from insta_follower import InstaFollower


ACCOUNT_TO_FOLLOW = ""
USERNAME = ""
PASSWORD = ""

bot = InstaFollower()
bot.login(username=USERNAME, password=PASSWORD)
bot.find_followers(similar_account=ACCOUNT_TO_FOLLOW)
bot.follow()

bot.driver.quit()
