# -*- coding: utf-8 -*-
from utils import RedirectStdStreams
from multiprocessing import Process


class AppUnderTest:

    def __init__(self, app_create, host="127.0.0.1", port=5013):
        self.app = app_create()
        self.host = host
        self.port = port

        def run_app():
            import os
            devnull = open(os.devnull, 'w')
            with RedirectStdStreams(stdout=devnull, stderr=devnull):
                self.app.run(
                    host=self.host,
                    port=self.port,
                    use_reloader=False,
                    debug=True)
        self.proccess = Process(target=run_app)

    @property
    def base_url(self):
        return "http://%s:%d" % (self.host, self.port)

    def enter(self):
        self.proccess.start()

    def exit(self):
        self.proccess.terminate()
        self.proccess.join()

    def __enter__(self):
        self.enter()

    def __exit__(self, exc_type, exc_value, traceback):
        self.exit()
