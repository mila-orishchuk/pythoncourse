'''
TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

    first_channel() - turns on the first channel from the list.
    last_channel() - turns on the last channel from the list.
    turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
    next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
    previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
    current_channel() - returns the name of the current channel.
    is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list,
    or "No" - in the other case.

The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

'''

class TVController:

    channel = 0

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        self.channel = 0
        return self.channels[self.channel]

    def last_channel(self):
        self.channel = len(self.channels) - 1
        return self.channels[self.channel]

    def turn_channel(self, channel):
        self.channel = channel - 1
        return self.channels[self.channel]

    def next_channel(self):
        # self.channel =  self.channel + 1 if self.channel != len(self.channels) - 1 else 0
        if self.channel != len(self.channels) - 1:
            self.channel += 1
        else:
            self.channel = 0
        return self.channels[self.channel]

    def previous_channel(self):
        # self.channel = (self.channel if self.channel != 0 else len(self.channels)) - 1
        if self.channel != 0:
            self.channel -= 1
        else:
            self.channel = len(self.channels) - 1
        return self.channels[self.channel]

    def current_channel(self):
        return self.channels[self.channel]

    def is_exist(self, channel):
        self.channel = channel
        if channel in self.channels:
            return 'Yes'
        else:
            return 'No'


if __name__ == '__main__':
    CHANNELS = ["BBC", "Discovery", "TV1000"]
    controller = TVController(CHANNELS)

    print(controller.first_channel())

    print(controller.last_channel())

    print(controller.turn_channel(1))

    print(controller.next_channel())

    print(controller.previous_channel())

    print(controller.current_channel())

    print(controller.is_exist(1))

    print(controller.is_exist("BBC"))
