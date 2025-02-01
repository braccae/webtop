import json
from dataclasses import dataclass
from datetime import datetime
from dataclasses import asdict

@dataclass
class WindsurfRelease:
    url: str
    name: str
    version: str
    product_version: str
    hash: str
    timestamp: int
    sha256hash: str
    supports_fast_update: bool
    windsurf_version: str

    @property
    def release_date(self) -> datetime:
        """Convert timestamp to datetime object"""
        return datetime.fromtimestamp(self.timestamp)
    
    @classmethod
    def from_json(cls, json_data: str) -> 'WindsurfRelease':
        """Create a WindsurfRelease instance from JSON string"""
        data = json.loads(json_data)
        
        # Handle different JSON structures
        if 'packages' in data:
            windsurf_data = data['packages']['windsurf']
        else:
            windsurf_data = data.get('windsurf', data)
        
        return cls(
            url=windsurf_data['url'],
            name=windsurf_data['name'],
            version=windsurf_data['version'],
            product_version=windsurf_data['productVersion'],
            hash=windsurf_data['hash'],
            timestamp=windsurf_data['timestamp'],
            sha256hash=windsurf_data['sha256hash'],
            supports_fast_update=windsurf_data['supportsFastUpdate'],
            windsurf_version=windsurf_data['windsurfVersion']
        )

    def to_dict(self) -> dict:
        """Convert the data class to a dictionary with camelCase keys"""
        data = asdict(self)
        
        return {
            'url': data['url'],
            'name': data['name'],
            'version': data['version'],
            'productVersion': data['product_version'],
            'hash': data['hash'],
            'timestamp': data['timestamp'],
            'sha256hash': data['sha256hash'],
            'supportsFastUpdate': data['supports_fast_update'],
            'windsurfVersion': data['windsurf_version']
        }

    def save_json(self, filepath: str, structure: str = 'packages', indent: int = 2):
        """Save the config to a JSON file
        
        Args:
            filepath: Path to save the JSON file
            structure: How to structure the output JSON:
                      'packages' - Under packages.windsurf
                      'windsurf' - Under windsurf key only
                      'flat' - No nesting
            indent: Number of spaces for JSON indentation
        """
        data = self.to_dict()
        if structure == 'packages':
            data = {'packages': {'windsurf': data}}
        elif structure == 'windsurf':
            data = {'windsurf': data}
            
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=indent)

    @classmethod
    def load_json(cls, filepath: str) -> 'WindsurfRelease':
        """Load a WindsurfRelease from a JSON file"""
        with open(filepath, 'r') as f:
            json_str = f.read()
        return cls.from_json(json_str)