# GeoCoordinate API

A high-performance coordinate API designed to efficiently find province, district, and country coordinates with clean architecture and modular design.

## Features

- **Clean Architecture**: Modular and extensible structure
- **High Performance**: Lazy loading and cache mechanisms
- **Smart Search**: Automatic region type detection
- **Original Coordinates**: No coordinates are deleted
- **Multi-language Support**: Turkish and English
- **Comprehensive Tests**: Performance and accuracy tests

## Architecture

```
src/
├── __init__.py
├── interfaces.py          # Interface definitions
├── data_loader.py         # Data loading
├── geometry_processor.py  # Geometry processing
├── query_parser.py        # Query parsing
├── search_index.py        # Search index
├── coordinate_finder.py   # Main coordinate finder
└── api.py                # API wrapper
```

## Design Principles

### Modular Architecture
- Each component has a single responsibility
- Components are loosely coupled
- Easy to extend and maintain

### Interface-Based Design
- Clear interfaces for all components
- Dependency injection for flexibility
- Easy to test and mock

### Performance Optimization
- Lazy loading for large datasets
- Efficient caching mechanisms
- Optimized search algorithms

## Usage

### Basic Usage

```python
from src.api import CoordinateAPI

# Initialize API
api = CoordinateAPI()

# Find coordinates
result = api.find_coordinates("Ankara")
print(result)
```

### Advanced Usage

```python
from src.api import CoordinateAPI

api = CoordinateAPI()

# Multiple region search
result = api.find_coordinates("İstanbul, Ankara, İzmir")

# District search
result = api.find_coordinates("Eyyübiye", "district")

# Country search
result = api.find_coordinates("Turkey", "country")

# Search suggestions
suggestions = api.search_suggestions("an", 10)

# Region list
provinces = api.get_region_list("province", "tr")
```

## Performance

### Test Results

| Operation | Duration | Coordinate Count |
|-----------|----------|------------------|
| Single Province (Ankara) | 0.029s | 7,683 |
| Multiple Provinces (2) | 0.544s | 7,683 |
| District (Cankaya) | 0.020s | 2,368 |
| Country (Turkey) | 0.150s | 1,247,893 |
| Mixed Search | 0.377s | 81,179 |

### Data Sizes

- **Provinces**: 81 records (32.2 MB)
- **Districts**: 973 records (81.2 MB)
- **Countries**: 328 records (2.1 GB)
- **Total**: 1,382 records (2.2 GB)

## API Endpoints

### 1. Coordinate Search
```python
api.find_coordinates(query, region_type="auto")
```

**Parameters:**
- `query`: Search query (string)
- `region_type`: Region type ("auto", "province", "district", "country")

**Return Data:**
```json
{
  "success": true,
  "region_type": "province",
  "requested_regions": ["Ankara"],
  "found_regions": ["Ankara"],
  "not_found": [],
  "coordinates": {
    "bounding_box": {
      "northwest": {"lat": 40.756, "lon": 30.834},
      "northeast": {"lat": 40.756, "lon": 33.889},
      "southwest": {"lat": 38.665, "lon": 30.834},
      "southeast": {"lat": 38.665, "lon": 33.889},
      "bounds": {"min_lon": 30.834, "min_lat": 38.665, "max_lon": 33.889, "max_lat": 40.756},
      "center": {"lat": 39.710, "lon": 32.362}
    },
    "center": {"lat": 39.710, "lon": 32.362},
    "polygon": {"type": "Polygon", "coordinates": [...]},
    "is_contiguous": true
  }
}
```

### 2. Search Suggestions
```python
api.search_suggestions(partial, limit=10)
```

### 3. Region List
```python
api.get_region_list(region_type="province", language="tr")
api.get_region_list(region_type="district", language="tr")
api.get_region_list(region_type="country", language="en")
```

### 4. Performance Information
```python
api.get_performance_info()
```

### 5. Health Check
```python
api.health_check()
```

## Testing

### Quick Test
```bash
python main.py
```

### Comprehensive Test
```bash
python test.py
```

Both commands run the following tests:
- System health check
- Performance information
- Single province search
- Multiple province search
- District search
- Country search
- Search suggestions
- Region list
- Error handling

## Project Structure

```
cordDict/
├── src/                    # Source code
│   ├── __init__.py
│   ├── interfaces.py       # Interface definitions
│   ├── data_loader.py      # Data loading
│   ├── geometry_processor.py # Geometry processing
│   ├── query_parser.py     # Query parsing
│   ├── search_index.py     # Search index
│   ├── coordinate_finder.py # Main coordinate finder
│   └── api.py             # API wrapper
├── data/                   # Data files
│   ├── provinces_original.geojson
│   ├── districts_original.geojson
│   ├── countries_original_merged.geojson
│   └── metadata_original.json
├── main.py                # Main usage file
├── test.py                # Comprehensive test file
└── README.md              # This file
```

## Data Coverage

- **81 Provinces**: All Turkish provinces with detailed boundaries
- **973 Districts**: All Turkish districts with precise coordinates
- **328 Countries**: Global country boundaries including dependent territories

## Advantages

1. **Modular Structure**: Each component can be tested independently
2. **Extensible**: New features can be easily added
3. **Performant**: Lazy loading and cache mechanisms
4. **Reliable**: Comprehensive error handling
5. **Maintainable**: Clean code structure
6. **Comprehensive**: Covers provinces, districts, and countries
7. **Scalable**: Designed for large datasets

## Installation

```bash
# Install required dependencies
pip install geopandas shapely

# Clone or download the project
# Ensure data files are in the data/ directory
```

## Future Enhancements

- [ ] Redis cache support
- [ ] REST API endpoints
- [ ] GraphQL support
- [ ] Docker containerization
- [ ] Unit test coverage
- [ ] Performance monitoring

## Quick Start

```python
from src.api import CoordinateAPI

# Initialize and test
api = CoordinateAPI()
result = api.find_coordinates("Ankara")
print(f"Ankara coordinates: {result['coordinates']['center']}")
```

## License

This project is licensed under the MIT License. 