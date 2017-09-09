import PIthon  
  
PIConnector.connect_to_Server("Server")  
value, timestamp = PIConnector.get_tag_snapshot('sinusoid')  
print('Timestamp: {0} Value: {1}'.format(timestamp, value))  