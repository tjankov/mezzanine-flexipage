"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.utils import override_settings
from django.template import Template
from django.forms import ModelForm
from django.db import models
from flexipage.utils import get_flexi_template, get_flexi_template_location,\
    get_template_variables, get_flexi_tags, get_flexi_forms, get_settings_forms,\
    get_flexi_form_tags


class SimpleTest(TestCase):
    def test_templates_identified(self):
        pass
        
    def test_something(self):
        self.assertEqual(1,1)

class TestModel(models.Model):
    pass
    

class TestForm(ModelForm):
    class Meta:
        model = TestModel

class UtilsTest(TestCase):
    def test_get_template_variables(self):
        test_template = get_flexi_template('flexipage/tests/test.html')
        template_variables = get_template_variables(test_template)
        self.assertEqual(template_variables, ['first_variable', 'flexi_second_variable',
                                              'flexiform_third_variable','flexiform_TestForm'])

        
    def test_get_flexi_template(self):
        test_template = get_flexi_template('flexipage/tests/test.html')
        self.assertIsInstance(test_template, Template)

        
    def test_get_flexi_template_without_full_path(self):
        test_template = get_flexi_template('tests/test.html')
        self.assertIsInstance(test_template, Template)

        
    def test_get_flexi_template_location(self):
        test_template = get_flexi_template_location('flexipage/tests/test.html')
        self.assertEqual(test_template, 'flexipage/tests/test.html')

        
    def test_get_flexi_template_location_without_full_path(self):
        test_template = get_flexi_template_location('tests/test.html')
        self.assertEqual(test_template, 'flexipage/tests/test.html')

        
    def test_get_flexi_tags(self):
        template_variables = get_flexi_tags('flexipage/tests/test.html')
        self.assertEqual(template_variables, ['flexi_second_variable'])

        
    def test_get_flexi_form_tags(self):
        template_variables = get_flexi_form_tags('flexipage/tests/test.html')
        self.assertEqual(template_variables, ['flexiform_third_variable','flexiform_TestForm'])
        

    def test_get_settings_forms(self):
        with self.settings(FLEXI_FORMS=('IncorrectFormName',)):
            with self.assertRaises(ImportError):
                get_settings_forms()

        with self.settings(FLEXI_FORMS=('IncorrectModule.IncorrectFormName',)):
            with self.assertRaises(ImportError):
                get_settings_forms()
                

    def test_get_flexi_forms(self):
        with self.settings(FLEXI_FORMS=('flexipage.tests.TestForm',)):
            forms = get_flexi_forms('flexipage/tests/test.html')
            self.assertEqual(forms, {'flexiform_TestForm':TestForm})

            
class FlexiPageTest(TestCase):
    def test_templates_available(self):
        pass

class FormsTest(TestCase):
    def test_modelforms_render(self):
        pass

    def test_modelforms_save(self):
        pass
        
