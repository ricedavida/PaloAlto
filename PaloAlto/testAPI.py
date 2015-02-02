import unittest
from PaAPI import *
class testRules (unittest.TestCase):
    '''
    Class for testing the PaAPI.py and Rules.py Classes which are part of the PaloAlto API project

        Authors:
            David Rice riceda@potsdam.edu
        Last Updated:
            01/29/2015 
    '''

    apiKeyFile = "paconnect.conf"
    
    name = "test"
    memFrom = ["trust", "untrust"] #Rule From members
    memTo = ["trust", "untrust"] # Rule To members
    src = ["any"] # Rule Source
    dst = ["any"] # Rule Destination
    srv = ["any"] # Rule Service
    app = ["any"] # Rule Application
    act = "allow" # Rule Action
    srcUsr = ["any"] # Rule Source User
    disRsp = "no" # Rule Disable Server Response (yes or no)
    negSrc = "no" # Rule Negate Source (yes or no)
    negDst = "no" # Rule Negate Destination (yes or no)
    disable = "yes" # Rule Disable (yes or no)
    group = ["bellus"] # Rule Groups
    hipProf = ["any"] # Rule hipProf
    logStart = "yes" # Rule Log Start (yes or no)
    logEnd = "yes" # Rule Log End (yes or no)
    desc = "This is a test" # Rule Description
    pa = ""
    rule = ""
    
    def setUp(self):
        self.pa = PaAPI (self.apiKeyFile)
        self.rule = self.pa.createFireWallRule(
                    self.name, 
                    self.memFrom, 
                    self.memTo,
                    self.src, 
                    self.dst, 
                    self.srv, 
                    self.app, 
                    self.act, 
                    self.srcUsr, 
                    self.disRsp, 
                    self.negSrc, 
                    self.negDst, 
                    self.disable, 
                    self.group, 
                    self.hipProf, 
                    self.logStart, 
                    self.logEnd, 
                    self.desc
                )

    # write a rule to the PaloAlto, Commit and check if it exists
    def test_createAndCommitFireWallRule(self):
        self.pa.writeFireWallRule(self.rule)
        self.pa.commitFireWallConfiguration()
        print ("Committing the Rule")
        sleep(30)
        localPa = PaAPI (self.apiKeyFile)
        localRule = localPa.getFireWallRule(self.rule.getRuleName())
        print ("Testing if the Rule exists")
        self.assertEqual(localRule.getRuleName(), self.name)
    
    # delete a rule from the PaloAlto, Commit and check if it exists (it should raise a ValueError)    
    def test_deleteAndCommitFireWallRule(self):
        localRule = self.pa.getFireWallRule(self.name)
        self.pa.deleteFireWallRule(localRule)
        self.pa.commitFireWallConfiguration()
        print ("Deleting the Rule")
        sleep(30)
        localPa = PaAPI (self.apiKeyFile)
        print ("Ensuring the Rule does not exist on the PaloAlto")
        with self.assertRaises(ValueError):
            localPa.getFireWallRule(self.name).getRuleName()

if __name__ == '__main__':
    unittest.main()