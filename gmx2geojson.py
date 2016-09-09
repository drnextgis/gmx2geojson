#!env/bin/python

import click
import geojson

from collections import OrderedDict


@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def main(input, output):
    """This script converts GeoMixer vector tile data to GeoJSON format.

    \b
    Convert gmx.json to collection.geojson:
        gmx2geojson input_fle.json output_file.geojson
    """
    source = geojson.load(input)
    features = list()

    for item in source.get('values'):

        attrs = OrderedDict()
        for idx, ele in enumerate(item):
            if not isinstance(ele, dict):
                key = 'property%s' % (idx, )
                attrs[key] = ele
            else:
                geom = ele
                geom['type'] = (
                    'MultiPolygon' if geom['type'] == 'MULTIPOLYGON' else
                    'Polygon' if geom['type'] == 'POLYGON' else
                    'MultiLineString' if geom['type'] == 'MULTILINESTRING' else
                    'LineString' if geom['type'] == 'LINESTRING' else
                    'MultiPoint' if geom['type'] == 'MULTIPOINT' else
                    'Point' if geom['type'] == 'POINT' else geom['type'])

        feature = geojson.Feature(geometry=geom, properties=attrs)
        features.append(feature)

    collection = geojson.FeatureCollection(features)
    geojson.dump(collection, output)
