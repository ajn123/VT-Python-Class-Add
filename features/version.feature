Feature: Valid Version

	@version
	Scenario Outline: Testing Python Version
		Given I have Python <version> installed
		When I try to check my version
		Then I should see <expected>

		Examples: Versions
			| version | expected   |
			| 2.7.4   | no error   |
			| 2.9.9   | a warning  |
			| 3.0.1   | an error   |
