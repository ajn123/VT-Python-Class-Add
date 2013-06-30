Feature: Valid Version

	@search
	Scenario Outline: Testing Python Version
		Given I have Python <version> installed
		When I try to run the program
		Then I should see <message>

		Examples: Versions
			| version | message   |
			| 2.7.4   | no error  |
			| 2.9.9   | a warning |
			| 3.0.1   | an error  |
