import logging

from acmepack.core import Nucleus

log = logging.getLogger('demo')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)12s %(levelname)5s %(threadName)s - %(message)s',
                        datefmt="%a %d %H:%M:%S")
    log.info('Initializing nucleus with no arguments')
    n = Nucleus()

    count = 3
    result = n.test(count)
    log.debug('Nucleic status for %i items is %s', count, result)
    log.info('That is all, folks!')
