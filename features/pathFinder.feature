Feature: Path Finder

 	I want to find the shortest path between two points in an standard chess game (8x8) using knight movements

@automated
Scenario: Find shortest path between same point situated in one corner
    Given my starting point is A1
    And my destination point is A1
    When I look for one of the shortest path
    Then the path is one of the following ones
    |combination|
    |A1 C2 A1|
    |A1 B3 A1|

@automated
Scenario: Find shortest path between same point situated in the middle of the game
    Given my starting point is F5
    And my destination point is F5
    When I look for one of the shortest path
    Then the path is one of the following ones
    |combination|
    |F5 E7 F5|
    |F5 G7 F5|
    |F5 H6 F5|
    |F5 H4 F5|
    |F5 G3 F5|
    |F5 E3 F5|
    |F5 D4 F5|
    |F5 D6 F5|

@automated
Scenario: Find shortest path between two points that are only one knight movement distance
    Given my starting point is B6
    And my destination point is C4
    When I look for one of the shortest path
    Then the path is one of the following ones
    |combination|
    |B6 C4|

@automated
Scenario: Find shortest path between two points that are separated by two knight movements distance
    Given my starting point is C3
    And my destination point is F6
    When I look for one of the shortest path
    Then the path is one of the following ones
    |combination|
    |C3 D5 F6|
    |C3 E4 F6|

@automated
Scenario: Find shortest path between two points that are separated by two knight movements distance
    Given my starting point is B6
    And my destination point is F1
    When I look for one of the shortest path
    Then the path is one of the following ones
    |combination|
    |B6 C4 D2 F1|
    |B6 D5 E3 F1|

