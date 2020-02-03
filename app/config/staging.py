''' Configuration loader for staging environment '''
import os
from kazoo.client import KazooClient

#pylint: disable=R0903
class StagingConfig():
    ''' Configuration handler '''
    zk = KazooClient(hosts=os.getenv('ZOOKEEPER_HOST') + ':' + os.getenv('ZOOKEEPER_PORT'))
    zk.start()

    data, stat = zk.get("/spai/davinci-api/staging/git_mlrepo_url")
    GIT_MLREPO_BASE_URL = data.decode("utf-8")

    zk.stop()
    zk = None
    data = None
    stat = None
