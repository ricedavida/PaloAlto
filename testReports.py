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
    pa = PaAPI (apiKeyFile)
    paDyn = PaAPI (apiKeyFile)
    #report = pa.getReport("botnet")
    reportDyn = paDyn.getDynamicReport("top-app-summary", "", "1")    
    
    '''
    def test_getReportName(self):
        self.assertEqual(self.report[0].getReportName(), "top-app-summary")
    
    def testc_getApp(self):
        self.assertTrue(isinstance(self.report[0].getApp(), str))
        
    def test_getRiskLevel(self):
        self.assertTrue(self.report[0].getRiskLevel().isdigit())
        
    def test_getBytes(self):
        self.assertTrue(self.report[0].getBytes().isdigit())
        
    def test_getSessions(self):
        self.assertTrue(self.report[0].getSessions().isdigit())
    '''    
    
    '''
    def test_dynamic_getReportName(self):
        self.assertEqual(self.reportDyn[0].getReportName(), "top-app-summary")
    
    def test_dynamic_getApp(self):
        self.assertTrue(isinstance(self.reportDyn[0].getApp(), str))
        
    def test_dynamic_getRiskLevel(self):
        self.assertTrue(self.reportDyn[0].getRiskLevel().isdigit())
        
    def test_dynamic_getBytes(self):
        self.assertTrue(self.reportDyn[0].getBytes().isdigit())
        
    def test_dynamic_getSessions(self):
        self.assertTrue(self.reportDyn[0].getSessions().isdigit())
    '''   
    
    def test_test(self):
        reports = [
                   #"custom-dynamic-report",
                   "acc-summary", "top-app-summary", "top-application-categories-summary", "top-application-risk-summary", 
                   "top-application-subcategories-summary", "top-application-tech-summary", "top-applications-summary", "top-applications-trsum", 
                   "top-attacker-countries-summary", "top-attackers-summary", "top-attacks-acc", "top-blocked-url-categories-summary", "top-blocked-url-summary", 
                   "top-blocked-url-user-behavior-summary", "top-data-dst-countries-summary", "top-data-dst-summary", "top-data-egress-zones-summary", 
                   "top-data-filename-summary", "top-data-filetype-summary", "top-data-ingress-zones-summary", "top-data-src-countries-summary", 
                   "top-data-src-summary", "top-data-type-summary", "top-dst-countries-summary", "top-dst-summary", "top-egress-zones-summary", 
                   "top-hip-objects-details", "top-hip-objects-summary", "top-hip-profiles-details", "top-hip-profiles-summary", "top-hip-report-links", 
                   "top-hr-applications-summary", "top-ingress-zones-summary", "top-rule-summary", "top-spyware-download-summary", "top-spyware-phonehome-summary", 
                   "top-spyware-threats-summary", "top-src-countries-summary", "top-src-summary", "top-threat-egress-zones-summary", "top-threat-ingress-zones-summary", 
                   "top-threats-type-summary", "top-url-categories-summary", "top-url-summary", "top-url-user-behavior-summary", "top-victim-countries-summary", 
                   "top-victims-summary", "top-viruses-summary", "top-vulnerabilities-summary"
                   ]
        
        for report in reports:
            #print (report + " - " + self.paDyn.getDynamicReport(report, "","1")[0].getApp())
            print ('Report: ' + report)
            self.paDyn.getDynamicReport(report, "", "")
            
            
    
    '''    
    def test_test2(self):
        reports = [
                   "bandwidth-trend", "botnet", "hruser-top-applications", "hruser-top-threats", "hruser-top-url-categories", 
                   "risk-trend", "risky-users", "spyware-infected-hosts", "threat-trend", "top-application-categories", 
                   "top-applications", "top-attackers", "top-attackers-by-countries", "top-attacks", "top-blocked-url-categories", 
                   "top-blocked-url-user-behavior", "top-blocked-url-users", "top-blocked-websites", "top-connections", 
                   "top-denied-applications", "top-denied-destinations", "top-denied-sources", "top-destination-countries", 
                   "top-destinations", "top-egress-interfaces", "top-egress-zones", "top-http-applications", "top-ingress-interfaces", 
                   "top-ingress-zones", "top-rules", "top-source-countries", "top-sources", "top-spyware-threats", 
                   "top-technology-categories", "top-url-categories", "top-url-user-behavior", "top-url-users", "top-users", 
                   "top-victims", "top-victims-by-countries", "top-viruses", "top-vulnerabilities", "top-websites", 
                   "unknown-tcp-connections", "unknown-udp-connections", "wildfire-file-digests"
                ]
        
        for report in reports:
            #print (report + " - " + self.paDyn.getDynamicReport(report, "","1")[0].getApp())
            print ('Report: ' + report)
            self.paDyn.getReport(report)
    '''    
    '''
    def test_type_getReport_ValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.pa.getReport("blah")
    
    
    
    
    def test_type_getDynamicReport_ValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.pa.getDynamicReport("blah", "", "")
            
    def test_period_getDynamicReport_ValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.pa.getDynamicReport("acc-summary", "blah", "")        
    
    def test_topN_getDynamicReport_ValueErrorHandle(self):
        with self.assertRaises(ValueError):
            self.pa.getDynamicReport("acc-summary", "", "blah")
    '''
if __name__ == '__main__':
    unittest.main()