import requests
# using requests library
try:
    time = requets.get('https://pgorelease.nianticlabs.com/plfe/').elapsed.total_seconds()
    if time < 3:
        print "Go! catch them all!"
    else:
        print "Servers are down, go back to work"
except:
    print "Go! Cacth them all!"
