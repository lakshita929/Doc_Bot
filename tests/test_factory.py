from functools import wraps

from .test_suite import TEST_SUITE


class TEST_BUNDLE:
    def __init__(self, bundle_name=''):
        self.bundle_name = bundle_name
        TEST_SUITE.test_bundles.append(self)
        self.subtests = []
    
    def add_test(self, test_name='', default_params={}, multi=False):
        def decorator(test_func):
            default_params['multi'] = multi
            test_obj = TEST(test_name, test_func, default_params)
            self.subtests.append(test_obj)
            return test_obj

        return decorator
        
    def __repr__(self):
        print(f'Test Bundle : {self.bundle_name}')
        print(f'Number of tests in this bundle: {len(self.subtests)}')
        print(f'Tests in this bundle: ')
        for i in range(len(self.subtests)):
            print(self.subtests[i])


class TEST:
    def __init__(self, test_name='', test_function=None, default_params={}):
        self.test_name = test_name
        self.test_function = test_function
        self.default_params = default_params
        
        
    def __call__(self):
        if (self.default_params['multi']):
            del(self.default_params['multi'])
            test_keys = [k for k in self.default_params.keys() if k!= 'multi']
            for i in range(len(self.default_params[test_keys[0]])):
                temp_params = {}
                for key in self.default_params.keys():
                    temp_params[key] = self.default_params[key][i]
                self.test_function(temp_params)
        else:
            del(self.default_params['multi'])
            self.test_function(**self.default_params)
        
    def __repr__(self):
        out_str = f'Test Name: {self.test_name}, '
        out_str += f'Test Function: {self.test_function.__name__}'
        out_str += f', Default Params: {self.default_params}'
        return out_str
        
        
def test(test_name='', default_params={}, multi=False):
    def decorator(test_func):
        default_params['multi'] = multi
        test_obj = TEST(test_name, test_func, default_params)
        TEST_SUITE.add_test(test_obj)
        return test_obj

    return decorator