import os
import codecs

from pyecharts.engine import EchartsEnvironment

from pyecharts_snapshot.main import make_a_snapshot, DEFAULT_DELAY


class SnapshotEnvironment(EchartsEnvironment):
    def render_chart_to_notebook(self, **_):
        """
        Disable html rendering (_repr_html_) in jupyter.
        """
        return None

    def render_chart_to_file(
            self,
            chart,
            object_name='chart',
            path='render.png',
            template_name='simple_chart.html',
            verbose=True,
            delay=DEFAULT_DELAY,
            **kwargs):
        _, extension = os.path.splitext(path)
        super(SnapshotEnvironment, self).render_chart_to_file(
            chart=chart,
            object_name=object_name,
            path='tmp.html',
            template_name=template_name,
            **kwargs
        )
        make_a_snapshot('tmp.html', path, delay=delay, verbose=verbose)
        os.unlink('tmp.html')
        content = None
        if extension == '.svg':
            with codecs.open(path, 'r', 'utf-8') as f:
                content = f.read()
        else:
            with open(path, 'rb') as f:
                content = f.read()
        return content
