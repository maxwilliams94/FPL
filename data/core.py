import requests
from datetime import datetime, timedelta
import pickle
from pathlib import Path
import os
from definitions import ROOT_DIR


class FplDataLoader(object):
    @staticmethod
    def get(pickle_path):
        if os.path.exists(pickle_path):
            with open(pickle_path) as f:
                old_data: FplData = pickle.load(f)
                if (datetime.now() - old_data.age) > timedelta(days=1):
                    old_data.refresh(force=True)
                    return old_data
        else:
            data = FplData()
            data.refresh()
            return data


class FplData(object):

    def __init__(self, pickle_path=Path(os.path.join('data', 'fpl_data.pickle'))):
        self.api_address = "https://fantasy.premierleague.com/api/bootstrap-static/"
        self.pickle_path = pickle_path

    def refresh(self, force: bool = False):
        """
        check age of data and refresh if necessary
        :param force: ignore age when refreshing data
        """
        # todo only refresh on aged data, otherwise load from pickle
        self._download_data()
        self._parse_raw_data()
        self._save_as_pickle()

    def _parse_raw_data(self):
        """
        Parse raw data from an api call (json) into instance variables
        :return:
        """
        self.total_players = self.raw_data['total_players']
        self.phases = self.raw_data['phases']  # Link months to game weeks ([dict])
        self.teams = self.raw_data['teams']  # team data [dict]
        self.footballers = self.raw_data['elements']  # player status/status (current)
        self.fb_stats = self.raw_data['element_stats']  # possible stats for a player (no data)
        self.p_types = self.raw_data['element_types']  # types of player

    def _download_data(self):
        """
        download and parse fpl data from fantasyPL api
        :return:
        """
        self.raw_data = requests.get(self.api_address).json()
        self.age = datetime.now()

    def _save_as_pickle(self, ):
        with open(self.pickle_path, 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def from_pickle(pickle_path):
        with open(pickle_path, 'rb') as f:
            # noinspection PickleLoad
            return pickle.load(f)
