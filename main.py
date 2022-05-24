##
# main.py

from concurrent.futures import thread
from PySide6 import QtWidgets
import pygame
from colours import RGB
import threading


class Simulation:
    def __init__(self, size: tuple[int, int]):
        self.size = size


        # Create pygame objects for actually doing the stuff
        # Screen created later so we dont have a random frozen window
        self.screen = None
        self.clock = pygame.time.Clock()

        self.running = False
        self.simulating = False

    # Constant
    @property
    def framerate(self):
        return 60

    def _process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

                # return early bc we dont have to bother with the other stuff
                return

    def start(self):
        """
        Creates an actual pygame window with the stuff but it doesnt actually
        run the simulation
        """
        self.screen = pygame.display.set_mode(self.size)

        self.running = True
        while self.running:
            events = pygame.event.get()
            print(events)
            self._process_events(events)

            # Clear screen
            self.screen.fill(RGB.WHITE)

            # Do stuff

            # Refresh
            pygame.display.flip()
            self.clock.tick(self.framerate)

        pygame.quit()


class ControlWindow(QtWidgets.QMainWindow):
    def __init__(self, simulation: Simulation, *args):
        super().__init__(*args)
        self.simulation = simulation
        
        # We need to thread this so that both the Qt window and Pygame window can be updated
        self.simulation_thread = None

        self.button_start_pygame = QtWidgets.QPushButton("Start Pygame window")

        self.initUI()

    def button_start_pygame_clicked(self):
        """
        Either starts or stops the simulation depending
        """
        if self.simulation.running:
            # If it isn't, something's likely gone wrong with the self.simulation.running boolean
            assert isinstance(self.simulation_thread, threading.Thread), "self.simulation_thread is somehow not a Thread"

            self.simulation.running = False
            self.simulation_thread.join()

            self.button_start_pygame.setText("Start Pygame window")
        else:
            self.simulation_thread = threading.Thread(target=self.simulation.start)
            self.simulation_thread.start()

            self.button_start_pygame.setText("Stop Pygame window")

    def initUI(self):
        self.setWindowTitle("Simulation control")

        central = QtWidgets.QWidget()
        self.setCentralWidget(central)

        main_vbox = QtWidgets.QVBoxLayout()

        self.button_start_pygame.clicked.connect(self.button_start_pygame_clicked)

        main_vbox.addWidget(self.button_start_pygame)


        central.setLayout(main_vbox)


def main():
    app = QtWidgets.QApplication()

    sim_size = (600, 400)
    sim = Simulation(sim_size)

    control_window = ControlWindow(sim)

    control_window.show()
    app.exec()


if __name__ == "__main__":
    main()
