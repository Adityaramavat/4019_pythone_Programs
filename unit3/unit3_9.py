from abc import ABC, abstractmethod

# 1. Create the "Interface"
# We make it an interface by ensuring it ONLY contains abstract methods and no actual code.
class MediaPlayerInterface(ABC):
    
    @abstractmethod
    def play(self):
        pass
        
    @abstractmethod
    def stop(self):
        pass

# 2. Utilize the interface in another class
class AudioPlayer(MediaPlayerInterface):
    
    # We MUST implement the play() method
    def play(self):
        print("Playing the audio file.")
        
    # We MUST implement the stop() method
    def stop(self):
        print("Stopping the audio.")

# Create an object of the class that utilized the interface
my_player = AudioPlayer()

# Call the methods
my_player.play()
my_player.stop()