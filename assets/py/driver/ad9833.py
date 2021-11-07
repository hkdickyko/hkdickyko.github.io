class AD9833(object):

    def __init__(self, spi, ss, ClockFreq=25000000):
        self.spi = spi
        self.ss = ss
        self.freq = 10000
        self.shape_word = 0x2000
        self.ClockFreq = ClockFreq

    def _bytes(self, integer):
        return divmod(integer, 0x100)

    def _send(self, data):
        high, low = self._bytes(data)
        buf = bytearray([high,low])
        self.ss.value(0)
        self.spi.write(buf)
        self.ss.value(1)

    def set_freq(self, value):
        self.freq = value

    def set_type(self, inter):
        if inter == 1:
            self.shape_word = 0x2020
        elif inter == 2:
            self.shape_word = 0x2002
        else:
            self.shape_word = 0x2000

    @property
    def shape_type(self):
        # square: 0x2020, sin: 0x2000, triangle: 0x2002
        if self.shape_word == 0x2020:
            return "Square"
        elif self.shape_word == 0x2002:
            return "Triangle"
        else:
            return "Sine"

    def send(self):
        word = hex(int(round((self.freq*2**28)/self.ClockFreq)))
        MSB = (int(word, 16) & 0xFFFC000) >> 14
        LSB = int(word, 16) & 0x3FFF
        # Set control bits DB15 = 0 and DB14 = 1; for frequency register 0
        MSB |= 0x4000
        LSB |= 0x4000
        self._send(0x2100)
        # Set the frequency
        self._send(LSB)  # lower 14 bits
        self._send(MSB)  # Upper 14 bits
        self._send(self.shape_word)