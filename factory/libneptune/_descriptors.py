class KnobDescriptor:
    CW = True
    CCW = False
    CENTER = object()

    def __init__(self, dio, dio2=None):
        self._name = None
        self._dio = dio
        self._dio2 = dio2

    def _get_io(self, obj):
        h = obj.hubble
        dio = getattr(h, self._dio)
        dio2 = getattr(h, self._dio2) if self._dio2 else None
        return h, dio, dio2

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, obj, value):
        h, dio, dio2 = self._get_io(obj)

        if dio2 is None:
            dio.value = value
            return

        if value is self.CW:
            dio.value = True
            dio2.value = False
        elif value is self.CENTER:
            dio.value = False
            dio2.value = True
        elif value is self.CCW:
            dio.value = False
            dio2.value = False

    def __get__(self, obj, objtype=None):
        _, dio, dio2 = self._get_io(obj)

        if dio2 is None:
            return dio.value

        if dio.value:
            return self.CW
        else:
            if dio2.value:
                return self.CENTER
            else:
                return self.CCW


class CVDescriptor:
    def __init__(self, aio):
        self._name = None
        self._aio = aio

    def _get_io(self, obj):
        return getattr(obj.hubble, self._aio)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, obj, value: float):
        self._get_io(obj).voltage = value

    def __get__(self, obj, objtype=None) -> float:
        return self._get_io(obj).voltage


class SwitchDescriptor:
    def __init__(self, dio):
        self._name = None
        self._dio = dio

    def _get_io(self, obj):
        return getattr(obj.hubble, self._dio)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, obj, value: bool):
        self._get_io(obj).value = value

    def __get__(self, obj, objtype=None) -> bool:
        return self._get_io(obj).value
