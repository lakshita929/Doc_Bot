from time import time


class TEST_SUITE(object):
    test_list = []
    test_bundles = []
    
    @staticmethod
    def add_test(test):
        TEST_SUITE.test_list.append(test)
        
    @staticmethod
    def add_test_bundle(test_bundle):
        TEST_SUITE.test_bundles.append(test_bundle)
        
    @staticmethod
    def run():
        print('Running All Individual Tests and Test Bundles....')
        successful_tests = 0
        failed_tests = []
        failed_bundles = []
        
        for bundle in TEST_SUITE.test_bundles:
            successful_bundle_tests = 0
            failed_bundle_tests = []
            print('---------------------------------------------')
            print(f'--### Running Test Bundle : {bundle.bundle_name} ###--')
            start_time = time()
            for test in bundle.subtests:
                result = TEST_SUITE.run_test(test)
                if result == 1:
                    successful_bundle_tests += 1
                else:
                    failed_bundle_tests.append(test.test_name)
                    failed_bundles.append({bundle.bundle_name : test.test_name})
            end_time = time()
            print(f'Finished Running Test Bundle. Took {end_time - start_time} seconds to run.')
            print(f'Number Of Tests Ran in this bundle : {len(bundle.subtests)}')
            print(f'{successful_bundle_tests} out of {len(bundle.subtests)} tests passed successfully.')
            print(f'Failed Tests : {", ".join(failed_bundle_tests)}')
            print('---------------------------------------------')
        
        print('-------------------------------------------')
        print('Finished Running Bundles, Running Individual Tests....') 
        for test in TEST_SUITE.test_list:
            print(f'--## Running Test : {test.test_name} #--')        
            result = TEST_SUITE.run_test(test)
            if result == 1:
                successful_tests += 1
            else:
                failed_tests.append(test.test_name)
        print('--------------------------------------------')
        
        print('-- Finished Running Individual Tests --')
        print(f'{successful_tests} out of {len(TEST_SUITE.test_list)} tests passed successfully.')
        print(f'Failed Tests : {", ".join(failed_tests)}')
        print(f'Failed Bundles : {", ".join([f"{list(i.keys())[0]}:{list(i.values())[0]}" for i in failed_bundles])}')
            
        
    @staticmethod
    def run_test(test):
        start_time = time()
        print(f'############################ Test Run : {test.test_name} ############################')
        try:
            test()
            return 1
        except Exception as e:
            print(f'!!!!!!!!!!!!!!!!! Test Failed : Exception Occured : {e} !!!!!!!!!!!!!!!!!')
            return 0
        end_time = time()
        print(f'------Finished Running Test : {test.test_name}, Took : {end_time - start_time} seconds to run.-------')
        
            
    @staticmethod
    def list_tests():
        i = 0
        for test in TEST_SUITE.test_list:
            print(f'{i}. {test}')
            print(test)
            print('---------------------------------------------')