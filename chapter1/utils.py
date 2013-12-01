from urlparse import urljoin
import ipdb


def print_twitter_url():
    print urljoin('http://www.twitter.com', 'mbrochh')

arg1 = 3
ipdb.set_trace()  # BREAKPOINT
arg2 = 8
ipdb.set_trace()  # breakpoint
foo = 'bar'
result = arg1 + arg2
ipdb.set_trace()  # breakpoint
print 'try to set a breakpoint before this statement'
ipdb.set_trace()  # breakpoint
print 'Good bye!'
