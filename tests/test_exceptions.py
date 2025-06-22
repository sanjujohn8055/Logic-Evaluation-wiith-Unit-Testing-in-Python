from src.exceptions import MappingException

def test_mapping_exception_raised():
    try:
        raise MappingException("Test error")
    except MappingException as e:
        assert str(e) == "Test error"
