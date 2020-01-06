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
        log.info("robot initialized")  
        self.encoderInit(7, 5, True, 1, 1, 50, .5, .5, .5, 0, self.motor, 50, -4092, 4092, -1, 1) #Most numbers should be checked, especially PIDF. Distance per pulse should be determined in degrees (makes sense)
#                                              ^  PIDF     ^
    def encoderInit(self, A, B, Reverse, distPerPulse, minRate, maxPeriod, P, I, D, F, motor, period, minInput, maxInput, minOutput, maxOutput):
        """Creates an encoder object using two channel parameters, creates a PID controller
        with multiple parameters, and is ready for PID loop"""
        self.encoder = wpilib.Encoder(aChannel = A, bChannel = B)
        self.encoder.setName("Encoder1")
        self.encoder.setReverseDirection(Reverse) #If reversed, positive is considered forward. May change.
        self.encoder.setDistancePerPulse(distPerPulse)
        self.encoder.setMinRate(minRate)
        self.encoder.setMaxPeriod(maxPeriod)

#        self.PIDcontrol = wpilib.PIDController(P, I, D, F, self.encoder, motor, period)
#        self.PIDcontrol.setInputRange(minInput, maxInput)
#        self.PIDcontrol.setContinuous()
#        self.PIDcontrol.setOutputRange(minOutput, maxOutput)
#        self.PIDcontrol.enable()
    def resetEncoder(self):
        self.encoder.reset()
    def setSpeed(self, rate = 0):
        """rate should be between -360 and 360, probably needs modification"""
        #self.PIDcontrol.setSetpoint(self.encoder.getDistance()+rate)
    def operatorControl(self):
        self.encoder.reset()
        log.info("operator control")
        while self.isOperatorControl and self.isEnabled:
            rate = self.controller.getRawAxis(1)*360
            log.debug("encoder position is %f", self.encoder.getDistance())
            wpilib.Timer.delay(.1)
            self.setSpeed(rate)

if __name__ == "__main__":
    main()