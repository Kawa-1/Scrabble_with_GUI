from __future__ import annotations
from bag import Bag


class Racks:

    bag = Bag()


    @classmethod
    def reset_bag_for_racks(cls) -> noReturn:
        """For future use to reset letters in bag"""

        Racks.bag = Bag()