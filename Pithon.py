"""
functions to connect to the PI server and fetch the current tag value

"""

def connect_to_Server(serverName):  
    piServers = PIServers()  
    global piServer  
    piServer = piServers[serverName]  
    piServer.Connect(False)  
  
def get_tag_snapshot(tagname):  
    tag = PIPoint.FindPIPoint(piServer, tagname)  
    lastData = tag.Snapshot()  
    return lastData.Value, lastData.Timestamp  