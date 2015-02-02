class Rules:
    '''
    This class will be used in the creation of Rule objects
    
        Authors:
            David Rice riceda@potsdam.edu
        Last Updated:
            01/29/2015
    '''
    name = "" # Rule name
    memFrom = [] #Rule From members
    memTo = [] # Rule To members
    src = [] # Rule Source
    dst = [] # Rule Destination
    srv = [] # Rule Service
    app = [] # Rule Application
    act = "" # Rule Action
    srcUsr = [] # Rule Source User
    disRsp = "" # Rule Disable Server Response (yes or no)
    negSrc = "" # Rule Negate Source (yes or no)
    negDst = "" # Rule Negate Destination (yes or no)
    disable = "" # Rule Disable (yes or no)
    group = [] # Rule Groups
    hipProf = [] # Rule hipProf
    logStart = "" # Rule Log Start (yes or no)
    logEnd = "" # Rule Log End (yes or no)
    desc = "" # Rule Description

    '''
    Constructor: will create and return a Rule object
    
        Constructor args: 
            name => name of the rule (string)
            memFrom => from members of the rule (list of strings => zones)
            memTo => to members of the rule (list of strings => zones)
            src => sources of the rule (list of strings)
            dst => destination of the rule (list of strings)
            srv => services of the rule (list of strings)
            app => applications of the rule (list of strings)
            act => action of the rule (string => 'allow' or 'deny')
            srcUsr => source users of the rule (list of strings)
            disRsp => disable server response of the rule (string => 'yes' or 'no')
            negSrc => negate sources of the rule (string => 'yes' or 'no')
            negDst => negate destinations of the rule (string => 'yes' or 'no')
            disable => disable the rule (string => 'yes' or 'no')
            group => groups of the rule (list of strings)
            hipProf => hip-profiles of the rule (list of strings)
            logStart => start the log of the rule (string => 'yes' or 'no')
            logEnd => end the log of the rule (string => 'yes' or 'no')
            desc => description of the rule (string)
    '''
    def __init__(self, name, memFrom, memTo, src, dst, srv, app, act, srcUsr, disRsp, negSrc, negDst, disable, group, hipProf, logStart, logEnd, desc):
        if type(name) is not str:
            raise TypeError("Type must be a string")
        if type(memFrom) is not list:
            raise TypeError("Type must be a list")
        if type(memTo) is not list:
            raise TypeError("Type must be a list")
        if type(src) is not list:
            raise TypeError("Type must be a list")
        if type(dst) is not list:
            raise TypeError("Type must be a list")
        if type(srv) is not list:
            raise TypeError("Type must be a list")
        if type(app) is not list:
            raise TypeError("Type must be a list")
        if type(act) is not str:
            raise TypeError("Type must be a string")
        if act != "allow" and act != "deny":
            raise ValueError("Value must be 'allow' or 'deny'")
        if type(srcUsr) is not list:
            raise TypeError("Type must be a list")
        if type(disRsp) is not str:
            raise TypeError("Type must be a string")
        if disRsp != "yes" and disRsp != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        if type(negSrc) is not str:
            raise TypeError("Type must be a string")
        if negSrc != "yes" and negSrc != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        if type(negDst) is not str:
            raise TypeError("Type must be a string")
        if negDst != "yes" and negDst != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        if type(disable) is not str:
            raise TypeError("Type must be a string")
        if disable != "yes" and disable != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        if type(group) is not list:
            raise TypeError("Type must be a list")
        if type(hipProf) is not list:
            raise TypeError("Type must be a list")
        if type(logStart) is not str:
            raise TypeError("Type must be a string")
        if logStart != "yes" and logStart != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        if type(logEnd) is not str:
            raise TypeError("Type must be a string")
        if logEnd != "yes" and logEnd != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        if type(desc) is not str:
            raise TypeError("Type must be a string")
        self.name = name
        self.memFrom = memFrom
        self.memTo = memTo
        self.src = src
        self.dst = dst
        self.srv = srv
        self.app = app
        self.act = act
        self.srcUsr = srcUsr
        self.disRsp = disRsp
        self.negSrc = negSrc
        self.negDst = negDst
        self.disable = disable
        self.group = group
        self.hipProf = hipProf
        self.logStart = logStart
        self.logEnd = logEnd
        self.desc = desc
    
    
    ### Generate Methods ###
    '''
    genRuleNameXML: will return an XML string version of the Rule's name
    '''
    def genRuleNameXML(self):
        return "[@name='" + self.name + "']"
    
    '''
    genRuleFromMembersXML: will return an XML string version of the Rule's 'from' members (if any exist)
    '''
    def genRuleFromMembersXML(self):
        if self.memFrom:
            retStr = "<from>"
            for attr in self.memFrom:
                retStr = retStr + "<member>" + attr + "</member>"
            retStr = retStr + "</from>"
            return retStr
        else:
            return ""
    
    '''
    genRuleToMembersXML: will return an XML string version of the Rule's 'to' members (if any exist)
    '''
    def genRuleToMembersXML(self):
        if self.memTo:
            retStr = "<to>"
            for attr in self.memTo:
                retStr = retStr + "<member>" + attr + "</member>"
            retStr = retStr + "</to>"
            return retStr
        else:
            return ""
    
    '''
    genRuleSourceXML: will return an XML string version of the Rule's sources (if any exist)
    '''
    def genRuleSourceXML(self):
        if self.src:
            retStr = "<source>"
            for attr in self.src:
                retStr = retStr + "<member>" + attr + "</member>"
            retStr = retStr + "</source>"
            return retStr
        else:
            return ""
    
    
    '''
    genRuleDestinationXML: will return an XML string version of the Rule's destinations (if any exist)
    '''
    def genRuleDestinationXML(self):
        if self.dst:
            retStr = "<destination>"
            for attr in self.dst:
                retStr = retStr + "<member>" + attr + "</member>"
            retStr = retStr + "</destination>"
            return retStr
        else:
            return ""
    
    '''
    genRuleServiceXML: will return an XML string version of the Rule's Services (if any exist)
    '''
    def genRuleServiceXML(self):
        if self.srv:
            retStr = "<service>"
            for attr in self.srv:
                retStr = retStr + "<member>" + attr + "</member>"
            retStr = retStr + "</service>"
            return retStr
        else:
            return ""
    
    '''
    genRuleApplicationXML: will return an XML string version of the Rule's applications (if any exist)
    '''
    def genRuleApplicationXML(self):
        if self.app:
            retStr = "<application>"
            for attr in self.app:
                retStr = retStr + "<member>" + attr + "</member>"
            retStr = retStr + "</application>"
            return retStr
        else:
            return ""
    
    '''
    genRuleActionXML: will return an XML string version of the Rule's action (or defaults to deny)
    '''
    def genRuleActionXML(self):
        if self.act:
            return "<action>" + self.act + "</action>"
        else:
            return "<action>deny</action>"
    
    '''
    genRuleSourceUserXML: will return an XML string version of the Rule's source users (if any exist)
    '''
    def genRuleSourceUserXML(self):
        if self.srcUsr:
            retStr = "<source-user>"
            for attr in self.srcUsr:
                retStr = retStr + "<member>" + attr + "</member>"
            retStr = retStr + "</source-user>"
            return retStr
        else:
            return ""
    
    '''
    genRuleDisableServerResponseXML: will return an XML string version of the Rule's disable server response status (defaults to yes)
    '''
    def genRuleDisableServerResponseXML(self):
        if self.disRsp:
            return "<option><disable-server-response-inspection>" + self.disRsp + "</disable-server-response-inspection></option>"
        else:
            return "<option><disable-server-response-inspection>yes</disable-server-response-inspection></option>"

    '''
    genRuleNegateSourceXML: will return an XML string version of the Rule's negate source status (defaults to no)
    '''
    def genRuleNegateSourceXML(self):
        if self.negSrc:
            return "<negate-source>" + self.negSrc + "</negate-source>"
        else:
            return "<negate-source>no</negate-source>"
    
    '''
    genRuleNegateDestinationXML: will return an XML string version of the Rule's negate destination status (defaults to no)
    '''
    def genRuleNegateDestinationXML(self):
        if self.negDst:
            return "<negate-destination>" + self.negDst + "</negate-destination>"
        else:
            return "<negate-destination>no</negate-destination>"
    
    '''
    genRuleDisabledXML: will return an XML string version of the Rule's disabled status (defaults to yes)
    '''
    def genRuleDisabledXML(self):
        if self.disable:
            return "<disabled>" + self.disable + "</disabled>"
        else:
            return "<disabled>yes</disabled>"
    
    '''
    genRuleGroupsXML: will return an XML string version of the Rule's groups (if any exist)
    '''
    def genRuleGroupsXML(self):
        if self.group:
            retStr = "<profile-setting><group>"
            for attr in self.group:
                retStr = retStr + "<member>" + attr + "</member>"
            retStr = retStr + "</group></profile-setting>"
            return retStr
        else:
            return ""
    
    '''
    genRuleHipProfilesXML: will return an XML string version of the Rule's hip-profiles (if any exist)
    '''
    def genRuleHipProfilesXML(self):
        if self.hipProf:
            retStr = "<hip-profiles>"
            for attr in self.hipProf:
                retStr = retStr + "<member>" + attr + "</member>"
            retStr = retStr + "</hip-profiles>"
            return retStr
        else:
            return ""
    
    '''
    genRuleLogStartXML: will return an XML string version of the Rule's log start status (defaults to no)
    '''
    def genRuleLogStartXML(self):
        if self.logStart:
            return "<log-start>" + self.logStart + "</log-start>"
        else:
            return "<log-start>no</log-start>"
    
    '''
    genRuleLogEndXML: will return an XML string version of the Rule's log end status (defaults to no)
    '''
    def genRuleLogEndXML(self):
        if self.logEnd:
            return "<log-end>" + self.logEnd + "</log-end>"
        else:
            return "<log-end>no</log-end>"
    
    '''
    genRuleDescriptionXML: will return an XML string version of the Rule's description (if it exists)
    '''
    def genRuleDescriptionXML(self):
        if self.desc:
            return "<description>" + self.desc + "</description>"
        else:
            return ""
    
    
    ### Get Methods ###
    '''
    getRuleName: will return the Rule's name
    '''  
    def getRuleName(self):
        return self.name
    
    '''
    getRuleFromMembers: will return a list of the Rule's from members
    ''' 
    def getRuleFromMembers(self):
        return self.memFrom
    
    '''
    getRuleToMembers: will return a list of the Rule's to members
    ''' 
    def getRuleToMembers(self):
        return self.memTo
    
    '''
    getRuleSource: will return a list of the Rule's sources
    ''' 
    def getRuleSource(self):
        return self.src
    
    '''
    getRuleDestination: will return a list of the Rule's destinations
    ''' 
    def getRuleDestination(self):
        return self.dst
    
    '''
    getRuleService: will return a list of the Rule's services
    ''' 
    def getRuleService(self):
        return self.srv
    
    '''
    getRuleApplication: will return a list of the Rule's applications
    ''' 
    def getRuleApplication(self):
        return self.app
    
    '''
    getRuleAction: will return the Rule's action
    ''' 
    def getRuleAction(self):
        return self.act
    
    '''
    getRuleSourceUser: will return a list of the Rule's source users
    ''' 
    def getRuleSourceUser(self):
        return self.srcUsr
    
    '''
    getRuleDisableServerResponse: will return the Rule's disable server response status 
    ''' 
    def getRuleDisableServerResponse(self):
        return self.disRsp
    
    '''
    getRuleNegateSource: will return the Rule's negate source status 
    ''' 
    def getRuleNegateSource(self):
        return self.negSrc
    
    '''
    getRuleNegateDestination: will return the Rule's negate destination status 
    ''' 
    def getRuleNegateDestination(self):
        return self.negDst
    
    '''
    getRuleDisabled: will return the Rule's disabled status 
    ''' 
    def getRuleDisabled(self):
        return self.disable
    
    '''
    getRuleGroups: will return a list of the Rule's groups
    ''' 
    def getRuleGroups(self):
        return self.group
    
    '''
    getRuleHipProfiles: will return a list of the Rule's hip-profiles
    ''' 
    def getRuleHipProfiles(self):
        return self.hipProf
    
    '''
    getRuleLogStart: will return the Rule's log start status 
    ''' 
    def getRuleLogStart(self):
        return self.logStart
    
    '''
    getRuleLogEnd: will return the Rule's log end status 
    ''' 
    def getRuleLogEnd(self):
        return self.logEnd
    
    '''
    getRuleDescription: will return the Rule's description 
    ''' 
    def getRuleDescription(self):
        return self.desc
    
    
    
    ### Set Methods ###
    '''
    setRuleName: will set the Rule's name
    
        setRuleName args:
            name => name of the Rule (string)
    ''' 
    def setRuleName(self, name):
        if type(name) is not str:
            raise TypeError("Type must be a string")
        self.name = name
    
    '''
    setRuleFromMembers: will set the Rule's from members
    
        setRuleFromMembers args:
            memFrom => from members of the rule (list of strings => zones)
    ''' 
    def setRuleFromMembers(self, memFrom):
        if type(memFrom) is not list:
            raise TypeError("Type must be a list")
        self.memFrom = memFrom
    
    '''
    setRuleToMembers: will set the Rule's to members
    
        setRuleToMembers args:
            memTo => to members of the rule (list of strings => zones)
    ''' 
    def setRuleToMembers(self, memTo):
        if type(memTo) is not list:
            raise TypeError("Type must be a list")
        self.memTo = memTo
    
    '''
    setRuleSource: will set the Rule's sources
    
        setRuleSource args:
            src => sources of the rule (list of strings)
    ''' 
    def setRuleSource(self, src):
        if type(src) is not list:
            raise TypeError("Type must be a list")
        self.src = src
    
    '''
    setRuleDestination: will set the Rule's destinations
    
        setRuleDestination args:
            dst => destinations of the rule (list of strings)
    ''' 
    def setRuleDestination(self, dst):
        if type(dst) is not list:
            raise TypeError("Type must be a list")
        self.dst = dst
    
    '''
    setRuleService: will set the Rule's services
    
        setRuleService args:
            srrv => services of the rule (list of strings)
    ''' 
    def setRuleService(self, srv):
        if type(srv) is not list:
            raise TypeError("Type must be a list")
        self.srv = srv
    
    '''
    setRuleApplication: will set the Rule's applications
    
        setRuleApplications args:
            app => applications of the rule (list of strings)
    ''' 
    def setRuleApplication(self, app):
        if type(app) is not list:
            raise TypeError("Type must be a list")
        self.app = app
    
    '''
    setRuleAction: will set the Rule's action
    
        setRuleSource args:
            act => action of the rule (string => 'allow' or 'deny')
    ''' 
    def setRuleAction(self, act):
        if type(act) is not str:
            raise TypeError("Type must be a string")
        if act != "allow" and act != "deny":
            raise ValueError("Value must be 'allow' or 'deny'")
        self.act = act
    
    '''
    setRuleSourceUser: will set the Rule's source users
    
        setRuleSourceUser args:
            srcUsr => source users of the rule (list of strings)
    ''' 
    def setRuleSourceUser(self, srcUsr):
        if type(srcUsr) is not list:
            raise TypeError("Type must be a list")
        self.srcUsr = srcUsr
    
    '''
    setRuleDisableServerResponse: will set the Rule's disable server response status
    
        setRuleDisableServerResponse args:
            disRsp => disable server response of the rule (string => 'yes' or 'no')
    ''' 
    def setRuleDisableServerResponse(self, disRsp):
        if type(disRsp) is not str:
            raise TypeError("Type must be a string")
        if disRsp != "yes" and disRsp != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        self.disRsp = disRsp
    
    '''
    setRuleNegateSource: will set the Rule's negate source status
    
        setRuleNegateSource args:
            negSrc => negate sources of the rule (string => 'yes' or 'no')
    ''' 
    def setRuleNegateSource(self, negSrc):
        if type(negSrc) is not str:
            raise TypeError("Type must be a string")
        if negSrc != "yes" and negSrc != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        self.negSrc = negSrc
    
    '''
    setRuleNegateDestination: will set the Rule's negate destination status
    
        setRuleNegateDestination args:
            negDst => negate destinations of the rule (string => 'yes' or 'no')
    ''' 
    def setRuleNegateDestination(self, negDst):
        if type(negDst) is not str:
            raise TypeError("Type must be a string")
        if negDst != "yes" and negDst != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        self.negDst = negDst
    
    '''
    setRuleDisabled: will set the Rule's disabled status
    
        setRuleDisabled args:
            disable => disable the rule (string => 'yes' or 'no')
    '''
    def setRuleDisabled(self, disable):
        if type(disable) is not str:
            raise TypeError("Type must be a string")
        if disable != "yes" and disable != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        self.disable = disable
    
    '''
    setRuleGroups: will set the Rule's groups
    
        setRuleGroups args:
            group => groups of the rule (list of strings)
    ''' 
    def setRuleGroups(self, group):
        if type(group) is not list:
            raise TypeError("Type must be a list")
        self.group = group
    
    '''
    setRuleHipProfiles: will set the Rule's hip-profiles (list of strings)
    
        setRuleHipProfiles args:
            hipProf => hip-profiles of the rule (list of strings)
    ''' 
    def setRuleHipProfiles(self, hipProf):
        if type(hipProf) is not list:
            raise TypeError("Type must be a list")
        self.hipProf = hipProf
    
    '''
    setRuleLogStart: will set the Rule's log start status
    
        setRulelogStart args:
            logStart => start the log of the rule (string => 'yes' or 'no')
    '''
    def setRuleLogStart(self, logStart):
        if type(logStart) is not str:
            raise TypeError("Type must be a string")
        if logStart != "yes" and logStart != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        self.logStart = logStart
    
    '''
    setRuleLogEnd: will set the Rule's log end status
    
        setRulelogEnd args:
            logEnd => end the log of the rule (string => 'yes' or 'no')
    '''
    def setRuleLogEnd(self, logEnd):
        if type(logEnd) is not str:
            raise TypeError("Type must be a string")
        if logEnd != "yes" and logEnd != "no":
            raise ValueError("Value must be a 'yes' or a 'no'")
        self.logEnd = logEnd
    
    '''
    setRuleDescription: will set the Rule's description
    
        setRuleDescription args:
            desc => description of the rule (string)
    '''
    def setRuleDescription(self, desc):
        if type(desc) is not str:
            raise TypeError("Type must be a string")
        self.desc = desc