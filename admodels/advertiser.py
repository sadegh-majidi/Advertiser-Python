from admodels.base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    __all_advertisers: list = []

    def __init__(self, _id: int, name: str) -> None:
        super(Advertiser, self).__init__()
        super._id = _id
        self.__name = name
        Advertiser.__all_advertisers.append(self)

    @staticmethod
    def get_total_clicks() -> int:
        return sum((advertiser.get_clicks() for advertiser in Advertiser.__all_advertisers), start=0)

    @staticmethod
    def help() -> None:
        print('Advertiser Fields ->\n'
              'id: unique id of advertiser\n'
              'name: name of this advertiser\n'
              'views: number of total views of this advertiser\'s ads\n'
              'clicks: number of total clicks of this advertiser\'s ads'
              )
