from admodels.base_model import BaseAdvertising
from admodels.advertiser import Advertiser


class Ad(BaseAdvertising):
    __ids: list = []

    def __init__(self, _id: int, title: str, img_url: str, link: str, advertiser: Advertiser) -> None:
        super(Ad, self).__init__()
        assert not any(i == _id for i in Ad.__ids), f'Id {_id} is duplicated. Id of the Ad Should be unique.'
        assert advertiser is not None, 'Must provide an advertiser to ad.'
        self._id = _id
        self.__title = title
        self.__img_URL = img_url
        self.__link = link
        self.__advertiser = advertiser
        Ad.__ids.append(_id)

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        self.__title = title

    def get_img_url(self) -> str:
        return self.__img_URL

    def set_img_url(self, img_url: str) -> None:
        self.__img_URL = img_url

    def get_link(self) -> str:
        return self.__link

    def set_link(self, link: str) -> None:
        self.__link = link

    def set_advertiser(self, advertiser: Advertiser) -> None:
        self.__advertiser = advertiser

    def inc_clicks(self) -> None:
        super().inc_clicks()
        self.__advertiser.inc_clicks()

    def inc_views(self) -> None:
        super().inc_views()
        self.__advertiser.inc_views()

    def describe_me(self) -> None:
        print('Name: Ad\n'
              'Description: This class is a blueprint to create advertisement objects and derived from '
              'BaseAdvertising Base class.'
              )
