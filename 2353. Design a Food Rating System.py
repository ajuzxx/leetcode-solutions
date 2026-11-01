from collections import defaultdict
import heapq
class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        self.food_to_rating = {}
        self.food_to_cuisine = {}
        self.cuisine_to_heap = defaultdict(list)

        for food,rating,cuisine in zip(foods,ratings,cuisines):
            self.food_to_rating[food] = rating
            self.food_to_cuisine[food] = cuisine
            heapq.heappush(self.cuisine_to_heap[cuisine],(-rating,food))

        

    def changeRating(self, food, newRating):
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[cuisine],(-newRating,food))
        

    def highestRated(self, cuisine):
        while self.cuisine_to_heap[cuisine][0][0]!= - self.food_to_rating[self.cuisine_to_heap[cuisine][0][1]]:
            heapq.heappop(self.cuisine_to_heap[cuisine])

        return self.cuisine_to_heap[cuisine][0][1]
        

        
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)