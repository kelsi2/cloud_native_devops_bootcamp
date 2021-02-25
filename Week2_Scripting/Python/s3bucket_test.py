import unittest


class TestS3(unittest.TestCase):
    def test_bucket_name_value(self):
        bucket = 'cloudskillstutorial'

        self.assertEqual(bucket, 'cloudskillstutorial')

    def test_region_value(self):
        region = 'us-west-2'

        self.assertEqual(region, 'us-west-2')

    def test_bucket_name_is_string(self):
        bucket = 'cloudskillstutorial'

        self.assertTrue(type(bucket), str)

    def test_region_is_string(self):
        region = 'us-west-2'

        self.assertTrue(type(region), str)


if __name__ == '__main__':
    unittest.main()
