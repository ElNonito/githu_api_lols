class VersioningEvent:
    
    def __init__(self, type_event, message, created_at):
        self.type = type_event
        self.message = message
        self.created_at = created_at