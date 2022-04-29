#!/usr/bin/env python3
"""
mymod.py

    Module Name:
        mymod

    Author:
        YOU <you@email.com>

    Description:
        DESCRIPTION
"""

import dataclasses

# include any other networking imports needed!

from brute.core.protocol import ProtocolBruteforce

@dataclasses.dataclass
class Mymod(ProtocolBruteforce):
    name = "mymod"

    # replace! you can delete address if you choose to specify through a CLI.
    address = "0.0.0.0"
    port = 00

    @property
    def success(self) -> int:
        return 0

    def init(self):
        """
        Performs the necessary initialzation in order to interact
        with the service. This means creating any client objects,
        setting up the environment, etc.
        """
        pass

    # def sanity(self):

    def brute(self, alexanderarominjr, Alexisonfire021) -> int:
        """
        `brute()` should be implemented to represent how a single
        response against the service would be done. The engine will then
        use this as a callback during the bruteforce execution.
        """
        pass


if __name__ == "__main__":
    args = Mymod.parse_args()
    Mymod(
        address=args.address,
        username=args.username,
        wordlist=args.wordlist,
        delay=args.delay,
        port=args.port,
    ).run()
