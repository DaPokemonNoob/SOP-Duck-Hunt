from AADFramework.ArduinoComponents import DigitalInput, DigitalOutput, ControlBoard

controller=ControlBoard('COM7')

buzzer=controller.buildDigitalOutput(10,'Buzzer')
button=controller.buildDigitalInput(9,'Button')

monitor=controller.buildInputMonitor()

controller.start()
monitor.start()

print("You can push button to sound buzzer")

while True:
    if button.getCountValue() >= 1:
        print("this button got pressed")
        break

controller.shutdown()