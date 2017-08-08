import logging

log_level = logging.DEBUG

log_format = '%(levelname) -10s %(asctime) -5d: %(message)s'
formatter = logging.Formatter(fmt=log_format)

console = logging.StreamHandler()
console.setLevel(log_level)
console.setFormatter(formatter)


class Constant:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
