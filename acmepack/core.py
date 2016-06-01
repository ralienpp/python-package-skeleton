'''This module is just a skeleton demo with no intellectual payload whatsoever'''

class Nucleus(object):
    '''Skeleton class'''
    def __init__(self, dummy='nothing'):
        '''Initialize the nucleus with a dummy value
        :param dummy:   a string that will be used inside `test`'''
        self.dummy = dummy

    def test(self, number):
        '''This function replicates the dummy value several times
        :param number:    int, how many times to replicate
        :returns:         string'''
        return self.dummy * number
