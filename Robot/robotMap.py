class RobotMap():
    """
    Robot map stores imutable values needed for interface with the hardware
    """
    def __init__(self):
        """intilize the robot map"""
        self.motorsMap = CANMap()
        self.pneumaticsMap = PneumaticsMap()
        self.controllerMap = ControllerMap()
        self.networkTableMap = NetworkTableMap()

class CANMap():
    def __init__(self):
        pass

class PneumaticsMap():
    def __init__(self):
        pass

class ControllerMap():
    def __init__(self):
        pass

class networkTableMap():
    def __init__(self):
        pass
