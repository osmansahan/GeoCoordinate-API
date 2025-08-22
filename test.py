from src.api import CoordinateAPI
import json

def test_api():
    print("COORDINATE API TEST ===\n")
    
    # Initialize API
    api = CoordinateAPI()
    print("API initialized successfully\n")
    
    # 1. ANKARA PROVINCE TEST
    print("1. ANKARA PROVINCE TEST:")
    print("-" * 30)
    result = api.find_coordinates('Ankara')
    print(f"Success: {result['success']}")
    if result['success']:
        print(f"Found regions: {result['found_regions']}")
        print(f"Center: {result['coordinates']['center']}")
        print(f"Bounding Box: {result['coordinates']['bounding_box']['bounds']}")
        print(f"Coordinate count: {len(result['coordinates']['polygon']['coordinates'][0])}")
    print()
    
    # 2. CANKAYA DISTRICT TEST
    print("2. CANKAYA DISTRICT TEST:")
    print("-" * 30)
    result = api.find_coordinates('Cankaya', 'district')
    print(f"Success: {result['success']}")
    if result['success']:
        print(f"Found regions: {result['found_regions']}")
        print(f"Center: {result['coordinates']['center']}")
        print(f"Bounding Box: {result['coordinates']['bounding_box']['bounds']}")
        print(f"Coordinate count: {len(result['coordinates']['polygon']['coordinates'][0])}")
    print()
    
    # 3. MULTIPLE PROVINCES TEST
    print("3. MULTIPLE PROVINCES TEST (Ankara, Istanbul):")
    print("-" * 45)
    result = api.find_coordinates('Ankara, Istanbul')
    print(f"Success: {result['success']}")
    if result['success']:
        print(f"Found regions: {result['found_regions']}")
        print(f"Center: {result['coordinates']['center']}")
        print(f"Bounding Box: {result['coordinates']['bounding_box']['bounds']}")
        print(f"Coordinate count: {len(result['coordinates']['polygon']['coordinates'][0])}")
        print(f"Contiguous: {result['coordinates']['is_contiguous']}")
    print()
    
    # 4. SEARCH SUGGESTIONS
    print("4. SEARCH SUGGESTIONS (an):")
    print("-" * 25)
    suggestions = api.search_suggestions('an', 5)
    print(f"Suggestions count: {len(suggestions)}")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"   {i}. {suggestion['name']} ({suggestion['type']})")
    print()
    
    # 5. PERFORMANCE INFORMATION
    print("5. PERFORMANCE INFORMATION:")
    print("-" * 25)
    perf = api.get_performance_info()
    print(f"Province count: {perf['data_info']['provinces_count']}")
    print(f"District count: {perf['data_info']['districts_count']}")
    print(f"Province file size: {perf['data_info']['provinces_size_mb']:.1f} MB")
    print(f"District file size: {perf['data_info']['districts_size_mb']:.1f} MB")
    print()
    
    # 6. REGION LISTS
    print("6. REGION LISTS:")
    print("-" * 15)
    provinces = api.get_region_list('province', 'tr')
    districts = api.get_region_list('district', 'tr')
    print(f"Province count: {len(provinces)}")
    print(f"District count: {len(districts)}")
    print(f"First 5 provinces: {[p['name'] for p in provinces[:5]]}")
    print()
    
    # 7. HEALTH CHECK
    print("7. HEALTH CHECK:")
    print("-" * 15)
    health = api.health_check()
    print(f"Status: {health['status']}")
    print(f"Metadata loaded: {health['metadata_loaded']}")
    print(f"Search index ready: {health['search_index_ready']}")
    print()
    
    # 8. ERROR HANDLING TEST
    print("8. ERROR HANDLING TEST:")
    print("-" * 20)
    result = api.find_coordinates('NonExistentRegion')
    print(f"Non-existent region test: {result['success']}")
    print(f"Error message: {result['error']}")
    print()
    
    print("=== ALL TESTS COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    test_api() 