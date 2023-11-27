class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """create a new instance of a SerialGenerator object"""
        self.start = start
        self.times_run = 0

    def generate(self):
        """generates serial number based on # of times run, then increments
            times run an returns the serial number that was generated"""
        serial_number = self.start + self.times_run
        self.times_run += 1
        return serial_number

    def reset(self):
        """resets times run to 0"""
        self.times_run = 0
