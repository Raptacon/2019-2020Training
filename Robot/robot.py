import wpilib
import logging
import ctre

log = logging.getLogger("console")
log.setLevel(logging.DEBUG)
def main():
    wpilib.run(MyRobot)

class MyRobot(wpilib.SampleRobot):

    def robotInit(self):
        self.controller = wpilib.XboxController(0)
        self.motor = ctre.WPI_TalonSRX(1)
        self.motor.setQuadraturePosition(0)
        log.info("robot initialized")  
        self.encoderInit(.5, .5, .5, 0, self.motor, 50, -4092, 4092, -1, 1) #Most numbers should be checked, especially PIDF. Distance per pulse should be determined in degrees (makes sense)
#                                                      ^  PIDF     ^
    def encoderInit(self, P, I, D, F, motor, period, minInput, maxInput, minOutput, maxOutput):
        """Creates an encoder object using two channel parameters, creates a PID controller
        with multiple parameters, and is ready for PID loop"""
        self.motor.set(mode = self.motor.ControlMode.Position, demand0 = 0)


    def setSpeed(self, rate = 0):
        """rate should be between -360 and 360, probably needs modification"""
        #self.PIDcontrol.setSetpoint(self.encoder.getDistance()+rate)

    def operatorControl(self):
        log.info("operator control")
        while self.isOperatorControl and self.isEnabled:
            rate = self.controller.getRawAxis(1)*4092
            log.debug("position: %f, rate: %f", self.motor.getQuadraturePosition(), rate)
            wpilib.Timer.delay(.1)
            self.motor.set(mode = self.motor.ControlMode.Position, demand0 = rate)
if __name__ == "__main__":
    main()