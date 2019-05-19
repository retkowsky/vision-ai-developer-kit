import sys
import traceback


class CameraClientError(Exception):
    """
        Raised for CameraClient exceptions
    """
    pass


def log_unknown_exception(message, hub_manager=None):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_string = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
    message = ("%s:\n%s" % (message, traceback_string))
    print(message)
    if hub_manager:
        # TODO: make this a full message
        hub_manager.send_message_to_upstream(message)
