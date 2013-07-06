Feature: Valid Version

	@version @travis
	Scenario Outline: Testing Python Version
		Given I have Python <version> installed
		When I try to check my version
		Then I should see <expected> in my message

		Examples: Versions
			| version | expected     |
			| 2.7.4   | "Nothing"    |
			| 2.9.9   | "Warning"    |
			| 3.0.1   | "Error"      |
