class thermo:
    def __init__(self, temp):
        self.temp = temp
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            if self.temp >= 41:
                print("CRITICAL TEMPERATURE! " + str(self.temp) + "°C")
            elif self.temp >= 37:
                print("FEVER! " + str(self.temp) + "°C")
            else:
                print("NORMAL TEMPERATURE " + str(self.temp) + "°C")
        else:
            print("Thermometer is off. Can't show status.")
            
def main():
    thermo1 = thermo(36.5)
    thermo1.show_status()
    thermo1.turn_on()
    thermo1.show_status()
    thermo1.temp = 38.2
    thermo1.show_status()
    thermo1.temp = 41.5
    thermo1.show_status()
    thermo1.turn_off()
    thermo1.show_status()

if __name__ == "__main__": 
    main()