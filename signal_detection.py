from scipy.stats import norm

class Signal_Detection: 
    def __init__(self, hits, misses, falseAlarm, correctRejections):
        self.hits = hits
        self.misses = misses
        self.falseAlarm = falseAlarm
        self.correctRejections = correctRejections

    def d_prime(self):
        h = self.hits / (self.hits + self.misses)
        FA = self.falseAlarm / (self.falseAlarm + self.correctRejections)
        
        zH = norm.ppf(h)
        zFA = norm.ppf(FA)
        
        d_prime_value = zH - zFA
        print("d-prime:", d_prime_value)  # Fixed indentation
        return d_prime_value

    def criterion(self):
        h = self.hits / (self.hits + self.misses)
        FA = self.falseAlarm / (self.falseAlarm + self.correctRejections)
        
        zH = norm.ppf(h)
        zFA = norm.ppf(FA)
        
        criterion_value = -0.5 * (zH + zFA)
        print("Criterion:", criterion_value)
        return criterion_value

sd = Signal_Detection(hits=10, misses=2, falseAlarm=3, correctRejections=15)

d_prime_value = sd.d_prime()
criterion_value = sd.criterion()

