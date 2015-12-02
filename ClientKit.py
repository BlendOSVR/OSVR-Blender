import bge

class ClientKit(bge.type.KX_GameObject):

    def __init__(self, gameObjectToBeReplaced):
        self._instance = None
        self._context = None
        self.AppID = ""
        ensureStarted()

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

    def ensureStarted():
        if self._context is None:
            if len(self.AppID) == 0:
                #OSVR ClientKit instance needs AppID set to a reverse-order DNS name! Using dummy name...
                self.AppID = "com.osvr.osvr-blender.dummy"
            print("[OSVR] Starting with app ID: " + self.AppID)
            self._context = new OSVR.ClientKit.ClientContext(self.AppID, 0);

        if not self._context.CheckStatus():
            #OSVR Server not detected. Start OSVR Server and restart the application.

    def endObject():
        if self._context is not None:
            #Shutting down OSVR
            self._context.Dispose()
            self._context = None
        super().endObject()
