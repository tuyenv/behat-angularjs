<?php

use Behat\Behat\Context\ClosuredContextInterface,
    Behat\Behat\Context\TranslatedContextInterface,
    Behat\Behat\Context\BehatContext,
    Behat\Behat\Exception\PendingException;
use Behat\Gherkin\Node\PyStringNode,
    Behat\Gherkin\Node\TableNode;

use Behat\Mink\Mink,
    Behat\Mink\Session,
    Behat\Mink\Driver\GoutteDriver,
    Behat\Mink\Driver\Goutte\Client as GoutteClient;

use Behat\MinkExtension\Context\MinkContext;
use Behat\Behat\Tester\Exception\PendingException;
use Behat\Behat\Context\SnippetAcceptingContext;
use Behat\MinkExtension\Context\MinkContext;

//
// Require 3rd-party libraries here:
//
//   require_once 'PHPUnit/Autoload.php';
//   require_once 'PHPUnit/Framework/Assert/Functions.php';
//

/**
 * Features context.
 */
class FeatureContext extends MinkContext implements SnippetAcceptingContext
{
    /**
     * Initializes context.
     * Every scenario gets it's own context object.
     *
     * @param array $parameters context parameters (set them up through behat.yml)
     */
    public function __construct(array $parameters)
    {
        // Initialize your context here
    }

    /**
     * @Given /^I am authenticated as "([^"]*)" using "([^"]*)"$/
     */
    public function iAmAuthenticatedAs($username, $password) {
        $this->visit('/login');
        $this->fillField('username', $username);
        $this->fillField('password', $password);
        $this->pressButton('Sign in');
    }

    /**
     * @When /^I am wait for the page to be loaded "([^"]*)"$/
     */
    public function iAmWaitForThePageToBeLoaded($time)
    {
        //sleep($time);
        //$this->getSession()->wait($time, "document.readyState === 'complete'");


        // Wait for angular to load
        $this->getSession()->wait(1000, "typeof angular != 'undefined'");
        // Wait for angular to be testable
        $this->getPage()->evaluateScript(
            'angular.getTestability(document.body).whenStable(function() {
                window.__testable = true;
            })'
        );
        $this->getSession()->wait(1000, 'window.__testable == true');
    }

    /**
     * @Given /^I visit "([^"]*)"$/
     */
    public function iVisit($arg1)
    {
        $this->visit($arg1);
    }

//
// Place your definition and hook methods here:
//
//    /**
//     * @Given /^I have done something with "([^"]*)"$/
//     */
//    public function iHaveDoneSomethingWith($argument)
//    {
//        doSomethingWith($argument);
//    }
//
}
