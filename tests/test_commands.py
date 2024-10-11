""" 
Test suite for verifying the arithmetic commands and REPL behavior in the App class.
This module contains unit tests for basic arithmetic operations such as addition,
subtraction, multiplication, and division, along with tests for REPL menu handling.
"""
import pytest
from app import App
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand


def test_add_command(capfd, monkeypatch):
    """
    Test the AddCommand to ensure that the addition of two numbers is computed and displayed correctly.
    Simulates user input to provide the numbers to be added and verifies the output.
    """
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = AddCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "The result of 5 + 3 = 8" in out, "The addition result should be 8."

def test_subtract_command(capfd, monkeypatch):
    """
    Test the SubtractCommand to verify that subtraction between two numbers is performed correctly.
    Simulates user input for the subtraction operands and checks the displayed result.
    """
    inputs = iter(['9', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = SubtractCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "The result of 9 - 4 = 5" in out, "The subtraction result should be 5."

def test_multiply_command(capfd, monkeypatch):
    """
    Test the MultiplyCommand to ensure that multiplication of two numbers is handled and displayed correctly.
    Provides user input via simulation and verifies the multiplication output.
    """
    inputs = iter(['6', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = MultiplyCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "The result of 6 * 7 = 42" in out, "The multiplication result should be 42."

def test_divide_command(capfd, monkeypatch):
    """
    Test the DivideCommand to confirm that division between two numbers is executed and shown correctly.
    Simulates user input to supply the division operands and checks the output for correctness.
    """
    inputs = iter(['8', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "The result of 8 / 4 = 2" in out, "The division result should be 2."

def test_dividebyzero_command(capfd, monkeypatch):
    """
    Test the DivideCommand to ensure proper error handling when attempting to divide by zero.
    Simulates input where the denominator is zero and verifies that the correct error message is displayed.
    """
    inputs = iter(['10', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "DivisionByZero Exception" in out, "This operation should raise a division by zero error."

def test_app_menu_command(capfd, monkeypatch):
    """
    Test the App's REPL functionality to ensure that the 'menu' command works as expected
    and that the application exits properly when the 'exit' command is issued.
    Simulates user interaction with the REPL menu and exit commands.
    """
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    assert str(e.value) == "Exiting...", "The app did not exit as expected."
