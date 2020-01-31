from kazoo.client import KazooClient
import os


class StagingConfig(object):

    zk = KazooClient(hosts=os.getenv('ZOOKEEPER_HOST') + ':' + os.getenv('ZOOKEEPER_PORT'))
    zk.start()
    
    data, stat = zk.get("/spai/davinci-api/staging/git_mlrepo_url")
    GIT_MLREPO_BASE_URL = data.decode("utf-8")

    zk.stop()
    zk = None
    data = None
    stat = None
