This application will send a filtered List of processes to New Relic Insights with Host, CPU, Memory Usage, PID, and Commandline.  It is a Python based daemon

NRCONFIG
ProcessSearch: .*?compiz.*? is a regex of processes to push to Insights

NRURL: https://insights-collector.newrelic.com/v1/accounts/~~~~~~~~~/events is the New Relic API URL for the POST

NRINSERTKEY: ~~~~~~~~~~~~~~~~~ is the X-Insert-Key

LOGFILE: nrproc.log name of logfile

CHECKSPEEDSECS: 3 Frequency in Seconds to check processes

HOSTNAME:  (optional) Hostname is pick up from OS but this will override that action


Install is simple unzip in directory execute nrprocmain.py.  It is deamonized with the PID in tmp.  

It does require daemonize.  To install daemonize on ubuntu use pip install daemonize
[daemonize](https://pypi.python.org/pypi/daemonize/)



