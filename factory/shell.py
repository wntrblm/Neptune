# Copyright (c) 2024 Alethea Katherine Flowers.
# Published under the standard MIT License.
# Full text available at: https://opensource.org/licenses/MIT

import statistics
import time

import numpy as np
from wintertools import reportcard, thermalprinter, oscilloscope, waveform
from wintertools.print import print
from hubble import Hubble
import IPython

from libneptune import NeptuneLens, CCW, CW, CENTER

hubble = Hubble()
lens = NeptuneLens(hubble)
scope = oscilloscope.Oscilloscope()

lens.reset()
IPython.embed()
