import threading

# Thread-local storage to hold current user
_thread_locals = threading.local()


def get_current_user():
    """Return the user associated with the current request"""
    return getattr(_thread_locals, 'user', None)


class CurrentUserMiddleware:
    """
    Middleware that stores the current request's user in thread-local storage.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Save the user before processing the view
        _thread_locals.user = getattr(request, 'user', None)
        
        response = self.get_response(request)
        
        # Clean up after response (optional, for safety)
        _thread_locals.user = None

        return response
