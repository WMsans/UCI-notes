# Problem 2

If attributes were able to be initialized anywhere within the class rather than all in `__init__`, then the existence of the attribute would become dependent on the sequence of methods that get called on the object after its creation. If a method accessed an attribute before the method that creating it, it would raise an `AttributeError` every time it was invoked.
