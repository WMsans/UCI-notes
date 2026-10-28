import re


class Locator:
    _KIND = re.compile(r'[a-z]+')
    _PART = re.compile(r'[A-Za-z0-9]+')

    def __init__(self, srl: str) -> None:
        pieces = srl.split('://')
        if len(pieces) != 2:
            raise ValueError(f'{srl!r} is not a valid SRL')
        kind, rest = pieces
        if Locator._KIND.fullmatch(kind) is None:
            raise ValueError(f'{srl!r} is not a valid SRL')
        if '/' not in rest:
            raise ValueError(f'{srl!r} is not a valid SRL')
        location, resource = rest.split('/', 1)
        self._location_parts = location.split('.')
        for part in self._location_parts:
            if Locator._PART.fullmatch(part) is None:
                raise ValueError(f'{srl!r} is not a valid SRL')
        self._resource_parts = resource.split('/')
        for part in self._resource_parts:
            if Locator._PART.fullmatch(part) is None:
                raise ValueError(f'{srl!r} is not a valid SRL')
        self._kind = kind

    def srl(self) -> str:
        location = '.'.join(self._location_parts)
        resource = ''.join('/' + part for part in self._resource_parts)
        return f'{self._kind}://{location}{resource}'

    def kind(self) -> str:
        return self._kind

    def location(self) -> str:
        return '.'.join(self._location_parts)

    def location_parts(self) -> list[str]:
        return list(self._location_parts)

    def resource(self) -> str:
        return ''.join('/' + part for part in self._resource_parts)

    def resource_parts(self) -> list[str]:
        return list(self._resource_parts)

    def parent(self) -> 'Locator':
        if len(self._resource_parts) == 1:
            return self
        shorter = self.srl()[: -len(self._resource_parts[-1]) - 1]
        return Locator(shorter)

    def within(self, resource_part: str) -> 'Locator':
        return Locator(self.srl() + '/' + resource_part)


def _expect_value_error(srl: str) -> None:
    try:
        Locator(srl)
    except ValueError:
        return
    raise AssertionError(f'{srl!r} should have raised ValueError')


def _test_parts_of_a_valid_locator() -> None:
    loc = Locator('w://x.y.z/a/b/c')
    assert loc.srl() == 'w://x.y.z/a/b/c'
    assert loc.kind() == 'w'
    assert loc.location() == 'x.y.z'
    assert loc.location_parts() == ['x', 'y', 'z']
    assert loc.resource() == '/a/b/c'
    assert loc.resource_parts() == ['a', 'b', 'c']


def _test_single_part_location_and_resource() -> None:
    loc = Locator('ftp://host0/file')
    assert loc.location() == 'host0'
    assert loc.location_parts() == ['host0']
    assert loc.resource() == '/file'
    assert loc.resource_parts() == ['file']


def _test_parent_removes_last_resource_part() -> None:
    loc = Locator('w://x.y.z/a/b/c')
    assert loc.parent().srl() == 'w://x.y.z/a/b'
    assert loc.parent().parent().srl() == 'w://x.y.z/a'


def _test_parent_of_single_part_resource_is_itself() -> None:
    loc = Locator('w://x.y.z/a')
    assert loc.parent() is loc


def _test_within_appends_resource_part() -> None:
    loc = Locator('w://x.y.z/a/b/c')
    assert loc.within('d').srl() == 'w://x.y.z/a/b/c/d'
    assert loc.within('d').resource_parts() == ['a', 'b', 'c', 'd']
    assert loc.srl() == 'w://x.y.z/a/b/c'


def _test_parts_lists_are_copies() -> None:
    loc = Locator('w://x.y/z')
    parts = loc.location_parts()
    parts.append('hacked')
    assert loc.location() == 'x.y'
    parts = loc.resource_parts()
    parts.clear()
    assert loc.resource() == '/z'


def _test_invalid_srls_raise() -> None:
    _expect_value_error('')
    _expect_value_error('w')
    _expect_value_error('w://')
    _expect_value_error('w:/x.y/a')
    _expect_value_error('w:x.y/a')
    _expect_value_error('w://x.y://a')
    _expect_value_error('W://x.y/a')
    _expect_value_error('w1://x.y/a')
    _expect_value_error('w://x.y')
    _expect_value_error('w:///a')
    _expect_value_error('w://.x.y/a')
    _expect_value_error('w://x.y./a')
    _expect_value_error('w://x..y/a')
    _expect_value_error('w://x._y/a')
    _expect_value_error('w://x.y/')
    _expect_value_error('w://x.y//a')
    _expect_value_error('w://x.y/a//b')
    _expect_value_error('w://x.y/a.b/c')


_test_parts_of_a_valid_locator()
_test_single_part_location_and_resource()
_test_parent_removes_last_resource_part()
_test_parent_of_single_part_resource_is_itself()
_test_within_appends_resource_part()
_test_parts_lists_are_copies()
_test_invalid_srls_raise()
