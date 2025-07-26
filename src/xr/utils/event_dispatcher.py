import logging
from typing import Callable, List

import xr

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())  # To avoid complaints about missing handler


class XrEventDispatcher:
    """
    Polls OpenXR events and dispatches them to subscribed handlers.

    Subscribers must be callables that accept a single event argument.
    """

    def __init__(self, instance):
        self.instance = instance
        self.subscribers: List[Callable[[object], None]] = []

    def subscribe(self, callback: Callable[[object], None]):
        """
        Register a callback to receive OpenXR events.

        Args:
            callback: A callable that takes one event argument.
        """
        self.subscribers.append(callback)

    def poll(self):
        """
        Polls events from the OpenXR runtime and dispatches them to all subscribers.
        """
        while True:
            try:
                event = xr.poll_event(self.instance)
                for subscriber in self.subscribers:
                    subscriber(event)
            except xr.EventUnavailable:
                break
