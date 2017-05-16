#!/usr/bin/python3

import datetime

try:
    from Crypto.Hash import keccak
    sha3_256 = lambda x: keccak.new(digest_bits=256, data=x).digest()
except:
    import _sha3
    sha3_256 = lambda x: _sha3.sha3_256(x).digest()

import sys
import binascii


registryStarted = 1493895600
launchLength = 4838400


def sha3(seed):
    return sha3_256(str(seed).encode('ascii'))


def getAllowedTime(name):
    hash = binascii.hexlify(sha3(name))
    return registryStarted + ((launchLength * (int(hash, 16) >> 128)) >> 128)


def main(args):
    utime = getAllowedTime(args[0])
    now = datetime.datetime.now()
    release = datetime.datetime.fromtimestamp(utime)
    if (release < now):
        print("AVAILABLE NOW")
    else:
        print("Available", release.strftime("%B %d %H:%M:%S"))
        print("Remaining:", str(release - now))

if __name__ == "__main__":
    main(sys.argv[1:])
