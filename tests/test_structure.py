import sys

from rattle import Template

from tests.utils import TemplateTestCase


PY3 = sys.version_info[0] == 3


class CommentTest(TemplateTestCase):

    def test_inline_comment(self):
        TESTS = (
            ('{# abc #}', ''),
            ('abc{# def #}', 'abc'),
            ('abc {# def #}', 'abc '),
            ('{# abc #}def', 'def'),
            ('{# abc #} def', ' def'),
            ('abc{# def #}ghi', 'abcghi'),
            ('abc {# def #} ghi', 'abc  ghi'),
        )
        for src, expect in TESTS:
            tmpl = Template(src)
            output = tmpl.render()
            self.assertRendered(output, expect, src)

    def test_multiple_inline_comment(self):
        TESTS = (
            ('{# abc #}{# ABC #}', ''),
            ('abc{# def #}ABC{# DEF #}', 'abcABC'),
            ('abc {# def #}ABC {# DEF #}', 'abc ABC '),
            ('{# abc #}def{# ABC #}DEF', 'defDEF'),
            ('{# abc #} def{# ABC #} DEF', ' def DEF'),
            ('abc{# def #}ghiABC{# DEF #}GHI', 'abcghiABCGHI'),
            ('abc {# def #} ghiABC {# DEF #} GHI', 'abc  ghiABC  GHI'),
        )
        for src, expect in TESTS:
            tmpl = Template(src)
            output = tmpl.render()
            self.assertRendered(output, expect, src)


class IfTest(TemplateTestCase):

    def test_if_true(self):
        TESTS = (
            ('{% if True %}Hello{% endif %}', 'Hello'),
            ('{% if True %}Hello{% endif %} world', 'Hello world'),
            ('{% if True %}Hello {% endif %}world', 'Hello world'),
            ('Hello {% if True %}world{% endif %}', 'Hello world'),
            ('Hello{% if True %} world{% endif %}', 'Hello world'),
            ('Hello {% if True %}world{% endif %} !', 'Hello world !'),
        )
        for src, expect in TESTS:
            tmpl = Template(src)
            output = tmpl.render()
            self.assertRendered(output, expect, src)

    def test_if_false(self):
        TESTS = (
            ('{% if False %}Hello{% endif %}', ''),
            ('{% if False %}Hello{% endif %} world', ' world'),
            ('{% if False %}Hello {% endif %}world', 'world'),
            ('Hello {% if False %}world{% endif %}', 'Hello '),
            ('Hello{% if False %} world{% endif %}', 'Hello'),
            ('Hello {% if False %}world{% endif %} !', 'Hello  !'),
        )
        for src, expect in TESTS:
            tmpl = Template(src)
            output = tmpl.render()
            self.assertRendered(output, expect, src)

    def test_if_true_or_false(self):
        TESTS = (
            ('{% if True or False %}Hello{% endif %}', 'Hello'),
            ('{% if True or False %}Hello{% endif %} world', 'Hello world'),
            ('{% if True or False %}Hello {% endif %}world', 'Hello world'),
            ('Hello {% if True or False %}world{% endif %}', 'Hello world'),
            ('Hello{% if True or False %} world{% endif %}', 'Hello world'),
            ('Hello {% if True or False %}world{% endif %} !', 'Hello world !'),
        )
        for src, expect in TESTS:
            tmpl = Template(src)
            output = tmpl.render()
            self.assertRendered(output, expect, src)

    def test_if_true_and_false(self):
        TESTS = (
            ('{% if True and False %}Hello{% endif %}', ''),
            ('{% if True and False %}Hello{% endif %} world', ' world'),
            ('{% if True and False %}Hello {% endif %}world', 'world'),
            ('Hello {% if True and False %}world{% endif %}', 'Hello '),
            ('Hello{% if True and False %} world{% endif %}', 'Hello'),
            ('Hello {% if True and False %}world{% endif %} !', 'Hello  !'),
        )
        for src, expect in TESTS:
            tmpl = Template(src)
            output = tmpl.render()
            self.assertRendered(output, expect, src)

    def test_if_else_true(self):
        TESTS = (
            ('{% if True %}abc{% else %}def{% endif %}', 'abc'),
            ('{% if True %}abc{% else %}def{% endif %} ghi', 'abc ghi'),
            ('{% if True %}abc {% else %}def {% endif %}ghi', 'abc ghi'),
            ('abc {% if True %}def{% else %}ghi{% endif %}', 'abc def'),
            ('abc{% if True %} def{% else %} ghi{% endif %}', 'abc def'),
            ('abc {% if True %}def{% else %}ghi{% endif %} jkl', 'abc def jkl'),
        )
        for src, expect in TESTS:
            tmpl = Template(src)
            output = tmpl.render()
            self.assertRendered(output, expect, src)

    def test_if_else_false(self):
        TESTS = (
            ('{% if False %}abc{% else %}def{% endif %}', 'def'),
            ('{% if False %}abc{% else %}def{% endif %} ghi', 'def ghi'),
            ('{% if False %}abc {% else %}def {% endif %}ghi', 'def ghi'),
            ('abc {% if False %}def{% else %}ghi{% endif %}', 'abc ghi'),
            ('abc{% if False %} def{% else %} ghi{% endif %}', 'abc ghi'),
            ('abc {% if False %}def{% else %}ghi{% endif %} jkl', 'abc ghi jkl'),
        )
        for src, expect in TESTS:
            tmpl = Template(src)
            output = tmpl.render()
            self.assertRendered(output, expect, src)

    def test_if_else_true_or_false(self):
        TESTS = (
            ('{% if True or False %}abc{% else %}def{% endif %}', 'abc'),
            ('{% if True or False %}abc{% else %}def{% endif %} ghi', 'abc ghi'),
            ('{% if True or False %}abc {% else %}def {% endif %}ghi', 'abc ghi'),
            ('abc {% if True or False %}def{% else %}ghi{% endif %}', 'abc def'),
            ('abc{% if True or False %} def{% else %} ghi{% endif %}', 'abc def'),
            ('abc {% if True or False %}def{% else %}ghi{% endif %} jkl', 'abc def jkl'),
        )
        for src, expect in TESTS:
            tmpl = Template(src)
            output = tmpl.render()
            self.assertRendered(output, expect, src)

    def test_if_else_true_and_false(self):
        TESTS = (
            ('{% if True and False %}abc{% else %}def{% endif %}', 'def'),
            ('{% if True and False %}abc{% else %}def{% endif %} ghi', 'def ghi'),
            ('{% if True and False %}abc {% else %}def {% endif %}ghi', 'def ghi'),
            ('abc {% if True and False %}def{% else %}ghi{% endif %}', 'abc ghi'),
            ('abc{% if True and False %} def{% else %} ghi{% endif %}', 'abc ghi'),
            ('abc {% if True and False %}def{% else %}ghi{% endif %} jkl', 'abc ghi jkl'),
        )
        for src, expect in TESTS:
            tmpl = Template(src)
            output = tmpl.render()
            self.assertRendered(output, expect, src)
