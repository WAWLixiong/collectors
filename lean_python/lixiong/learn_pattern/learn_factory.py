import json
import xml.etree.ElementTree as etree


class JsonConnector:

    def __init__(self, file_path):
        self.data = {}
        with open(file_path, 'wb', encoding='utf8') as f:
            self.data = json.loads(f)


    @property
    def parsed_data(self):
        return self.data


class XmlConnector:

    def __init__(self, file_path):
        self.tree = etree.parse(file_path)

    def parsed_data(self):
        return self.tree


def connection_factory(file_path):
    if file_path.endswith('json'):
        connector = JsonConnector
    elif file_path.endswith('xml'):
        connector = XmlConnector
    else:
        raise ValueError('Cannot connect to {}'.format(file_path))
    return connector(file_path)


def connect_to(file_path):
    facotor = None
    try:
        factor = connection_factory(file_path)
    except ValueError as e:
        print(e)
    return facotor
