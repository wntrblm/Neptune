from ._descriptors import CVDescriptor, KnobDescriptor, SwitchDescriptor

CW = KnobDescriptor.CW
CCW = KnobDescriptor.CCW
CENTER = KnobDescriptor.CENTER


class NeptuneLens:
    cutoff_knob = KnobDescriptor("IO3", "IO4")
    fm1_knob = KnobDescriptor("IO7", "IO8")
    fm1_cv = CVDescriptor("VOUT2A")
    fm2_knob = KnobDescriptor("IO9")
    fm2_cv = CVDescriptor("VOUT1B")
    hp_vol_knob = KnobDescriptor("IO2")
    hp_jack_to_dac = SwitchDescriptor("IO12")
    hp_jack_to_fg = SwitchDescriptor("IO13")
    lp_vol_knob = KnobDescriptor("IO1")
    lp_jack_to_dac = SwitchDescriptor("IO10")
    lp_jack_to_fg = SwitchDescriptor("IO11")
    reso_knob = KnobDescriptor("IO5")
    reso_cv = CVDescriptor("VOUT3A")
    salt_knob = KnobDescriptor("IO6")
    salt_cv = CVDescriptor("VOUT4A")
    vol_cv = CVDescriptor("VOUT2B")
    vol_jack_to_dac = SwitchDescriptor("IO14")

    def __init__(self, hubble):
        self.hubble = hubble

    def reset(self):
        self.cutoff_knob = CENTER
        self.fm1_knob = CENTER
        self.fm1_cv = 0
        self.fm2_knob = CCW
        self.fm2_cv = 0
        self.hp_vol_knob = CCW
        self.hp_jack_to_dac = False
        self.hp_jack_to_fg = False
        self.lp_vol_knob = CCW
        self.lp_jack_to_dac = False
        self.lp_jack_to_fg = False
        self.reso_knob = CCW
        self.reso_cv = 0
        self.salt_knob = CCW
        self.salt_cv = 0
        self.vol_cv = 0
        self.vol_jack_to_dac = False

    def knob_tests_low_pass_fully_open(self):
        self.reset()
        self.lp_vol_knob = CW
        self.cutoff_knob = CW
        self.lp_jack_to_fg = True

    def knob_tests_low_pass_centered(self):
        self.reset()
        self.lp_vol_knob = CW
        self.cutoff_knob = CENTER
        self.lp_jack_to_fg = True

    def knob_tests_low_pass_fully_closed(self):
        self.reset()
        self.lp_vol_knob = CW
        self.cutoff_knob = CCW
        self.lp_jack_to_fg = True

    def knob_tests_high_pass_fully_open(self):
        self.reset()
        self.hp_vol_knob = CW
        self.cutoff_knob = CCW
        self.hp_jack_to_fg = True

    def knob_tests_high_pass_centered(self):
        self.reset()
        self.hp_vol_knob = CW
        self.cutoff_knob = CENTER
        self.hp_jack_to_fg = True

    def knob_tests_high_pass_fully_closed(self):
        self.reset()
        self.hp_vol_knob = CW
        self.cutoff_knob = CW
        self.hp_jack_to_fg = True

    def knob_tests_resonant_low_pass(self):
        self.reset()
        self.lp_vol_knob = CW

        # Use the FM1 CV to get a specific frequency that helps us identify
        # the resonance
        self.cutoff_knob = CCW
        self.fm1_knob = CW
        self.fm1_cv = 4.0

        self.reso_knob = CW
        self.lp_jack_to_fg = True

    def knob_tests_salty_low_pass(self):
        self.reset()
        self.lp_vol_knob = CW

        # Use the FM1 CV to get a specific frequency that helps us identify
        # the feedback distortion
        self.cutoff_knob = CCW
        self.fm1_knob = CW
        self.fm1_cv = 4.0

        self.salt_knob = CW
        self.lp_jack_to_fg = True

    def knob_tests_self_oscillation(self):
        self.reset()
        self.cutoff_knob = CENTER
        self.reso_knob = CW

    def cv_tests_fm1_full(self):
        self.reset()
        self.lp_vol_knob = CW
        self.cutoff_knob = CCW
        self.fm1_knob = CW
        self.fm1_cv = +5.0
        self.lp_jack_to_fg = True

    def cv_tests_fm1_full_inversion(self):
        self.reset()
        self.lp_vol_knob = CW
        self.cutoff_knob = CW
        self.fm1_knob = CCW
        self.lp_jack_to_fg = True
        self.fm1_cv = +5.0

    def cv_tests_fm2_fully_open(self):
        self.reset()
        self.lp_vol_knob = CW
        self.cutoff_knob = CCW
        self.fm2_knob = CW
        self.lp_jack_to_fg = True
        self.fm2_cv = +5.0

    def cv_tests_vol_vca(self):
        self.reset()
        self.lp_vol_knob = CW
        self.cutoff_knob = CW
        self.lp_jack_to_fg = True
        self.vol_jack_to_dac = True
        self.vol_cv = +2.5

    def cv_tests_resonant_low_pass(self):
        self.reset()
        self.lp_vol_knob = CW
        self.cutoff_knob = CCW
        self.fm1_knob = CW
        self.fm1_cv = 4.0
        self.reso_cv = 7.8
        self.lp_jack_to_fg = True

    def cv_tests_salty_low_pass(self):
        self.reset()
        self.lp_vol_knob = CW
        self.cutoff_knob = CCW
        self.fm1_knob = CW
        self.fm1_cv = 4
        self.salt_cv = 5
        self.lp_jack_to_fg = True

    def cv_tests_self_oscillation(self):
        self.reset()
        self.cutoff_knob = CENTER
        self.reso_cv = +4.5
