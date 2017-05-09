# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s rer.news -t test_ernews.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src rer.news.testing.RER_NEWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_ernews.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a ERNews
  Given a logged-in site administrator
    and an add ernews form
   When I type 'My ERNews' into the title field
    and I submit the form
   Then a ernews with the title 'My ERNews' has been created

Scenario: As a site administrator I can view a ERNews
  Given a logged-in site administrator
    and a ernews 'My ERNews'
   When I go to the ernews view
   Then I can see the ernews title 'My ERNews'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add ernews form
  Go To  ${PLONE_URL}/++add++ERNews

a ernews 'My ERNews'
  Create content  type=ERNews  id=my-ernews  title=My ERNews


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the ernews view
  Go To  ${PLONE_URL}/my-ernews
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a ernews with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the ernews title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
