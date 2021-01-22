class BaseAdvertising:
    def __init__(self) -> None:
        self._id: int
        self._clicks: int = 0
        self._views: int = 0

    def get_clicks(self) -> int:
        return self._clicks

    def get_views(self) -> int:
        return self._views

    def inc_clicks(self) -> None:
        self._clicks += 1

    def inc_views(self) -> None:
        self._views += 1

    def describe_me(self) -> None:
        print('Name: BaseAdvertising\nDescription: This is base class for Ad and Advertiser classes.')
