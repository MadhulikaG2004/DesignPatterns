class Amplifier:
    def on(self): print("Amplifier: Powering on.")
    def off(self): print("Amplifier: Shutting down.")
    def set_volume(self, level): print(f"Amplifier: Volume set to {level}.")

class DvdPlayer:
    def on(self): print("DVD Player: Powering on.")
    def off(self): print("DVD Player: Shutting down.")
    def play(self, movie): print(f"DVD Player: Playing '{movie}'.")
    def stop(self): print("DVD Player: Stopped.")

class Projector:
    def on(self): print("Projector: Warming up.")
    def off(self): print("Projector: Cooling down.")
    def wide_screen_mode(self): print("Projector: Widescreen mode enabled.")

class SmartLights:
    def dim(self, level): print(f"Lights: Dimmed to {level}%.")
    def on(self): print("Lights: Full brightness.")

class StreamingService:
    def connect(self): print("Streaming: Connected to service.")
    def disconnect(self): print("Streaming: Disconnected.")
    def stream(self, movie): print(f"Streaming: Now streaming '{movie}'.")

# --- Facade ---

class HomeTheaterFacade:
    def __init__(self, amp, dvd, projector, lights, streaming):
        self.amp = amp
        self.dvd = dvd
        self.projector = projector
        self.lights = lights
        self.streaming = streaming

    def watch_movie(self, movie):
        print(f"\n--- Preparing to watch: {movie} ---")
        self.lights.dim(15)
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_volume(20)
        self.streaming.connect()
        self.streaming.stream(movie)
        print("--- Enjoy the movie! ---\n")

    def end_movie(self):
        print("\n--- Shutting down home theater ---")
        self.streaming.disconnect()
        self.amp.off()
        self.projector.off()
        self.lights.on()
        print("--- Home theater off ---\n")

# --- Client ---

if __name__ == "__main__":
    amp = Amplifier()
    dvd = DvdPlayer()
    projector = Projector()
    lights = SmartLights()
    streaming = StreamingService()

    theater = HomeTheaterFacade(amp, dvd, projector, lights, streaming)

    theater.watch_movie("Interstellar")
    theater.end_movie()