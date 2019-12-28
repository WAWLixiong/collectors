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

    @property
    def parsed_data(self):
        return self.tree


class Connect:

    def __init__(self, file_path):
        self.factor = self.connection_factory(file_path)

    def connection_factory(self, file_path):
        if file_path.endswith('json'):
            connector = JsonConnector
        elif file_path.endswith('xml'):
            connector = XmlConnector
        else:
            raise ValueError('Cannot connect to {}'.format(file_path))
        return connector(file_path)


if __name__ == '__main__':
    json_conn = Connect('hello.json')
    xml_conn = Connect('world.xml')
    json_data = json_conn.factor.parsed_data
    xml_data = xml_conn.factor.parsed_data

