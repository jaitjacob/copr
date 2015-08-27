# coding: utf-8
import six


class ApiError(Exception):
    def __init__(self, code, data, **kwargs):
        super(ApiError, self).__init__(**kwargs)

        self.code = code
        self.data = data

        self.headers = kwargs.get("headers", {})

    def __str__(self):
        return str(self.data)

    if six.PY2:
        def __unicode__(self):
            return unicode(self.data)


class AuthFailed(ApiError):
    def __init__(self, data, **kwargs):

        super(AuthFailed, self).__init__(401, data, **kwargs)
        self.headers["Authorization"] = "Basic"


class AccessForbidden(ApiError):
    def __init__(self, data, **kwargs):

        super(AccessForbidden, self).__init__(403, data, **kwargs)


class ObjectNotFoundError(ApiError):
    def __init__(self, data, **kwargs):
        super(ObjectNotFoundError, self).__init__(404, data, **kwargs)


class ObjectAlreadyExists(ApiError):
    def __init__(self, data, **kwargs):
        super(ObjectAlreadyExists, self).__init__(409, data, **kwargs)


class MalformedRequest(ApiError):
    def __init__(self, data=None, **kwargs):
        super(MalformedRequest, self).__init__(400, data, **kwargs)


class CannotProcessRequest(ApiError):
    def __init__(self, data=None, **kwargs):
        super(CannotProcessRequest, self).__init__(400, data, **kwargs)


class ServerError(ApiError):
    def __init__(self, data=None, **kwargs):
        super(ServerError, self).__init__(500, data, **kwargs)
