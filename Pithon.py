"""
functions to connect to the PI server and fetch the current tag value

"""
import sys  
sys.path.append('C:\\Program Files (x86)\\PIPC\\AF\\PublicAssemblies\\4.0\\')  
import clr  
clr.AddReference('OSIsoft.AFSDK')

from OSIsoft.AF.PI import *  
from OSIsoft.AF.Search import *  
from OSIsoft.AF.Asset import *  
from OSIsoft.AF.Data import *  
from OSIsoft.AF.Time import *

def connect_to_Server(serverName):  
    piServers = PIServers()  
    global piServer  
    piServer = piServers[serverName]  
    piServer.Connect(False)  
  
def get_tag_snapshot(tagname):  
    tag = PIPoint.FindPIPoint(piServer, tagname)  
    lastData = tag.Snapshot()  
    return lastData.Value, lastData.Timestamp  