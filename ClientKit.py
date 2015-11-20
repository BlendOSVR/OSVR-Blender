import bge

class ClientKit:

    def __init__(self):
        self._instance = None
        self._context = None
        self.AppID = ""

    def instance():
        doc = "The instance property."
        def fget(self):
            if self._instance is None:
                #find game object of type ClientKit
                if self._instance is None:
                    #raise error
                else
                    #don't destroy on load
            return self._instance
        def fdel(self):
            del self._instance
        return locals()
    instance = property(**instance())

    def context():
        doc = "The context property."
        def fget(self):
            EnsureStarted()
            return self._context
        def fdel(self):
            del self._context
        return locals()
    context = property(**context())

    def EnsureStarted():
        if self._context is None:
            if len(AppID) == 0:
                #OSVR ClientKit instance needs AppID set to a reverse-order DNS name! Using dummy name...
                AppID = "com.osvr.osvr-blender.dummy"
            #[OSVR] Starting with app ID: " + AppID
            self._context = new OSVR.ClientKit.ClientContext(AppID, 0);

        if not _context.CheckStatus():
            #OSVR Server not detected. Start OSVR Server and restart the application.
