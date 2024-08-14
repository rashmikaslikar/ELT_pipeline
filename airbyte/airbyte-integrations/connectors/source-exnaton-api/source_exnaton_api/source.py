from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
import logging
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream

from . import source_id_list

logger = logging.getLogger("airbyte")

class SourceExnatonApi(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        logger.info("Checking exnaton API connection...")
        input_id = config["source_id"]
        if input_id not in source_id_list.SOURCE_ID_LIST:
            result = f"Input source id {input_id} is invalid. Please check your spelling and input a valid Pokemon."
            logger.info(f" Exnaton API connection failed: {result}")
            return False, result
        else:
            logger.info(f"Exnaton API connection success: {input_id} is a valid Pokemon")
            return True, None

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        return [ExnatonApiStream(source_id=config["source_id"])]
    
class ExnatonApiStream(HttpStream):
    url_base = "https://exnaton-public-s3-bucket20230329123331528000000001.s3.eu-central-1.amazonaws.com/challenge/"

    # Set this as a noop.
    primary_key = None

    def __init__(self, source_id: str, **kwargs):
        super().__init__(**kwargs)
        # Here's where we set the variable from our input to pass it down to the source.
        self.source_id = source_id

    def path(self, **kwargs) -> str:
        source_id = self.source_id
        # This defines the path to the endpoint that we want to hit.
        return f"{source_id}"

    def request_params(
            self,
            stream_state: Mapping[str, Any],
            stream_slice: Mapping[str, Any] = None,
            next_page_token: Mapping[str, Any] = None,
    ) -> MutableMapping[str, Any]:
        # The api requires that we include the Pokemon name as a query param so we do that in this method.
        return {"source_id": self.source_id}

    def parse_response(
            self,
            response: requests.Response,
            stream_state: Mapping[str, Any],
            stream_slice: Mapping[str, Any] = None,
            next_page_token: Mapping[str, Any] = None,
    ) -> Iterable[Mapping]:
        # The response is a simple JSON whose schema matches our stream's schema exactly,
        # so we just return a list containing the response.
        return [response.json()]

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        # While the PokeAPI does offer pagination, we will only ever retrieve one Pokemon with this implementation,
        # so we just return None to indicate that there will never be any more pages in the response.
        return None