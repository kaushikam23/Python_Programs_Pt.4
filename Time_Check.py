class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def print_time(self):
        print(self.hours,":",self.minutes,":",self.seconds)

    def is_after(self, t2):
        if self.hours > t2.hours:
            return True
        elif self.hours == t2.hours and self.minutes > t2.minutes:
            return True
        elif self.hours == t2.hours and self.minutes == t2.minutes and self.seconds > t2.seconds:
            return True
        else:
            return False

    def increment(self, sec):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + sec
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60
        

time_obj = Time(2,30,45)
time_obj.print_time()
new_time_obj = Time(3,30,50)
print(time_obj.is_after(new_time_obj))
time_obj.increment(120)
time_obj.print_time()
