class AppExceptionBaseClass(Exception):
    pass


class ObjectNotFound(AppExceptionBaseClass):
    pass


class SchemaValidationError(AppExceptionBaseClass):
    pass
