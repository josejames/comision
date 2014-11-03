Feature: Calcular comision de venta
	Para calcular la comision de venta
	As un gunsmith
	Se implementa la clase comision

Scenario: commision of 1000 locks, 1000 stocks, 1000 barrels
	Given I have the "1000" locks, "1000" stocks, und "1000" barrels
	When I compute its commission
	Then I see the number "19860.0"

Scenario: commision of 11 locks, 11 stocks, 11 barrels
	Given I have the "11" locks, "11" stocks, und "11" barrels
	When I compute its commission
	Then I see the number "115.0"

Scenario: commision of 4 locks, 0 stocks, 0 barrels
	Given I have the "4" locks, "0" stocks, und "0" barrels
	When I compute its commission
	Then I see the number "18.0"