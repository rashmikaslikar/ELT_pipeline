import sys

from airbyte_cdk.entrypoint import launch
from exnaton_connector.source_http.source2 import SourceExnatonApi

def run():
    source = SourceExnatonApi()
    launch(source, sys.argv[1:])