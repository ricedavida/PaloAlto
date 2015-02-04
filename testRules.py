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
    pa = PaAPI (apiKeyFile)
    rule = pa.createFireWallRule(name, memFrom, memTo, src, dst, srv, app, act, srcUsr, disRsp, negSrc, negDst, disable, group, hipProf, logStart, logEnd, desc)

    ## Rules Tests ##
    #### Test gets ####
    def test_genRuleNameXML(self):
        self.assertEqual(self.rule.genRuleNameXML(), "[@name='test']")
        
    def test_genRuleFromMemberXML(self):
        self.assertEqual(self.rule.genRuleFromMembersXML(), "<from><member>trust</member><member>untrust</member></from>")
    
    def test_genRuleToMemberXML(self):
        self.assertEqual(self.rule.genRuleToMembersXML(), "<to><member>trust</member><member>untrust</member></to>")
    
    def test_genRuleSourceXML(self):
        self.assertEqual(self.rule.genRuleSourceXML(), "<source><member>any</member></source>")
    
    def test_genRuleDestinationXML(self):
        self.assertEqual(self.rule.genRuleDestinationXML(), "<destination><member>any</member></destination>")
    
    def test_genRuleServiceXML(self):
        self.assertEqual(self.rule.genRuleServiceXML(), "<service><member>any</member></service>")
    
    def test_genRuleApplicationXML(self):
        self.assertEqual(self.rule.genRuleApplicationXML(), "<application><member>any</member></application>")
        
    def test_genRuleActionXML(self):
        self.assertEqual(self.rule.genRuleActionXML(), "<action>allow</action>")
        
    def test_genRuleSourceUserXML(self):
        self.assertEqual(self.rule.genRuleSourceUserXML(), "<source-user><member>any</member></source-user>")
        
    def test_genRuleDisableServerResponseXML(self):
        self.assertEqual(self.rule.genRuleDisableServerResponseXML(), "<option><disable-server-response-inspection>no</disable-server-response-inspection></option>")
        
    def test_genRuleNegateSourceXML(self):
        self.assertEqual(self.rule.genRuleNegateSourceXML(), "<negate-source>no</negate-source>")
    
    def test_genRuleNegateDestinationXML(self):
        self.assertEqual(self.rule.genRuleNegateDestinationXML(), "<negate-destination>no</negate-destination>")
        
    def test_genRuleDisabledXML(self):
        self.assertEqual(self.rule.genRuleDisabledXML(), "<disabled>yes</disabled>")
    
    def test_genRuleGroupsXML(self):
        self.assertEqual(self.rule.genRuleGroupsXML(), "<profile-setting><group><member>bellus</member></group></profile-setting>")
        
    def test_genRuleHipProfilesXML(self):
        self.assertEqual(self.rule.genRuleHipProfilesXML(), "<hip-profiles><member>any</member></hip-profiles>")
        
    def test_genRuleLogStartXML(self):
        self.assertEqual(self.rule.genRuleLogStartXML(), "<log-start>yes</log-start>")
        
    def test_genRuleLogEndXML(self):
        self.assertEqual(self.rule.genRuleLogEndXML(), "<log-end>yes</log-end>")
        
    def test_genRuleDescriptionXML(self):
        self.assertEqual(self.rule.genRuleDescriptionXML(), "<description>This is a test</description>")


    
    def test_getRuleName(self):
        self.assertEqual(self.rule.getRuleName(), "test")

    def test_getRuleFromMembers(self):
        self.assertEqual(self.rule.getRuleFromMembers(), ["trust", "untrust"])
    
    def test_getRuleToMembers(self):
        self.assertEqual(self.rule.getRuleToMembers(), ["trust", "untrust"])
        
    def test_getRuleSource(self):
        self.assertEqual(self.rule.getRuleSource(), ["any"])
    
    def test_getRuleDestination(self):
        self.assertEqual(self.rule.getRuleDestination(), ["any"])
    
    def test_getRuleService(self):
        self.assertEqual(self.rule.getRuleService(), ["any"])
    
    def test_getRuleApplication(self):
        self.assertEqual(self.rule.getRuleApplication(), ["any"])
        
    def test_getRuleAction(self):
        self.assertEqual(self.rule.getRuleAction(), "allow")
    
    def test_getRuleSourceUser(self):
        self.assertEqual(self.rule.getRuleSourceUser(), ["any"])
    
    def test_getRuleDisableServerResponse(self):
        self.assertEqual(self.rule.getRuleDisableServerResponse(), "no")
        
    def test_getRuleNegateSource(self):
        self.assertEqual(self.rule.getRuleNegateSource(), "no")
    
    def test_getRuleNegateDestination(self):
        self.assertEqual(self.rule.getRuleNegateDestination(), "no")
        
    def test_getRuleDisabled(self):
        self.assertEqual(self.rule.getRuleDisabled(), "yes")
        
    def test_getRuleGroups(self):
        self.assertEqual(self.rule.getRuleGroups(), ["bellus"])
    
    def test_getRuleHipProfiles(self):
        self.assertEqual(self.rule.getRuleHipProfiles(), ["any"])
    
    def test_getRuleLogStart(self):
        self.assertEqual(self.rule.getRuleLogStart(), "yes")
        
    def test_getRuleLogEnd(self):
        self.assertEqual(self.rule.getRuleLogEnd(), "yes")
        
    def test_getRuleDescription(self):
        self.assertEqual(self.rule.getRuleDescription(), "This is a test")
        
        
    #### Test sets ####
    def test_setRuleName(self):
        self.rule.setRuleName("test")
        self.assertEqual(self.rule.getRuleName(), "test")

    def test_setRuleFromMembers(self):
        self.rule.setRuleFromMembers(["untrust", "trust"])
        self.assertEqual(self.rule.getRuleFromMembers(), ["untrust", "trust"])
    
    def test_setRuleToMembers(self):
        self.rule.setRuleToMembers(["untrust", "trust"])
        self.assertEqual(self.rule.getRuleToMembers(), ["untrust", "trust"])
        
    def test_setRuleSource(self):
        self.rule.setRuleSource(["test"])
        self.assertEqual(self.rule.getRuleSource(), ["test"])
    
    def test_setRuleDestination(self):
        self.rule.setRuleDestination(["test"])
        self.assertEqual(self.rule.getRuleDestination(), ["test"])
    
    def test_setRuleService(self):
        self.rule.setRuleService(["test"])
        self.assertEqual(self.rule.getRuleService(), ["test"])
    
    def test_setRuleApplication(self):
        self.rule.setRuleApplication(["test"])
        self.assertEqual(self.rule.getRuleApplication(), ["test"])
        
    def test_setRuleAction(self):
        self.rule.setRuleAction("allow")
        self.assertEqual(self.rule.getRuleAction(), "allow")
    
    def test_setRuleSourceUser(self):
        self.rule.setRuleSourceUser(["test"])
        self.assertEqual(self.rule.getRuleSourceUser(), ["test"])
    
    def test_setRuleDisableServerResponse(self):
        self.rule.setRuleDisableServerResponse("no")
        self.assertEqual(self.rule.getRuleDisableServerResponse(), "no")
        
    def test_setRuleNegateSource(self):
        self.rule.setRuleNegateSource("no")
        self.assertEqual(self.rule.getRuleNegateSource(), "no")
    
    def test_setRuleNegateDestination(self):
        self.rule.setRuleNegateDestination("no")
        self.assertEqual(self.rule.getRuleNegateDestination(), "no")
        
    def test_setRuleDisabled(self):
        self.rule.setRuleDisabled("no")
        self.assertEqual(self.rule.getRuleDisabled(), "no")
        
    def test_setRuleGroups(self):
        self.rule.setRuleGroups(["test"])
        self.assertEqual(self.rule.getRuleGroups(), ["test"])
    
    def test_setRuleHipProfiles(self):
        self.rule.setRuleHipProfiles(["test"])
        self.assertEqual(self.rule.getRuleHipProfiles(), ["test"])
    
    def test_setRuleLogStart(self):
        self.rule.setRuleLogStart("no")
        self.assertEqual(self.rule.getRuleLogStart(), "no")
        
    def test_setRuleLogEnd(self):
        self.rule.setRuleLogEnd("yes")
        self.assertEqual(self.rule.getRuleLogEnd(), "yes")
        
    def test_setRuleDescription(self):
        self.rule.setRuleDescription("test")
        self.assertEqual(self.rule.getRuleDescription(), "test")
    
    
    
    #### Test ValueError handling with sets####
    def test_setRuleDisableServerResponseValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.rule.setRuleDisableServerResponse("blah")
            
    def test_setRuleNegateSourceValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.rule.setRuleNegateSource("blah")
            
    def test_setRuleNegateDestinationValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.rule.setRuleNegateDestination("blah")
            
    def test_setRuleDisabledValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.rule.setRuleDisabled("blah")
            
    def test_setRuleLogStartValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.rule.setRuleLogStart("blah")
    
    def test_setRuleLogEndValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.rule.setRuleLogStart("blah")
            
    def test_setRuleLogEndValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.rule.setRuleAction("blah")
    
            
    #### Test TypeError handling with sets ####
    def test_setRuleNameTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleName([])

    def test_setRuleFromMembersTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleFromMembers("")
    
    def test_setRuleToMembersTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleToMembers("")
        
    def test_setRuleSourceTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleSource("")
    
    def test_setRuleDestinationTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleDestination("")
    
    def test_setRuleServiceTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleService("")
    
    def test_setRuleApplicationTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleApplication("")
        
    def test_setRuleActionTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleAction([])
    
    def test_setRuleSourceUserTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleSourceUser("")
    
    def test_setRuleDisableServerResponseTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleDisableServerResponse([])
        
    def test_setRuleNegateSourceTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleNegateSource([])
    
    def test_setRuleNegateDestinationTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleNegateDestination([])
        
    def test_setRuleDisabledTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleDisabled([])
        
    def test_setRuleGroupsTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleGroups("")
    
    def test_setRuleHipProfilesTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleHipProfiles("")
    
    def test_setRuleLogStartTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleLogStart([])
        
    def test_setRuleLogEndTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleLogEnd([])
        
    def test_setRuleDescriptionTypeErrorHandle(self):
        with self.assertRaises(TypeError):
            self.rule.setRuleDescription([])
            
            
            
    
if __name__ == '__main__':
    unittest.main()