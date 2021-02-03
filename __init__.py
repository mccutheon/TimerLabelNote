from modules import cbpi
from modules.core.hardware import  SensorActive
from modules.core.props import Property
import time
import threading
import datetime

@cbpi.sensor
class TimerLabelNote(SensorActive):

    timeConfig = Property.Number("Time", configurable=True, default_value=0, description="Time")
    running = 0
    currentTime = 0

    def get_unit(self):
        '''
        :return: Unit of the sensor as string. Should not be longer than 3 characters
        '''
        return " "

    def stop(self):
        '''
        Stop the sensor. Is called when the sensor config is updated or the sensor is deleted
        :return: 
        '''
        pass

    @cbpi.action("Set time")
    def setTime(self):
        self.currentTime = int(self.timeConfig)

    @cbpi.action("Clear time")
    def clearTime(self):
        self.currentTime = 0
        self.running = 0

    @cbpi.action("Pause Time")
    def pauseTime(self):
        self.running = 0

    def countdown(self):
        while (self.running == 1 and self.currentTime > 0):
            self.currentTime = self.currentTime - 1
            time.sleep(1)
        self.running = 0
        print("countdown done")
        #notify("AutoTune P Value", "value", type="info", timeout=NONE)

    def countup(self):
        while (self.running == 1 and self.currentTime < 25000):
            self.currentTime = self.currentTime + 1
            time.sleep(1)
        self.running = 0


    @cbpi.action("Start Countdown")
    def startCountdown(self):
        self.running = 1
        set_thread = threading.Thread(target=self.countdown)
        set_thread.start()

    @cbpi.action("Start Countup")
    def startCountup(self):
        self.running = 1
        set_thread = threading.Thread(target=self.countup)
        set_thread.start()



    def execute(self):
        '''
        Active sensor has to handle its own loop
        :return: 
        '''
        while self.is_running():
            self.data_received(str(datetime.timedelta(seconds=self.currentTime)))
            self.sleep(1)

    @classmethod
    def init_global(cls):
        '''
        Called one at the startup for all sensors
        :return: 
        '''

