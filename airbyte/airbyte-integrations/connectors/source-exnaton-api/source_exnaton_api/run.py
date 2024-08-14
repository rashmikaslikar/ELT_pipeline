import sys

from airbyte_cdk.entrypoint import launch
from . source import SourceExnatonApi

def run():
    source = SourceExnatonApi()
    launch(source, sys.argv[1:])