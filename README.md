# TimerLabelNote
An adjustable timer for craftbeerpi3 that can count up and down, pause, and reset. Countdown notifications are a work in progress.

Install in craftbeerpi3 plugins directory, and reboot pi

* cd craftbeerpi3/modules/plugins

* git clone https://github.com/mccutheon/TimerLabelNote.git
  
* sudo reboot

Once pi is rebooted, go to Hardware and add a sensor. There will now be an option for TimerLabelNote. Give it a name, and provide the number of seconds you'd like the timer to be.

On the brewing screen, you will now have a timer showing 00:00:00. Press the action button on the sensor, and choose 'Set Time', and your configured time will now show. To start the count up, countdown, pause, or reset, select the action button and choose desired action.


To-do

* get cbpi notifications working when countdown finishes
* remove chart option from action drop down
* add function that accepts parameter to set time
* change time input configuration from seconds to 00:00:00 like timer displays
