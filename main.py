#!/usr/bin/env python3
"""
SOLID Principles Compliant Coordinate API
========================================

This API is designed to find province and district coordinates efficiently.
It is developed with a modular structure following SOLID principles.

Usage:
    python main.py
"""

import json
import time
from src.api import CoordinateAPI

def main():
    """Main function"""
    print("SOLID Principles Compliant Coordinate API")
    print("=" * 50)
    
    # Initialize API
    start_time = time.time()
    api = CoordinateAPI()
    init_time = time.time() - start_time
    
    print(f"API initialized ({init_time:.2f} seconds)")
    print()
    
    # Health check
    print("System Health Check:")
    health = api.health_check()
    print(json.dumps(health, indent=2, ensure_ascii=False))
    print()
    
    # Performance info
    print("Performance Information:")
    perf = api.get_performance_info()
    print(json.dumps(perf, indent=2, ensure_ascii=False))
    print()
    
    # Test scenarios
    test_scenarios = [
        {
            "name": "Single Province Search",
            "query": "Aydın",
            "region_type": "auto"
        },
        {
            "name": "Multiple Province Search",
            "query": "İstanbul, Ankara, İzmir",
            "region_type": "auto"
        },
        {
            "name": "District Search",
            "query": "Eyyübiye",
            "region_type": "district"
        },
        {
            "name": "Mixed Search",
            "query": "Aydın ve İzmir",
            "region_type": "auto"
        }
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"Test {i}: {scenario['name']}")
        print(f"   Query: '{scenario['query']}'")
        print(f"   Type: {scenario['region_type']}")
        
        start_time = time.time()
        result = api.find_coordinates(scenario['query'], scenario['region_type'])
        query_time = time.time() - start_time
        
        print(f"   Duration: {query_time:.3f} seconds")
        
        if result['success']:
            print(f"   Success: {len(result['found_regions'])} regions found")
            if result['coordinates']['polygon']['type'] == 'Polygon':
                coord_count = len(result['coordinates']['polygon']['coordinates'][0])
                print(f"   Coordinate count: {coord_count}")
            elif result['coordinates']['polygon']['type'] == 'MultiPolygon':
                coord_count = sum(len(poly) for poly in result['coordinates']['polygon']['coordinates'])
                print(f"   Coordinate count: {coord_count}")
        else:
            print(f"   Error: {result['error']}")
        
        print()
    
    # Search suggestions test
    print("Search Suggestions Test:")
    suggestions = api.search_suggestions("an", 5)
    print(f"   {len(suggestions)} suggestions containing 'an':")
    for suggestion in suggestions:
        print(f"   - {suggestion['name']} ({suggestion['type']})")
    print()
    
    # Region list test
    print("Region List Test:")
    provinces = api.get_region_list("province", "tr")[:5]
    print(f"   First 5 provinces:")
    for province in provinces:
        print(f"   - {province['name']} (ID: {province['id']})")
    print()
    
    print("All tests completed!")

if __name__ == "__main__":
    main() 