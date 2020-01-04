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
        log.info("robot initialized")  
        self.encoderInit(1, 0, True, 0, 1, 50, 1, 1, 1, 0, self.motor, 50, -360, 360, -1, 1) #Most numbers should be checked, especially PIDF. Distance per pulse should be determined in degrees (makes sense)
#                                              ^  PIDF  ^
    def encoderInit(self, A, B, Reverse, distPerPulse, minRate, maxPeriod, P, I, D, F, motor, period, minInput, maxInput, minOutput, maxOutput):
        """Creates an encoder object using two channel parameters, creates a PID controller
        with multiple parameters, and is ready for PID loop"""
        self.encoder = wpilib.Encoder(A, B)
        self.encoder.setReverseDirection(Reverse) #If reversed, positive is considered forward. May change.
        self.encoder.setDistancePerPulse(distPerPulse)
        self.encoder.setMinRate(minRate)
        self.encoder.setMaxPeriod(maxPeriod)

        self.PIDcontrol = wpilib.PIDController(P, I, D, F, self.encoder, motor, period)
        self.PIDcontrol.setInputRange(minInput, maxInput)
        self.PIDcontrol.setContinuous()
        self.PIDcontrol.setOutputRange(minOutput, maxOutput)
        self.PIDcontrol.enable()
    def resetEncoder(self):
        self.encoder.reset()
    def setSpeed(self, rate = 0):
        """rate should be between -360 and 360, probably needs modification"""
        self.PIDcontrol.setSetpoint(self.encoder.getDistance()+rate)
    def operatorControl(self):
        log.info("operator control")
        while self.isOperatorControl and self.isEnabled:
            log.debug("joystick is %f y", self.controller.getY())
            wpilib.Timer.delay(.1)
            rate = self.controller.getY()*360
            self.setSpeed(rate)

if __name__ == "__main__":
    main()