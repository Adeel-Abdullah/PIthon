#Automated data extraction from the OSIsoft PI server
A simple python script to extract data from the OSIsoft pi server. This script uses the piconfig utility that accompanies the PI system for data extraction through the command line.

##Usage instructions
Simply add a text file with the name of tags.txt at the same path as the path of this script, with each tag name on a differet line. The script will take the dates given in the code and break requests down into smaller chunks and then fetch data from PI server so as not to bypass the arcmaxcollect limit.