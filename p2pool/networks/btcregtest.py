from p2pool.bitcoin import networks

PARENT = networks.nets['btcregtest']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 60*60//10 # shares
REAL_CHAIN_LENGTH = 60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = '5ad2c6ecbd7d9372'.decode('hex')
PREFIX = '8f2c8d54b3278bc8'.decode('hex')
P2P_PORT = 19444
MIN_TARGET = 0
MAX_TARGET = 2**256//2 - 1
PERSIST = False
WORKER_PORT = 19443
BOOTSTRAP_ADDRS = []
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: None if 100000 <= v else 'Bitcoin version too old. Upgrade to 0.11.2 or newer!' # not a bug. BIP65 support is ensured by SOFTFORKS_REQUIRED
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit', 'segwit2x'])
MINIMUM_PROTOCOL_VERSION = 3200
SEGWIT_ACTIVATION_VERSION = 15
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
# Some networks have block inclusion/order rules that p2pool doesn't understand (e.g. Litecoin's MWEB)
IMMUTABLE_BLOCKS = False
