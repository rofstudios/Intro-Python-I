"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append(dict(lat=123, lon=456, name="4th Place"))
print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
waypoints[0]['lon'] = -130
waypoints[0]['name'] = 'not a real place'

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
# asd = {'test': 1, 'test2': 2}
# for v in asd.items


# for v in waypoints:
#     # print("\nlat: %2f" % )
#     print(v['lat'])
#     print(v['lon'])
#     print(v['name'])

for w in waypoints:
    print("\nWaypoint:")
    for k, v in w.items():
        print("{0}: {1}".format(k, v))
        # print("\nWaypoint: %s: %f" % (k,v))
        # print("%s: %s" % (k,v))