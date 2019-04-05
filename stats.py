class Stats:
    def __init__(self, stre=10, stam=10, spd=10, skl=10, sag=10, smt=10):
        self.str = stre
        self.stam = stam
        self.spd = spd
        self.skl = skl
        self.sag = sag
        self.smt = smt


class SecondaryStats:
    def __init__(self, atp=0, dfp=0, dmg=0, res=0, tou=0, wil=0, pwr=0, vis=0):
        self.atp = atp
        self.dmg = dmg
        self.dfp = dfp
        self.res = res
        self.tou = tou
        self.wil = wil
        self.pwr = pwr
        self.vis = vis


class Vitals:
    def __init__(self, base_edr: float, base_vit: float, edr_mult=2.0, vit_mult=2.0):
        self.base_edr = base_edr
        self.base_vit = base_vit
        self.vit = base_vit * vit_mult
        self.edr = base_edr * edr_mult
        self.edr_mult = edr_mult
        self.vit_mult = vit_mult
        self.alive = True

    @property
    def max_vit(self):
        return self.vit_mult * self.base_vit

    @property
    def max_edr(self):
        return self.edr_mult * self.base_edr
