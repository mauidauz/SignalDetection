import scipy.stats as stats

class SignalDetection:
    def __init__(self, hit_rate, false_alarm_rate):
        """
        Initialize SignalDetection with hit rate and false alarm rate.

        Parameters:
            hit_rate (float): Proportion of hits (true positives).
            false_alarm_rate (float): Proportion of false alarms (false positives).
        """
        self.hit_rate = hit_rate
        self.false_alarm_rate = false_alarm_rate

    def d_prime(self):
        """
        Calculate d-prime, a measure of sensitivity in signal detection theory.

        Returns:
            float: The d-prime value.
        """
        # Convert hit rate and false alarm rate to z-scores
        z_hit = stats.norm.ppf(self.hit_rate)
        z_false_alarm = stats.norm.ppf(self.false_alarm_rate)

        # Calculate d-prime
        return z_hit - z_false_alarm

    def criterion(self):
        """
        Calculate criterion (c), which measures the decision threshold in signal detection theory.

        Returns:
            float: The criterion value.
        """
        # Convert hit rate and false alarm rate to z-scores
        z_hit = stats.norm.ppf(self.hit_rate)
        z_false_alarm = stats.norm.ppf(self.false_alarm_rate)

        # Calculate criterion
        return -0.5 * (z_hit + z_false_alarm)

# Example usage
if __name__ == "__main__":
    hit_rate = 0.85
    false_alarm_rate = 0.15

    sd = SignalDetection(hit_rate, false_alarm_rate)

    print(f"d-prime: {sd.d_prime():.2f}")
    print(f"criterion: {sd.criterion():.2f}")
