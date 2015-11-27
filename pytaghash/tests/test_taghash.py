import pytaghash.taghash

from .fixtures.tags import *
from .fixtures import abc_drum


class TestTagHash:
    @classmethod
    def setup_class(self):
        # patch bs4.Tag
        pytaghash.taghash.patch()

    def test_hash(self):
        hash = complex1.hash(depth=1)
        assert hash == {
            'li.00': [
                {'div.00': []},
                {'p.00': []},
                {'dl.00': []},
                {'p.00': []}
            ]
        }

        hash = complex1.hash(depth=2)
        assert hash == {
            'li.00': [
                {'div.00': []},
                {'p.00': []},
                {'dl.00': [
                    {'dd.00': []},
                    {'dt.00': []},
                ]},
                {'p.00': [
                    {'br.00': []}
                ]}
            ]
        }

        hash = complex3.hash(depth=3)
        assert hash == {
            'li.00': [
                {'div.01': [
                    {'p.00': [
                        {'br.00': []},
                        {'br.00': []}
                    ]}
                ]},
                {'div.00': []},
                {'p.00': []},
                {'a.00': [
                    {'img.00': []},
                    {'p.00': []}
                ]},
                {'div.00': []},
                {'a.00': []}
            ]
        }

    def test_compare_hash(self):
        # simple
        assert complex1.hash_compare(complex2, depth=1)
        # assert not complex1.hash_compare(complex4, depth=2)
        assert not complex1.hash_compare(complex3, depth=1)

        # compare with attributes
        # not much difference
        assert complex1.hash_compare(complex1_attrib, depth=1)

        # lots of difference
        assert not complex1.hash_compare(complex1_attrib_diff, depth=2)

        # deeper
        assert complex1.hash_compare(complex2, depth=2)
        assert not complex1.hash_compare(complex3, depth=2)

    def test_compare_hash_abc(self):
        ts1 = bs4.BeautifulSoup(abc_drum.short_comment_list, 'lxml').ul.li
        ts2 = bs4.BeautifulSoup(abc_drum.short_comment_list, 'lxml').ul.li.ul.li.ul.li

        assert not ts1.hash_compare(ts2, depth=2)

    def test_is_list(self):
        tag = nested_comments_abc
        assert not tag.li.is_list()
        assert tag.ul.li.ul.is_list()

    def test_is_list_kotaku(self):
        count = 0
        for tag in nested_comments_kotaku.div.find_all(True):
            if tag.is_list(depth=2, minimum_tags=3):
                count += 1
        assert count == 7

    def test_is_list_disqus(self):
        count = 0
        for tag in nested_comments_disqus.div.find_all(True):
            if tag.is_list(depth=2, minimum_tags=3):
                count += 1
        assert count == 60

    def test_structure_xpath(self):
        xpath = complex1.structure_xpath(depth=1)
        assert xpath == '// li [ count(div)=1 and count(dl)=1 and count(p)=2 ]'
        assert len(complex1.lxml.xpath(xpath)) == 1

        xpath = complex1.structure_xpath(depth=2)
        assert xpath == '// li [ count(div)=1 and count(dl)=1 and count(p)=2 and dl [ count(dd)=1 and count(dt)=1 ] and p [ count(br)=1 ] ]'
        assert len(complex1.lxml.xpath(xpath)) == 1

        tag = bs4.BeautifulSoup(abc_drum.short_comment_list, 'lxml').ul
        xpath = tag.structure_xpath(depth=1)
        assert xpath == '// ul [ count(li)=2 ]'
        assert len(tag.lxml.xpath(xpath)) == 2

        xpath = tag.structure_xpath(depth=2)
        assert xpath == '// ul [ count(li)=2 and li [ count(a)=1 and count(h3)=1 and count(p)=3 ] ]'
        assert len(tag.lxml.xpath(xpath)) == 2

        xpath = tag.structure_xpath(depth=3)
        assert xpath == '// ul [ count(li)=2 and li [ count(a)=1 and count(h3)=1 and count(p)=3 and p [ count(span)=2 ] ] ]'
        assert len(tag.lxml.xpath(xpath)) == 2

        xpath = '// li [ count(a)=1 and count(h3)=1 and count(p)=3 ]'
        assert len(tag.lxml.xpath(xpath)) == 4

    def test_identifying_xpath(self):
        ts = bs4.BeautifulSoup('''
        <html>
        <head>
        </head>
        <body>
            <ul class='comments-paginate page'>
                <li>1</li>
                <li>2</li>
                <li>3</li>
                <li>4</li>
            </ul>
            <ul id='comments'>
                <li>some shit</li>
                <li>
                    <ul>
                        <li> some more shit</li>
                    </ul>
                </li>
                <li>butts</li>
            </ul>
        </body>
        </html>
        ''', 'lxml')

        xpath = ts.find_all('ul')[1].find_all('li')[3].identifying_xpath()
        assert xpath == '//ul[@id="comments"]/li[3]'
        assert len(ts.lxml.xpath(xpath)) == 1
        xpath = ts.find_all('ul')[0].find_all('li')[1].identifying_xpath()
        assert xpath == '//ul[contains(@class, "comments-paginate") and contains(@class, "page")]/li[2]'
        assert len(ts.lxml.xpath(xpath)) == 1

    def test_count(self):
        assert complex1.count(depth=1) == 4
        assert complex1.count(depth=2) == 7

    def test_relative_xpath(self):
        tag = complex1.find('dt')
        xpath = tag.relative_xpath(complex1)

        assert xpath == 'dl[1]/dt[1]'
        assert len(complex1.lxml.xpath(xpath)) == 1

    def test_level(self):
        tag = bs4.BeautifulSoup('''
        <html>
            <body>
                <table>
                    <tr>
                        <td>
                            <p></p>
                        </td>
                    </tr>
                </table>
            </body>
        </html>
        ''', 'lxml')

        assert tag.p.level == 6