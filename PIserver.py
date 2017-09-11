import PIthon

import sys
import clr   
sys.path.append('C:\\Program Files (x86)\\PIPC\\AF\\PublicAssemblies\\4.0\\')  
clr.AddReference('OSIsoft.AFSDK')

from OSIsoft.AF.PI import *  
from OSIsoft.AF.Search import *  
from OSIsoft.AF.Asset import *  
from OSIsoft.AF.Data import *  
from OSIsoft.AF.Time import *
  
PIthon.connect_to_Server("Server")  
value, timestamp = PIthon.get_tag_snapshot('sinusoid')  
print('Timestamp: {0} Value: {1}'.format(timestamp, value))
