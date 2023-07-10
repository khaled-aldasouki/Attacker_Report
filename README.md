# ATTACKER_REPORT
A simple Linux tool used to get a quick report of failed SSH2 connection attempts from a log file

## NOTICE
-This script was written for Linux machines using CentOS and may run differently on other distros.
-The script uses regular expressions to identify failed attempts, meaning that it may not hold accurate results based on your system and the log file you're reporting.
-The script uses ipapi to find the geological location of the source IP, therefore please make sure you are connected to the internet before running the script.
-A sample file is provided for testing. 

## USAGE 
1. Download the latest release
2. Run <i>Attacker_Report.py</i> using your preferred IDE or Python interpretor
3. Enter the name/path of the log file you wish to report
4. You will get a report of each IP address, the number of failed attempts and its geological location shortname
