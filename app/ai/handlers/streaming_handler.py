"""
Streaming Handler Module
"""
import logging
from langchain.callbacks.base import BaseCallbackHandler

class StreamingHandler(BaseCallbackHandler):
    """
    The LLM callback class
    """
    def __init__(self, queue):
        self.queue = queue
        self.streaming_run_ids = set()

    def get_queue(self):
        return self.queue

    def on_chat_model_start(self, serialized, messages, run_id, **kwargs):
        """
        Override method: on_chat_model_start
        """
        logging.info("Streaming starts...")
        if serialized["kwargs"]["streaming"]:
            self.streaming_run_ids.add(run_id)

    def on_llm_new_token(self, token, **kwargs):
        logging.debug("Inside streaming handler %s", token)
        self.queue.put(token)

    def on_llm_end(self, response, run_id, **kwargs):
        """
        Override method: on_llm_end
        """
        logging.debug("Streaming ends...")
        if run_id in self.streaming_run_ids:
            self.queue.put(None)
            self.streaming_run_ids.remove(run_id)

    def on_llm_error(self, error, **kwargs):
        self.queue.put(None)
