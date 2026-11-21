
class Twitter:

    tweets: dict
    following: dict
    timestamp: int
    MAX_TWEETS = 10

    def __init__(self):
        self.tweets = defaultdict(set)
        self.following = defaultdict(set)
        self.timestamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].add((-self.timestamp, tweetId))
        self.following[userId].add(userId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        following_ids = self.following[userId]
        if following_ids is None:
            return []
        tweets = []
        for following_id in following_ids:
            follow_id_tweets = list(self.tweets[following_id])
            tweets.extend(follow_id_tweets)
        heapq.heapify(tweets)
        res = []
        while len(res) < self.MAX_TWEETS:
            if tweets == []:
                return res
            cur_tweet = heapq.heappop(tweets)
            res.append(cur_tweet[1])

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)
        self.following[followerId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId not in self.following[followerId]:
            return
        self.following[followerId].remove(followeeId)
        
