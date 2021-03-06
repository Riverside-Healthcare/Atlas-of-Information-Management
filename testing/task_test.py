"""
  Atlas of Information Management business intelligence library and documentation database.
  Copyright (C) 2020  Riverside Healthcare, Kankakee, IL

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

"""
    test case for /tasks urls
"""

import time
import unittest
import warnings

import urllib3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Tasks(unittest.TestCase):
    """
    test class from tasks

    setUp
    runText
        test for chrome
        test for ie
    cleanUp
    """

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

        self.my_site = "https://localhost:44380"

        # ie 11 cannot get browser output somehow, so change IE setting to alert w/ errors.
        # internet options > advanced > uncheck "disabled script debugging..." 2 boxes.
        # internet options > advanced > check "display a notification..."

        capabilities = DesiredCapabilities.INTERNETEXPLORER
        capabilities.update({"logLevel": "DEBUG"})
        capabilities["ignoreProtectedModeSettings"] = True
        self.explorer = webdriver.Ie(capabilities=capabilities)

        # chrome setup
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        self.chrome = webdriver.Chrome(options=options)

    def runTest(self):
        # pylint: disable=too-many-statements
        """
        test has inner function to run for both chrome and ie.
        """

        warnings.simplefilter("ignore", ResourceWarning)
        print("task")

        def test(driver, skip):
            report = self.my_site + "/tasks"
            driver.get(report)
            time.sleep(5)

            # open all tabs

            driver.find_elements_by_css_selector('a.tab-lnk[href="#recommendretire"]')[
                0
            ].click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")

            driver.find_elements_by_css_selector('a.tab-lnk[href="#dead"]')[0].click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")

            driver.find_elements_by_css_selector(
                'a.tab-lnk[href="#maintenancerequired"]'
            )[0].click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")

            driver.find_elements_by_css_selector('a.tab-lnk[href="#auditonly"]')[
                0
            ].click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")

            driver.find_elements_by_css_selector('a.tab-lnk[href="#missingschedule"]')[
                0
            ].click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")

            driver.find_elements_by_css_selector('a.tab-lnk[href="#notanalytics"]')[
                0
            ].click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")

            driver.find_elements_by_css_selector('a.tab-lnk[href="#topundocumented"]')[
                0
            ].click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")

            driver.find_elements_by_css_selector('a.tab-lnk[href="#newundocumented"]')[
                0
            ].click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")

            driver.find_elements_by_css_selector('a.tab-lnk[href="#canmakereports"]')[
                0
            ].click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")

            # for chrome
            if skip != 1:
                get_log(report, driver)

        def get_log(url, driver):
            logs = driver.get_log("browser")
            if len(logs) > 0:
                for log in logs:
                    if log["level"] == "SEVERE":
                        print(
                            url
                            + ","
                            + log["source"]
                            + ","
                            + log["level"]
                            + ","
                            + log["message"]
                        )

        test(self.chrome, 0)
        test(self.explorer, 1)

    def tearDown(self):
        self.chrome.close()
        self.explorer.close()


if __name__ == "__main__":
    unittest.main()
