from p2pool.bitcoin import networks

PARENT = networks.nets['cyberyen']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 4*60*60//10 # shares
REAL_CHAIN_LENGTH = 4*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
P2P_PORT = 9326
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 9327
BOOTSTRAP_ADDRS = [
        'dnsseed.cyberyen.work',
        ]
ANNOUNCE_CHANNEL = '#p2pool-ltc'
VERSION_CHECK = lambda v: None if 100400 <= v else 'Cybeyen version too old. Upgrade to 0.21.2 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit', 'taproot', 'mweb'])
MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
# Some networks have block inclusion/order rules that p2pool doesn't understand (e.g. Litecoin's MWEB)
IMMUTABLE_BLOCKS = True
