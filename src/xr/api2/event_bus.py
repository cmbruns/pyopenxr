import abc
import ctypes
import typing
import xr


class ISubscriber(abc.ABC):
    """
    Abstract base class for classes that subscribe to events from an EventBus.
    """
    @abc.abstractmethod
    def handle_event(self, event_key, event_data) -> None:
        """
        Receives an event from the EventBus
        :param event_key: key uniquely identifying an event type
        :param event_data: data associated with the event
        """
        pass


class EventBus(object):
    """
    Generic synchronous event bus that receives events and notifies subscribers.
    """
    def __init__(self) -> None:
        self.subscribers: typing.Dict[typing.Any, typing.Set[ISubscriber]] = dict()

    def subscribe(self, event_key, subscriber: ISubscriber) -> None:
        """Add a subscriber client to a particular event type"""
        if event_key not in self.subscribers:
            self.subscribers[event_key] = set()
        self.subscribers[event_key].add(subscriber)

    def post(self, event_key, event_data=None) -> None:
        """Post a new event to the event bus"""
        if event_key not in self.subscribers:
            return
        for subscriber in self.subscribers[event_key]:
            subscriber.handle_event(event_key, event_data)


class XrEventGenerator(object):
    """
    Dispatches OpenXR events to subscribers.
    """
    def __init__(self, instance: xr.Instance) -> None:
        self.instance = instance

    def poll_events(self, destination: EventBus) -> None:
        while True:
            try:
                event_buffer = xr.poll_event(self.instance)
                event_type = xr.StructureType(event_buffer.type)
                destination.post(event_key=event_type, event_data=event_buffer)
            except xr.EventUnavailable:
                break


class SessionStatus(ISubscriber):
    """
    Event subscriber that manages an OpenXR session state.
    """
    def __init__(self, session: xr.Session, event_source: EventBus, begin_info=xr.SessionBeginInfo()):
        self.session = session
        self._begin_info = begin_info
        self.state = xr.SessionState.UNKNOWN
        self.is_running = False
        self.exit_frame_loop = False
        event_source.subscribe(
            event_key=xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED,
            subscriber=self,
        )

    def handle_event(self, event_key, event_data) -> None:
        """
        Respond to OpenXR session state change events
        :param event_key: event type
        :param event_data: event buffer
        :return:
        """
        if event_key == xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED:
            event = ctypes.cast(
                ctypes.byref(event_data),
                ctypes.POINTER(xr.EventDataSessionStateChanged)).contents
            self.state = xr.SessionState(event.state)
            print(self.state.name)
            if self.state == xr.SessionState.READY:
                xr.begin_session(
                    session=self.session,
                    begin_info=self._begin_info,
                )
                self.is_running = True
            elif self.state == xr.SessionState.STOPPING:
                self.is_running = False
                xr.end_session(self.session)
            elif self.state == xr.SessionState.EXITING:
                self.exit_frame_loop = True


__all__ = [
    "EventBus",
    "ISubscriber",
    "SessionStatus",
    "XrEventGenerator",
]
