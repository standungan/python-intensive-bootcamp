"""Menjalankan cuplikan kode sungguhan agar output di slide dijamin benar."""
import io, contextlib, builtins

def run(src, inputs=()):
    it = iter(inputs)
    buf = io.StringIO()
    real = builtins.input
    def fake(prompt=''):
        v = next(it); print(prompt + v); return v
    builtins.input = fake
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(src, '<slide>', 'exec'), {'__name__': '__main__'})
    finally:
        builtins.input = real
    return buf.getvalue().rstrip('\n').split('\n') if buf.getvalue() else []

def run_err(src):
    try:
        exec(compile(src, '<slide>', 'exec'), {'__name__': '__main__'})
    except Exception as e:
        return f'{type(e).__name__}: {e}'
    return ''

import os, tempfile
def run_tmp(src, inputs=()):
    old = os.getcwd()
    with tempfile.TemporaryDirectory() as d:
        os.chdir(d)
        try: return run(src, inputs)
        finally: os.chdir(old)
