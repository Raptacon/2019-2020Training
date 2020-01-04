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
        log.info("robot initialized")  # /  PIDF  \
        self.encoderInit(1, 0, 0, 1, 50, 1, 1, 1, 0, self.motor, 50, -360, 360, -1, 1) #Most numbers should be checked, especially PIDF. Distance per pulse should be determined in degrees (makes sense)

    def encoderInit(self, A, B, distPerPulse, minRate, maxPeriod, P, I, D, F, motor, period, minInput, maxInput, minOutput, maxOutput):
        self.encoder = wpilib.Encoder(A, B)
        self.encoder.setReverseDirection(True)
        self.encoder.setDistancePerPulse(distPerPulse)
        self.encoder.setMinRate(minRate)
        self.encoder.setMaxPeriod(maxPeriod)
        self.PIDcontrol = wpilib.PIDController(P, I, D, F, self.encoder, motor, period)
        self.PIDcontrol.setInputRange(minInput, maxInput)
        self.PIDcontrol.setContinuous()
        self.PIDcontrol.setOutputRange(minOutput, maxOutput)
        self.PIDcontrol.enable()

        self.encoder = wpilib.Encoder(0,1) #DUMMY NUMBERS PLS CHANGE BECAUSE THEY HAVE ACTUALLY NO MEANING
        log.info("encoder initialized")

    def operatorControl(self):
        log.info("operator control")
        while self.isOperatorControl and self.isEnabled:
            log.debug("joystick is %f y", self.controller.getY())
            wpilib.Timer.delay(.1)
            self.PIDcontrol.setSetpoint(self.controller.getY()*360)

            log.debug("encoder:"+str(self.encoder.get())) #This *should* get the current count if I read the docs right -Alex

if __name__ == "__main__":
    main()