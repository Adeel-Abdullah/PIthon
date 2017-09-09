import PIthon  
  
PIthon.connect_to_Server("Server")  
value, timestamp = PIthon.get_tag_snapshot('sinusoid')  
print('Timestamp: {0} Value: {1}'.format(timestamp, value))
