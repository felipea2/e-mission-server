""" Query modules mapping functions to their query strings
structured:

module_name { query_string: function_for_query }

"""

modules = {
   # Trip Module
   'trips': {
   'get top': getTopTrips,
   'get all': getAllTrips,
   'get most recent': getRecentTrips},

   'utility': {},
   'pertubation': {}
 }

#returns the top trips for the user, defaulting to the top 10 trips
def getTopTrips(uid, options = 10):
    return []

#returns all trips to the user
def getAllTrips(uid):
    return []

def getRecentTrips(uid, options=10):
    return []
