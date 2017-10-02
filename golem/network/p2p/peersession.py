import logging

from golem.diag.service import DiagnosticsProvider

logger = logging.getLogger(__name__)

class PeerSessionInfo(object):

    attributes = [
        'remote_pubkey',
        'ip_port',
        'node_name'
    ]

    def __init__(self, peer):
        setattr(self, 'remote_pubkey', getattr(peer, 'remote_pubkey'))
        setattr(self, 'ip_port', getattr(peer, 'ip_port'))
        if hasattr(peer, 'node_name'):
            setattr(self, 'node_name', peer.node_name)

    def get_simplified_repr(self):
        repr = self.__dict__
        return repr


class PeerMonitor(DiagnosticsProvider):

    def __init__(self, peermanager):
        self.peermanager = peermanager

    def get_diagnostics(self, output_format):
        peer_data = []
        for peer in self.peermanager.peers:
            peer = PeerSessionInfo(peer).get_simplified_repr()
            peer_data.append(peer)
        return self._format_diagnostics(peer_data, output_format)
