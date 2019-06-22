Feature: List with unique strings

    Scenario: Creating a limited unique list of strings
        Given a new unique list
        When we add a null/empty string to the list
        Then the list should ignore and be empty

    Scenario: Validate the list order
        Given another new unique empty list
        When we add 4 itens
        Then the first added item is the first in the list and the last added item is the last
        And the list can be looked up by index counting from 0

    Scenario: Check for list "uniqueness"
        Given a new list with some itens
        When we add a item which was already in the list and not in the last position
        Then the item will not be duplicated and instead will go to the last position

    Scenario: Check for list length limit
        Given we have a list with 2 items with max length of 5
        When we add more itens then the list length
        Then the first itens should be removed and the new items inserted
