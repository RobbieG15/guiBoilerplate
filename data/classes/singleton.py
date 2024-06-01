# :Title: singleton.py
# :Description: Class to inherit in other classes to create singleton
# :Created: 5/31/2024
# :Last Modified: 5/31/2024
# :Author: Robert Greenslade


class Singleton(object):
    """
    Class to inherit from anywhere in the code where a singleton is needed

    Args:
        object (object): Singleton inherits from object
    """

    def __new__(cls, *args, **kwargs):
        # see if the instance is already in existence. If not, make a new one.
        if not hasattr(cls, "_singleton_instance"):
            cls._singleton_instance = super(Singleton, cls).__new__(cls)
        return cls._singleton_instance
