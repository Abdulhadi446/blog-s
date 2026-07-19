#!/usr/bin/env python3
"""
Test script to verify production configuration
"""
import os
import sys
from app import create_app

def test_production_config():
    """Test that production config loads correctly"""
    # Set environment to production
    os.environ['FLASK_CONFIG'] = 'production'
    
    # Create app
    app = create_app('production')
    
    # Test config values
    assert app.config['DEBUG'] == False, "DEBUG should be False in production"
    assert app.config['TESTING'] == False, "TESTING should be False in production"
    assert 'SECRET_KEY' in app.config, "SECRET_KEY should be set"
    
    print("✓ Production configuration test passed")
    return True

def test_development_config():
    """Test that development config loads correctly"""
    # Set environment to development
    os.environ['FLASK_CONFIG'] = 'development'
    
    # Create app
    app = create_app('development')
    
    # Test config values
    assert app.config['DEBUG'] == True, "DEBUG should be True in development"
    assert app.config['TESTING'] == False, "TESTING should be False in development"
    
    print("✓ Development configuration test passed")
    return True

def test_default_config():
    """Test that default config loads correctly"""
    # Remove FLASK_CONFIG to test default
    if 'FLASK_CONFIG' in os.environ:
        del os.environ['FLASK_CONFIG']
    
    # Create app
    app = create_app()
    
    # Should default to development
    assert app.config['DEBUG'] == True, "DEBUG should be True by default"
    
    print("✓ Default configuration test passed")
    return True

if __name__ == '__main__':
    try:
        test_production_config()
        test_development_config()
        test_default_config()
        print("\n✅ All configuration tests passed!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Configuration test failed: {e}")
        sys.exit(1)