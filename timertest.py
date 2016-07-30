from threading import Timer

class P:
    def __init__(self):
        self.freq = 0

    def start(self, n):
        print("start {}, f = {}".format(n, self.freq))

    def stop(self):
        print("stop")

    def ChangeFrequency(self, f):
        self.freq = f
   
p = P()

def stop_note(notes):
    p.stop()
    play_note(notes)

def play_note(notes):
    if len(notes) == 0:
        return
    note, duration = notes.pop(0)
    p.ChangeFrequency(note)
    p.start(50)
    noteTime = Timer(duration, stop_note, [notes])
    noteTime.start()

notes = [(10,1), (20, 0.5), (30, 2)]

play_note(notes)

