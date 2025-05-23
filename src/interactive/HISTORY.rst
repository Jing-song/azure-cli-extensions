.. :changelog:

Release History
===============

1.0.0b1
+++++
* Compliant with Python 3.12

0.5.3
+++++
* Optimize the visualization of help text when the window is reduced horizontally

0.5.2
+++++
* Add command skipped message in Scenario Execution Mode
* Fix Scenario Idx out of bound when selecting recommended scenario
* Fix `KeyError` when entering param not in sample in scenario mode

0.5.1
+++++
* Fix bugs to prevent users from exiting the entire az interactive by using Ctrl+C during command execution
* Fix confusing error message caused by uncompleted command loading and param update

0.5.0
+++++
* Support command recommendations that predicts the next commands users might need.
* Support scenario recommendations to help users complete the complex scenarios more smoothly and simply.
* Support new config `az config set interactive.enable_recommender=False` to disable these new recommenders.
* Fix display offset in toolbar.
* Add loading bar to avoid command execution errors caused by uncompleted command loading and param update. User can use CTRL+C to cancel the loading bar.
* Add value completion mechanism for parameter value in scenarios
* Support searching ability for scenarios
* Optimize parameter completion mechanism to recommend one parameter at a time

0.4.6
+++++
* Compatible with argcomplete 2.0.0

0.4.5
+++++
* Fix #17740: `az interactive` fails with `progress_patch() got an unexpected keyword argument 'det'`

0.4.4
+++++
* Remove dependency of azure-cli-core's ENV_ADDITIONAL_USER_AGENT

0.4.3
+++++
* Fix config problem in interactive

0.4.2
+++++
* Update to remain compatible with azure-cli 2.0.62.

0.4.1
+++++
* Remove command registration, rely on module to be called.

0.4.0
+++++
* Converted from interactive module to extension.

0.3.31
++++++
* Ensure global subscription parameter appears in parameters.

0.3.30
++++++
* Fix error found on windows where commands fail to run properly.

0.3.29
++++++
* Fix command loading problem in interactive that was caused by deprecated objects.

0.3.28
++++++
* Minor fixes

0.3.27
++++++
* Minor fixes

0.3.26
++++++
* Minor fixes

0.3.25
++++++
* Update PyYAML dependency to 4.2b4

0.3.24
++++++
* Minor fixes

0.3.23
++++++
* Minor fixes

0.3.22
++++++
* Fix dependency versions.

0.3.21
++++++
* Mute logging from parser for completions.
* Made interactive more resistant to stale/corrupted help caches.

0.3.20
++++++
* Allow interactive completers to function with positional arguments.
* More user-friendly output when users type '\'.
* Fix completions for parameters with no help.
* Fix descriptions for command-groups.

0.3.19
++++++
* Stops completions upon unrecognized commands.
* Add event hooks before and after command subtree is created.
* Allow completions for --ids parameters.
* `sdist` is now compatible with wheel 0.31.0

0.3.18
++++++
* Completions kick in as soon as command table loading is done.
* Fix bug with using `--style` parameter.
* Interactive lexer instantiated after command table dump if missing.
* Improvements to completer support.

0.3.17
++++++
* Persist history across different sessions
* Fixed history while in scope
* Updates to interactive telemetry
* Fixed progress meter for long running operations
* Completions more robust to command table exceptions

0.3.16
++++++
* Fix issue where user is prompted to login when using interactive mode in Cloud Shell.
* Fixed regression with missing parameter completions.

0.3.15
++++++
* Fixed issue where command option completions no longer appeared.

0.3.14
++++++
* Clean up unused test files

0.3.13
++++++
* Fix issue where interactive would not start on Python 2.
* Fix errors on start up
* Fix some commands not running in interactive mode

0.3.12
++++++
* Update for CLI core changes.

0.3.11
++++++
* minor fixes

0.3.10 (2017-09-22)
+++++++++++++++++++
* minor fixes

0.3.9 (2017-08-31)
++++++++++++++++++
* minor fixes

0.3.8 (2017-08-28)
++++++++++++++++++
* minor fixes

0.3.7 (2017-07-27)
++++++++++++++++++

* Improves the start up time by using cached commands


0.3.7 (2017-07-27)
++++++++++++++++++

* Increase test coverage

0.3.5 (2017-06-21)
++++++++++++++++++

* Enhance the '?' gesture to also inject into the next command

0.3.4 (2017-06-13)
++++++++++++++++++

* Fixes Interactive errors with the profile 2017-03-09-profile-preview (#3587)
* Allows '--version' as a parameter for interactive mode (#3645)
* Stop Interactive Mode from Throwing errors from Validation completions (#3570)
* Progress Reporting for template deployments (#3510)

0.3.3 (2017-05-30)
++++++++++++++++++

* --progress flag
* Removed --debug and --verbose from completions

0.3.2 (2017-05-18)
++++++++++++++++++

* Bug fixes.
* Remove 'interactive' from completions (#3324)

0.3.1 (2017-05-09)
++++++++++++++++++

* Add link to blog in ‘az interactive —help’ (#3252)


0.3.0 (2017-05-05)
++++++++++++++++++

* Integrate interactive into az
* Colors Options
* Rename 'shell' => 'interactive'


0.2.1
++++++++++++++++++

* CLI Performance changes integrated


0.2.0
++++++++++++++++++

* Public Preview release


0.1.1
++++++++++++++++++

* Preview release
