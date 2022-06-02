from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser

free1 = FreeUser('Jake', 'hilljake93@gmail.com', '1234567', 'biology', 1993)
prem1 = PremiumUser('Kate', 'khill734@gmail.com', '7654321', 'education', 1992)

free1.create_post('this is a free user title', 'this is the body for the free user', '4:30')
free1.create_post('this is another free user title', 'this is the second body for the free user', '4:20')
free1.create_post('this is another free user title', 'this is the second body for the free user', '2:20')
# prem1.create_post('this is a premium user title', 'this is the body for the premium user', '8:15')

# print((free1.posts_by_user_dict["Jake"][0]))
# print((free1.posts_by_user_dict["Jake"][1]))
print(free1.posts_by_user_dict)