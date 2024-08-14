import requests
import json

# class HttpApiSource:
#     def __init__(self, config):
#         self.api_url = config['api_url']

#     def fetch_data(self):
#         #headers = {"Authorization": f"Bearer {self.api_key}"}
#         response = requests.get(self.api_url, headers=None)
#         return response.json()

# def main():
#     with open('config.json') as config_file:
#         config = json.load(config_file)
#     source = HttpApiSource(config)
#     data = source.fetch_data()
#     print(json.dumps(data, indent=2))

# if __name__ == "__main__":
#     main()

import requests
import json
from typing import *
from airbyte_cdk.sources import Source, AbstractSource
from airbyte_cdk.models import AirbyteCatalog, AirbyteMessage, AirbyteStateMessage, ConfiguredAirbyteCatalog, SyncMode, AirbyteStream
from airbyte_cdk.models.airbyte_protocol import Type
from airbyte_cdk.sources.streams.http import HttpStream
import time

import requests
import sys
from airbyte_cdk.models import AirbyteConnectionStatus, Status, AirbyteMessage, AirbyteRecordMessage, ConfiguredAirbyteCatalog
from airbyte_cdk.sources import Source

class MyHttpSource(AbstractSource):
    def check(self, config: dict) -> AirbyteConnectionStatus:
        api_url = config.get("api_url")
        
        try:
            response = requests.get(api_url, headers=None)
            if response.status_code == 200:
                return AirbyteConnectionStatus(status=Status.SUCCEEDED)
            else:
                return AirbyteConnectionStatus(status=Status.FAILED, message=f"Failed to connect to API: {response.status_code}")
        except Exception as e:
            return AirbyteConnectionStatus(status=Status.FAILED, message=str(e))

    def discover(self,config: dict) -> AirbyteCatalog:
        streams = [
            AirbyteStream(
                name="my_stream",
                json_schema={"type": "object", "properties": {"field1": {"type": "string"}, "field2": {"type": "integer"}}}
            )
        ]
        return AirbyteCatalog(streams=streams)

    def read(self, config: dict, catalog: ConfiguredAirbyteCatalog, state: dict) -> Iterable[AirbyteMessage]:
        api_url = config.get("api_url")
        api_key = config.get("api_key")
        
        try:
            response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})
            response.raise_for_status()
            data = response.json()
            
            for record in data:
                yield AirbyteRecordMessage(
                    stream="my_stream",
                    data=record,
                    emitted_at=int(time.time()) * 1000
                )
        except Exception as e:
            print(f"Error reading data from API: {str(e)}")
