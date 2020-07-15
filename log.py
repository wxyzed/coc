
from __future__ import print_function
import logging
import sys
import coc

def create_evidence():
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)

    msg_fmt = logging.Formatter("%(asctime)-15s %(funcName)-20s"
                                "%(levelname)-8s %(message)s")

    strhndl = logging.StreamHandler(sys.stdout)
    strhndl.setFormatter(fmt=msg_fmt)

    fhndl = logging.FileHandler(__file__ + ".log", mode='a')
    fhndl.setFormatter(fmt=msg_fmt)

    logger.addHandler(strhndl)
    logger.addHandler(fhndl)

    logger.info("Evidence was created {}".format(my_file_name))

def create_hash():
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)

    msg_fmt = logging.Formatter("%(asctime)-15s %(funcName)-20s"
                                "%(levelname)-8s %(message)s")

    strhndl = logging.StreamHandler(sys.stdout)
    strhndl.setFormatter(fmt=msg_fmt)

    fhndl = logging.FileHandler(__file__ + ".log", mode='a')
    fhndl.setFormatter(fmt=msg_fmt)

    logger.addHandler(strhndl)
    logger.addHandler(fhndl)

    logger.info("Hash was created {}".format(my_hash))
