def reads_file(path: str) :
    """
    Description of the function:
    Reads and validates a .drk file and extracts the board information.

    Parameters:
    - path (str): Path to the .drk file.

    Returns:
    - dict: Contains the board information (dimensions, positions, units).

    Exceptions:
    - FileNotFoundError: If the file does not exist.
    - ValueError: If the file format is incorrect.

    Version:
    - specification: Sohaib El Kaich (v.1 22/02/25)
    """
    pass

def initialize_game(config: dict) :
    """
    Description of the function:
    Initializes the game state from the data in the .drk file.

    Parameters:
    - config (dict): Data extracted from the .drk file.

    Returns:
    - dict: Initial game state with positions and stats of entities.

    Exceptions:
    - KeyError: If essential information (map, altars, etc.) is missing.

    Version:
    - specification: Ayamn Lakhdar (v.1 22/02/25)
    """
    pass

def save_game_state(file: str, game_data: dict) :
    """
    Description of the function:
    Saves the current game state to a file.

    Parameters:
    - file (str): Name of the save file.
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the save is successful, False otherwise.

    Exceptions:
    - IOError: If an error occurs while writing the file.

    Version:
    - specification: Mireille Merciel Kamseu Takam (v.1 22/02/25)                              
    """
    pass

def check_game_over(game_data: dict) :
    """
    Description of the function:
    Checks the end game conditions.

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the game is over, False otherwise.

    Exceptions:
    - KeyError: If a necessary key is missing in game_data.

    Version:
    -specification: Soufiane Rguig(v.1 22/02/25)
    """
    pass

def afficher_statut_jeu(game_data: dict):
    """
    Description of the function:
    Displays the current state of the game, including turn number, apprentices, dragons, and eggs.

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - None: This function returns nothing as it is used solely to display the game status.

    Version:
    -  specification: Ayamn Lakhdar (v.1 22/02/25)
    """
    pass

def use_summon(player: int, game_data: dict) :
    """
    Description of the function:
    Checks the player's cooldown, teleports all their units to their altar, and updates the cooldown.

    Parameters:
    - player (int): Player number (1 or 2).
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the summon is successful, False if cooldown is active.

    Exceptions:
    - ValueError: If the player is invalid.

    Version:
    - specification: Soufiane Rguig(v.1 22/02/25)
    """
    pass

def teleport_units(player: int, game_data: dict) :
    """
    Description of the function:
    Finds the player's altar to teleport their apprentices and updates their positions.

    Parameters:
    - player (int): Player number (1 or 2).
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the teleport is successful, False otherwise.

    Exceptions:
    - ValueError: If the player is invalid.

    Version:
    -  specification: Ayamn Lakhdar (v.1 22/02/25)
    """
    pass

def regenerate_cooldown(game_data: dict) :
    """
    Description of the function:
    Regenerates the health of an entity.

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - bool: True if regeneration occurs.

    Version:
    - specification: Soufiane Rguig(v.1 22/02/25)
    """
    pass

def hatch_egg(apprentice_name: str, game_data: dict) :
    """
    Description of the function:
    Checks if an apprentice is on an egg tile to decrement the hatching time and hatch the egg.

    Parameters:
    - apprentice_name (str): Name of the apprentice.
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the egg hatches, False otherwise.

    Version:
    - specification: Soufiane Rguig(v.1 22/02/25)
    """
    pass

def is_alone_in_tile(name: str, game_data: dict) :
    """
    Description of the function:
    Checks if an entity exists on the board.

    Parameters:
    - name (str): Name of the entity.
    - game_data (dict): Current game state.

    Returns:
    - bool: True if only one entity exists, False otherwise.

    Version:
    - specification: Mireille Merciel Kamseu Takam (v.1 22/02/25) 
    """
    pass

def decrement_hatch_time(game_data: dict) :
    """
    Description of the function:
    Decrements the egg hatching preparation time.

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - None: This function modifies the game state in place.

    Version:
    - specification: Sohaib El Kaich (v.1 22/02/25)
    """
    pass

def egg_exists(name: str, game_data: dict) :
    """
    Description of the function:
    Checks if an egg exists on the board.

    Parameters:
    - name (str): Name of the egg.
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the egg exists, False otherwise.

    Version:
    -  specification: Ayamn Lakhdar (v.1 22/02/25)
    """
    pass

def egg_hation(game_data: dict) :
    """
    Description of the function:
    Removes the egg structure and replaces it with the dragon structure.

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - None: This function modifies the game state in place.

    Version:
    -specification: Sohaib El Kaich (v.1 22/02/25)
    """
    pass

def attack(dragon_name: str, direction: str, game_data: dict) :
    """
    Description of the function:
    Registers a dragon's attack.

    Parameters:
    - dragon_name (str): Name of the dragon.
    - direction (str): Direction of the attack.

    Exceptions:
    - KeyError: If the dragon does not exist.

    Version:
    -  specification: Ayamn Lakhdar (v.1 22/02/25)
    """
    pass

def parse_order(order: str, game_data: dict) :
    """
    Description of the function:
    Converts a player's order into an action understandable by the game.

    Parameters:
    - order (str): The order given by the player.
    - game_data (dict): Current game state.

    Returns:
    - dict: A dictionary representing the action.

    Exceptions:
    - ValueError: If the order is malformed or invalid.

    Version:
    - specification: Sohaib El Kaich (v.1 22/02/25)
    """
    pass

def reduce_health(name: str, game_data: dict) :
    """
    Description of the function:
    Reduces the health of an entity.

    Parameters:
    - name (str): Name of the dragon.
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the reduction occurs.

    Version:
    - specification: Mireille Merciel Kamseu Takam (v.1 22/02/25) 
    """
    pass

def dragon_exists(name: str, game_data: dict) :
    """
    Description of the function:
    Checks if a dragon exists on the board.

    Parameters:
    - name (str): Name of the dragon.
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the dragon exists, False otherwise.

    Exceptions:
    - KeyError: If `dragons` does not exist in game_data.

    Version:
    - specification: Sohaib El Kaich (v.1 22/02/25)
    """
    pass

def apply_attacks(game_data: dict) :
    """
    Description of the function:
    Applies all registered attacks simultaneously.

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - None: This function modifies the game state in place.

    Version:
    -specification: Mireille Merciel Kamseu Takam (v.1 22/02/25) 
    """
    pass

def remove_entity(game_data: dict) :
    """
    Description of the function:
    Removes entities with health less than or equal to 0 (hp <= 0).

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - None: This function modifies the game state in place.

    Version:
    - specification: Sohaib El Kaich (v.1 22/02/25)
    """
    pass

def manage_magic_link(name: str, game_data: dict) :
    """
    Description of the function:
    Applies the effects of the link between an apprentice and their dragons.

    Parameters:
    - name (str): Name of the dragon.
    - game_data (dict): Current game state.

    Returns:
    - None: This function modifies the game state in place.

    Version:
    - specification: Ayamn Lakhdar (v.1 22/02/25)
    """
    pass

def check_attack_path(game_data: dict) :
    """
    Description of the function:
    Calculates the tiles affected by a dragon's attack.

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - list: Tiles considered in the attack (tuples).

    Version:
    - specification: Mireille Merciel Kamseu Takam (v.1 22/02/25) 
    """
    pass

def move_entity(name: str, direction: str, game_data: dict) :
    """
    Description of the function:
    Moves an entity in a given direction.

    Parameters:
    - name (str): Name of the entity.
    - direction (str): Direction (N, NE, E, SE, S, SW, W, NW).
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the movement is successful, False otherwise.

    Exceptions:
    - ValueError: If the movement is invalid.

    Version:
    - specification: Soufiane Rguig(v.1 22/02/25)
    """
    pass

def can_move(name: str, direction: str, game_data: dict) :
    """
    Description of the function:
    Checks if an entity can move in a given direction.

    Parameters:
    - name (str): Name of the entity.
    - direction (str): Direction (N, NE, E, SE, S, SW, W, NW).
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the movement is possible, False otherwise.

    Exceptions:
    - KeyError: If the entity does not exist.
    - ValueError: If the direction is invalid.

    Version:
    - specification: Ayamn Lakhdar (v.1 22/02/25)
    """
    pass

def entity_exists(name: str, game_data: dict) :
    """
    Description of the function:
    Checks if an entity exists on the board.

    Parameters:
    - name (str): Name of the entity.
    - game_data (dict): Current game state.

    Returns:
    - bool: True if the entity exists, False otherwise.

    Exceptions:
    - KeyError: If `entity` does not exist in game_data.

    Version:
    - specification: Sohaib El Kaich (v.1 22/02/25)
    """
    pass

def check_movement_path(game_data: dict) :
    """
    Description of the function:
    Calculates the tiles an entity can move to.

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - list: Tiles considered in the movement (tuples).

    Version:
    - specification: Soufiane Rguig(v.1 22/02/25)
    """
    pass

def convert_direction(direction: str) :
    """
    Description of the function:
    Converts a direction (str) into a tuple of coordinates (int).

    Parameters:
    - direction: The direction of movement (str).

    Returns:
    - tuple: Direction as a tuple of coordinates (tuple).

    Version:
    - specification: Soufiane Rguig(v.1 22/02/25)
    """
    pass

def check_tile(game_data: dict, row: int, column: int) :
    """
    Description of the function:
    Checks if a position is within the board limits.

    Parameters:
    - game_data (dict): Current game state.
    - row: Row to move to (int).
    - column: Column to move to (int).

    Returns:
    - bool: True if the tile is within the board.

    Version:
    - specification: Soufiane Rguig(v.1 22/02/25)
    """
    pass

def regenerate_health(name: str, game_data: dict) :
    """
    Description of the function:
    Regenerates the health of a specific entity (apprentice or dragon).

    Parameters:
    - name (str): Name of the entity.
    - game_data (dict): Current game state.

    Returns:
    - bool: True if regeneration occurs, False otherwise.

    Exceptions:
    - KeyError: If the entity does not exist.

    Version:
    - specification: Sohaib El Kaich (v.1 22/02/25)
    """
    pass

def regenerate_entities(game_data: dict) :
    """
    Description of the function:
    Applies health regeneration to all surviving entities.

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - None: Modifies game_data in place.

    Exceptions:
    - KeyError: If a necessary key is missing in game_data.

    Version:
    -  specification: Ayamn Lakhdar (v.1 22/02/25)
    """
    pass

def validate_order(order: str) :
    """
    Description of the function:
    Validates the syntax of an order given by a player.

    Parameters:
    - order (str): The order given by the player.

    Returns:
    - bool: True if the order is valid, False otherwise.

    Version:
    - specification: Soufiane Rguig(v.1 22/02/25)
    """
    pass

def execute_turn_tasks(game_data: dict) :
    """
    Description of the function:
    Orchestrates the 5 phases of the game turn.

    Parameters:
    - game_data (dict): Current game state.

    Returns:
    - None: Modifies game_data in place.

    Exceptions:
    - KeyError: If a necessary key is missing in game_data.

    Version:
    - specification: Sohaib El Kaich (v.1 22/02/25)
    """
    pass

def record_last_action(game_data: dict, action: str) :
    """
    Description of the function:
    Records the last action that occurred in the previous turn.

    Parameters:
    - game_data (dict): Current state of the game.
    - action (str): The last action performed.

    Returns:
    - None: Updates game_data in place.

    Version:
    - Author: specification: Soufiane Rguig(v.1 22/02/25)
    """
    pass

def count_turns(game_data: dict) :
    """
    Description of the function:
    Calculates the number of turns that have elapsed since the start of the game.

    Parameters:
    - game_data (dict): Current state of the game.

    Returns:
    - int: Total number of turns played.

    Version:
    - specification: Mireille Merciel Kamseu Takam (v.1 22/02/25) 
    """
    pass

def generate_AI_orders(player: int, game_data: dict) :
    """
    Description of the function:
    Generates orders for an AI player.

    Parameters:
    - player (int): The AI player's number (1 or 2).
    - game_data (dict): The current state of the game.

    Returns:
    - list: A list of orders as strings.

    Version:
    - specification: Sohaib El Kaich (v.1 22/02/25)
    """
    pass