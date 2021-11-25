import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

DEFAULT_LOCATION = "static/file/1-hour-and-20-minutes-of-silence.mp3"


class Mp3_streamer(object):
    def __init__(self):
        self.mainloop = GObject.MainLoop()
        self.mp3_pipe = Gst.Pipeline()

        self.filesrc = Gst.ElementFactory.make("filesrc", "fsrc")
        self.filesrc.set_property("location", DEFAULT_LOCATION)
        self.mpegparser = Gst.ElementFactory.make("mpegaudioparse", "mparse")
        self.tcp_server_sink = Gst.ElementFactory.make("tcpserversink", "t_server")
        self.tcp_server_sink.set_property("port", 7006)
        self.tcp_server_sink.set_property("host", "0.0.0.0")
        self.queue = Gst.ElementFactory.make("queue", "q_1")

        self.mp3_pipe.add(self.filesrc)
        self.mp3_pipe.add(self.mpegparser)
        self.mp3_pipe.add(self.tcp_server_sink)
        self.mp3_pipe.add(self.queue)

        self.filesrc.link(self.mpegparser)
        self.mpegparser.link(self.queue)
        self.queue.link(self.tcp_server_sink)

    def run(self):
        # self.mainloop.run()
        self.mp3_pipe.set_state(Gst.State.PLAYING)
        print("play")

    def stop(self):
        self.mp3_pipe.set_state(Gst.State.PAUSED)
        # self.mainloop.quit()
        print("PAUSED")

    def change_music(self, new_file_addr):
        self.mp3_pipe.set_state(Gst.State.PAUSED)
        self.mp3_pipe.set_state(Gst.State.READY)
        self.filesrc.set_property("location", new_file_addr)
        self.mp3_pipe.set_state(Gst.State.PLAYING)
        print("change")


GObject.threads_init()
Gst.init()
