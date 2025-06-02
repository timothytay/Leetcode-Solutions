class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.userFollows = defaultdict(set)
        self.userTweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for user in self.userFollows[userId]:
            tweets = self.userTweets[user]
            for t in tweets:
                heapq.heappush(feed, t)
                if len(feed) > 10:
                    heapq.heappop(feed)
        tweets = self.userTweets[userId]
        for t in tweets:
            heapq.heappush(feed, t)
            if len(feed) > 10:
                heapq.heappop(feed)
        feed.sort(reverse=True)
        sortedFeed = [tweetId for timestamp, tweetId in feed]
        return sortedFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)