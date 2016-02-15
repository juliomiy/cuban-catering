"""TODO flesh this out. Currently a mockup to test a concept of location
"""
import random
class LocationServices:
def get_current_location():
    location_dict = {}
    #Germantown
    location_dict[0] = {"lat": 42.1342562,
                     "long":  -73.871242
                       }
    #hudson
    location_dict[1] = {"lat": 42.251476,
                        "long": -73.7862366
                       }
    #livingston
    location_dict[2] = {"lat": 42.1398114,
                        "long": -73.7870721
                        }
    maxkey = len(location_dict)
    if maxkey:
      index = random.randint(0,maxkey - 1)
      return location_dict[index]
