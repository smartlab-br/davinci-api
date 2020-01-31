''' Configuration loader for production environment '''
import os
from kazoo.client import KazooClient

class ProductionConfig():
    ''' Configuration handler '''
    zk = KazooClient(hosts=os.getenv('ZOOKEEPER_HOST') + ':' + os.getenv('ZOOKEEPER_PORT'))
    zk.start()

    data, stat = zk.get("/spai/davinci-api/prod/git_mlrepo_url")
    GIT_MLREPO_BASE_URL = data.decode("utf-8")

    zk.stop()
    zk = None
    data = None
    stat = None
