class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        final_list = []
        max_total = float('inf')
        
        # Convert list2 to a set for faster lookup
        set_list2 = set(list2)
        
        for j, restaurant in enumerate(list1):
            if restaurant in set_list2:
                i = list2.index(restaurant)
                total_index = i + j
                if total_index < max_total:
                    max_total = total_index
                    final_list = [restaurant]
                elif total_index == max_total:
                    final_list.append(restaurant)
                    
        return final_list

