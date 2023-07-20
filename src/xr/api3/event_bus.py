import ctypes
import xr


class EventBus(object):
    def __init__(self):
        self.subscribers = dict()

    def subscribe(self, event_key, subscriber):
        """Subscribe to a particular event type"""
        if event_key not in self.subscribers:
            self.subscribers[event_key] = set()
        self.subscribers[event_key].add(subscriber)

    def post(self, event_key, event_data=None):
        """Post an event to the event bus"""
        if event_key not in self.subscribers:
            return
        for subscriber in self.subscribers[event_key]:
            subscriber.notify(event_key, event_data)


class XrEventGenerator(object):
    def __init__(self, instance):
        self.instance = instance

    def poll_events(self, destination: EventBus):
        while True:
            try:
                event_buffer = xr.poll_event(self.instance)
                event_type = xr.StructureType(event_buffer.type)
                destination.post(event_key=event_type, event_data=event_buffer)
            except xr.EventUnavailable:
                break


class SessionStatus(object):
    def __init__(self, session: xr.Session, event_source: EventBus, begin_info=xr.SessionBeginInfo()):
        self.session = session
        self._begin_info = begin_info
        self.state = xr.SessionState.UNKNOWN
        event_source.subscribe(
            event_key=xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED,
            subscriber=self,
        )

    def notify(self, event_type, event_buffer):
        if event_type == xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED:
            event = ctypes.cast(
                ctypes.byref(event_buffer),
                ctypes.POINTER(xr.EventDataSessionStateChanged)).contents
            self.state = xr.SessionState(event.state)
            if self.state == xr.SessionState.READY:
                xr.begin_session(
                    session=self.session,
                    begin_info=self._begin_info,
                )
            elif self.state == xr.SessionState.STOPPING:
                xr.end_session(self.session)


__all__ = [
    "EventBus",
    "SessionStatus",
    "XrEventGenerator",
]
