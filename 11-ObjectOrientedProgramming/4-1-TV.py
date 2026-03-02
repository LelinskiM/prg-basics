# tv.py file
# class definition
class TV:
   def __init__(self):
      self.channels = []
      self.channel_No = 1
      self.is_on = False
   def turn_off(self):
        self.is_on = False
   def turn_on(self):
        self.is_on = True
   def show_Status(self):
        if self.is_on:
            print("TV is on " + "- Channel No " + str(self.channel_No))
        else:
            print("TV is off")
   def set_Chan(self,NChannel_No):
       if self.is_on:
           self.channel_No = NChannel_No
       else:
           print("TV is off. Can't change channel.")
   def set_Chanels(self,Chanels):
        if self.is_on:
            self.channels = Chanels
        else:
            print("TV is off. Can't set channels.")
   def show_chanels(self):
       if self.is_on:
           for i, channel in enumerate(self.channels):
                print(f"{i+1}. {channel}")
# tv_show.py file
# main program

def main():
   # object creation
   tv = TV()

   # object usage
   tv.show_Status()
   tv.turn_on()
   tv.show_Status()
   tv.show_chanels()
   tv.set_Chanels(["TVP1", "TVP2", "Polsat", "TVN", "FilmBox", "Discovery"])
   tv.show_chanels()
   tv.set_Chan(5)
   tv.show_Status()
   tv.turn_off()
   tv.show_Status()

if __name__ == "__main__":
   main() 