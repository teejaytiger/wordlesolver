
class letter:
    def __init__(self, alpha, color=None):
        self.color = None
        self.alpha = alpha
        if color:
            c = str(color).upper()
            if c == "G" or c == "GREEN":
                self.color = "G"
            if c == "Y" or c == "YELLOW":
                self.color = "Y"