import flet_core as ft
import pytest
from flet_core.protocol import Command


def test_instance_no_attrs_set():
    r = ft.Text()
    assert isinstance(r, ft.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=['text'],
            attrs={},
            commands=[],
        )
    ], 'Test failed'


def test_text_align_enum():
    r = ft.Text()
    assert r.text_align == ft.TextAlign.LEFT
    assert r._get_attr('textAlign') is None

    r = ft.Text(text_align=ft.TextAlign.RIGHT)
    assert isinstance(r.text_align, ft.TextAlign)
    assert isinstance(r._get_attr('textAlign'), str)
    assert r.text_align == ft.TextAlign.RIGHT
    assert r._get_attr('textAlign') == 'right'

    r = ft.Text(text_align='center')
    assert isinstance(r.text_align, ft.TextAlign)
    assert isinstance(r._get_attr('textAlign'), str)
    assert r.text_align == ft.TextAlign.CENTER
    assert r._get_attr('textAlign') == 'center'


def test_text_style_enum():
    r = ft.Text()
    assert r.style is None
    assert r._get_attr('style') is None

    r = ft.Text(style=ft.TextThemeStyle.DISPLAY_LARGE)
    assert isinstance(r.style, ft.TextThemeStyle)
    assert r.style == ft.TextThemeStyle.DISPLAY_LARGE
    assert r._get_attr('style') == 'displayLarge'

    r = ft.Text(style='bodyMedium')
    assert isinstance(r.style, str)
    assert r._get_attr('style') == 'bodyMedium'


def test_text_overflow_enum():
    r = ft.Text()
    assert r.overflow == ft.TextOverflow.FADE
    assert r._get_attr('overflow') is None

    r = ft.Text(overflow=ft.TextOverflow.ELLIPSIS)
    assert isinstance(r.overflow, ft.TextOverflow)
    assert isinstance(r._get_attr('overflow'), str)
    assert r.overflow == ft.TextOverflow.ELLIPSIS
    assert r._get_attr('overflow') == ft.TextOverflow.ELLIPSIS.value
    assert r._get_attr('overflow') == 'ellipsis'

    r = ft.Text(overflow='visible')
    assert isinstance(r.overflow, ft.TextOverflow)
    assert isinstance(r._get_attr('overflow'), str)
    assert r.overflow == ft.TextOverflow.VISIBLE
    assert r._get_attr('overflow') == ft.TextOverflow.VISIBLE.value
    assert r._get_attr('overflow') == 'visible'


def test_weight_enum():
    r = ft.Text()
    assert r.weight == ft.FontWeight.NORMAL
    assert r._get_attr('weight') is None

    r = ft.Text(weight=ft.FontWeight.BOLD)
    assert isinstance(r.weight, ft.FontWeight)
    assert isinstance(r._get_attr('weight'), str)
    assert r.weight == ft.FontWeight.BOLD
    assert r._get_attr('weight') == 'bold'

    r = ft.Text(weight='w100')
    assert isinstance(r.weight, ft.FontWeight)
    assert isinstance(r._get_attr('weight'), str)
    assert r.weight == ft.FontWeight.W_100
    assert r._get_attr('weight') == 'w100'
