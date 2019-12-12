import wpilib
import logging
import ctre

log = logging.getLogger("console")
log.setLevel(logging.DEBUG)
def main():
    wpilib.run(MyRobot)

class MyRobot(wpilib.SampleRobot):

    def robotInit(self):
        self.controller = wpilib.Joystick(0)
        self.motor = ctre.WPI_TalonSRX(0)
        self.pwMotor = wpilib.PWMSpeedController(0)
        log.info("robot initialized")

    def operatorControl(self):
        log.info("operator control")
        while self.isOperatorControl and self.isEnabled:
            log.debug("joystick is %f y %f x", self.controller.getY(), self.controller.getX())
            wpilib.Timer.delay(.1)
            self.motor.set(self.controller.getY())
            self.pwMotor.set(self.controller.getX())

if __name__ == "__main__":
    main()