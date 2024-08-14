# from source_http.source import HttpApiSource

# if __name__ == "__main__":
#     source = HttpApiSource()
#     source.fetch_data()

#from source_http.source import SourceHttp

#if __name__ == "__main__":
#    source = SourceHttp()
#    source.run()

import sys
from airbyte_cdk.entrypoint import launch
from exnaton_connector.source_http.source1 import MyHttpSource

if __name__ == "__main__":
    source = MyHttpSource()
    launch(source, sys.argv[1:])
