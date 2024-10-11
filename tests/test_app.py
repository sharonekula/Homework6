
"""
This module for the REPL functionality of the App class. 
"""
from app import App

def test_app_start_exit_command(capfd, monkeypatch):

    """Testing that the REPL (Read, Evaluate, Print, Loop) will exit on exit command correctly"""

    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    App.start()
    out, err = capfd.readouterr()

    assert "Welcome to my App. Type 'exit' to exit." in out
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):

    """Testing the unknown command input correctly"""

    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, err = capfd.readouterr()

    assert "Welcome to my App. Type 'exit' to exit." in out
    assert "Unknown command. Type 'exit' to exit." in out
    assert "Exiting..." in out
