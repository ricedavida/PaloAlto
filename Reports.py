class Reports:
    '''
    This class will be used in the creation of Reports, it is a single element of the report
    
        Authors:
            David Rice riceda@potsdam.edu
        Last Updated:
            02/03/2015
    '''
    
    reportName = ""
    reportAttrs = []

    '''
    Constructor: 
    
        Constructor args: 
            name => name of the rule (string)
    '''
    def __init__(self, reportName, reportAttrs):
        self.reportName = reportName
        self.reportAttrs = reportAttrs
        
        print (reportAttrs)
        
    
    def getReportName(self):
        return self.reportName
    
    def getFields(self):
        return self.reportAttrs