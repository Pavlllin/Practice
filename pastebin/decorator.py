class RouterDecorator:
    models = set()
    def __init__(self, clasz=None):
        if clasz is not None:
            return self.__call__(clasz)

    def __call__(self,clasz,*args, **kwargs):
        self.models.add((clasz))
        return clasz
