import logging


logging.basicConfig(filename='logfile.txt',
                    format='%(asctime)s - %(name)s - '
                           '%(levelname)s - line_number: %(lineno)d - '
                           'thread_id: %(thread)d - '
                           'process_id: %(process)d - %(module)s: %(message)s',
                    level=10
                    )
logging.debug('debug')
logging.info('info')
logging.error('error')


































