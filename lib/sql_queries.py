# Query to select all female bears and return their name and age
select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex='F';
"""

# Query to select all bears' names and order them in alphabetical order
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        bears.name
    FROM bears
    ORDER BY bears.name;
"""

# Query to select all bears' names and ages that are alive and order them from youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE alive=true
    ORDER BY bears.age;
"""

# Query to select the oldest bear and return its name and age
select_oldest_bear_and_returns_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    ORDER BY bears.age DESC
    LIMIT 1;
"""

# Query to select the youngest bear and return its name and age
select_youngest_bear_and_returns_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    ORDER BY bears.age
    LIMIT 1;
"""
