
"""
The stream module
"""
from queue import Queue
from threading import Thread

import logging

from app.ai.handlers import StreamingHandler

class Streamable:
    """
    Streamable chain
    """
    handler: StreamingHandler
    def set_handler(self, handler: StreamingHandler):
        self.handler = handler

    def stream(self, input):
        """
        Stream function
        Args:
            input(Any): the user input
        """
        def task():
            self(input, callbacks=[self.handler])
        Thread(target=task).start()
        self.listen_queue()

    def listen_queue(self):
        while True:
            token = self.handler.get_queue().get()
            if token is None:
                break
            logging.info("Sending token: %s", token)
            yield token