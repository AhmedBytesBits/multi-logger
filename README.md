# multi-logger
A multi-channel configurable logger 

### Installation
`pip install --upgrade multi-channel`

### Usage:
```python
from multilogger import Log

l = Log(
        aws_key=['your aws key'],
        aws_secret=['your aws secret'],
        aws_region=['region for your cloudwatch'],
        cloudwatch_group=['name of cloudwatch group'],
        cloudwatch_stream=['name of cloudwatch stream'],
        logfile=['path to file'],
        loge_level=['python logging level'],
        mode=['prod or dev']
).getLogger()

l.debug('this is a debug msg shown for level debug only')
l.info('this is an info msg shown for debug level and after')
l.warning('this is a warning msg shown for info level and after')
l.error('this is an error msg shown for warning level and after')
l.critical('this is a critical msg shown for critical level and after')
```

If you choose 'dev' mode then log entries will be only shown to console and saved to logfile.

In 'prod' mode, log entries are pushed to cloudwatch according to the defined credntials, group and stream

